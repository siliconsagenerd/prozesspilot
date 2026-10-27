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
    run = client.get(f"/api/runs/{run_id}", headers={"X-ProzessPilot-Operator": "1"}).json()
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
    run = client.get(f"/api/runs/{run_id}", headers={"X-ProzessPilot-Operator": "1"}).json()
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

    run = client.get(f"/api/runs/{run_id}", headers={"X-ProzessPilot-Operator": "1"}).json()
    assert run["state"] == "ReadyForReview"
    assert run["approvals"] == []
    called = [c.args[0] for c in mock_call.call_args_list]
    assert "send_email_mock" not in called
    assert "crm_update_mock" not in called


def _run_id_for(body="Frage zum ErgoChair?", email="anna@example.de"):
    r = client.post("/api/inquiries", json={"body": body, "customer_email": email})
    assert r.status_code == 200
    iid = r.json()["id"]
    r2 = client.post(f"/api/inquiries/{iid}/run")
    assert r2.status_code == 200
    return r2.json()["run_id"]


def test_ready_for_review_does_not_trigger_mock_send():
    from sqlalchemy import select

    from prozesspilot.config import settings
    from prozesspilot.db.models import AuditEvent
    from prozesspilot.db.session import db_session

    run_id = _run_id_for()
    run = client.get(f"/api/runs/{run_id}", headers={"X-ProzessPilot-Operator": "1"}).json()
    assert run["state"] == "ReadyForReview"
    assert run["requires_approval"] is False
    assert run["approvals"] == []
    assert not (settings.mock_email_dir / f"{run_id}.json").exists()

    with db_session() as s:
        events = s.execute(
            select(AuditEvent).where(
                AuditEvent.run_id == run_id,
                AuditEvent.event_type == "approved_and_mock_sent",
            )
        ).scalars().all()
    assert events == []


def test_explicit_approval_records_approval_and_mock_send():
    from sqlalchemy import select

    from prozesspilot.config import settings
    from prozesspilot.db.models import AuditEvent
    from prozesspilot.db.session import db_session

    run_id = _run_id_for()
    r = client.post(f"/api/runs/{run_id}/approve", json={"action": "approve"})
    assert r.status_code == 200

    run = client.get(f"/api/runs/{run_id}", headers={"X-ProzessPilot-Operator": "1"}).json()
    assert run["state"] == "Approved"
    assert len(run["approvals"]) == 1
    assert (settings.mock_email_dir / f"{run_id}.json").exists()

    with db_session() as s:
        events = s.execute(
            select(AuditEvent).where(
                AuditEvent.run_id == run_id,
                AuditEvent.event_type == "approved_and_mock_sent",
            )
        ).scalars().all()
    assert len(events) == 1


def test_repeated_approval_does_not_duplicate_mock_outbound():
    from sqlalchemy import select

    from prozesspilot.config import settings
    from prozesspilot.db.models import AuditEvent
    from prozesspilot.db.session import db_session

    run_id = _run_id_for()
    first = client.post(f"/api/runs/{run_id}/approve", json={"action": "approve"})
    assert first.status_code == 200

    email_file = settings.mock_email_dir / f"{run_id}.json"
    assert email_file.exists()
    mtime = email_file.stat().st_mtime

    with db_session() as s:
        before = len(
            s.execute(
                select(AuditEvent).where(
                    AuditEvent.run_id == run_id,
                    AuditEvent.event_type == "approved_and_mock_sent",
                )
            ).scalars().all()
        )

    second = client.post(f"/api/runs/{run_id}/approve", json={"action": "approve"})
    assert second.status_code == 200

    run = client.get(f"/api/runs/{run_id}", headers={"X-ProzessPilot-Operator": "1"}).json()
    assert run["state"] == "Approved"
    assert len(run["approvals"]) == 1
    assert email_file.stat().st_mtime == mtime

    with db_session() as s:
        after = len(
            s.execute(
                select(AuditEvent).where(
                    AuditEvent.run_id == run_id,
                    AuditEvent.event_type == "approved_and_mock_sent",
                )
            ).scalars().all()
        )
    assert after == before
