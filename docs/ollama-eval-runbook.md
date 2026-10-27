# Self-hosted Ollama evaluation runbook (Oracle -> AWS)

Status: proposal only. No resources provisioned, no model downloaded.

## Oracle capacity findings

- Tenancy: `vishrutpandey76` (`eu-frankfurt-1`).
- Existing instances (do not modify):
  - `stockflow-api`: VM.Standard.A1.Flex, 1 OCPU, 6 GB, AD-1
  - `voiceprompt`: VM.Standard.A1.Flex, 8 OCPU, 48 GB, AD-1
- Regional A1 quota observed: 16 OCPUs / 96 GB.
- Current A1 usage: 9 OCPUs / 54 GB.
- Remaining A1 capacity: 7 OCPUs / 42 GB.
- Proposed instance: `prozesspilot-ollama`, VM.Standard.A1.Flex, 4 OCPU, 24 GB, same AD-1, separate project-specific instance only.
- No GPU shape proposed. CPU-only inference.
- Credit expiry/balance and exact account-wide impact are not available through the current OCI CLI session; verify in the Oracle Console before provisioning. Do not assume free-tier coverage.

## Cost assumptions (26 days, estimate only)

- Compute: 4 OCPU + 24 GB for 26 days ~= USD 48.
- Boot/block volume (50 GB): ~= USD 1.
- Network: assumed minimal (SSH tunnel, no public endpoint).
- Total planning allowance: USD 55. Confirm credit balance before launch.

## Proposed model

- Tag: `qwen2.5:7b` (Ollama default quantization, Q4_K_M)
- License: Apache 2.0 (verify at download time)
- Download size: about 4.7 GB
- Requirements: about 8-12 GB RAM for model + context; 24 GB instance leaves margin
- Justification: small multilingual instruction model suitable for German classification and grounded drafting on CPU
- Digest and exact quantization must be recorded after approved download
- German quality is untested and must be measured, not assumed

## Secure connectivity

- Ollama binds to container port 11434, published only as `127.0.0.1:11434:11434`.
- No public 11434 exposure.
- Initial access from oldmac via SSH tunnel:
  `ssh -N -L 11434:127.0.0.1:11434 opc@<oracle-instance>`
- ProzessPilot uses `OLLAMA_BASE_URL=http://127.0.0.1:11434`.
- Paid-provider fallback remains disabled (`PROVIDER=ollama`).

## Deployment files

- `deploy/ollama/docker-compose.yml`
- `deploy/ollama/.env.example`

## Smoke test (after explicit approval)

1. Provision separate instance only.
2. Install Docker and Compose.
3. Start Compose.
4. Pull exactly `qwen2.5:7b`.
5. Run one classification case and one grounded-drafting case.
6. Measure cold and warm latency.
7. Verify structured JSON, citations, timeout/cancellation, and memory use.
8. If unsuitable, report measurements before resizing or changing models.

## Evaluation labels

`data/eval_cases.json` now includes:
- `acceptable_sources`: acceptable source index sets
- `deliberate_abstention`: true for spam and unclear cases

Citation presence alone is not citation correctness. Human review of unsupported claims remains required. Model confidence is not calibrated probability and does not bypass human approval.

## Bounded evaluation

- Same 12 cases and baseline/improved prompts.
- Record exact model tag/digest, prompt variant, generation settings, calls, retries, errors, timeouts, per-case results, human-reviewed unsupported claims, latency, and resource use.
- Do not invent dollar-per-token costs for self-hosted inference.

## AWS migration (prepare only, no provisioning now)

- Keep same Compose file, model digest, environment-based endpoint, and security approach.
- Use an AWS ARM64 instance (Graviton) to match Oracle A1 architecture.
- Transfer model volume or perform verified re-download; record size and estimated time.
- Validate before cutover; keep Oracle running for rollback.
- Shut down/delete Oracle resources only after explicit approval.
- Begin preparation at least 5 days before the 26-day credit expiry.
