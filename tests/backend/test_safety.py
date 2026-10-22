import json
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select

from prozesspilot.config import settings
from prozesspilot.db.models import Draft
from prozesspilot.db.session import db_session
from prozesspilot.main import _rate_buckets, app
from prozesspilot.providers.base import LLMResult

client = TestClient(app)

CLS_JSON = json.dumps({"classification": "product_question", "confidence": 0.92, "reasoning": "produktfrage"})
DRAFT_JSON = json.dumps({"text": "Sehr geehrte/r ..., vielen Dank. [Test KB]", "confidence": 0.9, "reasoning": "kb"})


def _fake_complete(prompt, system="", json_mode=False, max_tokens=None):
    classify = "classify" in system.lower() or "Classify" in prompt
    if classify or "Klassifik" in prompt:
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


def test_oversized_body_returns_413(monkeypatch):
    monkeypatch.setattr(settings, "max_inquiry_body_chars", 5)
    r = client.post("/api/inquiries", json={"body": "123456"})
    assert r.status_code == 413


def test_rate_limit_returns_429(monkeypatch):
    monkeypatch.setattr(settings, "rate_limit_per_minute", 2)
    _rate_buckets.clear()
    r1 = client.post("/api/inquiries", json={"body": "a"})
    r2 = client.post("/api/inquiries", json={"body": "b"})
    r3 = client.post("/api/inquiries", json={"body": "c"})
    assert r1.status_code == 200
    assert r2.status_code == 200
    assert r3.status_code == 429


def test_kb_top_k_capped(monkeypatch):
    import asyncio

    from prozesspilot.tools.kb_search import kb_search

    monkeypatch.setattr(settings, "max_kb_results", 1)
    res = asyncio.run(kb_search("ErgoChair Preis", top_k=5))
    assert len(res["results"]) <= 1


def test_budget_guard_blocks_run(monkeypatch):
    monkeypatch.setattr(settings, "max_workflow_tokens", 1)
    monkeypatch.setattr(settings, "cost_cap_usd_per_run", 0.0)

    r = client.post("/api/inquiries", json={"body": "Frage zum ErgoChair?", "customer_email": "anna@example.de"})
    iid = r.json()["id"]
    r2 = client.post(f"/api/inquiries/{iid}/run")
    run_id = r2.json()["run_id"]

    run = client.get(f"/api/runs/{run_id}").json()
    assert run["state"] == "Failed"

    with db_session() as s:
        draft = s.execute(select(Draft).where(Draft.run_id == run_id)).scalar_one_or_none()
        assert draft is None
