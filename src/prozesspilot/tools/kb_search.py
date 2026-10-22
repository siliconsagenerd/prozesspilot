"""Knowledge-base search (lightweight local retrieval with citations)."""
from __future__ import annotations

import math
import re
from collections import Counter

from sqlalchemy import select

from prozesspilot.config import settings
from prozesspilot.db.models import KnowledgeSource
from prozesspilot.db.session import db_session

_UMAP = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})


def _normalize(text: str) -> str:
    return text.translate(_UMAP).lower()


_STOPWORDS = {
    "der", "die", "das", "und", "oder", "in", "im", "am", "an", "auf", "zu", "von",
    "fuer", "für", "mit", "ist", "sind", "ein", "eine", "einer", "einem", "den",
    "dem", "des", "ich", "sie", "wir", "es", "ob", "wie", "was", "wo", "wann",
    "the", "a", "and", "or", "on", "at", "to", "of", "for", "with",
    "morgen", "heute", "gestern",
}


def _tokens(t: str) -> list[str]:
    return [w for w in re.findall(r"\w+", _normalize(t)) if w not in _STOPWORDS]


_COMPLAINT_TERMS = (
    "zurueck",
    "rueckgabe",
    "beschwerde",
    "reklamation",
    "defekt",
    "beschadigt",
    "ersatz",
    "erstattung",
    "garantie",
    "kaputt",
    "fehlerhaft",
    "mangel",
    "quietsch",
)


def _complaint_boost(query: str, source: KnowledgeSource) -> float:
    if source.category not in ("policy", "escalation"):
        return 0.0
    q = _normalize(query)
    if any(term in q for term in _COMPLAINT_TERMS):
        return 0.25
    return 0.0


def _score(query: str, doc: str) -> float:
    q = set(_tokens(query))
    d = _tokens(doc)
    if not q or not d:
        return 0.0
    dc = Counter(d)
    overlap = sum(dc[w] for w in q if w in dc)
    return overlap / (math.sqrt(len(d)) + 1)


async def kb_search(query: str, top_k: int = 3) -> dict:
    top_k = min(top_k, settings.max_kb_results)
    with db_session() as s:
        sources = s.execute(select(KnowledgeSource)).scalars().all()
        scored = []
        for src in sources:
            sc = _score(query, src.title + " " + src.content) + _complaint_boost(query, src)
            scored.append((sc, src))
        scored.sort(key=lambda x: x[0], reverse=True)
        results = []
        for sc, src in scored[:top_k]:
            if sc <= 0:
                continue
            results.append(
                {
                    "id": src.id,
                    "source_key": src.source_key,
                    "title": src.title,
                    "category": src.category,
                    "snippet": src.content[:400],
                    "score": round(sc, 3),
                }
            )
        return {"query": query, "results": results}


def get_source(source_key: str) -> KnowledgeSource:
    with db_session() as s:
        src = s.execute(
            select(KnowledgeSource).where(KnowledgeSource.source_key == source_key)
        ).scalar_one_or_none()
        if src is None:
            raise ValueError(f"unknown source key: {source_key}")
        s.expunge(src)
        return src


def validate_source_keys(source_keys: list[str]) -> None:
    if not isinstance(source_keys, list) or not all(isinstance(x, str) for x in source_keys):
        raise ValueError(f"malformed source keys: {source_keys!r}")
    with db_session() as s:
        found = {row[0] for row in s.execute(select(KnowledgeSource.source_key)).all()}
    unknown = [key for key in source_keys if key not in found]
    if unknown:
        raise ValueError(f"unknown source keys: {unknown}")
