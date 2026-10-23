"""Agent runtime: executes the inquiry-handling workflow step by step."""

from __future__ import annotations

import json
import time
from datetime import UTC, datetime

from sqlalchemy import select

from prozesspilot.agents.classifier import classify_inquiry
from prozesspilot.agents.drafter import draft_response
from prozesspilot.config import settings
from prozesspilot.db.models import (
    Draft,
    Inquiry,
    WorkflowRun,
    WorkflowStep,
)
from prozesspilot.db.session import db_session
from prozesspilot.eval.citations import extract_explicit_citations
from prozesspilot.observability.audit import audit
from prozesspilot.tools.crm_mock import crm_update_mock
from prozesspilot.tools.customer_lookup import customer_lookup
from prozesspilot.tools.email_mock import send_email_mock
from prozesspilot.tools.kb_search import kb_search
from prozesspilot.tools.registry import Tool, registry


def _register_tools() -> None:
    if "customer_lookup" not in registry.names():
        registry.register(Tool("customer_lookup", "Look up synthetic customer by email/name", customer_lookup))
        registry.register(Tool("kb_search", "Search local knowledge base", kb_search))
        registry.register(Tool("send_email_mock", "Mock email sender (disk only)", send_email_mock))
        registry.register(Tool("crm_update_mock", "Mock CRM updater (log only)", crm_update_mock))


_register_tools()


CLASSIFICATIONS = ["product_question", "complaint", "order_status", "quote_request", "spam", "unclear"]


def _completion_status(finish_reason, text):
    """Classify output completeness from provider evidence and a light heuristic."""
    if finish_reason in {"length", "max_tokens", "MAX_TOKENS", "model_length"}:
        return "length_stopped"
    if finish_reason in {"stop", "end_turn", "stop_sequence", "completed", "DONE"}:
        return "complete"
    stripped = (text or "").rstrip()
    if not stripped:
        return "unknown"
    ends_badly = stripped.endswith((",", ":", ";", "(", "[", "{"))
    lower_tail = stripped[-1].islower() and not stripped.endswith(("kb]", "]"))
    if ends_badly or lower_tail:
        return "heuristic_incomplete"
    return "unknown" if finish_reason is None else "provider_reported"


