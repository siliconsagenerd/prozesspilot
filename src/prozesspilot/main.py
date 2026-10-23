"""FastAPI application."""

from __future__ import annotations

import time
from collections import defaultdict, deque

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
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
from prozesspilot.db.session import db_session
from prozesspilot.observability.audit import audit

app = FastAPI(title="ProzessPilot")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMPLATES = Environment(
    loader=FileSystemLoader(str(settings.data_dir.parent / "src" / "prozesspilot" / "templates")),
    autoescape=True,
)


class InquiryIn(BaseModel):
    subject: str = ""
    body: str = Field(min_length=1)
    customer_email: str | None = None
    channel: str = "form"


class ApprovalIn(BaseModel):
    action: str  # approve / edit_approve / reject
    edited_text: str | None = None
    reason: str | None = None
    actor: str = "operator"


@app.on_event("startup")
def startup():
    settings.ensure_dirs()


@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}


# Customers
@app.get("/api/customers")
def list_customers():
    with db_session() as s:
        cs = s.execute(select(Customer)).scalars().all()
        return [{"id": c.id, "name": c.name, "email": c.email, "tier": c.tier} for c in cs]


_rate_buckets = defaultdict(deque)

def _rate_limit(key: str):
    now = time.time()
    q = _rate_buckets[key]
    while q and now - q[0] > 60:
        q.popleft()
    if len(q) >= settings.rate_limit_per_minute:
        raise HTTPException(429, "rate limit exceeded")
    q.append(now)

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
        out = []
        for i in inqs:
            # latest run
            run = s.execute(
                select(WorkflowRun)
                .where(WorkflowRun.inquiry_id == i.id)
                .order_by(WorkflowRun.started_at.desc())
            ).scalars().first()
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
):
    _rate_limit(request.client.host if request.client else "anon")
    run_id = await run_workflow(
        inquiry_id,
        prompt_variant=prompt_variant,
        classify_max_tokens=classify_max_tokens,
        draft_max_tokens=draft_max_tokens,
    )
    return {"run_id": run_id}


# Workflow runs
@app.get("/api/runs/{run_id}")
def get_run(run_id: str):
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
    await approve_run(
        run_id,
        payload.action,
        edited_text=payload.edited_text,
        reason=payload.reason,
        actor=payload.actor,
    )
    return {"ok": True}


@app.get("/api/runs/{run_id}/trace.html", response_class=HTMLResponse)
def trace_html(run_id: str):
    data = get_run(run_id)
    tmpl = TEMPLATES.get_template("trace.html")
    return tmpl.render(run=data)


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
async def eval_run(prompt_variant: str = "improved", provider: str | None = None):
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