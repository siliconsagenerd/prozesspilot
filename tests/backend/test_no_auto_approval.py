import json
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from prozesspilot.main import app
from prozesspilot.providers.base import LLMResult

client = TestClient(app)

CLS_JSON = json.dumps({"classification": "product_question", "confidence": 0.92, "reasoning": "produktfrage"})
DRAFT_JSON = json.dumps({"text": "Sehr geehrte/r ..., vielen Dank. [Test KB]", "confidence": 0.9, "reasoning": "kb"})


def _result(text):
    return LLMResult(
        text=text,
        provider="ollama",
        model="m",
        tokens_in=10,
        tokens_out=5,
        cost_usd=0.0,
        latency_ms=1,
    )


def _fake_complete(prompt, system="", json_mode=False, max_tokens=None):
    if "classify" in system.lower() or "Classify" in prompt or "Klassifik" in prompt:
        return _result(CLS_JSON)
    return _result(DRAFT_JSON)


@pytest.fixture(autouse=True)
def mock_llm():
    with patch("prozesspilot.agents.classifier.complete_with_fallback", new=AsyncMock(side_effect=_fake_complete)), \
         patch("prozesspilot.agents.drafter.complete_with_fallback", new=AsyncMock(side_effect=_fake_complete)):
        yield


def test_workflow_does_not_reach_approved_without_explicit_action():
    r = client.post("/api/inquiries", json={"body": "Frage zum ErgoChair?", "customer_email": "anna@example.de"})
    iid = r.json()["id"]
    r2 = client.post(f"/api/inquiries/{iid}/run")
    run_id = r2.json()["run_id"]

    run = client.get(f"/api/runs/{run_id}", headers={"X-ProzessPilot-Operator": "1"}).json()
    assert run["state"] != "Approved"
    assert run["approvals"] == []
