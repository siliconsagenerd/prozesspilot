# Complaint validation record (cases 03 and 09)

Date: 2026-10-23
Implementation commit: `a8ed3ea661a1f0470f40d11d965410d5e7fbf41b`
Validation run ID: `validation-complaint-a8ed3ea-20261023T084124Z`

## Provider route and model identifiers

- Route: OpenAI-compatible OmniRoute endpoint `http://127.0.0.1:20133/v1`
- Configured model identifier: `laya-v2/laya-v2`
- Provider-reported upstream model: `Beam-1.0-501B-A23B` (recorded from `response_model`; not independently verified as upstream identity)
- Token limits: classify 1024, draft 4096
- No fallback, retry, or automatic rerun was used.

## Artifact paths

- `/home/vishrutp/projects/prozesspilot-src/data/evaluations/validation-complaint-a8ed3ea-20261023T084124Z/manifest.json`
- `/home/vishrutp/projects/prozesspilot-src/data/evaluations/validation-complaint-a8ed3ea-20261023T084124Z/case_03_baseline.json`
- `/home/vishrutp/projects/prozesspilot-src/data/evaluations/validation-complaint-a8ed3ea-20261023T084124Z/case_03_improved.json`
- `/home/vishrutp/projects/prozesspilot-src/data/evaluations/validation-complaint-a8ed3ea-20261023T084124Z/case_09_baseline.json`
- `/home/vishrutp/projects/prozesspilot-src/data/evaluations/validation-complaint-a8ed3ea-20261023T084124Z/case_09_improved.json`

## Four-row result table

| Case | Variant | Run ID | Review decision | Result |
|---|---|---|---|---|
| case_03 | baseline | `70b87d67-b6b0-4380-ae94-2c209c712d92` | accept-with-notes | PASS |
| case_03 | improved | `9782966d-83bf-4243-a386-fb29368788ca` | accept-with-notes | PASS |
| case_09 | baseline | `60fd4bbe-c264-48cb-9e55-d1d452e5e5cd` | accept | PASS |
| case_09 | improved | `b91a393f-410b-4a77-bfa2-53a92206bc26` | accept | PASS |

All four runs classified `complaint`, routed `requires_human_approval`, and had `requires_approval=true`.
All four drafts were complete (`finish_reason=stop`, `completion_status=complete`) and had no citation format issues.

## Review notes

- case_03 baseline and improved: accepted with notes. The drafts distinguish unused-item return from defect remedy and cite the returns policy for replacement/repair. The improved variant could state more explicitly that use alone does not disqualify a defect complaint.
- case_09 baseline: accepted. It explicitly states that a reported defect does not mean the product was used, makes no unsupported invoice-correction promise, and escalates.
- case_09 improved: accepted. It states that no invoice correction can be confirmed from the retrieved sources and escalates.

## Automated validation statement

This is automated validation only. It did not approve or send any customer message, perform a human approval decision, or modify historical artifacts or prior review decisions.

## Remaining optional improvement

Optional, non-blocking wording-parity improvement: add an explicit sentence in the improved complaint variants stating that a reported defect does not mean the item was used, matching the case_09 baseline wording. No code or prompt change is required for this validation record.
