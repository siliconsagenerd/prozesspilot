# Runbook (local only)

## Workspace
Authoritative local workspace: `~/projects/prozesspilot` on oldmac.

## Backend tests
```bash
cd ~/projects/prozesspilot
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check src tests
```

## Fresh database migration
```bash
tmpdir=$(mktemp -d)
db="$tmpdir/t.db"
DATABASE_URL="sqlite:///$db" PYTHONPATH=src .venv/bin/python -m alembic upgrade head
echo "exit=$?"
rm -rf "$tmpdir"
```

## Frontend build
```bash
cd ~/projects/prozesspilot/frontend
npm ci
npm run build
```

## Serve
```bash
cd ~/projects/prozesspilot
PYTHONPATH=src .venv/bin/python -m prozesspilot.cli seed
PYTHONPATH=src .venv/bin/python -m prozesspilot.cli serve
```

## Safety limits
In-memory, per-process rate limiter; see SECURITY.md. Not production-ready.

## Status
Local-only. No GitHub creation or deployment yet.
