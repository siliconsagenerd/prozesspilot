from fastapi.testclient import TestClient

from prozesspilot.config import settings
from prozesspilot.main import app

client = TestClient(app)


def test_public_demo_snapshot_without_credentials():
    r = client.get("/public/demo-snapshot")
    assert r.status_code == 200
    data = r.json()
    assert data["label"] == "Recorded example from a completed live run — not a new inference."
    assert data["recorded_example"] is True
    assert data["new_inference"] is False
    assert len(data["retrieved_sources"]) == 3
    assert len(data["cited_sources"]) == 1
    assert data["classification"] == "complaint"
    assert data["requires_approval"] is True
    assert data["approval_performed"] is False
    assert data["customer_sending"] == "disabled"


def test_protected_api_rejects_unauthenticated(monkeypatch):
    monkeypatch.setattr(settings, "operator_auth_required", True)
    r = client.get("/api/inquiries")
    assert r.status_code == 401
    r_allowed = client.get("/api/inquiries", headers={"X-ProzessPilot-Operator": "1"})
    assert r_allowed.status_code == 401


def test_public_cannot_invoke_inference(monkeypatch):
    monkeypatch.setattr(settings, "operator_auth_required", True)
    r = client.post("/api/inquiries/demo/run")
    assert r.status_code == 401


def test_public_cannot_modify_data(monkeypatch):
    monkeypatch.setattr(settings, "operator_auth_required", True)
    r = client.post("/api/inquiries", json={"body": "test"})
    assert r.status_code == 401


def test_public_cannot_approve_draft(monkeypatch):
    monkeypatch.setattr(settings, "operator_auth_required", True)
    r = client.post("/api/runs/demo/approve", json={"action": "approve"})
    assert r.status_code == 401
