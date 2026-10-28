import asyncio
import glob
import json
from unittest.mock import AsyncMock, patch

import httpx
import pytest

from prozesspilot.config import settings
from prozesspilot.main import app
from prozesspilot.providers.base import LLMResult
from prozesspilot.tools import registry as reg

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


async def _run_to_approval(client):
    r = await client.post("/api/inquiries", json={"body": "Frage zum ErgoChair?", "customer_email": "anna@example.de"})
    iid = r.json()["id"]
    r2 = await client.post(f"/api/inquiries/{iid}/run")
    return r2.json()["run_id"]


def test_concurrent_approval_one_winner():
    async def main():
        transport = httpx.ASGITransport(app=app, raise_app_exceptions=False)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            run_id = await _run_to_approval(client)
            responses = await asyncio.gather(
                client.post(f"/api/runs/{run_id}/approve", json={"action": "approve"}),
                client.post(f"/api/runs/{run_id}/approve", json={"action": "approve"}),
            )
            statuses = sorted(r.status_code for r in responses)
            assert all(code == 200 for code in statuses), statuses
            run = (await client.get(f"/api/runs/{run_id}", headers={"X-ProzessPilot-Operator": "1"})).json()
            assert run["state"] == "Approved"
            assert run["email_sent"] is True
            assert run["outbound_completed"] is True

    asyncio.run(main())


def test_partial_failure_retries_without_duplicate_email():
    async def main():
        transport = httpx.ASGITransport(app=app, raise_app_exceptions=False)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            run_id = await _run_to_approval(client)
            orig_call = reg.registry.call
            calls = {"crm": 0}

            async def flaky(name, *a, **k):
                if name == "crm_update_mock":
                    calls["crm"] += 1
                    if calls["crm"] == 1:
                        raise RuntimeError("crm boom")
                return await orig_call(name, *a, **k)

            reg.registry.call = flaky
            try:
                r = await client.post(f"/api/runs/{run_id}/approve", json={"action": "approve"})
                assert r.status_code >= 400
            finally:
                reg.registry.call = orig_call

            before = len(glob.glob(str(settings.mock_email_dir / "*.json")))
            r2 = await client.post(f"/api/runs/{run_id}/approve", json={"action": "approve"})
            assert r2.status_code == 200
            after = len(glob.glob(str(settings.mock_email_dir / "*.json")))
            assert after == before, (before, after)

            run = (await client.get(f"/api/runs/{run_id}", headers={"X-ProzessPilot-Operator": "1"})).json()
            assert run["state"] == "Approved"
            assert run["email_sent"] is True
            assert run["crm_updated"] is True
            assert run["outbound_completed"] is True

    asyncio.run(main())
