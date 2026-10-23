"""Explicit citation extraction from draft text."""
from __future__ import annotations

import re
from typing import Any


def _normalize(value: Any) -> str:
    return " ".join(str(value or "").strip().lower().split())


def _source_identity(source: dict[str, Any]) -> str:
    for key in ("source_key", "title", "id"):
        value = source.get(key)
        if value:
            return str(value)
    return ""


def _match_source(marker: str, retrieved_sources: list[dict[str, Any]]) -> dict[str, Any] | None:
    norm_marker = _normalize(marker)
    if not norm_marker:
        return None
    for source in retrieved_sources:
        if not isinstance(source, dict):
            continue
        candidates = {
            _normalize(source.get("title")),
            _normalize(source.get("source_key")),
            _normalize(source.get("id")),
        }
        title = str(source.get("title") or "")
        if ":" in title:
            candidates.add(_normalize(title.split(":", 1)[-1]))
        if norm_marker in candidates:
            return source
    return None


def extract_explicit_citations(
    text: str | None,
    retrieved_sources: list[dict[str, Any]] | None = None,
) -> tuple[list[dict[str, Any]], list[str]]:
    """Return (cited_sources, citation_format_issues).

    Only markers/references that resolve to a retrieved source are citations.
    Malformed or unmatched bracket attempts are returned as format issues.
    """
    sources = [item for item in (retrieved_sources or []) if isinstance(item, dict)]
    cited: list[dict[str, Any]] = []
    seen: set[str] = set()
    issues: list[str] = []

    def add_source(source: dict[str, Any]) -> None:
        identity = _source_identity(source)
        if identity in seen:
            return
        seen.add(identity)
        cited.append(dict(source))

    if text:
        for match in re.finditer(r"\[([^\]]*)\]", text):
            marker = match.group(1).strip()
            if not marker:
                issues.append("[]")
                continue
            source = _match_source(marker, sources)
            if source is not None:
                add_source(source)
            else:
                issues.append(f"[{marker}]")

        # Record unclosed bracket attempts without treating them as citations.
        for match in re.finditer(r"\[[^\]]*$", text, re.MULTILINE):
            issues.append(match.group(0))

        # Support inline title references only when the full title appears
        # as a standalone phrase, not as a substring of another word.
        import re as _re
        for source in sources:
            title = str(source.get("title") or "").strip()
            if not title:
                continue
            norm_title = _normalize(title)
            norm_text = _normalize(text)
            pattern = r"(?<![\w])" + _re.escape(norm_title) + r"(?![\w])"
            if _re.search(pattern, norm_text):
                add_source(source)

    return cited, issues


def extract_citation_report(
    text: str | None,
    retrieved_sources: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    cited, issues = extract_explicit_citations(text, retrieved_sources)
    return {"cited_sources": cited, "citation_format_issues": issues}


# Backwards/alternative spellings.
extract_citations = extract_explicit_citations
parse_citations = extract_explicit_citations
def extract_cited_sources(text, retrieved_sources=None):
    return extract_explicit_citations(text, retrieved_sources)[0]


def get_citation_format_issues(text, retrieved_sources=None):
    return extract_explicit_citations(text, retrieved_sources)[1]
