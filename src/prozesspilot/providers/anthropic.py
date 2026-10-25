"""Anthropic provider (optional)."""

from __future__ import annotations

import time

import httpx

from prozesspilot.config import settings
from prozesspilot.providers.base import LLMResult, estimate_cost


class AnthropicProvider:
    name = "anthropic"

    def __init__(self) -> None:
        self.api_key = settings.anthropic_api_key
        self.model = settings.anthropic_model

    async def complete(
        self, prompt: str, system: str = "", json_mode: bool = False, max_tokens: int | None = None
    ) -> LLMResult:
        if not self.api_key:
            raise RuntimeError("ANTHROPIC_API_KEY not set")
        if json_mode:
            json_instruction = "Return ONLY valid JSON. Do not include markdown code fences or any conversational text."
            system = f"{system}\n\n{json_instruction}".strip() if system else json_instruction
        payload = {
            "model": self.model,
            "max_tokens": max_tokens or 1024,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            payload["system"] = system
        t0 = time.time()
        async with httpx.AsyncClient(timeout=settings.latency_sla_seconds) as c:
            r = await c.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": self.api_key,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json",
                },
                json=payload,
            )
            r.raise_for_status()
            data = r.json()
        latency = int((time.time() - t0) * 1000)
        text = "".join(b.get("text", "") for b in data.get("content", []))
        usage = data.get("usage", {})
        tin = usage.get("input_tokens", 0)
        tout = usage.get("output_tokens", 0)
        return LLMResult(
            text=text,
            provider=self.name,
            model=self.model,
            tokens_in=tin,
            tokens_out=tout,
            cost_usd=estimate_cost(self.name, self.model, tin, tout),
            latency_ms=latency,
            finish_reason=data.get("stop_reason"),
            response_model=data.get("model", self.model),
        )