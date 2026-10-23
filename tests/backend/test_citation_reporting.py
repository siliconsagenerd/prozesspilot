import json
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from prozesspilot.db.models import KnowledgeSource
from prozesspilot.db.session import db_session
from prozesspilot.eval.citations import extract_explicit_citations
from prozesspilot.eval.export import extract_run_record
from prozesspilot.main import app
from prozesspilot.providers.base import LLMResult

client = TestClient(app)

CLS_JSON = json.dumps({"classification": "product_question", "confidence": 0.9, "reasoning": "ok"})


def _make_fake(draft_text):
    def _fake_complete(prompt, system="", json_mode=False, max_tokens=None):
        if "classify" in system.lower() or "Klassifik" in prompt:
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
            text=json.dumps({"text": draft_text, "confidence": 0.9, "reasoning": "kb"}),
            provider="ollama",
            model="m",
            tokens_in=10,
            tokens_out=5,
            cost_usd=0.0,
            latency_ms=1,
            finish_reason="stop",
            response_model="m-response",
        )

    return _fake_complete


def _run(draft_text):
    fake = _make_fake(draft_text)
    with patch("prozesspilot.agents.classifier.complete_with_fallback", new=AsyncMock(side_effect=fake)), \
         patch("prozesspilot.agents.drafter.complete_with_fallback", new=AsyncMock(side_effect=fake)):
        r = client.post("/api/inquiries", json={"body": "ErgoChair 3000 Preis", "customer_email": "anna@example.de"})
        assert r.status_code == 200
        iid = r.json()["id"]
        r2 = client.post(f"/api/inquiries/{iid}/run")
        assert r2.status_code == 200
        return r2.json()["run_id"]


def test_draft_with_no_markers_has_zero_cited_sources():
    run_id = _run("Keine Zitation hier.")
    record = extract_run_record(run_id)
    assert record["cited_sources"] == []
    assert record["draft"]["cited_sources"] == []
    assert record["retrieved_sources"]


def test_draft_citing_one_of_several_retrieved_sources():
    with db_session() as s:
        s.add(KnowledgeSource(title="Other KB", category="product", content="other", source_path="o"))
    run_id = _run("Antwort [Test KB].")
    record = extract_run_record(run_id)
    assert len(record["cited_sources"]) == 1
    assert (record["cited_sources"][0].get("title") or record["cited_sources"][0].get("source_key")) == "Test KB"
    assert len(record["retrieved_sources"]) >= 1


def test_malformed_marker_recorded_as_format_issue():
    run_id = _run("Antwort [Unknown Source].")
    record = extract_run_record(run_id)
    assert record["cited_sources"] == []
    assert "[Unknown Source]" in record["citation_format_issues"]


def test_existing_retrieval_results_preserved():
    run_id = _run("Antwort [Test KB].")
    record = extract_run_record(run_id)
    assert record["retrieved_sources"]
    assert any((s.get("title") or s.get("source_key")) == "Test KB" for s in record["retrieved_sources"])


def test_extract_explicit_citations_direct():
    sources = [{"source_key": "a", "title": "A"}, {"source_key": "b", "title": "B"}]
    cited, issues = extract_explicit_citations("x [A] [bad]", sources)
    assert [s["source_key"] for s in cited] == ["a"]
    assert issues == ["[bad]"]
