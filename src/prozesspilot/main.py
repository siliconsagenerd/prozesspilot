"""FastAPI application."""

from __future__ import annotations

import hmac
import time
from collections import defaultdict, deque
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel, Field
from sqlalchemy import select

from prozesspilot.agents.runtime import approve_run, run_workflow
from prozesspilot.config import settings
from prozesspilot.db.models import (
    Customer,
    Draft,
    Inquiry,
    KnowledgeSource,
    WorkflowRun,
    WorkflowStep,
)
from prozesspilot.db.session import db_session, init_db
from prozesspilot.observability.audit import audit


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings.ensure_dirs()
    settings.validate_provider_keys()
    init_db()
    yield

app = FastAPI(title="ProzessPilot", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://prozesspilot.duckdns.org",
        "https://prozesspilot-editorial.vercel.app",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "X-ProzessPilot-Operator"],
)

@app.middleware("http")
async def protect_operator_api(request: Request, call_next):
    path = request.url.path
    if settings.operator_auth_required and path.startswith("/api/") and request.method != "OPTIONS":
        expected = settings.operator_token
        supplied = request.headers.get("x-prozesspilot-operator", "")
        if not expected or not hmac.compare_digest(supplied, expected):
            return JSONResponse({"detail": "authentication required"}, status_code=401)
    # Origin validation for CSRF defense on state-changing API requests
    if request.method in ("POST", "PUT", "DELETE", "PATCH") and path.startswith("/api/"):
        origin = request.headers.get("origin")
        if origin:
            allowed = {
                "https://prozesspilot.duckdns.org",
                "https://prozesspilot-editorial.vercel.app",
                "http://localhost:5173",
                "http://127.0.0.1:5173",
                "http://localhost:5174",
                "http://127.0.0.1:5174",
            }
            if origin not in allowed:
                return JSONResponse({"detail": "untrusted origin"}, status_code=403)
    return await call_next(request)

@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "img-src 'self' data:; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "script-src 'self'; "
        "connect-src 'self' http://localhost:* http://127.0.0.1:* https://prozesspilot.duckdns.org; "
        "frame-ancestors 'none';"
    )
    if request.url.scheme == "https":
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response

_rate_buckets = defaultdict(deque)

def _rate_limit(key: str):
    now = time.time()
    q = _rate_buckets[key]
    while q and now - q[0] > 60:
        q.popleft()
    if len(q) >= settings.rate_limit_per_minute:
        retry_after = 60
        if q:
            retry_after = max(1, int(60 - (now - q[0])))
        raise HTTPException(429, "rate limit exceeded", headers={"Retry-After": str(retry_after)})
    q.append(now)

TEMPLATES = Environment(
    loader=FileSystemLoader(str(__import__("pathlib").Path(__file__).resolve().parent / "templates")),
    autoescape=True,
)


class InquiryIn(BaseModel):
    subject: str = ""
    body: str = Field(min_length=1)
    customer_email: str | None = None
    channel: str = "form"


class ApprovalIn(BaseModel):
    action: str  # approve / edit_approve / reject
    edited_text: str | None = Field(default=None, max_length=8000)
    reason: str | None = Field(default=None, max_length=1000)



@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}

@app.get("/public/demo-snapshot")
def public_demo_snapshot(request: Request):
    _rate_limit(request.client.host if request.client else "anon")
    import json
    from pathlib import Path

    snapshot_path = Path(__file__).resolve().parent / "data" / "demo_snapshot.json"
    with snapshot_path.open("r", encoding="utf-8") as f:
        return json.load(f)


# Customers
@app.get("/api/customers")
def list_customers():
    with db_session() as s:
        cs = s.execute(select(Customer)).scalars().all()
        return [{"id": c.id, "name": c.name, "email": c.email, "tier": c.tier} for c in cs]


# Inquiries
@app.post("/api/inquiries")
async def create_inquiry(payload: InquiryIn, request: Request):
    _rate_limit(request.client.host if request.client else "anon")
    if len(payload.body) > settings.max_inquiry_body_chars:
        raise HTTPException(413, "body too large")
    with db_session() as s:
        cust_id = None
        if payload.customer_email:
            c = s.execute(select(Customer).where(Customer.email == payload.customer_email)).scalar_one_or_none()
            if c:
                cust_id = c.id
        inq = Inquiry(subject=payload.subject, body=payload.body, channel=payload.channel, customer_id=cust_id)
        s.add(inq)
        s.flush()
        inq_id = inq.id
    audit(None, "inquiry_created", payload={"inquiry_id": inq_id})
    return {"id": inq_id}


