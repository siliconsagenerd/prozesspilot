"""Inquiry classifier."""

from __future__ import annotations

import json

from prozesspilot.providers.factory import complete_with_fallback

BASELINE_SYSTEM = (
    "You classify German customer inquiries. "
    "Return JSON with keys: classification, confidence (0-1), reasoning. "
    "classification one of: product_question, complaint, order_status, quote_request, spam, unclear."
)

IMPROVED_SYSTEM = (
    "You are a precise classifier for German customer-service inquiries. "
    "Classify into exactly one of: product_question, complaint, order_status, quote_request, spam, unclear. "
    "Consider tone, intent, and explicit requests. "
    "Return ONLY valid JSON: {\"classification\": str, \"confidence\": number 0-1, \"reasoning\": str}. "
    "Confidence reflects how certain the classification is. If ambiguous, choose 'unclear' with lower confidence."
)


async def classify_inquiry(text: str, prompt_variant: str = "improved", max_tokens: int | None = None) -> dict:
    system = IMPROVED_SYSTEM if prompt_variant == "improved" else BASELINE_SYSTEM
    prompt = f"Inquiry:\n{text}\n\nRespond with JSON only."
    res = await complete_with_fallback(prompt, system=system, json_mode=True, max_tokens=max_tokens)
    try:
        data = json.loads(res.text)
    except json.JSONDecodeError:
        # try to extract
        start = res.text.find("{")
        end = res.text.rfind("}")
        data = json.loads(res.text[start : end + 1]) if start != -1 else {}
    classification = data.get("classification", "unclear")
    if classification not in ("product_question", "complaint", "order_status", "quote_request", "spam", "unclear"):
        classification = "unclear"
    confidence = float(data.get("confidence", 0.5))
    confidence = max(0.0, min(1.0, confidence))
    return {
        "classification": classification,
        "confidence": confidence,
        "reasoning": data.get("reasoning", ""),
        "provider": res.provider,
        "model": res.model,
        "tokens_in": res.tokens_in,
        "tokens_out": res.tokens_out,
        "cost_usd": res.cost_usd,
        "finish_reason": res.finish_reason,
        "response_model": res.response_model,
    }