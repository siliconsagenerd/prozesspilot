"""OpenAI-compatible provider."""

from __future__ import annotations

import time

import httpx

from prozesspilot.config import settings
from prozesspilot.providers.base import LLMResult, estimate_cost


class OpenAIProvider:
    name = "openai"

    def __init__(self) -> None:
        self.base_url = settings.openai_base_url.rstrip("/")
        self.api_key = settings.openai_api_key
        self.model = settings.openai_model

    async def complete(
        self, prompt: str, system: str = "", json_mode: bool = False, max_tokens: int | None = None
    ) -> LLMResult:
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY not set")
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        payload = {"model": self.model, "messages": messages, "temperature": 0.2}
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        if json_mode:
            payload["response_format"] = {"type": "json_object"}
        t0 = time.time()
        async with httpx.AsyncClient(timeout=settings.latency_sla_seconds) as c:
            r = await c.post(
                f"{self.base_url}/chat/completions",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json=payload,
            )
            r.raise_for_status()
            data = r.json()
        latency = int((time.time() - t0) * 1000)
        choice = data["choices"][0]
        message = choice.get("message", {})
        text = message.get("content") or ""
        usage = data.get("usage", {})
        tin = usage.get("prompt_tokens", 0)
        tout = usage.get("completion_tokens", 0)
        return LLMResult(
            text=text,
            provider=self.name,
            model=self.model,
            tokens_in=tin,
            tokens_out=tout,
            cost_usd=estimate_cost(self.name, self.model, tin, tout),
            latency_ms=latency,
            finish_reason=choice.get("finish_reason"),
            response_model=data.get("model", self.model),
        )