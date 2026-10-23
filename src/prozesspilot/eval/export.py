"""Evaluation export helpers using authoritative full draft text."""

from __future__ import annotations

import json
from typing import Any

from sqlalchemy import select

from prozesspilot.db.models import Draft, WorkflowRun, WorkflowStep
from prozesspilot.db.session import db_session


FULL_DRAFT_UNAVAILABLE_LABEL = "preview only; full-draft review unavailable"


def _step_dict(step: WorkflowStep) -> dict[str, Any]:
    return {
        "index": step.step_index,
        "name": step.name,
        "status": step.status,
        "model_provider": step.model_provider,
        "model_name": step.model_name,
        "prompt_version": step.prompt_version,
        "input_summary": step.input_summary,
        "output_summary": step.output_summary,
        "tool_calls": step.tool_calls,
        "citations": step.citations,
        "confidence": step.confidence,
        "latency_ms": step.latency_ms,
        "tokens_in": step.tokens_in,
        "tokens_out": step.tokens_out,
        "cost_usd": step.cost_usd,
        "finish_reason": step.finish_reason,
        "response_model": step.response_model,
        "requested_max_tokens": step.requested_max_tokens,
        "completion_status": step.completion_status,
        "error": step.error,
    }


def _retrieved_sources(steps: list[WorkflowStep]) -> list[dict[str, Any]]:
    for step in steps:
        if step.name != "kb_search":
            continue
        for tool_call in step.tool_calls or []:
            output = tool_call.get("output") if isinstance(tool_call, dict) else None
            if isinstance(output, dict) and isinstance(output.get("results"), list):
                return [dict(item) for item in output["results"] if isinstance(item, dict)]
        if isinstance(step.citations, list):
            return [dict(item) for item in step.citations if isinstance(item, dict)]
    return []


def _draft_step(steps: list[WorkflowStep]) -> WorkflowStep | None:
    for step in steps:
        if step.name == "draft":
            return step
    return None


def extract_run_record(run_id: str) -> dict[str, Any]:
    """Return one run with the full draft text used for review."""
    with db_session() as s:
        run = s.get(WorkflowRun, run_id)
        if run is None:
            raise ValueError(f"run not found: {run_id}")
        draft = s.execute(select(Draft).where(Draft.run_id == run_id)).scalar_one_or_none()
        steps = list(
            s.execute(
                select(WorkflowStep)
                .where(WorkflowStep.run_id == run_id)
                .order_by(WorkflowStep.step_index)
            ).scalars()
        )
        step_dicts = [_step_dict(step) for step in steps]
        retrieved_sources = _retrieved_sources(steps)
        draft_step = _draft_step(steps)
        preview = draft_step.output_summary if draft_step is not None else None
        full_text = draft.original_text if draft is not None and draft.original_text else None
        full_available = full_text is not None
        cited_sources = (
            list(draft.citations)
            if draft is not None and draft.citations
            else (list(draft_step.citations) if draft_step is not None and draft_step.citations else [])
        )
        draft_record = {
            "id": draft.id if draft is not None else None,
            "full_text": full_text,
            "preview": preview,
            "review_text": full_text if full_available else preview,
            "full_available": full_available,
            "review_status": "full" if full_available else FULL_DRAFT_UNAVAILABLE_LABEL,
            "citations": cited_sources,
            "confidence": draft.confidence if draft is not None else None,
            "reasoning": draft.reasoning if draft is not None else None,
            "edited_text": draft.edited_text if draft is not None else None,
        }
        run_data = {
            "run_id": run.id,
            "inquiry_id": run.inquiry_id,
            "state": run.state,
            "classification": run.classification,
            "confidence": run.confidence,
            "routing_decision": run.routing_decision,
            "requires_approval": run.requires_approval,
            "total_cost_usd": run.total_cost_usd,
            "total_latency_ms": run.total_latency_ms,
            "total_tokens": run.total_tokens,
            "error": run.error,
        }

    return {
        **run_data,
        "steps": step_dicts,
        "draft": draft_record,
        "retrieved_sources": retrieved_sources,
        "cited_sources": cited_sources,
    }


def extract_run_records(run_ids: list[str]) -> list[dict[str, Any]]:
    return [extract_run_record(run_id) for run_id in run_ids]


def render_review_packet(records: list[dict[str, Any]], title: str = "Human Review Packet") -> str:
    """Render records as markdown, preserving full draft text and blank review fields."""
    lines = [f"# {title}", "", "Full draft text is authoritative. `output_summary` is a preview only.", ""]
    for record in records:
        draft = record["draft"]
        lines.extend(
            [
                f"## Run {record['run_id']}",
                "",
                f"- Classification: {record['classification']}",
                f"- Confidence: {record['confidence']}",
                f"- Routing: {record['routing_decision']}",
                f"- Draft review status: {draft['review_status']}",
                "",
                "### Retrieved sources",
            ]
        )
        for source in record["retrieved_sources"]:
            lines.append(f"- {source.get('source_key') or source.get('title') or source.get('id')}")
        lines.extend(["", "### Cited sources"])
        for source in record["cited_sources"]:
            lines.append(f"- {source.get('source_key') or source.get('title') or source.get('id')}")
        lines.extend(["", "### Full draft", "", draft["review_text"] or "_unavailable_", ""])
        lines.extend(
            [
                "### Human review",
                "",
                "- Decision: ",
                "- Notes: ",
                "",
            ]
        )
    return "\n".join(lines)


def write_json(path: str, value: Any) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
