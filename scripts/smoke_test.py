#!/usr/bin/env python3
"""Bounded ProzessPilot smoke test against the local backend.

This script is intentionally not run during startup verification. It performs
one classification and one grounded draft through the normal API. It makes
model calls only when explicitly executed.
"""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request

BASE_URL = "http://127.0.0.1:18099"
TIMEOUT_SECONDS = 30


def fetch_json(method: str, url: str, payload: dict | None = None) -> tuple[int, dict]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, method=method)
    if data is not None:
        request.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            status = response.status
            raw = response.read()
    except urllib.error.HTTPError as exc:
        raw = exc.read()
        detail = raw.decode("utf-8", errors="replace")[:300]
        raise RuntimeError(f"{method} {url} failed with HTTP {exc.code}: {detail}") from exc
    except Exception as exc:
        raise RuntimeError(f"{method} {url} failed: {exc}") from exc

    try:
        body = json.loads(raw.decode("utf-8")) if raw else {}
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{method} {url} returned non-JSON HTTP {status}: {raw[:200]!r}") from exc
    if not isinstance(body, dict):
        raise RuntimeError(f"{method} {url} returned JSON that is not an object: {type(body).__name__}")
    if status >= 400:
        raise RuntimeError(f"{method} {url} failed with HTTP {status}: {body}")
    return status, body


def require_key(body: dict, key: str, context: str) -> None:
    if key not in body:
        raise RuntimeError(f"{context} response is missing required key {key!r}; got keys {sorted(body)}")


def main() -> int:
    status, schema = fetch_json("GET", f"{BASE_URL}/openapi.json")
    paths = schema.get("paths", {})
    for required_path in ("/api/inquiries", "/api/inquiries/{inquiry_id}/run", "/api/runs/{run_id}"):
        if required_path not in paths:
            raise RuntimeError(f"OpenAPI schema is missing {required_path}")

    inquiry_schema = schema.get("components", {}).get("schemas", {}).get("InquiryIn", {})
    required_fields = inquiry_schema.get("required", [])
    if "body" not in required_fields:
        raise RuntimeError(f"InquiryIn required fields do not include 'body': {required_fields}")

    inquiry_payload = {"body": "Kurze Testanfrage: Bitte klassifizieren und einen kurzen Antwortentwurf erstellen."}
    _, inquiry = fetch_json("POST", f"{BASE_URL}/api/inquiries", inquiry_payload)
    require_key(inquiry, "id", "create inquiry")
    inquiry_id = inquiry["id"]

    _, run = fetch_json("POST", f"{BASE_URL}/api/inquiries/{inquiry_id}/run?prompt_variant=improved")
    require_key(run, "run_id", "run workflow")
    run_id = run["run_id"]

    _, result = fetch_json("GET", f"{BASE_URL}/api/runs/{run_id}")
    print(json.dumps(
        {
            "inquiry_id": inquiry_id,
            "run_id": run_id,
            "run_keys": sorted(result),
            "classification": result.get("classification"),
            "confidence": result.get("confidence"),
            "state": result.get("state"),
        },
        ensure_ascii=False,
        indent=2,
    ))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"smoke test failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
