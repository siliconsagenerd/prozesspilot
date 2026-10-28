"""add outbound approval tracking to workflow_runs
Revision ID: c1d2e3f4a5b6
Revises: d4e5f6a7b8c9
Create Date: 2026-10-26 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "c1d2e3f4a5b6"
down_revision: Union[str, Sequence[str], None] = "d4e5f6a7b8c9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column("workflow_runs", sa.Column("outbound_completed", sa.Boolean(), nullable=False, server_default=sa.false()))
    op.add_column("workflow_runs", sa.Column("email_sent", sa.Boolean(), nullable=False, server_default=sa.false()))
    op.add_column("workflow_runs", sa.Column("crm_updated", sa.Boolean(), nullable=False, server_default=sa.false()))
    op.add_column("workflow_runs", sa.Column("approval_owner", sa.String(36), nullable=True))
    op.add_column("workflow_runs", sa.Column("approval_claimed_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column("workflow_runs", sa.Column("approval_lease_expires_at", sa.DateTime(timezone=True), nullable=True))

    # Backfill only runs with trustworthy completion evidence.
    bind = op.get_bind()
    workflow_runs = sa.table(
        "workflow_runs",
        sa.column("id"),
        sa.column("state"),
        sa.column("outbound_completed"),
        sa.column("email_sent"),
        sa.column("crm_updated"),
    )
    audit_events = sa.table("audit_events", sa.column("run_id"), sa.column("event_type"))
    subq = sa.select(audit_events.c.run_id).where(audit_events.c.event_type == "approved_and_mock_sent")
    stmt = workflow_runs.update().where(
        workflow_runs.c.state == "Approved",
        workflow_runs.c.id.in_(subq),
    ).values(outbound_completed=True, email_sent=True, crm_updated=True)
    bind.execute(stmt)

def downgrade() -> None:
    op.drop_column("workflow_runs", "approval_lease_expires_at")
    op.drop_column("workflow_runs", "approval_claimed_at")
    op.drop_column("workflow_runs", "approval_owner")
    op.drop_column("workflow_runs", "crm_updated")
    op.drop_column("workflow_runs", "email_sent")
    op.drop_column("workflow_runs", "outbound_completed")