@app.get("/api/inquiries")
def list_inquiries():
    with db_session() as s:
        inqs = s.execute(select(Inquiry).order_by(Inquiry.created_at.desc())).scalars().all()
        runs = s.execute(select(WorkflowRun).order_by(WorkflowRun.started_at.desc())).scalars().all()
        latest_by_inquiry = {}
        for r in runs:
            latest_by_inquiry.setdefault(r.inquiry_id, r)
        out = []
        for i in inqs:
            run = latest_by_inquiry.get(i.id)
            out.append(
                {
                    "id": i.id,
                    "subject": i.subject,
                    "body": i.body[:120],
                    "status": run.state if run else i.status,
                    "run_id": run.id if run else None,
                    "created_at": i.created_at.isoformat(),
                }
            )
        return out


@app.post("/api/inquiries/{inquiry_id}/run")
async def run(
    inquiry_id: str,
    request: Request,
    prompt_variant: str = "improved",
    classify_max_tokens: int | None = None,
    draft_max_tokens: int | None = None,
    experimental: bool = False,
):
    _rate_limit(request.client.host if request.client else "anon")
    ceiling = settings.experimental_max_tokens if experimental else settings.max_tokens_per_call
    for _name, _v in (("classify_max_tokens", classify_max_tokens), ("draft_max_tokens", draft_max_tokens)):
        if _v is not None and (_v <= 0 or _v > 8192):
            raise HTTPException(400, f"{_name} must be between 1 and 8192")
        if _v is not None and _v > ceiling:
            raise HTTPException(400, f"{_name} exceeds configured maximum of {ceiling}")
    run_id = await run_workflow(
        inquiry_id,
        prompt_variant=prompt_variant,
        classify_max_tokens=classify_max_tokens,
        draft_max_tokens=draft_max_tokens,
        experimental=experimental,
    )
    return {"run_id": run_id}


# Workflow runs
def _operator_authorized(request: Request) -> bool:
    if not settings.operator_auth_required:
        return True
    expected = settings.operator_token
    if not expected:
        return False
    supplied = request.headers.get("x-prozesspilot-operator", "")
    return hmac.compare_digest(supplied, expected)

@app.get("/api/runs/{run_id}")
def get_run(run_id: str, request: Request):
    if not _operator_authorized(request):
        raise HTTPException(401, "operator authentication required")
    return _fetch_run(run_id)


def _fetch_run(run_id: str):
    with db_session() as s:
        r = s.get(WorkflowRun, run_id)
        if not r:
            raise HTTPException(404, "run not found")
        steps = s.execute(
            select(WorkflowStep).where(WorkflowStep.run_id == run_id).order_by(WorkflowStep.step_index)
        ).scalars().all()
        draft = s.execute(select(Draft).where(Draft.run_id == run_id)).scalar_one_or_none()
        from prozesspilot.db.models import Approval as _A

        approvals = s.execute(select(_A).where(_A.run_id == run_id)).scalars().all()
        inq = s.get(Inquiry, r.inquiry_id)
        cust = s.get(Customer, inq.customer_id) if (inq and inq.customer_id) else None
        return {
            "id": r.id,
            "inquiry_id": r.inquiry_id,
            "inquiry": {"subject": inq.subject, "body": inq.body} if inq else None,
            "customer": (
                {"name": cust.name, "email": cust.email, "tier": cust.tier, "history": cust.history_summary}
                if cust
                else None
            ),
            "state": r.state,
            "classification": r.classification,
            "confidence": r.confidence,
            "classification_confidence": r.confidence,
            "routing_decision": r.routing_decision,
            "requires_approval": r.requires_approval,
            "email_sent": r.email_sent,
            "crm_updated": r.crm_updated,
            "outbound_completed": r.outbound_completed,
            "approval_owner": r.approval_owner,
            "approval_lease_expires_at": (
                r.approval_lease_expires_at.isoformat() if r.approval_lease_expires_at else None
            ),
            "total_cost_usd": r.total_cost_usd,
            "total_latency_ms": r.total_latency_ms,
            "total_tokens": r.total_tokens,
            "error": r.error,
            "started_at": r.started_at.isoformat(),
            "finished_at": r.finished_at.isoformat() if r.finished_at else None,
            "steps": [
                {
                    "index": st.step_index,
                    "name": st.name,
                    "status": st.status,
                    "model_provider": st.model_provider,
                    "model_name": st.model_name,
                    "prompt_version": st.prompt_version,
                    "input_summary": st.input_summary,
                    "output_summary": st.output_summary,
                    "tool_calls": st.tool_calls,
                    "citations": st.citations,
                    "confidence": st.confidence,
                    "latency_ms": st.latency_ms,
                    "tokens_in": st.tokens_in,
                    "tokens_out": st.tokens_out,
                    "cost_usd": st.cost_usd,
                    "finish_reason": st.finish_reason,
                    "response_model": st.response_model,
                    "requested_max_tokens": st.requested_max_tokens,
                    "completion_status": st.completion_status,
                    "error": st.error,
                }
                for st in steps
            ],
            "draft": (
                {
                    "original_text": draft.original_text,
                    "edited_text": draft.edited_text,
                    "citations": draft.citations,
                    "cited_sources": draft.cited_sources,
                    "citation_format_issues": draft.citation_format_issues,
                    "confidence": draft.confidence,
                    "draft_confidence": draft.confidence,
                    "reasoning": draft.reasoning,
                }
                if draft
                else None
            ),
            "approvals": [
                {"action": a.action, "reason": a.reason, "actor": a.actor, "created_at": a.created_at.isoformat()}
                for a in approvals
            ],
        }


