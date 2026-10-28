"""CLI entry point."""

from __future__ import annotations

import asyncio
import json

import click
from sqlalchemy import select

from prozesspilot.config import ROOT
from prozesspilot.db.models import Customer, KnowledgeSource
from prozesspilot.db.session import db_session, init_db


@click.group()
def main():
    """ProzessPilot CLI."""
    pass


@main.command()
def initdb():
    """Create tables (dev only; prefer alembic)."""
    init_db()
    click.echo("db initialized")


@main.command()
def seed():
    """Seed synthetic customers and knowledge base."""
    init_db()
    data_dir = ROOT / "data"
    customers_path = data_dir / "customers.json"
    customers = json.loads(customers_path.read_text(encoding="utf-8")) if customers_path.exists() else []
    kb_files = sorted((data_dir / "kb").glob("*.json"))
    with db_session() as s:
        for c in customers:
            exists = s.execute(select(Customer).where(Customer.email == c["email"])).scalar_one_or_none()
            if exists:
                continue
            s.add(Customer(**c))
        for f in kb_files:
            items = json.loads(f.read_text(encoding="utf-8"))
            for k in items:
                key = k.get("source_key")
                if key:
                    exists = s.execute(
                        select(KnowledgeSource).where(KnowledgeSource.source_key == key)
                    ).scalar_one_or_none()
                else:
                    exists = None
                if exists is None:
                    exists = s.execute(
                        select(KnowledgeSource).where(KnowledgeSource.title == k["title"])
                    ).scalar_one_or_none()
                if exists is not None:
                    if exists.source_key is None and key:
                        exists.source_key = key
                    continue
                s.add(KnowledgeSource(**k))
    click.echo("seeded")


@main.command()
@click.option("--host", default="0.0.0.0")
@click.option("--port", default=8000)
def serve(host, port):
    """Run API server."""
    import uvicorn

    uvicorn.run("prozesspilot.main:app", host=host, port=port, reload=True)


@main.command()
def evalrun():
    """Run evaluation suite (improved prompt)."""
    from prozesspilot.eval.runner import run_eval

    asyncio.run(run_eval())


if __name__ == "__main__":
    main()