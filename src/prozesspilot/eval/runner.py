"""Evaluation runner."""

from __future__ import annotations

import asyncio

from sqlalchemy import select

from prozesspilot.agents.runtime import run_workflow
from prozesspilot.config import settings
from prozesspilot.db.models import Evaluation, Inquiry, WorkflowRun
from prozesspilot.db.session import db_session
from prozesspilot.eval.cases import CASES
from prozesspilot.eval_preflight import preflight_evaluation


def evaluate_abstention(deliberate_abstention: bool | None, citations_present: bool) -> bool:
    """Evaluate whether abstention behavior matches expected contract.

    deliberate_abstention is mandatory (cannot be None).
    - If deliberate_abstention is True: model must abstain (no citations present).
    - If deliberate_abstention is False: model must provide citations.
    """
    if not isinstance(deliberate_abstention, bool):
        raise ValueError(f"malformed deliberate_abstention: {deliberate_abstention!r}")
    actual_abstention = not citations_present
    return actual_abstention == deliberate_abstention


def evaluate_source_ids(
    acceptable_source_ids: list[str] | None,
    found_ids: list[str],
    match_mode: str = "any",
) -> bool | None:
    """Evaluate whether cited source IDs match acceptable source criteria.

    match_mode:
      - 'any': at least one cited source must be in acceptable_source_ids.
      - 'all': every ID in acceptable_source_ids must be cited.
    Returns None if acceptable_source_ids is None or empty.
    Raises ValueError on malformed inputs.
    """
    if acceptable_source_ids is None or len(acceptable_source_ids) == 0:
        return None
    if not isinstance(acceptable_source_ids, list) or not all(isinstance(x, str) for x in acceptable_source_ids):
        raise ValueError(f"malformed acceptable_source_ids: {acceptable_source_ids!r}")
    if match_mode not in ("any", "all"):
        raise ValueError(f"unknown match_mode: {match_mode!r}")

    found_set = set(found_ids)
    if match_mode == "any":
        return any(sid in found_set for sid in acceptable_source_ids)
    return all(sid in found_set for sid in acceptable_source_ids)


