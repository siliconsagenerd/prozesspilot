import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_KEYS = {
    "product.ergochair_3000",
    "product.deskpro_monitor_arm",
    "policy.returns_and_complaints",
    "policy.order_status",
    "process.quote_request",
    "policy.escalation",
}


def _env(db):
    env = os.environ.copy()
    env["DATABASE_URL"] = f"sqlite:///{db}"
    env["PYTHONPATH"] = str(ROOT / "src")
    return env


def test_fresh_migration_and_repeated_seed():
    d = tempfile.mkdtemp()
    db = os.path.join(d, "t.db")
    env = _env(db)
    r = subprocess.run(
        [sys.executable, "-m", "alembic", "upgrade", "head"],
        cwd=str(ROOT), env=env, capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    for _ in range(2):
        r = subprocess.run(
            [sys.executable, "-m", "prozesspilot.cli", "seed"],
            cwd=str(ROOT), env=env, capture_output=True, text=True,
        )
        assert r.returncode == 0, r.stderr
    code = (
        "import json, os\n"
        "from prozesspilot.db.session import db_session\n"
        "from prozesspilot.db.models import KnowledgeSource\n"
        "from sqlalchemy import select\n"
        "with db_session() as s:\n"
        "    rows=s.execute(select(KnowledgeSource)).scalars().all()\n"
        "    keys={r.source_key for r in rows}\n"
        "    print(len(rows))\n"
        "    print(sorted(keys))\n"
    )
    r = subprocess.run([sys.executable, "-c", code], cwd=str(ROOT), env=env, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    lines = r.stdout.strip().splitlines()
    assert lines[0] == "6"
    assert set(eval(lines[1])) == EXPECTED_KEYS


def test_unknown_source_reference_fails():
    from prozesspilot.tools.kb_search import get_source, validate_source_keys

    try:
        get_source("does.not.exist")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
    try:
        validate_source_keys(["does.not.exist"])
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
