"""Knowledge-base search (lightweight local retrieval with citations)."""

from __future__ import annotations

import math
import re

from sqlalchemy import select

from prozesspilot.config import settings
from prozesspilot.db.models import KnowledgeSource
from prozesspilot.db.session import db_session


def _tokens(t: str) -> list[str]:
    return re.findall(r"\w+", t.lower())


def _score(query: str, doc: str) -> float:
    q = set(_tokens(query))
    d = _tokens(doc)
    if not q or not d:
        return 0.0
    # tf-idf-ish cosine-ish simple score
    from collections import Counter

    dc = Counter(d)
    overlap = sum(dc[w] for w in q if w in dc)
    # length normalization
    return overlap / (math.sqrt(len(d)) + 1)


async def kb_search(query: str, top_k: int = 3) -> dict:
    top_k = min(top_k, settings.max_kb_results)
    with db_session() as s:
        sources = s.execute(select(KnowledgeSource)).scalars().all()
        scored = []
        for src in sources:
            sc = _score(query, src.title + " " + src.content)
            scored.append((sc, src))
        scored.sort(key=lambda x: x[0], reverse=True)
        results = []
        for sc, src in scored[:top_k]:
            if sc <= 0:
                continue
            results.append(
                {
                    "id": src.id,
                    "title": src.title,
                    "category": src.category,
                    "snippet": src.content[:400],
                    "score": round(sc, 3),
                }
            )
        return {"query": query, "results": results}