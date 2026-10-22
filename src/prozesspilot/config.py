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
    max_workflow_tokens: int = 4000
    rate_limit_per_minute: int = 30

    # Routing thresholds
    confidence_auto_approve: float = 0.85
    confidence_human_gate: float = 0.80

    # Mocked outbound
    mock_email_dir: Path = ROOT / "data" / "mock_emails"

    @property
    def is_cloud_key_present(self) -> bool:
        return bool(self.openai_api_key or self.anthropic_api_key)

    def ensure_dirs(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.mock_email_dir.mkdir(parents=True, exist_ok=True)


settings = Settings()
settings.ensure_dirs()