# Human Review Decisions — 2026-10-22

Reviewer: Vishrut Pandey
Review date/time UTC: 2026-10-22T21:09:30Z
Packet path: /Users/vishrutpandeymacbook/Documents/prozesspilot-human-review-packet.md
Frozen implementation commit: d0102c1eebbb661bbad7a943b20ef004cf2bb8fa

Scope: Cases 03, 06, and 09 only. No other cases were reviewed.

## case_03 — baseline
Decision: needs_editing

Supported claims:
- Warranty claim is supported by the captured `Produkt: ErgoChair 3000` source.

Unsupported claims:
- Return/repair option is unsupported because the captured sources did not include `Rückgabe- und Beschwerdepolitik`.
- Order-number and video request are procedural additions not supported by captured source text.

Citation assessment:
- Citation to `Produkt: ErgoChair 3000` supports the warranty claim only.
- Citation does not support the return/repair or follow-up request claims.

Personalization assessment:
- Personalization is appropriate for the captured customer context.

Routing assessment:
- Routing is `requires_human_approval`, consistent with complaint handling and low confidence.

Review notes:
- Retrieval missed the returns policy.
- Output is complete, but contains unsupported return/repair framing.

## case_03 — improved
Decision: needs_editing

Supported claims:
- Honest abstention is supported by the captured sources.
- Appropriate personalization is supported by the captured customer context.

Unsupported claims:
- No substantive unsupported factual claim is present; the draft abstains where source support is missing.

Citation assessment:
- No cited source is used to support an unsupported claim.

Personalization assessment:
- Personalization is appropriate for the captured customer context.

Routing assessment:
- Routing is `requires_human_approval`, consistent with complaint handling and low confidence.

Review notes:
- Output is truncated mid-sentence.
- Retrieval gap remains.

## case_06 — baseline
Decision: needs_editing

Supported claims:
- Spam classification is correct.

Unsupported claims:
- Substantive response to spam is inappropriate.
- Security advice is unsourced.
- Product names are gratuitously mentioned and irrelevant to the spam inquiry.

Citation assessment:
- Citations to `Produkt: DeskPro Monitorarm` and `Produkt: ErgoChair 3000` do not support the spam/security response.

Personalization assessment:
- No meaningful customer personalization is present; customer was not found.

Routing assessment:
- Routing is `ready_for_review`, consistent with expected spam routing.

Review notes:
- Spam classification is correct, but response content and citation use are defective.

## case_06 — improved
Decision: needs_editing

Supported claims:
- Better content with no product leak.

Unsupported claims:
- No substantive unsupported factual claim is present beyond routing/calibration concerns.

Citation assessment:
- No irrelevant product citations are present.

Personalization assessment:
- No meaningful customer personalization is present; customer was not found.

Routing assessment:
- Routing deviates from expected `ready_for_review`.
- Confidence `0.1` is implausible for obvious spam.

Review notes:
- Content improves over baseline, but calibration and routing are defective.

## case_09 — baseline
Decision: needs_editing

Supported claims:
- Escalation is supported by the captured `Eskalationsrichtlinie` source.

Unsupported claims:
- Damage resolution process is unsupported.
- Invoice-correction process is unsupported.

Citation assessment:
- `Eskalationsrichtlinie` supports escalation only.
- Product citations do not support damage resolution or invoice correction.

Personalization assessment:
- Personalization is appropriate for the captured customer context.

Routing assessment:
- Routing is `requires_human_approval`, consistent with complaint handling and low confidence.

Review notes:
- Output is truncated.
- Damage and invoice claims are unsupported.

## case_09 — improved
Decision: accept

Supported claims:
- All assertions map to the captured `Eskalationsrichtlinie` source.
- Correctly abstains on unsupported damage and invoice procedures.

Unsupported claims:
- None identified in the accepted draft.

Citation assessment:
- Citation to `Eskalationsrichtlinie` supports the escalation and abstention behavior.

Personalization assessment:
- Personalization is appropriate for the captured customer context.

Routing assessment:
- Routing is `requires_human_approval`, consistent with complaint handling and low confidence.

Review notes:
- Retrieval gap remains, but does not invalidate the draft.

# Defect summary

- Retrieval defect affecting cases 03 and 09: the historical evaluation missed the returns policy source for both cases.
- Baseline hallucination defects: case_03 included unsupported return/repair and follow-up claims; case_06 responded substantively to spam with unsourced security advice and irrelevant product mentions; case_09 included unsupported damage-resolution and invoice-correction claims.
- Improved-run defects: case_03 output was truncated mid-sentence; case_06 routing deviated from expected `ready_for_review` with implausible confidence `0.1`; case_09 retrieval gap remained but the draft was accepted.
- The later offline retrieval fix was not part of this historical evaluation and is not reflected in the raw results reviewed here.
