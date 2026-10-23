"""add cited sources and citation format issues to drafts
Revision ID: 8163f9d2d504
Revises: 5fb977e1ed01
Create Date: 2026-10-23 09:10:33.222933
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "8163f9d2d504"
down_revision: Union[str, Sequence[str], None] = "5fb977e1ed01"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("drafts", sa.Column("cited_sources", sa.JSON(), nullable=True))
    op.add_column("drafts", sa.Column("citation_format_issues", sa.JSON(), nullable=True))


def downgrade() -> None:
    op.drop_column("drafts", "citation_format_issues")
    op.drop_column("drafts", "cited_sources")
