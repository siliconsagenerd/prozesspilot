"""add source_key to knowledge sources"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = "b7c2e1f0a9d8"
down_revision: Union[str, Sequence[str], None] = "29f0792e3d10"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("knowledge_sources") as batch_op:
        batch_op.add_column(sa.Column("source_key", sa.String(length=120), nullable=True))
        batch_op.create_unique_constraint("uq_knowledge_sources_source_key", ["source_key"])


def downgrade() -> None:
    with op.batch_alter_table("knowledge_sources") as batch_op:
        batch_op.drop_constraint("uq_knowledge_sources_source_key", type_="unique")
        batch_op.drop_column("source_key")
