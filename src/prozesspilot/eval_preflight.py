"""Fail-closed preflight checks for Laya evaluation runs."""

from __future__ import annotations

from typing import Any

CLASSIFICATIONS = {
    "product_question",
    "complaint",
    "order_status",
    "quote_request",
    "spam",
    "unclear",
}


class PreflightError(RuntimeError):
    """Raised when evaluation configuration is incomplete or unsafe."""


def _get(settings: Any, name: str) -> Any:
    if isinstance(settings, dict):
        return settings.get(name)
    return getattr(settings, name, None)


def preflight_evaluation(
    settings: Any,
    cases: Any,
    prompt_variants: Any,
    limits: Any,
) -> dict[str, Any]:
    """Validate evaluation configuration before any workflow or provider call.

    Returns a sanitized configuration summary. Raises ``PreflightError`` on any
    missing or unsafe configuration.
    """
    provider = _get(settings, "provider")
    if not provider:
        raise PreflightError("provider is not explicitly configured")
    if provider != "openai":
        raise PreflightError(f"evaluation requires openai provider, got {provider!r}")

    model = _get(settings, "openai_model")
    base_url = _get(settings, "openai_base_url")
    api_key = _get(settings, "openai_api_key")
    fallback = _get(settings, "fallback_provider")

    if not model:
        raise PreflightError("openai_model is not configured")
    if not base_url or not str(base_url).startswith(("http://", "https://")):
        raise PreflightError("openai_base_url is not configured")
    if not api_key:
        raise PreflightError("openai_api_key is not configured")
    if fallback:
        raise PreflightError("fallback_provider must be empty for evaluation")

    sla = _get(settings, "latency_sla_seconds")
    if not sla or sla <= 0:
        raise PreflightError("latency_sla_seconds must be positive")

    if not isinstance(cases, list) or not cases:
        raise PreflightError("cases must be a non-empty list")
    ids = []
    for case in cases:
        if not isinstance(case, dict):
            raise PreflightError("each case must be an object")
        for field in ("id", "body"):
            if not case.get(field):
                raise PreflightError(f"case missing required field: {field}")
        ids.append(case["id"])
        acceptable = case.get("acceptable_classifications")
        if acceptable is not None and not set(acceptable).issubset(CLASSIFICATIONS):
            raise PreflightError(f"invalid acceptable_classifications in case {case['id']}")
    if len(ids) != len(set(ids)):
        raise PreflightError("case ids must be unique")

    if not isinstance(prompt_variants, dict) or not prompt_variants:
        raise PreflightError("prompt_variants must be a non-empty mapping")
    for name, text in prompt_variants.items():
        if not name or not isinstance(text, str) or not text.strip():
            raise PreflightError(f"prompt variant {name!r} is empty")

    if not isinstance(limits, dict) or not limits:
        raise PreflightError("limits must be a non-empty mapping")
    for name, value in limits.items():
        if not isinstance(value, int) or value <= 0:
            raise PreflightError(f"limit {name!r} must be a positive integer")

    summary = {
        "provider": provider,
        "model": model,
        "base_url": base_url,
        "api_key_present": True,
        "fallback_provider": None,
        "latency_sla_seconds": sla,
        "case_count": len(cases),
        "case_ids": ids,
        "prompt_variants": sorted(prompt_variants),
        "limits": dict(limits),
    }
    print("Evaluation preflight OK:", summary)
    return summary
