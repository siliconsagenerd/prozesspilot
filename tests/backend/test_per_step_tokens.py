import json
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from prozesspilot.main import app
from prozesspilot.providers.base import LLMResult

client = TestClient(app)
CLS = json.dumps({"classification": "product_question", "confidence": 0.9, "reasoning": "ok"})
DRAFT = json.dumps({"text": "Antwort [Test KB]", "confidence": 0.9, "reasoning": "ok"})

def fake_complete(prompt, system="", json_mode=False, max_tokens=None):
    if "classify" in system.lower() or "Classify" in prompt or "Klassifik" in prompt:
        assert max_tokens == 7
        return LLMResult(text=CLS, provider="ollama", model="m", tokens_in=1, tokens_out=1, cost_usd=0.0, latency_ms=1)
    assert max_tokens == 9
    return LLMResult(text=DRAFT, provider="ollama", model="m", tokens_in=1, tokens_out=1, cost_usd=0.0, latency_ms=1)

@pytest.fixture(autouse=True)
def mock_llm():
    with patch("prozesspilot.agents.classifier.complete_with_fallback", new=AsyncMock(side_effect=fake_complete)), \
         patch("prozesspilot.agents.drafter.complete_with_fallback", new=AsyncMock(side_effect=fake_complete)):
        yield

def test_per_step_token_limits():
    r = client.post("/api/inquiries", json={"body": "Frage?", "customer_email": "anna@example.de"})
    iid = r.json()["id"]
    r2 = client.post(f"/api/inquiries/{iid}/run", params={"classify_max_tokens": 7, "draft_max_tokens": 9})
    assert r2.status_code == 200
