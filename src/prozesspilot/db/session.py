"""Database session helpers."""

from __future__ import annotations

from contextlib import contextmanager

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from prozesspilot.config import settings

engine = create_engine(settings.database_url, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


@contextmanager
def db_session():
    s = SessionLocal()
    try:
        yield s
        s.commit()
    except Exception:
        s.rollback()
        raise
    finally:
        s.close()


def migrate_db() -> None:
    if engine.dialect.name != "sqlite":
        return
    with engine.begin() as conn:
        cols = {r[1] for r in conn.execute(text("PRAGMA table_info(audit_events)"))}
        if "prev_hash" not in cols:
            conn.execute(text("ALTER TABLE audit_events ADD COLUMN prev_hash VARCHAR(64)"))
        if "event_hash" not in cols:
            conn.execute(text("ALTER TABLE audit_events ADD COLUMN event_hash VARCHAR(64)"))


def init_db() -> None:
    from prozesspilot.db import models  # noqa: F401

    Base = models.Base
    Base.metadata.create_all(bind=engine)
    migrate_db()
