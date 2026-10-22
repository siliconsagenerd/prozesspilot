import os
import tempfile
from pathlib import Path

import pytest

tmp = tempfile.mkdtemp()
os.environ["DATABASE_URL"] = f"sqlite:///{tmp}/test.db"
os.environ["PROZESSPILOT_ENV"] = "test"

# ensure src on path
import sys  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))  # noqa: E402


@pytest.fixture(autouse=True)
def fresh_db():
    from prozesspilot.db.models import Base  # noqa
    from prozesspilot.db.session import engine

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    try:
        from prozesspilot.main import _rate_buckets
        _rate_buckets.clear()
    except Exception:
        pass
    # seed kb minimal
    from prozesspilot.db.models import Customer, KnowledgeSource
    from prozesspilot.db.session import db_session

    with db_session() as s:
        s.add(
            KnowledgeSource(
                title="Test KB",
                category="product",
                content="ErgoChair 3000 Preis 349 EUR",
                source_path="t",
            )
        )
        s.add(
            Customer(name="Anna", email="anna@example.de", tier="standard")
        )
    yield