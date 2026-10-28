"""Pydantic-validated configuration for ProzessPilot."""

from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(ROOT / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "ProzessPilot"
    env: Literal["dev", "test", "prod"] = "dev"
    database_url: str = f"sqlite:///{ROOT / 'data' / 'prozesspilot.db'}"
    data_dir: Path = ROOT / "data"

    # Model allowlists
    allowed_openai_models: list[str] = ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-3.5-turbo", "laya-v3", "laya/laya"]
    allowed_anthropic_models: list[str] = [
        "claude-3-5-sonnet-latest",
        "claude-3-5-sonnet-20241022",
        "claude-3-haiku-20240307",
    ]
    allowed_ollama_models: list[str] = ["llama3.1:8b", "llama3:8b", "mistral:latest", "qwen2.5:7b"]

    # Provider selection
    provider: Literal["openai", "ollama", "anthropic"] = "ollama"
    fallback_provider: str | None = None

    openai_api_key: str | None = None
    openai_base_url: str = "https://api.openai.com/v1"
    openai_model: str = "gpt-4o-mini"

    anthropic_api_key: str | None = None
    anthropic_model: str = "claude-3-5-sonnet-latest"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1:8b"

    # Cost / latency budgets
    cost_cap_usd_per_run: float = 0.50
    latency_sla_seconds: float = 30.0

    # Safety limits
    max_inquiry_body_chars: int = 4000
    max_kb_results: int = 5
    max_tokens_per_call: int = 1024
    experimental_max_tokens: int = 4096
    max_workflow_tokens: int = 4000
    rate_limit_per_minute: int = 30

    # Routing thresholds
    confidence_auto_approve: float = 0.85
    confidence_human_gate: float = 0.80

    # Mocked outbound
    mock_email_dir: Path = ROOT / "data" / "mock_emails"
    # Public demo safety
    operator_auth_required: bool = False  # Set True in production and provide OPERATOR_TOKEN
    operator_token: str = ""
    openai_allowed_hosts: str = ""

    @property
    def is_cloud_key_present(self) -> bool:
        return bool(self.openai_api_key or self.anthropic_api_key)

    def ensure_dirs(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.mock_email_dir.mkdir(parents=True, exist_ok=True)

    def validate_provider_keys(self) -> None:
        if self.operator_auth_required and not self.operator_token:
            raise ValueError("OPERATOR_TOKEN required when OPERATOR_AUTH_REQUIRED=true")
        if self.provider == "openai" and not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY required when provider is 'openai'")
        if self.provider == "anthropic" and not self.anthropic_api_key:
            raise ValueError("ANTHROPIC_API_KEY required when provider is 'anthropic'")


settings = Settings()
settings.ensure_dirs()