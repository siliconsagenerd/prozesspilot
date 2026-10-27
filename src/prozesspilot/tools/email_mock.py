"""Mock email sender (writes to disk, never sends)."""

from __future__ import annotations

import json
import time

from prozesspilot.config import settings


async def send_email_mock(to: str, subject: str, body: str, run_id: str) -> dict:
    import re
    # Sanitize run_id to avoid path traversal
    safe_run_id = re.sub(r"[^a-zA-Z0-9_\-]", "_", str(run_id or "run"))
    settings.mock_email_dir.mkdir(parents=True, exist_ok=True)
    fn = (settings.mock_email_dir / f"{safe_run_id}.json").resolve()
    if not str(fn).startswith(str(settings.mock_email_dir.resolve())):
        fn = settings.mock_email_dir / f"sanitized_{safe_run_id}.json"
    if fn.exists():
        counter = 1
        while (settings.mock_email_dir / f"{safe_run_id}_{counter}.json").exists():
            counter += 1
        fn = settings.mock_email_dir / f"{safe_run_id}_{counter}.json"
    record = {"to": to, "subject": subject, "body": body, "sent_at": time.time(), "mock": True}
    fn.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"mock": True, "path": str(fn), "to": to}