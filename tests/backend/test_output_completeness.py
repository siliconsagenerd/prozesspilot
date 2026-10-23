import json
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from prozesspilot.main import app
from prozesspilot.providers.base import LLMResult

client = TestClient(app)

CLS_JSON = json.dumps({"classification": "product_question", "confidence": 0.9, "reasoning": "ok"})
LONG_DRAFT = "A" * 500 + " [Test KB]"

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
        finish_reason="length",
        response_model="m-response",
    )

@pytest.fixture(autouse=True)
def mock_llm():
    with patch("prozesspilot.agents.classifier.complete_with_fallback", new=AsyncMock(side_effect=_fake_complete)), \
         patch("prozesspilot.agents.drafter.complete_with_fallback", new=AsyncMock(side_effect=_fake_complete)):
        yield

def test_provider_length_stop_is_captured_and_full_draft_preserved():
    r = client.post("/api/inquiries", json={"body": "Frage?", "customer_email": "anna@example.de"})
    iid = r.json()["id"]
    r2 = client.post(f"/api/inquiries/{iid}/run")
    assert r2.status_code == 200
    run_id = r2.json()["run_id"]
    run = client.get(f"/api/runs/{run_id}").json()
    draft_step = [s for s in run["steps"] if s["name"] == "draft"][0]
    assert draft_step["finish_reason"] == "length"
    assert draft_step["completion_status"] == "length_stopped"
    assert draft_step["response_model"] == "m-response"
    assert draft_step["requested_max_tokens"] is not None
    assert run["draft"]["original_text"] == LONG_DRAFT
    assert run["draft"]["original_text"] not in (draft_step["output_summary"],)
    assert len(draft_step["output_summary"]) <= 400
    assert draft_step["output_summary"] == LONG_DRAFT[:400]

def test_unknown_status_when_no_finish_reason():
    def _fake(prompt, system="", json_mode=False, max_tokens=None):
        if "classify" in system.lower() or "Classify" in prompt or "Klassifik" in prompt:
            return LLMResult(
            text=CLS_JSON, provider="ollama", model="m", tokens_in=1, tokens_out=1, cost_usd=0.0, latency_ms=1
        )
        return LLMResult(
            text=json.dumps({"text": "Kurze Antwort [Test KB]", "confidence": 0.9, "reasoning": "kb"}),
            provider="ollama",
            model="m",
            tokens_in=1,
            tokens_out=1,
            cost_usd=0.0,
            latency_ms=1,
        )
    with patch("prozesspilot.agents.classifier.complete_with_fallback", new=AsyncMock(side_effect=_fake)), \
         patch("prozesspilot.agents.drafter.complete_with_fallback", new=AsyncMock(side_effect=_fake)):
        r = client.post("/api/inquiries", json={"body": "Frage?", "customer_email": "anna@example.de"})
        iid = r.json()["id"]
        r2 = client.post(f"/api/inquiries/{iid}/run")
        run = client.get(f"/api/runs/{r2.json()['run_id']}").json()
        draft_step = [s for s in run["steps"] if s["name"] == "draft"][0]
        assert draft_step["finish_reason"] is None
        assert draft_step["completion_status"] == "unknown"