async def run_workflow(
    inquiry_id: str,
    prompt_variant: str = "improved",
    classify_max_tokens: int | None = None,
    draft_max_tokens: int | None = None,
) -> str:
    """Run full workflow for an inquiry. Returns run_id."""
    with db_session() as s:
        inq = s.get(Inquiry, inquiry_id)
        if inq is None:
            raise ValueError("inquiry not found")
        run = WorkflowRun(inquiry_id=inquiry_id, state="Classifying")
        s.add(run)
        s.flush()
        run_id = run.id
        inq.run_id = run_id
        inq.status = "processing"

    audit(run_id, "workflow_started", payload={"inquiry_id": inquiry_id, "prompt_variant": prompt_variant})

    customer_ctx = None
    classification = None
    confidence = None
    classification_confidence = None
    draft_confidence = None
    kb_results = []
    draft_text = ""
    reasoning = ""
    routing = None
    requires_approval = False

    async def record_step(idx, name, **kw):
        with db_session() as s:
            step = WorkflowStep(run_id=run_id, step_index=idx, name=name, **kw)
            s.add(step)

    # Step 0: classify
    t0 = time.time()
    try:
        inq_body = None
        with db_session() as s:
            inq = s.get(Inquiry, inquiry_id)
            inq_body = inq.body
            inq.subject = inq.subject
        cls_result = await classify_inquiry(
            inq_body or "",
            prompt_variant=prompt_variant,
            max_tokens=classify_max_tokens if classify_max_tokens is not None else settings.max_tokens_per_call,
        )
        classification = cls_result["classification"]
        classification_confidence = float(cls_result["confidence"])
        confidence = classification_confidence
        latency = int((time.time() - t0) * 1000)
        await record_step(
            0,
            "classify",
            status="done",
            model_provider=cls_result["provider"],
            model_name=cls_result["model"],
            prompt_version=f"classify-{prompt_variant}",
            input_summary=(inq_body or "")[:300],
            output_summary=f"{classification} (conf={confidence:.2f})",
            confidence=confidence,
            latency_ms=latency,
            tokens_in=cls_result.get("tokens_in", 0),
            tokens_out=cls_result.get("tokens_out", 0),
            cost_usd=cls_result.get("cost_usd", 0.0),
            finish_reason=cls_result.get("finish_reason"),
            response_model=cls_result.get("response_model"),
            requested_max_tokens=(
                classify_max_tokens if classify_max_tokens is not None else settings.max_tokens_per_call
            ),
            completion_status=_completion_status(cls_result.get("finish_reason"), cls_result.get("text", "")),
        )
    except Exception as e:  # noqa: BLE001
        await record_step(0, "classify", status="failed", error=str(e), completion_status="unknown")
        _fail_run(run_id, str(e))
        return run_id

    audit(run_id, "classified", payload={"classification": classification, "confidence": confidence})

    # update run state
    with db_session() as s:
        r = s.get(WorkflowRun, run_id)
        r.classification = classification
        r.confidence = confidence
        r.state = "Drafting"

    # Step 1: customer lookup
    t0 = time.time()
    try:
        email = None
        with db_session() as s:
            inq = s.get(Inquiry, inquiry_id)
            # try to find customer email in body? Use inquiry customer link if present
            if inq.customer_id:
                pass
        # look up by inquiry's customer if linked else search body for email
        import re

        m = re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", inq_body or "")
        email = m.group(0) if m else None
        # if linked customer, fetch
        with db_session() as s:
            inq = s.get(Inquiry, inquiry_id)
            if inq.customer_id:
                from prozesspilot.db.models import Customer

                c = s.get(Customer, inq.customer_id)
                if c:
                    email = c.email
        lookup = await registry.call("customer_lookup", email=email) if email else {"found": False, "customer": None}
        customer_ctx = lookup.get("customer")
        latency = int((time.time() - t0) * 1000)
        await record_step(
            1,
            "customer_lookup",
            status="done",
            input_summary=f"email={email}",
            output_summary=json.dumps(lookup.get("customer") or {"found": False})[:400],
            tool_calls=[{"tool": "customer_lookup", "input": {"email": email}, "output": lookup}],
            latency_ms=latency,
        )
    except Exception as e:  # noqa: BLE001
        await record_step(1, "customer_lookup", status="failed", error=str(e))

    # Step 2: kb search (skipped for spam to avoid irrelevant product context)
    t0 = time.time()
    if classification == "spam":
        kb_results = []
        await record_step(
            2,
            "kb_search",
            status="skipped",
            input_summary=(inq_body or "")[:200],
            output_summary="kb_search skipped: spam classification",
            citations=[],
            latency_ms=0,
        )
    else:
        try:
            kb = await registry.call("kb_search", query=inq_body or "")
            kb_results = kb.get("results", [])
            latency = int((time.time() - t0) * 1000)
            await record_step(
                2,
                "kb_search",
                status="done",
                input_summary=(inq_body or "")[:200],
                output_summary=f"{len(kb_results)} sources",
                tool_calls=[{"tool": "kb_search", "input": {"query": (inq_body or "")[:200]}, "output": kb}],
                citations=[{"id": r["id"], "source_key": r.get("source_key"), "title": r["title"]} for r in kb_results],
                latency_ms=latency,
            )
        except Exception as e:  # noqa: BLE001
            await record_step(2, "kb_search", status="failed", error=str(e))

    # Budget guard
    too_many_tokens = (
        cls_result.get("tokens_in", 0) + cls_result.get("tokens_out", 0)
    ) >= settings.max_workflow_tokens
    too_costly = cls_result.get("cost_usd", 0.0) >= settings.cost_cap_usd_per_run
    if too_many_tokens or too_costly:
        _fail_run(run_id, "workflow budget exceeded")
        return run_id
    # Step 3: draft
    t0 = time.time()
    try:
        draft_res = await draft_response(
            inquiry_body=inq_body or "",
            classification=classification,
            customer=customer_ctx,
            kb_results=kb_results,
            prompt_variant=prompt_variant,
            max_tokens=draft_max_tokens if draft_max_tokens is not None else settings.max_tokens_per_call,
        )
        draft_text = draft_res["text"]
        reasoning = draft_res.get("reasoning", "")
        draft_confidence = draft_res.get("confidence", None)
        if draft_confidence is not None:
            draft_confidence = float(draft_confidence)
        else:
            draft_confidence = confidence
        latency = int((time.time() - t0) * 1000)
        await record_step(
            3,
            "draft",
            status="done",
            model_provider=draft_res["provider"],
            model_name=draft_res["model"],
            prompt_version=f"draft-{prompt_variant}",
            input_summary=f"classification={classification}",
            output_summary=draft_text[:400],
            citations=[{"id": r["id"], "source_key": r.get("source_key"), "title": r["title"]} for r in kb_results],
            confidence=draft_confidence,
            latency_ms=latency,
            tokens_in=draft_res.get("tokens_in", 0),
            tokens_out=draft_res.get("tokens_out", 0),
            cost_usd=draft_res.get("cost_usd", 0.0),
            finish_reason=draft_res.get("finish_reason"),
            response_model=draft_res.get("response_model"),
            requested_max_tokens=(
                draft_max_tokens if draft_max_tokens is not None else settings.max_tokens_per_call
            ),
            completion_status=_completion_status(draft_res.get("finish_reason"), draft_text),
        )
    except Exception as e:  # noqa: BLE001
        await record_step(3, "draft", status="failed", error=str(e), completion_status="unknown")
        _fail_run(run_id, str(e))
        return run_id

    # Persist draft
    kb_citation_sources = [{"id": r["id"], "source_key": r.get("source_key"), "title": r["title"]} for r in kb_results]
    cited_sources, citation_issues = extract_explicit_citations(draft_text, kb_citation_sources)
    with db_session() as s:
        s.add(
            Draft(
                run_id=run_id,
                original_text=draft_text,
                citations=kb_citation_sources,
                cited_sources=cited_sources,
                citation_format_issues=citation_issues,
                confidence=draft_confidence,
                reasoning=reasoning,
            )
        )

    # Step 4: routing decision
    routing = _route(classification, confidence, customer_ctx)
    requires_approval = routing["requires_approval"]
    with db_session() as s:
        r = s.get(WorkflowRun, run_id)
        r.routing_decision = routing["decision"]
        r.requires_approval = requires_approval
        r.confidence = confidence
        if requires_approval:
            r.state = "AwaitingApproval"
        else:
            r.state = "ReadyForReview"  # eligible for review; no human approval fabricated
    await record_step(
        4,
        "route",
        status="done",
        input_summary=f"classification={classification}, confidence={confidence:.2f}",
        output_summary=routing["decision"],
        confidence=confidence,
        latency_ms=0,
    )
    audit(run_id, "routed", payload=routing)

    # If no approval needed, simulate outbound (mock) automatically? 
    # Spec: high-confidence simple product question may be marked "ready for review".
    # We mark ready_for_review and do NOT send email. Only on explicit approve.
    # Human review always gates outbound action (safety). routing_decision records auto-eligibility.
    with db_session() as s:
        r = s.get(WorkflowRun, run_id)
        if requires_approval:
            r.state = "AwaitingApproval"
        else:
            r.state = "ReadyForReview"
    audit(run_id, "routed", payload={"requires_approval": requires_approval})

    # finalize totals
    _finalize_totals(run_id)
    with db_session() as s:
        r = s.get(WorkflowRun, run_id)
        if r.state not in ("AwaitingApproval", "ReadyForReview"):
            r.state = r.state
        r.finished_at = datetime.now(UTC)
        inq = s.get(Inquiry, r.inquiry_id)
        if inq:
            inq.status = r.state
    audit(run_id, "workflow_finished", payload={"state": routing["decision"]})
    return run_id


