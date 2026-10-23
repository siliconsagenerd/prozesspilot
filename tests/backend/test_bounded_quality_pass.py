"""Instruction/contract regression tests for the bounded quality pass.

These are mocked contract checks. They do not prove that a live model always
complies with the drafting instructions.
"""
import json
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from prozesspilot.agents.drafter import BASELINE_SYSTEM, IMPROVED_SYSTEM
from prozesspilot.agents.runtime import _route
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


def test_order_status_citation_instruction_contract():
    """Instruction/contract test: drafting systems require cited policy sources."""
    for system in (BASELINE_SYSTEM, IMPROVED_SYSTEM):
        lowered = system.lower()
        assert "order-status" in lowered
        assert "delivery times" in lowered
        assert "status definitions" in lowered
        assert "cite" in lowered
        assert "tracking" in lowered
        assert "stock" in lowered
        assert "order-lookup" in lowered or "order lookup" in lowered


def test_spam_drafter_receives_no_product_kb_context():
    cls_json = json.dumps({"classification": "spam", "confidence": 0.99, "reasoning": "spam"})
    draft_json = json.dumps({"text": "Keine Antwort noetig.", "confidence": 0.1, "reasoning": "spam"})

    def fake_complete(prompt, system="", json_mode=False, max_tokens=None):
        if "classify" in system.lower() or "Classify" in prompt or "Klassifik" in prompt:
            return _llm_result(cls_json)
        assert "(no sources)" in prompt
        return _llm_result(draft_json)

    with patch("prozesspilot.agents.classifier.complete_with_fallback", new=AsyncMock(side_effect=fake_complete)), \
         patch("prozesspilot.agents.drafter.complete_with_fallback", new=AsyncMock(side_effect=fake_complete)):
        r = client.post("/api/inquiries", json={"body": "Gewinnspiel jetzt klicken",
                                      "customer_email": "anna@example.de"})
        assert r.status_code == 200
        run_id = client.post(f"/api/inquiries/{r.json()['id']}/run").json()["run_id"]
    record = extract_run_record(run_id)
    step = next(s for s in record["steps"] if s["name"] == "kb_search")
    assert step["status"] == "skipped"
    assert record["retrieved_sources"] == []


def test_classification_and_draft_confidence_stored_separately():
    cls_json = json.dumps({"classification": "product_question", "confidence": 0.7, "reasoning": "ok"})
    draft_json = json.dumps({"text": "Antwort [Test KB]", "confidence": 0.4, "reasoning": "kb"})

    def fake_complete(prompt, system="", json_mode=False, max_tokens=None):
        if "classify" in system.lower() or "Classify" in prompt or "Klassifik" in prompt:
            return _llm_result(cls_json)
        return _llm_result(draft_json)

    with patch("prozesspilot.agents.classifier.complete_with_fallback", new=AsyncMock(side_effect=fake_complete)), \
         patch("prozesspilot.agents.drafter.complete_with_fallback", new=AsyncMock(side_effect=fake_complete)):
        r = client.post("/api/inquiries", json={"body": "ErgoChair 3000 Preis", "customer_email": "anna@example.de"})
        assert r.status_code == 200
        run_id = client.post(f"/api/inquiries/{r.json()['id']}/run").json()["run_id"]
    record = extract_run_record(run_id)
    assert record["confidence"] == 0.7
    assert record["classification_confidence"] == 0.7
    assert record["draft"]["confidence"] == 0.4
    assert record["draft"]["draft_confidence"] == 0.4
    # Routing uses the documented classification confidence, not the draft confidence.
    assert _route("product_question", 0.7, None)["requires_approval"] is True
    assert _route("product_question", 0.4, None)["requires_approval"] is True


def test_routing_policy_compliance_vs_fixture_label_mismatch():
    # A complaint prediction is policy-compliant with approval, even if a frozen
    # fixture (for example a product question) expected ready_for_review.
    policy = _route("complaint", 0.99, None)
    assert policy["decision"] == "requires_human_approval"
    assert policy["decision"] != "ready_for_review"
