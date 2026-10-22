import json
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from prozesspilot.main import app
from prozesspilot.providers.base import LLMResult

client = TestClient(app)

CLS_JSON = json.dumps({"classification": "product_question", "confidence": 0.92, "reasoning": "produktfrage"})
DRAFT_JSON = json.dumps({"text": "Sehr geehrte/r ..., vielen Dank. [Test KB]", "confidence": 0.9, "reasoning": "kb"})


def _fake_complete(prompt, system="", json_mode=False, max_tokens=None):
    if "classify" in system.lower() or "Classify" in prompt or "Klassifik" in prompt:
        return LLMResult(
            text=CLS_JSON, provider="ollama", model="m", tokens_in=10, tokens_out=5, cost_usd=0.0, latency_ms=1
        )
    return LLMResult(
        text=DRAFT_JSON, provider="ollama", model="m", tokens_in=10, tokens_out=5, cost_usd=0.0, latency_ms=1
    )


@pytest.fixture(autouse=True)
def mock_llm():
    with patch("prozesspilot.agents.classifier.complete_with_fallback", new=AsyncMock(side_effect=_fake_complete)), \
         patch("prozesspilot.agents.drafter.complete_with_fallback", new=AsyncMock(side_effect=_fake_complete)):
        yield


def test_approval_flow():
    r = client.post("/api/inquiries", json={"body": "Frage zum ErgoChair?", "customer_email": "anna@example.de"})
    iid = r.json()["id"]
    r2 = client.post(f"/api/inquiries/{iid}/run")
    run_id = r2.json()["run_id"]
    # approve
    r3 = client.post(f"/api/runs/{run_id}/approve", json={"action": "approve"})
    assert r3.status_code == 200
    run = client.get(f"/api/runs/{run_id}").json()
    assert run["state"] == "Approved"
    assert len(run["approvals"]) == 1


def test_reject_requires_reason():
    r = client.post("/api/inquiries", json={"body": "Frage?", "customer_email": "anna@example.de"})
    iid = r.json()["id"]
    r2 = client.post(f"/api/inquiries/{iid}/run")
    run_id = r2.json()["run_id"]
    r3 = client.post(f"/api/runs/{run_id}/approve", json={"action": "reject"})
    assert r3.status_code == 400


def test_edit_preserves_original():
    r = client.post("/api/inquiries", json={"body": "Frage?", "customer_email": "anna@example.de"})
    iid = r.json()["id"]
    r2 = client.post(f"/api/inquiries/{iid}/run")
    run_id = r2.json()["run_id"]
    client.post(f"/api/runs/{run_id}/approve", json={"action": "edit_approve", "edited_text": "edited reply"})
    run = client.get(f"/api/runs/{run_id}").json()
    assert run["draft"]["original_text"] != "edited reply"
    assert run["draft"]["edited_text"] == "edited reply"

def test_high_confidence_does_not_auto_approve_or_send():
    from unittest.mock import patch

    from prozesspilot.tools.registry import registry

    with patch("prozesspilot.agents.runtime.registry.call", wraps=registry.call) as mock_call:
        r = client.post("/api/inquiries", json={"body": "Frage zum ErgoChair?", "customer_email": "anna@example.de"})
        iid = r.json()["id"]
        r2 = client.post(f"/api/inquiries/{iid}/run")
        run_id = r2.json()["run_id"]

    run = client.get(f"/api/runs/{run_id}").json()
    assert run["state"] == "ReadyForReview"
    assert run["approvals"] == []
    called = [c.args[0] for c in mock_call.call_args_list]
    assert "send_email_mock" not in called
    assert "crm_update_mock" not in called
