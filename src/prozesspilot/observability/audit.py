"""Audit event helpers."""

from __future__ import annotations

import hashlib
import json
from datetime import UTC

from sqlalchemy import event, select

from prozesspilot.db.models import AuditEvent, new_id
from prozesspilot.db.models import now as _now
from prozesspilot.db.session import db_session


def _hash_event(row: AuditEvent) -> str:
    created = ""
    if row.created_at is not None:
        dt = row.created_at
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=UTC)
        created = dt.astimezone(UTC).isoformat()
    payload = {
        "id": row.id,
        "run_id": row.run_id,
        "event_type": row.event_type,
        "actor": row.actor,
        "payload": row.payload or {},
        "created_at": created,
        "prev_hash": row.prev_hash,
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()


def audit(run_id: str | None, event_type: str, actor: str = "system", payload: dict | None = None) -> None:
    # Scrub potential sensitive keys from payload before saving
    safe_payload = {}
    if payload:
        for k, v in payload.items():
            if any(secret in k.lower() for secret in ("token", "key", "password", "secret", "auth")):
                safe_payload[k] = "[REDACTED]"
            else:
                safe_payload[k] = v

    with db_session() as s:
        stmt = select(AuditEvent.event_hash).order_by(AuditEvent.created_at.desc(), AuditEvent.id.desc()).limit(1)
        if run_id is not None:
            stmt = stmt.where(AuditEvent.run_id == run_id)
        else:
            stmt = stmt.where(AuditEvent.run_id.is_(None))
        prev_hash = s.execute(stmt).scalar_one_or_none() or ("0" * 64)

        row = AuditEvent(
            id=new_id(),
            run_id=run_id,
            event_type=event_type,
            actor=actor,
            payload=safe_payload,
            prev_hash=prev_hash,
            created_at=_now(),
        )
        row.event_hash = _hash_event(row)
        s.add(row)
        s.flush()


@event.listens_for(AuditEvent, "before_update")
def _reject_audit_update(mapper, connection, target):
    raise ValueError("AuditEvent rows are immutable")


@event.listens_for(AuditEvent, "before_delete")
def _reject_audit_delete(mapper, connection, target):
    raise ValueError("AuditEvent rows are immutable")
