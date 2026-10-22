import asyncio

from prozesspilot.tools.kb_search import kb_search


def test_kb_search_returns_citation():
    res = asyncio.run(kb_search("ErgoChair Preis"))
    assert res["results"]
    assert res["results"][0]["title"] == "Test KB"