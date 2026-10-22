"""Mock CRM updater (logs only, no external write)."""

from __future__ import annotations

from prozesspilot.observability.audit import audit


async def crm_update_mock(run_id: str, customer_id: str | None, summary: str) -> dict:
    audit(run_id, "crm_update_mock", actor="system", payload={"customer_id": customer_id, "summary": summary})
    return {"mock": True, "logged": True}