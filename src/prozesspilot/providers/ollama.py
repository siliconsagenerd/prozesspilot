"""Ollama local provider."""

from __future__ import annotations

import time

import httpx

from prozesspilot.config import settings
from prozesspilot.providers.base import LLMResult, estimate_cost


class OllamaProvider:
    name = "ollama"

    def __init__(self) -> None:
        self.base_url = settings.ollama_base_url.rstrip("/")
        self.model = settings.ollama_model

    async def complete(
        self, prompt: str, system: str = "", json_mode: bool = False, max_tokens: int | None = None
    ) -> LLMResult:
        opts = {"temperature": 0.2}
        if max_tokens:
            opts["num_predict"] = max_tokens
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system,
            "stream": False,
            "options": opts,
        }
        if json_mode:
            payload["format"] = "json"
        t0 = time.time()
        async with httpx.AsyncClient(timeout=120) as c:
            r = await c.post(f"{self.base_url}/api/generate", json=payload)
            r.raise_for_status()
            data = r.json()
        latency = int((time.time() - t0) * 1000)
        text = data.get("response", "")
        tin = data.get("prompt_eval_count", 0)
        tout = data.get("eval_count", 0)
        return LLMResult(
            text=text,
            provider=self.name,
            model=self.model,
            tokens_in=tin,
            tokens_out=tout,
            cost_usd=estimate_cost(self.name, self.model, tin, tout),
            latency_ms=latency,
            finish_reason=data.get("done_reason") or ("stop" if data.get("done") else None),
            response_model=data.get("model", self.model),
        )