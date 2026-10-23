"""Response drafter with citations."""

from __future__ import annotations

import json

from prozesspilot.providers.factory import complete_with_fallback

BASELINE_SYSTEM = (
    "You draft a German customer-service reply. Use provided sources. "
    "Return JSON: {text, confidence, reasoning}. Cite source titles in text. "
    "Complaint rules: distinguish a 30-day unused-item return from defect remedies (replacement/repair); "
    "do not promise invoice corrections unless a source supports them; "
    "do not infer that a product was used merely because a defect is reported; "
    "use clean explicit [Title] citation markers; preserve escalation for complaints. "
    "Order-status rules: cite the retrieved policy source for delivery times and status definitions; "
    "do not state tracking, stock, or order-lookup details unless a source supports them."
)

IMPROVED_SYSTEM = (
    "You are a careful German customer-service agent. "
    "Draft a polite, concise German reply to the inquiry. "
    "Use ONLY the provided knowledge-base snippets; cite them by title in brackets like [Title]. "
    "If no source supports a claim, say you cannot confirm and offer escalation. "
    "Consider customer tier/history if provided. "
    "Complaint rules: distinguish a 30-day unused-item return from defect remedies (replacement/repair); "
    "do not promise invoice corrections unless a source supports them; "
    "do not infer that a product was used merely because a defect is reported; "
    "keep citation markers clean and explicit as [Title]; preserve escalation for complaints. "
    "Order-status rules: cite the retrieved policy source for delivery times and status definitions; "
    "do not state tracking, stock, or order-lookup details unless a source supports them. "
    "Return ONLY valid JSON: {\"text\": str, \"confidence\": number 0-1, \"reasoning\": str}."
)


async def draft_response(
    inquiry_body: str,
    classification: str,
    customer: dict | None,
    kb_results: list,
    prompt_variant: str = "improved",
    max_tokens: int | None = None,
) -> dict:
    system = IMPROVED_SYSTEM if prompt_variant == "improved" else BASELINE_SYSTEM
    sources = "\n".join(f"- [{r['title']}] {r['snippet']}" for r in kb_results) or "(no sources)"
    cust = json.dumps(customer, ensure_ascii=False) if customer else "none"
    prompt = (
        f"Classification: {classification}\n"
        f"Customer: {cust}\n"
        f"Knowledge sources:\n{sources}\n\n"
        f"Inquiry:\n{inquiry_body}\n\n"
        "Draft the reply as JSON."
    )
    res = await complete_with_fallback(prompt, system=system, json_mode=True, max_tokens=max_tokens)
    try:
        data = json.loads(res.text)
    except json.JSONDecodeError:
        start = res.text.find("{")
        end = res.text.rfind("}")
        if start != -1:
            data = json.loads(res.text[start : end + 1])
        else:
            data = {"text": res.text, "confidence": 0.5, "reasoning": ""}
    text = data.get("text", res.text)
    conf = float(data.get("confidence", 0.6))
    conf = max(0.0, min(1.0, conf))
    return {
        "text": text,
        "confidence": conf,
        "reasoning": data.get("reasoning", ""),
        "provider": res.provider,
        "model": res.model,
        "tokens_in": res.tokens_in,
        "tokens_out": res.tokens_out,
        "cost_usd": res.cost_usd,
        "finish_reason": res.finish_reason,
        "response_model": res.response_model,
    }