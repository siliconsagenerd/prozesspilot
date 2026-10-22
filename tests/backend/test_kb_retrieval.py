import asyncio
import json
from pathlib import Path

from sqlalchemy import select

from prozesspilot.db.models import KnowledgeSource
from prozesspilot.db.session import db_session
from prozesspilot.tools.kb_search import kb_search

ROOT = Path(__file__).resolve().parents[2]
KB = json.loads((ROOT / "data" / "kb" / "sources.json").read_text(encoding="utf-8"))


def _seed():
    with db_session() as s:
        for item in KB:
            exists = s.execute(
                select(KnowledgeSource).where(KnowledgeSource.source_key == item["source_key"])
            ).scalar_one_or_none()
            if exists is None:
                s.add(KnowledgeSource(**item))


def _cleanup():
    keys = {item["source_key"] for item in KB}
    with db_session() as s:
        for src in s.execute(select(KnowledgeSource)).scalars().all():
            if src.source_key in keys:
                s.delete(src)


def test_complaint_return_retrieves_policy():
    _seed()
    try:
        res = asyncio.run(kb_search("Mein ErgoChair 3000 quietscht nach zwei Wochen. Ich moechte ihn zurueckgeben."))
        titles = [r["title"] for r in res["results"]]
        assert "Rückgabe- und Beschwerdepolitik" in titles
    finally:
        _cleanup()


def test_open_complaint_retrieves_policy_or_escalation():
    _seed()
    try:
        res = asyncio.run(kb_search("Ich habe eine offene Beschwerde zum Monitorarm, Erstattung ausstehend."))
        titles = [r["title"] for r in res["results"]]
        assert any(t in titles for t in ("Rückgabe- und Beschwerdepolitik", "Eskalationsrichtlinie"))
    finally:
        _cleanup()


def test_product_question_retains_product_source():
    _seed()
    try:
        res = asyncio.run(kb_search("Was kostet der ErgoChair 3000 und welche Farben gibt es?"))
        assert res["results"]
        assert res["results"][0]["title"] == "Produkt: ErgoChair 3000"
    finally:
        _cleanup()


def test_unrelated_query_no_fabricated_relevance():
    _seed()
    try:
        res = asyncio.run(kb_search("Wettervorhersage fuer morgen in Berlin"))
        assert res["results"] == []
    finally:
        _cleanup()

def test_case_09_damaged_invoice_retrieves_policy():
    _seed()
    try:
        res = asyncio.run(kb_search("Der gelieferte ErgoChair 3000 ist beschädigt und die Rechnung ist falsch."))
        titles = [r["title"] for r in res["results"]]
        assert "Rückgabe- und Beschwerdepolitik" in titles
    finally:
        _cleanup()
