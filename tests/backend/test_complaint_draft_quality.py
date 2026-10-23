import json
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from prozesspilot.agents.drafter import BASELINE_SYSTEM, IMPROVED_SYSTEM
from prozesspilot.eval.export import extract_run_record
from prozesspilot.main import app
from prozesspilot.providers.base import LLMResult

client = TestClient(app)
CLS_JSON = json.dumps({"classification": "product_question", "confidence": 0.9, "reasoning": "ok"})


def _make_fake(draft_text):
    def _fake_complete(prompt, system="", json_mode=False, max_tokens=None):
        if "classify" in system.lower() or "Klassifik" in prompt:
            return LLMResult(
                text=CLS_JSON,
                provider="ollama",
                model="m",
                tokens_in=10,
                tokens_out=5,
                cost_usd=0.0,
                latency_ms=1,
                finish_reason="stop",
                response_model="m-response",
            )
        return LLMResult(
            text=json.dumps({"text": draft_text, "confidence": 0.9, "reasoning": "kb"}),
            provider="ollama",
            model="m",
            tokens_in=10,
            tokens_out=5,
            cost_usd=0.0,
            latency_ms=1,
            finish_reason="stop",
            response_model="m-response",
        )

    return _fake_complete


def _run(draft_text):
    fake = _make_fake(draft_text)
    with patch("prozesspilot.agents.classifier.complete_with_fallback", new=AsyncMock(side_effect=fake)), \
         patch("prozesspilot.agents.drafter.complete_with_fallback", new=AsyncMock(side_effect=fake)):
        r = client.post("/api/inquiries", json={"body": "ErgoChair 3000 Preis", "customer_email": "anna@example.de"})
        assert r.status_code == 200
        iid = r.json()["id"]
        r2 = client.post(f"/api/inquiries/{iid}/run")
        assert r2.status_code == 200
        return r2.json()["run_id"]


def test_prompt_contains_complaint_quality_rules():
    for system in (BASELINE_SYSTEM, IMPROVED_SYSTEM):
        lowered = system.lower()
        assert "30-day unused-item return" in lowered
        assert "defect remedies" in lowered
        assert "invoice corrections" in lowered
        assert "used merely because a defect" in lowered
        assert "escalation" in lowered


def test_long_defect_draft_distinguishes_return_from_defect():
    draft = (
        "Sehr geehrte Kundin, vielen Dank fuer Ihre Nachricht. "
        + "Bei einem Defekt bieten wir Ersatz oder Reparatur an. " * 30
        + "[Test KB]"
    )
    run_id = _run(draft)
    record = extract_run_record(run_id)
    full_text = record["draft"]["full_text"]
    assert "Ersatz oder Reparatur" in full_text
    assert "Rückgabe innerhalb von 30 Tagen" not in full_text
    assert len(record["cited_sources"]) == 1
    assert record["citation_format_issues"] == []


def test_long_invoice_draft_does_not_promise_correction_without_support():
    draft = (
        "Sehr geehrte Frau Mueller, vielen Dank fuer Ihre Nachricht. "
        + "Eine Korrektur der Rechnung kann ich aus den vorliegenden Informationen nicht bestaetigen. " * 20
        + "[Test KB]"
    )
    run_id = _run(draft)
    record = extract_run_record(run_id)
    full_text = record["draft"]["full_text"].lower()
    assert "nicht bestaetigen" in full_text
    assert "korrigieren wir" not in full_text
    assert len(record["cited_sources"]) == 1
    assert record["citation_format_issues"] == []


def test_long_draft_preserves_explicit_citations():
    draft = (
        "Einleitung. " * 40
        + "Antwort mit Quelle [Test KB]. "
        + "Abschluss. " * 40
    )
    run_id = _run(draft)
    record = extract_run_record(run_id)
    assert len(record["cited_sources"]) == 1
    assert (record["cited_sources"][0].get("title") or record["cited_sources"][0].get("source_key")) == "Test KB"
    assert record["citation_format_issues"] == []


def test_long_malformed_citation_remains_format_issue():
    draft = (
        "Einleitung. " * 40
        + "Antwort mit [Unknown Source]. "
        + "Abschluss. " * 40
    )
    run_id = _run(draft)
    record = extract_run_record(run_id)
    assert record["cited_sources"] == []
    assert "[Unknown Source]" in record["citation_format_issues"]
