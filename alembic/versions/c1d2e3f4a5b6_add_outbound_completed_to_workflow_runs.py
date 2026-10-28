"""add outbound_completed to workflow_runs
Revision ID: c1d2e3f4a5b6
Revises: 8163f9d2d504
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

def downgrade() -> None:
    op.drop_column("workflow_runs", "outbound_completed")
