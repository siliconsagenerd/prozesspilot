# ProzessPilot Evaluation Report

Date: 2026-10-22

## Synthetic dataset scope

- 12 synthetic customer-service inquiries, 2 prompt variants (`baseline`, `improved`) per inquiry = 24 workflows.
- Cases and expected labels are stored in `data/eval_cases.json`.
- Knowledge base: 6 sources in `data/kb/sources.json`.
- Case hash (manifest): `ceb819418b6afab2d05bd54752f444314a2d62021b1773e4f3ce96d0dc60afd9`
- Prompt hash (manifest): `bb3c4437f7411183933571421c9668b38dd85d5a5dee97f1b8075fa029ee6915`
- Case file hash (current): `880785ffb676bb3952f12eeb476cab661ad43f1f1ed79efadb8faf7676254ebb`
- Knowledge-base hash (current): `03fe69666534218fa691f377b1d96b91a5bc0fb6d853c343a200cee45869f94b`
- Evaluation runs are intentionally ignored (`data/evaluations/` in `.gitignore`); raw outputs remain on disk and are not committed.

## Baseline vs improved results

Successful run: `eval-20261022T190411Z` (24 workflows, 48 application requests).

| Metric | Baseline | Improved |
|---|---:|---:|
| Workflows | 12 | 12 |
| Classification match | 12/12 | 12/12 |
| Routing match | 11/12 | 10/12 |
| Expected sources retrieved | 9/12 | 9/12 |
| Truncated outputs | 12/12 | 9/12 |
| Total cost (USD) | 0.010177 | 0.008665 |
| Total latency (ms) | 94603 | 71849 |
| Total tokens | 37085 | 35507 |

Routing mismatches:
- `case_04` both variants: expected `ready_for_review`, actual `requires_human_approval` (truncated classify/draft path).
- `case_06` improved only: expected `ready_for_review`, actual `requires_human_approval`.

## Attempt ledger

- `data/evaluations/eval-20261022T185244Z`: first run; all classify steps failed with `all providers failed: All connection attempts failed`; no successful scoring.
- `data/evaluations/eval-20261022T190411Z`: second run after provider configuration fix; all 24 workflows completed.
- `data/evaluations/limit_deviation.md`: records the token-limit deviation and compatibility probes.

## Token-limit deviation

Approved protocol limits were `classify: 128`, `draft: 384`. Executed limits were `classify: 1024`, `draft: 2048` because Laya returned reasoning-only content at the approved limits. The larger limits are not retroactively approved; original limits remain 128/384. Compatibility probes recorded in `limit_deviation.md`.

## Configuration failure and fix

- The first run failed because the application silently fell back to Ollama when OpenAI configuration was incomplete.
- Fix: disable silent Ollama fallback and require explicit OpenAI provider/model/base URL/API key for evaluation.
- Preflight checks were added in `src/prozesspilot/eval_preflight.py` and invoked by `run_eval`.
- Executed source changes are preserved in `docs/evaluation/executed-source-changes.patch`.

## Actual served model vs configured route

- Configured route: OpenAI-compatible provider (`provider=openai`), model `laya-v2/laya-v2`.
- Run records report `model_provider=openai` and `model_name=laya-v2/laya-v2`.
- The served model identifier is taken from run records; upstream identity is not independently verified.

## Unknown upstream costs

- Costs are provider-returned estimates (`total_cost_usd`), not independently verified against upstream pricing.
- No separate upstream billing audit was performed.

## Retrieval/scoring limitations

- Knowledge-base retrieval originally used title/content token overlap and could miss policy sources for complaint/return inquiries.
- ASCII/umlaut mismatch (`Rückgabe` vs `Rueckgabe`) caused source-key evaluator mismatches; stable `source_key` values were added to sources and used for citations and evaluation labels.
- A small German/English stopword filter was added to avoid fabricated relevance for unrelated queries.
- Corrected source-key scoring changes at least `case_04` from false to true; `case_03` and `case_09` remain false under the recorded retrieval results.
- Retrieval scores are heuristic and are not a semantic or calibrated relevance measure.

## Human citation review

Human citation review is still pending. Automated checks verify expected source retrieval, but they do not verify that every factual claim in a draft is supported by the cited source.
