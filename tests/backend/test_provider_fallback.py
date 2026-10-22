import asyncio

import pytest

from prozesspilot.providers import factory


class _FailingOpenAI:
    def __init__(self):
        pass

    async def complete(self, prompt, system="", json_mode=False, max_tokens=None):
        raise RuntimeError("managed provider down")


class _OllamaSpy:
    called = False

    def __init__(self):
        pass

    async def complete(self, prompt, system="", json_mode=False, max_tokens=None):
        _OllamaSpy.called = True
        raise AssertionError("Ollama must not be called")


def test_managed_provider_failure_does_not_call_ollama(monkeypatch):
    monkeypatch.setattr("prozesspilot.config.settings.provider", "openai")
    monkeypatch.setattr("prozesspilot.config.settings.fallback_provider", None)
    monkeypatch.setattr("prozesspilot.config.settings.openai_api_key", "test-key")

    monkeypatch.setitem(factory.REGISTRY, "openai", _FailingOpenAI)
    monkeypatch.setitem(factory.REGISTRY, "ollama", _OllamaSpy)
    _OllamaSpy.called = False

    with pytest.raises(RuntimeError, match="all providers failed"):
        asyncio.run(factory.complete_with_fallback("hello"))

    assert _OllamaSpy.called is False
