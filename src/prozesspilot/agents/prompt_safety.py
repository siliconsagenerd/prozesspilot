"""Helpers for safely embedding untrusted user text in LLM prompts."""

from __future__ import annotations


def escape_for_xml_tag(text: str, tag: str = "inquiry") -> str:
    """Neutralise angle brackets so user text cannot break out of its wrapper.

    Replaces ``<`` and ``>`` with HTML entities, which LLMs read transparently
    but which prevent any ``</tag>`` (or other tag) from terminating the wrapper.
    """
    if text is None:
        return ""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap_inquiry(text: str) -> str:
    """Wrap untrusted inquiry text in an XML tag for prompt-injection mitigation."""
    return f"<inquiry>\n{escape_for_xml_tag(text)}\n</inquiry>"


def wrap_customer(customer: dict | None) -> str:
    """Wrap untrusted customer data so it cannot break out of its delimiter."""
    if not customer:
        return "none"
    import json

    return "<customer>\n" + escape_for_xml_tag(json.dumps(customer, ensure_ascii=False)) + "\n</customer>"

def wrap_kb_snippet(title: str, snippet: str) -> str:
    """Escape a KB title/snippet before embedding in a prompt."""
    return f"- [{escape_for_xml_tag(title)}] <kb>\n{escape_for_xml_tag(snippet)}\n</kb>"
