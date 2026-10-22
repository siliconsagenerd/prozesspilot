"""Model provider abstraction with fallback chain."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class LLMResult:
    text: str
    provider: str
    model: str
    tokens_in: int = 0
    tokens_out: int = 0
    cost_usd: float = 0.0
    latency_ms: int = 0


class Provider(Protocol):
    name: str

    async def complete(
        self, prompt: str, system: str = "", json_mode: bool = False, max_tokens: int | None = None
    ) -> LLMResult: ...


def estimate_cost(provider: str, model: str, tin: int, tout: int) -> float:
    # Rough per-1k token pricing (USD). Good enough for estimates.
    rates = {
        "openai": {"in": 0.00015, "out": 0.0006},
        "anthropic": {"in": 0.003, "out": 0.015},
        "ollama": {"in": 0.0, "out": 0.0},
    }
    r = rates.get(provider, {"in": 0.0, "out": 0.0})
    return round((tin / 1000) * r["in"] + (tout / 1000) * r["out"], 6)