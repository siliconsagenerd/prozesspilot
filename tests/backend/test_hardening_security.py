import pytest
import asyncio
from prozesspilot.tools.email_mock import send_email_mock
from prozesspilot.observability.audit import audit
from prozesspilot.db.models import AuditEvent
from prozesspilot.db.session import db_session
from prozesspilot.providers.openai import OpenAIProvider
from prozesspilot.providers.ollama import OllamaProvider
from prozesspilot.config import settings
from fastapi.testclient import TestClient
from prozesspilot.main import app

def test_email_mock_path_traversal_sanitized(tmp_path, monkeypatch):
    monkeypatch.setattr(settings, "mock_email_dir", tmp_path)
    res = asyncio.run(send_email_mock("user@example.de", "Test", "Body", "../../etc/passwd"))
    assert res["mock"] is True
    assert "passwd" not in res["path"] or "sanitized" in res["path"] or tmp_path.as_posix() in res["path"]
    assert (tmp_path).exists()

def test_audit_scrubs_secrets():
    audit("test_run_sec", "test_event", actor="system", payload={"api_key": "supersecret123", "normal_field": "ok"})
    with db_session() as s:
        evt = s.query(AuditEvent).filter_by(run_id="test_run_sec").order_by(AuditEvent.id.desc()).first()
        assert evt is not None
        assert evt.payload.get("api_key") == "[REDACTED]"
        assert evt.payload.get("normal_field") == "ok"

def test_provider_model_and_host_validation():
    p = OpenAIProvider()
    p.model = "unauthorized-malicious-model"
    p.api_key = "dummy"
    with pytest.raises(ValueError, match="allowlist"):
        asyncio.run(p.complete("test"))

    p_ol = OllamaProvider()
    p_ol.base_url = "http://malicious-external-site.com"
    with pytest.raises(ValueError, match="not permitted"):
        asyncio.run(p_ol.complete("test"))

def test_csrf_origin_check():
    client = TestClient(app)
    # Untrusted origin on POST to API
    resp = client.post("/api/inquiries", json={"body": "Hello"}, headers={"Origin": "https://evil-attacker.com"})
    assert resp.status_code == 403
    assert resp.json()["detail"] == "untrusted origin"
