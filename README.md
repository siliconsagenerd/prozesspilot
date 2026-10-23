# ProzessPilot — Customer Inquiry Workflow Copilot

[![GitHub](https://img.shields.io/badge/GitHub-siliconsagenerd%2Fprozesspilot-181717?logo=github)](https://github.com/siliconsagenerd/prozesspilot)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Vue](https://img.shields.io/badge/Vue-3-4FC08D?logo=vue.js)](https://vuejs.org/)
[![Tests](https://img.shields.io/badge/tests-pytest%20%2B%20ruff-2ea44f)](https://github.com/siliconsagenerd/prozesspilot/actions)

[Deutsch](#deutsch) | [English](#english)

Local-first AI workflow copilot for handling **synthetic German customer inquiries**. Demonstrates
structured multi-step AI workflow, tool use, retrieval with citations, confidence-based human
approval, full observability/audit trail, and evaluation.

> Built as a portfolio project for EUROKEY Software GmbH (Saarbrücken) — Werkstudent
> "Künstliche Intelligenz & LLM". All data is synthetic; no real email/CRM writes occur.

## Deutsch

ProzessPilot ist ein lokaler KI-Workflow-Copilot für **synthetische deutsche Kundenanfragen**.
Er demonstriert strukturierte mehrstufige KI-Workflows, Werkzeugnutzung, Retrieval mit
Zitaten, konfidenzbasierte Freigabe durch Menschen, vollständige Observability/Audit-Trails
und Evaluation.

> Portfolio-Projekt für EUROKEY Software GmbH (Saarbrücken). Alle Daten sind synthetisch;
> es erfolgen keine echten E-Mail-/CRM-Schreibvorgänge.

### Schnellstart

```bash
cd ~/projects/prozesspilot
python -m pip install -e ".[dev]"
cp .env.example .env
PYTHONPATH=src alembic upgrade head
PYTHONPATH=src python -m prozesspilot.cli seed
PYTHONPATH=src python -m prozesspilot.cli serve
cd frontend && npm install && npm run dev
```

### Bekannte Einschränkungen

- Retrieval ist keyword/TF-IDF, nicht embeddings-basiert.
- Evaluation umfasst 12 synthetische Fälle; keine statistische Signifikanz.
- Keine echte Authentifizierung oder Multi-Tenancy (außerhalb des v1-Umfangs).
- Deutsche Antwortqualität hängt vom Modell ab.

---

## English

## What this project covers

| Concern | What ProzessPilot shows |
|---|---|
| Multi-step AI workflow | Classify, customer lookup, KB search, draft, route, human approval |
| Tool use | SQL customer lookup, local KB retrieval, mock email/CRM actions |
| Retrieval with citations | Seeded knowledge sources and explicit `[Title]` citation markers |
| Confidence routing | Classification confidence drives routing; draft confidence is tracked separately |
| Human-in-the-loop | Approve, edit and approve, or reject with reason |
| Observability | Trace JSON, HTML timeline, latency, tokens, cost, audit log |
| Evaluation | 12 synthetic German cases, baseline vs improved prompt |

## Features

- Submit synthetic German inquiries through the form or seeded samples.
- Classify inquiries and route complaints, low-confidence, or high-value cases to approval.
- Search a local knowledge base and draft replies with citations.
- Keep full drafts visible and editable before approval.
- Record every step, model call, tool I/O, citation, latency, token, cost, and decision.
- Run evaluations and persist results for inspection.
- Mock all outbound actions; no real email, CRM, payment, or customer writes.

Code paths: `src/prozesspilot/agents/runtime.py`, `src/prozesspilot/agents/drafter.py`,
`src/prozesspilot/eval/runner.py`, `frontend/src/views`.

## Architecture

```text
Process Definition (YAML) -> Agent Runtime (tools, decision, HITL gate, fallback)
  -> Observability (trace JSON + HTML timeline, cost, audit log)
  -> Evaluation (12 German cases, baseline vs improved prompt)
```

## Project structure

```text
prozesspilot/
├── src/prozesspilot/        # FastAPI app, agents, DB, eval, CLI
├── frontend/                # Vue 3 + TypeScript + Vite UI
├── tests/backend/           # pytest regression tests
├── docs/demo/               # Local demo checklist
├── data/                    # Synthetic customers, KB sources, eval cases
├── alembic/                 # Database migrations
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Quick start

Docker:

```bash
docker compose up
```

Local development:

```bash
cd ~/projects/prozesspilot
python -m pip install -e ".[dev]"
cp .env.example .env
PYTHONPATH=src alembic upgrade head
PYTHONPATH=src python -m prozesspilot.cli seed
PYTHONPATH=src python -m prozesspilot.cli serve
# frontend
cd frontend && npm install && npm run dev
```

## Configuration

| Variable | Default | Purpose |
|---|---|---|
| `provider` | `ollama` | LLM provider: `openai`, `ollama`, or `anthropic` |
| `fallback_provider` | unset | Optional fallback provider |
| `openai_api_key` | unset | OpenAI API key |
| `openai_base_url` | `https://api.openai.com/v1` | OpenAI-compatible base URL |
| `openai_model` | `gpt-4o-mini` | OpenAI model |
| `anthropic_api_key` | unset | Anthropic API key |
| `anthropic_model` | `claude-3-5-sonnet-latest` | Anthropic model |
| `ollama_base_url` | `http://localhost:11434` | Ollama base URL |
| `ollama_model` | `llama3.1:8b` | Ollama model |
| `database_url` | `sqlite:///.../data/prozesspilot.db` | SQLAlchemy database URL |
| `cost_cap_usd_per_run` | `0.50` | Per-run cost cap |
| `latency_sla_seconds` | `30.0` | Latency SLA |
| `max_inquiry_body_chars` | `4000` | Maximum inquiry body size |
| `max_kb_results` | `5` | Maximum KB results |
| `max_tokens_per_call` | `1024` | Maximum tokens per model call |
| `max_workflow_tokens` | `4000` | Maximum workflow tokens |
| `rate_limit_per_minute` | `30` | Per-client request rate limit |
| `confidence_auto_approve` | `0.85` | Auto-approve threshold |
| `confidence_human_gate` | `0.80` | Human gate threshold |
| `mock_email_dir` | `data/mock_emails` | Mock email output directory |

## API

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/health` | Health check |
| `GET` | `/api/customers` | List customers |
| `POST` | `/api/inquiries` | Create an inquiry |
| `GET` | `/api/inquiries` | List inquiries and latest runs |
| `POST` | `/api/inquiries/{inquiry_id}/run` | Run the workflow |
| `GET` | `/api/runs/{run_id}` | Get run details, draft, citations, and confidence |
| `POST` | `/api/runs/{run_id}/approve` | Approve, edit, or reject a draft |
| `GET` | `/api/runs/{run_id}/trace.html` | Render the trace timeline |
| `GET` | `/api/kb` | List knowledge sources |
| `GET` | `/api/eval/cases` | List evaluation cases |
| `POST` | `/api/eval/run` | Run an evaluation |
| `GET` | `/api/eval/results` | List evaluation results |

Example:

```bash
curl -X POST http://127.0.0.1:8000/api/inquiries \
  -H "Content-Type: application/json" \
  -d '{"body":"Wo ist meine Bestellung?","channel":"form"}'
```

## Tests

```bash
cd ~/projects/prozesspilot
PYTHONPATH=src pytest -q
PYTHONPATH=src ruff check src tests
cd frontend
npm run build
```

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
- LLM judge is not used as objective truth.
- No real auth/multi-tenancy (out of scope for v1).
- German quality depends on model; Ollama small models may be weaker.
- Provider/model identity is provider-reported only.
- Historical expected-routing conflicts remain unresolved.
- No full 12-case rerun was performed against the final implementation.

## Acknowledgements

Built with FastAPI, SQLAlchemy, Alembic, Vue 3, Vite, pytest, and Ruff. Inspired by the
SecureDoc AI README format.

## Documentation

- `docs/demo/demo-checklist.md` - local demo checklist and routing behavior notes.

## About / Resources / License

ProzessPilot is a local portfolio project. Repository:
https://github.com/siliconsagenerd/prozesspilot

License: MIT (see `LICENSE` if present).
