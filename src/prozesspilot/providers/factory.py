"""Provider factory + fallback chain."""

from __future__ import annotations

from prozesspilot.config import settings
from prozesspilot.providers.anthropic import AnthropicProvider
from prozesspilot.providers.ollama import OllamaProvider
from prozesspilot.providers.openai import OpenAIProvider

REGISTRY = {
    "openai": OpenAIProvider,
    "anthropic": AnthropicProvider,
    "ollama": OllamaProvider,
}


def get_provider(name: str | None = None):
    name = name or settings.provider
    cls = REGISTRY.get(name)
    if cls is None:
        raise ValueError(f"unknown provider {name}")
    return cls()


def provider_chain() -> list:
    chain = [get_provider(settings.provider)]
    if settings.fallback_provider:
        try:
            chain.append(get_provider(settings.fallback_provider))
        except Exception:
            pass
    # Always allow ollama as last resort if not already
    if not any(p.name == "ollama" for p in chain):
        try:
            chain.append(OllamaProvider())
        except Exception:
            pass
    return chain


async def complete_with_fallback(prompt: str, system: str = "", json_mode: bool = False, max_tokens: int | None = None):
    last_err = None
    for p in provider_chain():
        try:
            return await p.complete(prompt, system=system, json_mode=json_mode, max_tokens=max_tokens)
        except Exception as e:  # noqa: BLE001
            last_err = e
            continue
    raise RuntimeError(f"all providers failed: {last_err}")