def _route(classification, confidence, customer) -> dict:
    settings_ = settings
    requires = False
    reasons = []
    if classification == "complaint":
        requires = True
        reasons.append("complaint")
    if classification == "unclear":
        requires = True
        reasons.append("unclear")
    if confidence < settings_.confidence_human_gate:
        requires = True
        reasons.append("low_confidence")
    if customer and customer.get("tier") in ("premium", "vip"):
        requires = True
        reasons.append("high_value_customer")
    if customer and customer.get("has_open_complaint"):
        requires = True
        reasons.append("open_complaint")
    decision = "requires_human_approval" if requires else "ready_for_review"
    return {"requires_approval": requires, "decision": decision, "reasons": reasons}


def _fail_run(run_id: str, err: str) -> None:
    with db_session() as s:
        r = s.get(WorkflowRun, run_id)
        r.state = "Failed"
        r.error = err
        r.finished_at = datetime.now(UTC)
        inq = s.get(Inquiry, r.inquiry_id)
        if inq:
            inq.status = "Failed"
    audit(run_id, "workflow_failed", payload={"error": err})


def _finalize_totals(run_id: str) -> None:
    with db_session() as s:
        steps = s.execute(select(WorkflowStep).where(WorkflowStep.run_id == run_id)).scalars().all()
        r = s.get(WorkflowRun, run_id)
        r.total_cost_usd = round(sum(st.cost_usd or 0 for st in steps), 6)
        r.total_latency_ms = sum(st.latency_ms or 0 for st in steps)
        r.total_tokens = sum((st.tokens_in or 0) + (st.tokens_out or 0) for st in steps)


