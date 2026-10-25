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
    """Return explicit provider chain.

    Only uses explicitly configured settings.provider and, if non-empty,
    settings.fallback_provider. No silent or automatic fallback to Ollama.
    """
    primary = settings.provider
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
):
    last_err = None
    for p in provider_chain():
        try:
            return await p.complete(
                prompt,
                system=system,
                json_mode=json_mode,
                max_tokens=max_tokens,
            )
        except Exception as e:  # noqa: BLE001
            last_err = e
            continue
    raise RuntimeError(f"all providers failed: {last_err}")
