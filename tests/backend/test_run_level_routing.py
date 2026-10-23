"""Run-level routing confidence regression tests."""
import json
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from prozesspilot.agents.runtime import _route
from prozesspilot.db.models import Customer
from prozesspilot.db.session import db_session
from prozesspilot.eval.export import extract_run_record
from prozesspilot.main import app
from prozesspilot.providers.base import LLMResult

client = TestClient(app)


def _llm_result(text):
    return LLMResult(
        text=text,
        provider="ollama",
        model="m",
        tokens_in=10,
        tokens_out=5,
        cost_usd=0.0,
        latency_ms=1,
        finish_reason="stop",
        response_model="m-response",
    )


def _run_with_confidences(classification_confidence, draft_confidence, body):
    cls_json = json.dumps(
        {
            "classification": "product_question",
            "confidence": classification_confidence,
            "reasoning": "ok",
        }
    )
    draft_json = json.dumps(
        {
            "text": "Antwort [Test KB]",
            "confidence": draft_confidence,
            "reasoning": "kb",
        }
    )

    def fake_complete(prompt, system="", json_mode=False, max_tokens=None):
        if "classify" in system.lower() or "Classify" in prompt or "Klassifik" in prompt:
            return _llm_result(cls_json)
        return _llm_result(draft_json)

    with patch(
        "prozesspilot.agents.classifier.complete_with_fallback",
        new=AsyncMock(side_effect=fake_complete),
    ), patch(
        "prozesspilot.agents.drafter.complete_with_fallback",
        new=AsyncMock(side_effect=fake_complete),
    ):
        r = client.post("/api/inquiries", json={"body": body})
        assert r.status_code == 200
        run_id = client.post(f"/api/inquiries/{r.json()['id']}/run").json()["run_id"]
    return extract_run_record(run_id)


def test_high_classification_low_draft_routes_on_classification():
    record = _run_with_confidences(0.95, 0.1, "ErgoChair 3000 Preis")
    assert record["confidence"] == 0.95
    assert record["classification_confidence"] == 0.95
    assert record["draft"]["confidence"] == 0.1
    assert record["draft"]["draft_confidence"] == 0.1
    assert record["routing_decision"] == "ready_for_review"
    assert _route("product_question", 0.95, None)["decision"] == "ready_for_review"


def test_low_classification_high_draft_routes_on_classification():
    record = _run_with_confidences(0.4, 0.95, "ErgoChair 3000 Preis")
    assert record["confidence"] == 0.4
    assert record["classification_confidence"] == 0.4
    assert record["draft"]["confidence"] == 0.95
    assert record["draft"]["draft_confidence"] == 0.95
    assert record["routing_decision"] == "requires_human_approval"
    assert _route("product_question", 0.4, None)["decision"] == "requires_human_approval"


def test_premium_high_draft_still_escalates():
    with db_session() as s:
        s.add(Customer(name="Premium", email="premium@example.de", tier="premium"))
    record = _run_with_confidences(
        0.95, 0.95, "ErgoChair 3000 Preis premium@example.de"
    )
    assert record["confidence"] == 0.95
    assert record["draft"]["confidence"] == 0.95
    assert record["routing_decision"] == "requires_human_approval"
    assert _route(
        "product_question", 0.95, {"tier": "premium"}
    )["decision"] == "requires_human_approval"


def test_premium_low_draft_still_escalates():
    with db_session() as s:
        s.add(Customer(name="Premium", email="premium@example.de", tier="premium"))
    record = _run_with_confidences(
        0.95, 0.1, "ErgoChair 3000 Preis premium@example.de"
    )
    assert record["confidence"] == 0.95
    assert record["draft"]["confidence"] == 0.1
    assert record["routing_decision"] == "requires_human_approval"
    assert _route(
        "product_question", 0.95, {"tier": "premium"}
    )["decision"] == "requires_human_approval"
