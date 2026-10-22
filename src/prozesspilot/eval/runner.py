"""Evaluation runner."""

from __future__ import annotations

import asyncio

from sqlalchemy import select

from prozesspilot.agents.runtime import run_workflow
from prozesspilot.config import settings
from prozesspilot.db.models import Evaluation, Inquiry, WorkflowRun
from prozesspilot.db.session import db_session
from prozesspilot.eval.cases import CASES


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


async def run_eval(prompt_variant: str = "improved", provider_override: str | None = None) -> dict:
    if provider_override:
        settings.provider = provider_override  # type: ignore
    results = []
    for case in CASES:
        # Validate case contract strictly
        if "deliberate_abstention" not in case or not isinstance(case["deliberate_abstention"], bool):
            raise ValueError(f"case {case.get('id')} missing boolean deliberate_abstention")
        if "acceptable_source_ids" not in case or not isinstance(case["acceptable_source_ids"], list):
            raise ValueError(f"case {case.get('id')} missing list acceptable_source_ids")

        # create inquiry
        with db_session() as s:
            inq = Inquiry(subject="", body=case["body"], channel="eval")
            # link customer if email present
            if case.get("customer_email"):
                from prozesspilot.db.models import Customer
                c = s.execute(select(Customer).where(Customer.email == case["customer_email"])).scalar_one_or_none()
                if c:
                    inq.customer_id = c.id
            s.add(inq)
            s.flush()
            inq_id = inq.id

        run_id = await run_workflow(inq_id, prompt_variant=prompt_variant)

        # gather inside db_session to avoid detached instance attribute errors
        with db_session() as s:
            r = s.get(WorkflowRun, run_id)
            predicted = r.classification
            routing = r.routing_decision
            expected_routing = (
                "requires_human_approval"
                if case["expected_routing"] == "requires_human_approval"
                else "ready_for_review"
            )

            from prozesspilot.db.models import Draft
            d = s.execute(select(Draft).where(Draft.run_id == run_id)).scalar_one_or_none()
            citations_present = bool(d and d.citations)
            citation_keys = [c.get("title") for c in (d.citations if d and d.citations else []) if isinstance(c, dict)]

            deliberate_abstention = case["deliberate_abstention"]
            abstention_correct = evaluate_abstention(deliberate_abstention, citations_present)

            acceptable_sources = case["acceptable_sources"]
            sources_correct = evaluate_source_ids(acceptable_sources, citation_keys)

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

            # fix provider/model from steps if available
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

            results.append(
                {
                    "case_id": case["id"],
                    "predicted": predicted,
                    "expected": case["expected_classification"],
                    "classification_correct": predicted == case["expected_classification"],
                    "routing": routing,
                    "expected_routing": expected_routing,
                    "routing_correct": routing == expected_routing,
                    "citations_present": citations_present,
                    "deliberate_abstention": deliberate_abstention,
                    "abstention_correct": abstention_correct,
                    "acceptable_sources": acceptable_sources,
                    "sources_found": citation_keys,
                    "sources_correct": sources_correct,
                    "latency_ms": r.total_latency_ms,
                    "cost_usd": r.total_cost_usd,
                }
            )

    # aggregate
    n = len(results)
    cls_acc = sum(1 for r in results if r["classification_correct"]) / n if n else 0
    route_acc = sum(1 for r in results if r["routing_correct"]) / n if n else 0
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
