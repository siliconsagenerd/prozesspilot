import json
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from prozesspilot.eval.export import extract_run_record, render_review_packet
from prozesspilot.main import app
from prozesspilot.providers.base import LLMResult

client = TestClient(app)

CLS_JSON = json.dumps({"classification": "product_question", "confidence": 0.9, "reasoning": "ok"})
LONG_DRAFT = "A" * 400 + " IMPORTANT CITATION [Test KB] and substantive text after char 400"


def _fake_complete(prompt, system="", json_mode=False, max_tokens=None):
    if "classify" in system.lower() or "Classify" in prompt or "Klassifik" in prompt:
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
        text=json.dumps({"text": LONG_DRAFT, "confidence": 0.9, "reasoning": "kb"}),
        provider="ollama",
        model="m",
        tokens_in=10,
        tokens_out=5,
        cost_usd=0.0,
        latency_ms=1,
        finish_reason="stop",
        response_model="m-response",
    )


@pytest.fixture(autouse=True)
def mock_llm():
    with patch("prozesspilot.agents.classifier.complete_with_fallback", new=AsyncMock(side_effect=_fake_complete)), \
         patch("prozesspilot.agents.drafter.complete_with_fallback", new=AsyncMock(side_effect=_fake_complete)):
        yield


def test_full_draft_survives_export_and_packet():
    r = client.post("/api/inquiries", json={"body": "Frage?", "customer_email": "anna@example.de"})
    assert r.status_code == 200
    iid = r.json()["id"]
    r2 = client.post(f"/api/inquiries/{iid}/run")
    assert r2.status_code == 200
    run_id = r2.json()["run_id"]

    record = extract_run_record(run_id)
    assert record["draft"]["full_text"] == LONG_DRAFT
    assert len(record["draft"]["full_text"]) > 400
    assert "IMPORTANT CITATION" in record["draft"]["full_text"]
    assert record["draft"]["review_status"] == "full"

    packet = render_review_packet([record])
    assert "IMPORTANT CITATION" in packet
    assert "substantive text after char 400" in packet
