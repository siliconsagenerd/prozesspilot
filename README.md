# ProzessPilot — Customer Inquiry Workflow Copilot

[![GitHub](https://img.shields.io/badge/GitHub-siliconsagenerd%2Fprozesspilot-181717?logo=github)](https://github.com/siliconsagenerd/prozesspilot)

Local-first AI workflow copilot for handling **synthetic German customer inquiries**.
Demonstrates structured multi-step AI workflow, tool use, retrieval with citations,
confidence-based human approval, full observability/audit trail, and evaluation.

> Built as a portfolio project for EUROKEY Software GmbH (Saarbrücken) — Werkstudent
> "Künstliche Intelligenz & LLM". All data is synthetic; no real email/CRM writes occur.

## What it does

1. Operator submits a synthetic German inquiry (form or sample).
2. Workflow: classify → customer lookup (SQL) → knowledge-base search (RAG) → draft German reply with citations → confidence routing.
3. Routing: complaint / low confidence / high-value customer → human approval gate; high-confidence simple product question → ready for review.
4. Human approves / edits+approves / rejects with reason. Approval records outcome + audit entry. **No email is ever sent** (mocked to disk).
5. Full trace: every step, model/prompt, tool I/O, citations, latency, tokens, cost, decision, human action.

## Architecture

```
Process Definition (YAML) -> Agent Runtime (tools, decision, HITL gate, fallback)
  -> Observability (trace JSON + HTML timeline, cost, audit log)
  -> Evaluation (12 German cases, baseline vs improved prompt)
```

## Stack

Python 3.11+, FastAPI, SQLAlchemy + Alembic + SQLite, Pydantic settings, httpx,
Chroma-alternative lightweight local retrieval, Vue 3 + TS + Vite, Jinja2 trace viewer,
pytest, Ruff, Docker/Compose, GitHub Actions.

Providers: OpenAI-compatible, Ollama (local), optional Anthropic. Fallback chain on failure.

## Quick start

```bash
cd Nebelkammer
python -m pip install -e ".[dev]"
cp .env.example .env
# optional: start Ollama; otherwise tests mock providers
PYTHONPATH=src alembic upgrade head
PYTHONPATH=src python -m prozesspilot.cli seed
PYTHONPATH=src python -m prozesspilot.cli serve
# frontend
cd frontend && npm install && npm run dev
```

Or Docker: `docker compose up`.

## Tests

```bash
PYTHONPATH=src pytest -q
ruff check src tests
```

## Evaluation

```bash
PYTHONPATH=src python -m prozesspilot.cli evalrun
```
Runs 12 synthetic German cases, reports classification/routing/citation accuracy,
latency, cost. Results persisted in `evaluations` table; view via `/api/eval/results` or UI.

## Mocked integrations

- Email: writes to `data/mock_emails/<run_id>.json` (never sends).
- CRM: logs audit event only.

## Safety

- No real outbound email/SMS/CRM writes/payments.
- Human approval mandatory before any simulated outbound action.
- No GDPR compliance claim; privacy considerations documented honestly.
- No API keys or infra details exposed.

## Known limitations

- Retrieval is keyword/TF-IDF, not embedding-based (Chroma optional upgrade).
- Evaluation set is small (12 cases); no statistical significance claimed.
- LLM judge not used as objective truth.
- No real auth/multi-tenancy (out of scope for v1).
- German quality depends on model; Ollama small models may be weaker.
## Safety limits (single-process only)

The API enforces request/body/rate/workflow limits for the local demo:
- inquiry body max `max_inquiry_body_chars` (default 4000 chars) -> HTTP 413
- per-client rate `rate_limit_per_minute` (default 30) -> HTTP 429
- KB retrieval `top_k` capped by `max_kb_results` (default 5)
- per-provider-call `max_tokens` (`max_tokens_per_call`, default 800)
- per-workflow token/cost budget (`max_workflow_tokens`, `cost_cap_usd_per_run`)

The rate limiter is in-memory and per-process. It does not coordinate across workers/replicas
and is suitable only for the local single-process demo. Production/multi-worker deployment
would require a shared limiter (e.g. Redis). Not production-ready.

## Provider and evaluation status

- Providers: OpenAI-compatible, Ollama, optional Anthropic; fallback chain on failure.
  Mocked providers are used in tests; no paid provider calls are made by default.
- Evaluation: 12 synthetic German cases; baseline vs improved prompt; results persisted.
  No statistical significance claimed; LLM judge not used as objective truth.
- Retrieval: keyword/TF-IDF over seeded knowledge sources; embeddings optional upgrade.

## Repository

GitHub: https://github.com/siliconsagenerd/prozesspilot

The authoritative local workspace remains `~/projects/prozesspilot` on oldmac. This project is a
local portfolio demo only; no deployment or customer-message sending is performed.

## Documentation

- `docs/demo/demo-checklist.md` - local demo checklist and routing behavior notes.
