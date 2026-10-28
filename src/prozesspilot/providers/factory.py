"""Provider factory + fallback chain."""

from __future__ import annotations

import contextvars
import logging
import time
from collections import defaultdict

from prozesspilot.config import settings
from prozesspilot.providers.anthropic import AnthropicProvider
from prozesspilot.providers.ollama import OllamaProvider
from prozesspilot.providers.openai import OpenAIProvider

logger = logging.getLogger(__name__)

REGISTRY = {
    "openai": OpenAIProvider,
    "anthropic": AnthropicProvider,
    "ollama": OllamaProvider,
}

_CIRCUIT_STATE: dict[str, dict] = defaultdict(lambda: {"failures": 0, "last_failure": 0.0})
CIRCUIT_THRESHOLD = 5
CIRCUIT_COOLDOWN_SECONDS = 30.0


def reset_circuit_breaker() -> None:
    _CIRCUIT_STATE.clear()


_provider_override_var: contextvars.ContextVar = contextvars.ContextVar("provider_override", default=None)

def set_provider_override(name: str | None = None):
    _provider_override_var.set(name)

def get_provider(name: str | None = None):
    if name is None:
        name = _provider_override_var.get() or settings.provider
    cls = REGISTRY.get(name)
    if cls is None:
        raise ValueError(f"unknown provider {name}")
    return cls()


def provider_chain(provider: str | None = None) -> list:
    """Return explicit provider chain."""
    primary = provider or _provider_override_var.get() or settings.provider
    chain = [get_provider(primary)]
    fb = (settings.fallback_provider or "").strip()
    if fb and fb != primary:
        chain.append(get_provider(fb))
    return chain


async def complete_with_fallback(
    prompt: str,
    system: str = "",
    json_mode: bool = False,
    max_tokens: int | None = None,
    provider: str | None = None,
):
    now = time.time()
    last_err = None
    for p in provider_chain(provider):
        p_name = getattr(p, "name", type(p).__name__)
        state = _CIRCUIT_STATE[p_name]
        if state["failures"] >= CIRCUIT_THRESHOLD and (now - state["last_failure"] < CIRCUIT_COOLDOWN_SECONDS):
            logger.warning("circuit breaker open for %s, skipping", p_name)
            continue

        try:
            res = await p.complete(
                prompt,
                system=system,
                json_mode=json_mode,
                max_tokens=max_tokens,
            )
            state["failures"] = 0
            return res
        except Exception as e:  # noqa: BLE001
            state["failures"] += 1
            state["last_failure"] = time.time()
            logger.warning("provider %s failed: %s", p_name, e)
            last_err = e
            continue
    raise RuntimeError(f"all providers failed: {last_err}")

