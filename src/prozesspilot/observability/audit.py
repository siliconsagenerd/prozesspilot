"""Audit event helpers."""

from __future__ import annotations

from prozesspilot.db.models import AuditEvent
from prozesspilot.db.session import db_session


def audit(run_id: str | None, event_type: str, actor: str = "system", payload: dict | None = None) -> None:
    with db_session() as s:
        s.add(AuditEvent(run_id=run_id, event_type=event_type, actor=actor, payload=payload or {}))