async def run_eval(
    prompt_variant: str = "improved",
    provider_override: str | None = None,
    case_ids: list[str] | None = None,
    classify_max_tokens: int | None = None,
    draft_max_tokens: int | None = None,
) -> dict:
    if provider_override:
        settings.provider = provider_override  # type: ignore
    preflight_evaluation(
        settings,
        CASES,
        {prompt_variant: prompt_variant},
        {"max_tokens_per_call": settings.max_tokens_per_call},
    )
    selected_cases = CASES
    if case_ids is not None:
        wanted = set(case_ids)
        selected_cases = [case for case in CASES if case["id"] in wanted]

    for case in selected_cases:
        if "deliberate_abstention" not in case or not isinstance(case["deliberate_abstention"], bool):
            raise ValueError(f"case {case.get('id')} missing boolean deliberate_abstention")
        if "acceptable_sources" not in case or not isinstance(case["acceptable_sources"], list):
            raise ValueError(f"case {case.get('id')} missing list acceptable_sources")

    semaphore = asyncio.Semaphore(3)

    async def _run_one(case: dict) -> dict:
        async with semaphore:
            with db_session() as s:
                inq = Inquiry(subject="", body=case["body"], channel="eval")
                if case.get("customer_email"):
                    from prozesspilot.db.models import Customer
                    c = s.execute(select(Customer).where(Customer.email == case["customer_email"])).scalar_one_or_none()
                    if c:
                        inq.customer_id = c.id
                s.add(inq)
                s.flush()
                inq_id = inq.id

            run_id = await run_workflow(
                inq_id,
                prompt_variant=prompt_variant,
                classify_max_tokens=classify_max_tokens,
                draft_max_tokens=draft_max_tokens,
            )

            with db_session() as s:
                r = s.get(WorkflowRun, run_id)
                predicted = r.classification
                routing = r.routing_decision
                expected_routing = (
                    "requires_human_approval"
                    if case["expected_routing"] == "requires_human_approval"
                    else "ready_for_review"
                )

                from prozesspilot.db.models import Draft, WorkflowStep
                from prozesspilot.eval.citations import extract_explicit_citations
                from prozesspilot.eval.export import _retrieved_sources
                d = s.execute(select(Draft).where(Draft.run_id == run_id)).scalar_one_or_none()
                steps_for_retrieval = s.execute(
                    select(WorkflowStep).where(WorkflowStep.run_id == run_id)
                ).scalars().all()
                retrieved_sources = _retrieved_sources(list(steps_for_retrieval))
                if d is not None and not d.cited_sources and d.original_text:
                    cited, issues = extract_explicit_citations(d.original_text, retrieved_sources)
                    d.cited_sources = cited
                    d.citation_format_issues = issues
                explicit_citations = list(d.cited_sources) if d is not None and d.cited_sources else []
                citations_present = bool(explicit_citations)
                draft_step = next((st for st in steps_for_retrieval if getattr(st, "name", None) == "draft"), None)
                completion_status = getattr(draft_step, "completion_status", None) if draft_step is not None else None
                execution_complete = r.state in ("ReadyForReview", "AwaitingApproval")
                citation_keys = [
                    c.get("source_key") or c.get("title")
                    for c in explicit_citations
                    if isinstance(c, dict)
                ]

                deliberate_abstention = case["deliberate_abstention"]
                abstention_correct = evaluate_abstention(deliberate_abstention, citations_present)
                classification_confidence = float(r.confidence) if r.confidence is not None else 0.0
                from prozesspilot.db.models import Customer as _Customer
                inq_obj = s.get(Inquiry, r.inquiry_id)
                cust_obj = s.get(_Customer, inq_obj.customer_id) if (inq_obj and inq_obj.customer_id) else None
                customer_ctx = None
                if cust_obj is not None:
                    customer_ctx = {
                        "tier": cust_obj.tier,
                        "has_open_complaint": bool(getattr(cust_obj, "has_open_complaint", False)),
                    }
                from prozesspilot.agents.runtime import _route as _route_policy
                policy_routing = _route_policy(predicted, classification_confidence, customer_ctx)
                routing_policy_compliant = (routing == policy_routing["decision"])

                acceptable_sources = case["acceptable_sources"]
                sources_correct = evaluate_source_ids(acceptable_sources, citation_keys)

                from prozesspilot.eval.export import extract_run_record
                record = extract_run_record(run_id)

                row = Evaluation(
                    case_id=case["id"],
                    prompt_variant=prompt_variant,
                    model_provider=settings.provider,
                    model_name=(
                        settings.ollama_model
                        if settings.provider == "ollama"
                        else (settings.openai_model if settings.provider == "openai" else settings.anthropic_model)
                    ),
                    predicted_classification=predicted,
                    expected_classification=case["expected_classification"],
                    classification_correct=(predicted == case["expected_classification"]),
                    routing_correct=(routing == expected_routing),
                    citations_present=citations_present,
                    latency_ms=r.total_latency_ms,
                    tokens=r.total_tokens,
                    cost_usd=r.total_cost_usd,
                )

                from prozesspilot.db.models import WorkflowStep as _WS
                steps = s.execute(select(_WS).where(_WS.run_id == run_id)).scalars().all()
                if steps:
                    row.model_provider = steps[0].model_provider or row.model_provider
                    row.model_name = steps[0].model_name or row.model_name

                row.notes = (
                    f"deliberate_abstention={deliberate_abstention}; abstention_correct={abstention_correct}; "
                    f"acceptable_sources={acceptable_sources}; sources_found={citation_keys}; "
                    f"sources_correct={sources_correct}"
                )
                s.add(row)

                result = {
                    "case_id": case["id"],
                    "predicted": predicted,
                    "expected": case["expected_classification"],
                    "classification_correct": predicted == case["expected_classification"],
                    "routing": routing,
                    "expected_routing": expected_routing,
                    "routing_correct": routing == expected_routing,
                    "routing_policy_compliant": routing_policy_compliant,
                    "routing_matches_expected": routing == expected_routing,
                    "routing_matches_frozen_expected": routing == expected_routing,
                    "execution_complete": execution_complete,
                    "completion_status": completion_status,
                    "classification_confidence": classification_confidence,
                    "draft_confidence": float(d.confidence) if d is not None and d.confidence is not None else None,
                    "citation_format_issues": (
                        list(d.citation_format_issues) if d is not None and d.citation_format_issues else []
                    ),
                    "content_quality_findings": (
                        (["missing_citation"] if (not citations_present and not deliberate_abstention) else [])
                        + (["citation_format_issue"] if (d is not None and d.citation_format_issues) else [])
                    ),
                    "defects": (
                        (["missing_citation"] if (not citations_present and not deliberate_abstention) else [])
                        + (["citation_format_issue"] if (d is not None and d.citation_format_issues) else [])
                    ),
                    "citations_present": citations_present,
                    "deliberate_abstention": deliberate_abstention,
                    "abstention_correct": abstention_correct,
                    "acceptable_sources": acceptable_sources,
                    "sources_found": citation_keys,
                    "sources_correct": sources_correct,
                    "latency_ms": r.total_latency_ms,
                    "cost_usd": r.total_cost_usd,
                    "run_id": run_id,
                    "draft_text": record["draft"]["full_text"],
                    "draft_preview": record["draft"]["preview"],
                    "draft_review_status": record["draft"]["review_status"],
                    "retrieved_sources": record["retrieved_sources"],
                    "cited_sources": record["cited_sources"],
                    "steps": record["steps"],
                }
                return result

    results = list(await asyncio.gather(*(_run_one(case) for case in selected_cases)))

    # aggregate
    n = len(results)
    cls_acc = sum(1 for r in results if r["classification_correct"]) / n if n else 0
    route_acc = sum(1 for r in results if r["routing_correct"]) / n if n else 0
    policy_acc = sum(1 for r in results if r.get("routing_policy_compliant")) / n if n else 0
    exec_acc = sum(1 for r in results if r.get("execution_complete")) / n if n else 0
    cit_rate = sum(1 for r in results if r["citations_present"]) / n if n else 0

    abst_cases = [r for r in results if r.get("deliberate_abstention") is not None]
    abst_acc = (sum(1 for r in abst_cases if r.get("abstention_correct")) / len(abst_cases)) if abst_cases else 0.0

    src_cases = [r for r in results if r.get("acceptable_sources")]
    src_acc = (sum(1 for r in src_cases if r.get("sources_correct")) / len(src_cases)) if src_cases else None

    agg = {
        "n": n,
        "prompt_variant": prompt_variant,
        "provider": settings.provider,
        "classification_accuracy": round(cls_acc, 3),
        "routing_accuracy": round(route_acc, 3),
        "routing_policy_compliance": round(policy_acc, 3),
        "execution_completion_rate": round(exec_acc, 3),
        "citation_rate": round(cit_rate, 3),
        "abstention_accuracy": round(abst_acc, 3),
        "source_accuracy": (round(src_acc, 3) if src_acc is not None else None),
        "total_cost_usd": round(sum(r["cost_usd"] for r in results), 6),
        "results": results,
    }
    return agg


if __name__ == "__main__":
    import sys
    variant = sys.argv[1] if len(sys.argv) > 1 else "improved"
    prov = sys.argv[2] if len(sys.argv) > 2 else None
    out = asyncio.run(run_eval(variant, provider_override=prov))
    print({k: v for k, v in out.items() if k != "results"})