async def approve_run(
    run_id: str,
    action: str,
    edited_text: str | None = None,
    reason: str | None = None,
    actor: str = "operator",
) -> None:
    from prozesspilot.db.models import Approval

    with db_session() as s:
        run = s.get(WorkflowRun, run_id)
        if run is None:
            raise ValueError("run not found")
        if run.state == "Approved":
            # Repeated approval is a no-op: outbound mock actions were already recorded.
            audit(run_id, "approval_duplicate_ignored", actor=actor, payload={"reason": reason})
            return
        draft = s.execute(select(Draft).where(Draft.run_id == run_id)).scalar_one_or_none()
        if draft is None:
            raise ValueError("no draft")
        if action == "edit_approve" and edited_text:
            draft.edited_text = edited_text
        s.add(Approval(run_id=run_id, action=action, edited_text=edited_text, reason=reason, actor=actor))

    audit(run_id, f"approval_{action}", actor=actor, payload={"reason": reason})

    if action == "reject":
        with db_session() as s:
            r = s.get(WorkflowRun, run_id)
            r.state = "Rejected"
            r.finished_at = datetime.now(UTC)
            inq = s.get(Inquiry, r.inquiry_id)
            if inq:
                inq.status = "Rejected"
        audit(run_id, "rejected", actor=actor, payload={"reason": reason})
        return

    # approve or edit_approve -> simulate outbound (mock)
    final_text = edited_text if (action == "edit_approve" and edited_text) else None
    to_email = "unknown@example.com"
    cust_id = None
    with db_session() as s:
        d = s.execute(select(Draft).where(Draft.run_id == run_id)).scalar_one_or_none()
        final_text = final_text or (d.edited_text or d.original_text)
        run = s.get(WorkflowRun, run_id)
        inq = run.inquiry if run else None
        if inq and inq.customer:
            to_email = inq.customer.email
            cust_id = inq.customer.id

    await registry.call("send_email_mock", to=to_email, subject="Re: Ihre Anfrage", body=final_text, run_id=run_id)
    await registry.call("crm_update_mock", run_id=run_id, customer_id=cust_id, summary=final_text[:200])

    with db_session() as s:
        r = s.get(WorkflowRun, run_id)
        r.state = "Approved"
        r.finished_at = datetime.now(UTC)
        inq = s.get(Inquiry, r.inquiry_id)
        if inq:
            inq.status = "Approved"
    audit(run_id, "approved_and_mock_sent", actor=actor, payload={"mock": True})