@app.post("/api/runs/{run_id}/approve")
async def approve(run_id: str, payload: ApprovalIn):
    if payload.action not in ("approve", "edit_approve", "reject"):
        raise HTTPException(400, "bad action")
    if payload.action == "reject" and not payload.reason:
        raise HTTPException(400, "reason required")
    try:
        await approve_run(
            run_id,
            payload.action,
            edited_text=payload.edited_text,
            reason=payload.reason,
            actor="operator",
        )
    except ValueError as e:
        msg = str(e)
        if msg in ("run not found", "no draft"):
            raise HTTPException(404 if msg == "run not found" else 400, msg) from e
        raise HTTPException(409, "invalid approval state") from e
    except Exception as e:
        raise HTTPException(500, "approval failed") from e
    return {"ok": True}


@app.get("/api/runs/{run_id}/trace.html", response_class=HTMLResponse)
def trace_html(run_id: str, request: Request, lang: str = "de"):
    if not _operator_authorized(request):
        raise HTTPException(401, "operator authentication required")
    data = _fetch_run(run_id)
    if lang not in ("de", "en"):
        lang = "de"
    if lang == "en":
        try:
            from prozesspilot.data_tr import DATA_TR
        except Exception:
            DATA_TR = {}
        def td(x):
            if not isinstance(x, str):
                return x
            return DATA_TR.get(x, x)
        if data.get("inquiry"):
            data["inquiry"]["subject"] = td(data["inquiry"].get("subject"))
            data["inquiry"]["body"] = td(data["inquiry"].get("body"))
        if data.get("customer"):
            data["customer"]["history"] = td(data["customer"].get("history"))
        data["classification"] = td(data.get("classification"))
        data["routing_decision"] = td(data.get("routing_decision"))
        if data.get("error"):
            data["error"] = td(data.get("error"))
        for st in (data.get("steps") or []):
            st["input_summary"] = td(st.get("input_summary"))
            st["output_summary"] = td(st.get("output_summary"))
            if st.get("error"):
                st["error"] = td(st.get("error"))
            if st.get("citations"):
                for c in st["citations"]:
                    c["title"] = td(c.get("title"))
        if data.get("draft"):
            data["draft"]["original_text"] = td(data["draft"].get("original_text"))
            if data["draft"].get("edited_text"):
                data["draft"]["edited_text"] = td(data["draft"].get("edited_text"))
            data["draft"]["reasoning"] = td(data["draft"].get("reasoning"))
    tmpl = TEMPLATES.get_template("trace.html")
    return tmpl.render(run=data, lang=lang)


# Knowledge sources
@app.get("/api/kb")
def list_kb():
    with db_session() as s:
        srcs = s.execute(select(KnowledgeSource)).scalars().all()
        return [{"id": x.id, "title": x.title, "category": x.category} for x in srcs]


# Eval endpoints
@app.get("/api/eval/cases")
def eval_cases():
    from prozesspilot.eval.cases import CASES

    return CASES


@app.post("/api/eval/run")
async def eval_run(request: Request, prompt_variant: str = "improved", provider: str | None = None):
    _rate_limit(request.client.host if request.client else "anon")
    from prozesspilot.eval.runner import run_eval

    return await run_eval(prompt_variant=prompt_variant, provider_override=provider)


@app.get("/api/eval/results")
def eval_results():
    from sqlalchemy import select as sel

    from prozesspilot.db.models import Evaluation

    with db_session() as s:
        rows = s.execute(sel(Evaluation).order_by(Evaluation.created_at.desc())).scalars().all()
        return [
            {
                "case_id": r.case_id,
                "prompt_variant": r.prompt_variant,
                "model_provider": r.model_provider,
                "model_name": r.model_name,
                "predicted": r.predicted_classification,
                "expected": r.expected_classification,
                "classification_correct": r.classification_correct,
                "routing_correct": r.routing_correct,
                "citations_present": r.citations_present,
                "latency_ms": r.latency_ms,
                "cost_usd": r.cost_usd,
            }
            for r in rows
        ]