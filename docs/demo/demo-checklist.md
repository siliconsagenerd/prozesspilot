# Local Demo Checklist

Local-only. No production use, no push/deploy, no live database.

## 1. Required local commands and ports

- Backend default port: `8000`
- Frontend Vite dev port: `5174`
- Recommended backend port for frontend proxy: `18099`
- Backend health: `curl http://127.0.0.1:PORT/health`

Non-destructive checks:

```bash
cd ~/projects/prozesspilot
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check src tests
cd ~/projects/prozesspilot/frontend
npm run build
```

## 2. Disposable seeded database setup

```bash
cd ~/projects/prozesspilot
tmpdir=$(mktemp -d)
db="$tmpdir/prozesspilot-demo.db"
DATABASE_URL="sqlite:///$db" PYTHONPATH=src .venv/bin/python -m prozesspilot.cli initdb
DATABASE_URL="sqlite:///$db" PYTHONPATH=src .venv/bin/python -m prozesspilot.cli seed
DATABASE_URL="sqlite:///$db" PYTHONPATH=src .venv/bin/python -m prozesspilot.cli serve --host 127.0.0.1 --port 18099
```

Frontend:

```bash
cd ~/projects/prozesspilot/frontend
npm run dev -- --host 127.0.0.1 --port 5174
```

Use only the temporary database. Delete `tmpdir` after the demo.

## 3. German/English toggle check

1. Open `http://127.0.0.1:5174/`.
2. Confirm German text is default.
3. Click `Sprache wechseln`.
4. Confirm English text appears.
5. Click again and confirm German returns.

## 4. Inbox and Run detail checks

1. Open Inbox.
2. Open a run.
3. Confirm run state, classification, confidence, routing, and request text are visible.
4. Confirm the full draft is visible in the editable text box.
5. Confirm citation markers remain explicit as `[Title]`.
6. Confirm retrieved sources are not presented as explicit citations.

## 5. Evaluation screen checks

1. Open Evaluation.
2. Confirm the screen loads.
3. Confirm `Eval (improved prompt) starten` is visible.
4. Do not run a live evaluation during a local demo unless a disposable database and provider are intentionally configured.

## 6. Approval boundary

`ReadyForReview` is a workflow routing state. It is not customer-message approval and does not mean the draft has been approved for sending.


## Routing behavior (commit `4cfdbb69`)

Commit `4cfdbb69` changed routing from the previous post-draft confidence to classification confidence.

- `WorkflowRun.confidence` stores classification confidence.
- `Draft.confidence` stores post-draft confidence.
- `_route(classification, confidence, customer)` is called with classification confidence.
- Draft confidence no longer overwrites routing confidence.
- `routing_policy_compliant` and `routing_correct` are reported separately in evaluation results.

Regression coverage status:

- Covered: complaint escalation independent of confidence (`tests/backend/test_routing.py`, `tests/backend/test_bounded_quality_pass.py`).
- Covered: premium/VIP escalation independent of confidence (`tests/backend/test_routing.py`).
- Covered at unit level: high classification confidence can route ready; low classification confidence requires approval (`tests/backend/test_routing.py`).
- Missing run-level coverage: high classification confidence with low draft confidence; low classification confidence with high draft confidence.
- Missing run-level coverage for premium/VIP escalation with high/low draft confidence combinations.

## 7. Known limitations

- Provider/model identity is provider-reported only.
- Historical expected-routing conflicts remain unresolved.
- No full 12-case rerun was performed against the final implementation.
