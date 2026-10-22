"""Evaluation runner."""

from __future__ import annotations

import asyncio

from sqlalchemy import select

from prozesspilot.agents.runtime import run_workflow
from prozesspilot.config import settings
from prozesspilot.db.models import Evaluation, Inquiry, WorkflowRun
from prozesspilot.db.session import db_session
from prozesspilot.eval.cases import CASES


async def run_eval(prompt_variant: str = "improved", provider_override: str | None = None) -> dict:
    if provider_override:
        settings.provider = provider_override  # type: ignore
    results = []
    for case in CASES:
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
        # gather
        with db_session() as s:
            r = s.get(WorkflowRun, run_id)
            predicted = r.classification
            routing = r.routing_decision
            expected_routing = (
                "requires_human_approval"
                if case["expected_routing"] == "requires_human_approval"
                else "ready_for_review"
            )
            # check citations: draft has citations?
            from prozesspilot.db.models import Draft

            d = s.execute(select(Draft).where(Draft.run_id == run_id)).scalar_one_or_none()
            citations_present = bool(d and d.citations)
            row = Evaluation(
                case_id=case["id"],
                prompt_variant=prompt_variant,
                model_provider=r.steps[0].model_provider if False else settings.provider,
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
                "latency_ms": r.total_latency_ms,
                "cost_usd": r.total_cost_usd,
            }
        )
    # aggregate
    n = len(results)
    cls_acc = sum(1 for r in results if r["classification_correct"]) / n if n else 0
    route_acc = sum(1 for r in results if r["routing_correct"]) / n if n else 0
    cit_rate = sum(1 for r in results if r["citations_present"]) / n if n else 0
    agg = {
        "n": n,
        "prompt_variant": prompt_variant,
        "provider": settings.provider,
        "classification_accuracy": round(cls_acc, 3),
        "routing_accuracy": round(route_acc, 3),
        "citation_rate": round(cit_rate, 3),
        "total_cost_usd": round(sum(r["cost_usd"] for r in results), 6),
        "avg_latency_ms": int(sum(r["latency_ms"] for r in results) / n) if n else 0,
        "results": results,
    }
    return agg


def run_eval_sync():
    return asyncio.run(run_eval(prompt_variant="improved"))