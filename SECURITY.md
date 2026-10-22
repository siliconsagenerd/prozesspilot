# Security notes

## Scope
Local portfolio demo only. No production deployment, no real auth, no multi-tenancy.

## Data handling
- Synthetic German inquiries only. No real customer PII expected.
- Email/CRM integrations are mocked (disk write / audit log). No outbound network writes.
- No API keys or infra details exposed in UI or traces.

## Safety limits
- Inquiry body max `max_inquiry_body_chars` (default 4000) -> HTTP 413.
- Per-client rate `rate_limit_per_minute` (default 30) -> HTTP 429.
- KB `top_k` capped by `max_kb_results` (default 5).
- Per-call `max_tokens` (`max_tokens_per_call`, default 800).
- Per-workflow token/cost budget (`max_workflow_tokens`, `cost_cap_usd_per_run`).

## Rate limiter limitation
The rate limiter is in-memory and per-process. It does not protect multiple workers/replicas.
It is suitable only for the current local single-process demo. Production/multi-worker
deployment would require a shared limiter. It is not production-ready.

## Human approval
Human approval is required before any simulated outbound action. Auto-eligible runs are still
marked and do not send email.

## Known gaps
- No authentication/authorization.
- No GDPR compliance claim.
- Retrieval is keyword/TF-IDF, not embedding-based.
