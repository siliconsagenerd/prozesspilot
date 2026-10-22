"""Evaluation cases (German synthetic inquiries)."""

from __future__ import annotations

import json

from prozesspilot.config import ROOT

CASES = json.loads((ROOT / "data" / "eval_cases.json").read_text(encoding="utf-8"))