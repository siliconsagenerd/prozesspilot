from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from prozesspilot.eval_preflight import PreflightError, preflight_evaluation


def _settings(**overrides):
    base = dict(
        provider="openai",
        openai_model="laya-v2/laya-v2",
        openai_base_url="http://127.0.0.1:20133/v1",
        openai_api_key="secret",
        fallback_provider="",
        latency_sla_seconds=30,
    )
    base.update(overrides)
    return SimpleNamespace(**base)


def _valid_inputs():
    cases = [{"id": "c1", "body": "hello", "acceptable_classifications": ["product_question"]}]
    prompts = {"baseline": "classify", "improved": "classify better"}
    limits = {"classify_max_tokens": 1024, "draft_max_tokens": 2048}
    return cases, prompts, limits


def test_missing_provider_aborts_before_provider_call(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("prozesspilot.providers.factory.complete_with_fallback", mock)
    cases, prompts, limits = _valid_inputs()
    with pytest.raises(PreflightError):
        preflight_evaluation(_settings(provider=""), cases, prompts, limits)
    mock.assert_not_called()


def test_missing_api_key_aborts_before_provider_call(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("prozesspilot.providers.factory.complete_with_fallback", mock)
    cases, prompts, limits = _valid_inputs()
    with pytest.raises(PreflightError):
        preflight_evaluation(_settings(openai_api_key=""), cases, prompts, limits)
    mock.assert_not_called()


def test_fallback_provider_aborts_before_provider_call(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("prozesspilot.providers.factory.complete_with_fallback", mock)
    cases, prompts, limits = _valid_inputs()
    with pytest.raises(PreflightError):
        preflight_evaluation(_settings(fallback_provider="ollama"), cases, prompts, limits)
    mock.assert_not_called()


def test_missing_cases_aborts_before_provider_call(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("prozesspilot.providers.factory.complete_with_fallback", mock)
    _, prompts, limits = _valid_inputs()
    with pytest.raises(PreflightError):
        preflight_evaluation(_settings(), [], prompts, limits)
    mock.assert_not_called()


def test_missing_prompt_aborts_before_provider_call(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("prozesspilot.providers.factory.complete_with_fallback", mock)
    cases, _, limits = _valid_inputs()
    with pytest.raises(PreflightError):
        preflight_evaluation(_settings(), cases, {}, limits)
    mock.assert_not_called()


def test_valid_config_returns_sanitized_summary(capsys):
    cases, prompts, limits = _valid_inputs()
    summary = preflight_evaluation(_settings(), cases, prompts, limits)
    assert summary["provider"] == "openai"
    assert summary["api_key_present"] is True
    assert "openai_api_key" not in summary
    assert summary["case_count"] == 1
    captured = capsys.readouterr()
    assert "Evaluation preflight OK" in captured.out
