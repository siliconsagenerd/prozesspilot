"""Mock email sender (writes to disk, never sends)."""

from __future__ import annotations

import json
import time

from prozesspilot.config import settings


async def send_email_mock(to: str, subject: str, body: str, run_id: str) -> dict:
    settings.mock_email_dir.mkdir(parents=True, exist_ok=True)
    fn = settings.mock_email_dir / f"{run_id}.json"
    record = {"to": to, "subject": subject, "body": body, "sent_at": time.time(), "mock": True}
    fn.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"mock": True, "path": str(fn), "to": to}