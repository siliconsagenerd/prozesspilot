"""Customer lookup tool (SQLite)."""

from __future__ import annotations

from sqlalchemy import select

from prozesspilot.db.models import Customer
from prozesspilot.db.session import db_session


async def customer_lookup(email: str | None = None, name: str | None = None) -> dict:
    with db_session() as s:
        q = select(Customer)
        if email:
            q = q.where(Customer.email == email)
        elif name:
            safe_name = name.replace("%", "\\%").replace("_", "\\_")
            q = q.where(Customer.name.ilike(f"%{safe_name}%", escape="\\"))
        c = s.execute(q).scalar_one_or_none()
        if c is None:
            return {"found": False, "customer": None}
        return {
            "found": True,
            "customer": {
                "id": c.id,
                "name": c.name,
                "email": c.email,
                "tier": c.tier,
                "history_summary": c.history_summary,
                "previous_orders": c.previous_orders,
                "has_open_complaint": c.has_open_complaint,
            },
        }