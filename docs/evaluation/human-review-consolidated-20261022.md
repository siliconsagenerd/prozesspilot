# Consolidated Human Review — 12 Cases (24 Variants)

Recorded-at (documentation): 2026-10-23T04:43:06Z
Actual human review time: completed before this consolidation; exact per-case review timestamps are not captured in the preserved artifacts.
Reviewer: Vishrut Pandey

Historical evaluation: `eval-20261022T190411Z`
Retrieval-fix commit: `d0102c1eebbb661bbad7a943b20ef004cf2bb8fa`
Current HEAD at consolidation: `6692ca0530175f88bdcc56f3d69473970e853386` on `main`
Working tree at consolidation: clean (`git status --porcelain=v1` empty)

Source of judgments: user-supplied human-review decisions, reformatted for recording. These are not new model reviews and do not authorize sending any customer message.

## 1. Preservation and scope

Preserved unchanged:
- original evaluation artifacts under `data/evaluations/eval-20261022T190411Z/`
- original human-review packet: `docs/evaluation/human-review-packet.md`
- existing review record for cases 03, 06, and 09: `docs/evaluation/human-review-decisions-20261022.md`
- retrieval-verification report: `docs/evaluation/retrieval-verification-20261022.md`

This document is documentation only. It does not change implementation, prompts, retrieval configuration, evaluation expectations, historical scores, or artifacts.

## 2. Decision vocabulary

Labels used in this consolidated record:
- `accept`
- `accept-with-notes`
- `conditional approval`
- `needs-editing`
- unresolved rubric question

`Accept` means the draft may be acceptable as historical output; it does not authorize sending a customer message. `Conditional approval` means the draft needs the specified corrections before use and is not approved for delivery as-is.

## 3. Authoritative decisions for cases 03, 06, and 09

These are retained exactly as recorded in `docs/evaluation/human-review-decisions-20261022.md`. They are not replaced by labels from any later summary.

| Case | Variant | Authoritative decision |
|---|---|---|
| case_03 | baseline | needs-editing |
| case_03 | improved | needs-editing |
| case_06 | baseline | needs-editing |
| case_06 | improved | needs-editing |
| case_09 | baseline | needs-editing |
| case_09 | improved | accept |

## 4. Consolidated 24-variant decision table

| Case | Variant | Decision | Primary review note |
|---|---|---|---|
| case_01 | baseline | accept-with-notes | Complete despite automated truncated flag; greeting less professional |
| case_01 | improved | accept | Preferred for tone and email structure |
| case_02 | baseline | accept-with-notes | Facts grounded; register too informal |
| case_02 | improved | accept | Preferred for form of address |
| case_03 | baseline | needs-editing | Warranty supported; return/repair and follow-up requests unsupported; retrieval missed policy |
| case_03 | improved | needs-editing | Honest abstention; truncated mid-sentence; retrieval gap remains |
| case_04 | baseline | conditional approval | Visibly incomplete; spam-folder advice unsourced |
| case_04 | improved | conditional approval | Visibly incomplete; missing explicit citation |
| case_05 | baseline | conditional approval | Visibly incomplete |
| case_05 | improved | conditional approval | Missing process citation and greeting |
| case_06 | baseline | needs-editing | Spam classification correct; substantive response, unsourced advice, product leak |
| case_06 | improved | needs-editing | Better content and no product leak; routing and confidence concerns |
| case_07 | baseline | accept-with-notes | Appropriate clarification; personalization preference |
| case_07 | improved | accept-with-notes | Appropriate clarification; personalization gap |
| case_08 | baseline | accept-with-notes | Color and delivery stated; narrow interpretation of immediate availability |
| case_08 | improved | accept-with-notes | Distinguishes listed information from unverified availability; unsourced Vertrieb forwarding |
| case_09 | baseline | needs-editing | Escalation supported; damage and invoice claims unsupported; truncated |
| case_09 | improved | accept | Assertions map to escalation source; abstains on unsupported procedures |
| case_10 | baseline | conditional approval | Factual answers supported; abstention rubric unresolved |
| case_10 | improved | accept-with-notes | Mixed factual/subjective inquiry handled with explicit abstention |
| case_11 | baseline | accept-with-notes | Corrects false premises; abstention semantics unresolved |
| case_11 | improved | accept-with-notes | Marginally preferred; completeness uncertain |
| case_12 | baseline | accept-with-notes | Facts grounded; acknowledges thanks; no customer name |
| case_12 | improved | accept-with-notes | Facts grounded; too terse; needs warm acknowledgment |

Aggregate reviewer preference as stated by the reviewer: improved 9, baseline 2, tie 1. This is a descriptive result for these 12 cases only and is not a measured performance advantage.

## 5. Artifact-derived routing (not reviewer judgment)

The following values were extracted from preserved raw artifacts. They are separated from reviewer judgments.

| Case | Variant | Classification | Confidence | Actual routing | Expected routing |
|---|---|---|---|---|---|
| case_01 | baseline | product_question | 0.98 | ready_for_review | ready_for_review |
| case_01 | improved | product_question | 0.95 | ready_for_review | ready_for_review |
| case_02 | baseline | product_question | 0.95 | ready_for_review | ready_for_review |
| case_02 | improved | product_question | 1.00 | ready_for_review | ready_for_review |
| case_03 | baseline | complaint | 0.75 | requires_human_approval | requires_human_approval |
| case_03 | improved | complaint | 0.30 | requires_human_approval | requires_human_approval |
| case_04 | baseline | order_status | 0.72 | requires_human_approval | ready_for_review |
| case_04 | improved | order_status | 0.30 | requires_human_approval | ready_for_review |
| case_05 | baseline | quote_request | 0.92 | requires_human_approval | requires_human_approval |
| case_05 | improved | quote_request | 0.95 | requires_human_approval | requires_human_approval |
| case_06 | baseline | spam | 0.97 | ready_for_review | ready_for_review |
| case_06 | improved | spam | 0.10 | requires_human_approval | ready_for_review |
| case_07 | baseline | unclear | 0.30 | requires_human_approval | requires_human_approval |
| case_07 | improved | unclear | 0.60 | requires_human_approval | requires_human_approval |
| case_08 | baseline | product_question | 0.80 | requires_human_approval | requires_human_approval |
| case_08 | improved | product_question | 0.65 | requires_human_approval | requires_human_approval |
| case_09 | baseline | complaint | 0.65 | requires_human_approval | requires_human_approval |
| case_09 | improved | complaint | 0.40 | requires_human_approval | requires_human_approval |
| case_10 | baseline | product_question | 0.95 | ready_for_review | ready_for_review |
| case_10 | improved | product_question | 0.90 | ready_for_review | ready_for_review |
| case_11 | baseline | product_question | 0.98 | ready_for_review | ready_for_review |
| case_11 | improved | product_question | 0.95 | ready_for_review | ready_for_review |
| case_12 | baseline | product_question | 0.95 | ready_for_review | ready_for_review |
| case_12 | improved | product_question | 0.95 | ready_for_review | ready_for_review |

## 6. Detailed review records

### case_01 — baseline
Decision: accept-with-notes

Supported claims: Price 349 EUR; colors Schwarz, Grau, Blau.
Unsupported claims: None identified.
Citation assessment: [Produkt: ErgoChair 3000] supports the stated facts.
Personalization assessment: "Hallo Anna Müller" matches customer data but is less professional than "Frau Müller."
Routing assessment: No specific routing objection recorded.
Review notes: Draft appears complete despite the automated truncated flag. Preserve this mismatch without asserting a known root cause.

### case_01 — improved
Decision: accept

Supported claims: Price 349 EUR; colors Schwarz, Grau, Blau.
Unsupported claims: None identified.
Citation assessment: Correct product citation.
Personalization assessment: "Hallo Frau Müller" is appropriate; includes a closing salutation.
Routing assessment: No specific routing objection recorded.
Review notes: Preferred over baseline for tone and email structure.

### case_02 — baseline
Decision: accept-with-notes

Supported claims: Monitor capacity up to 12 kg; VESA compatibility 75x75 and 100x100.
Unsupported claims: None identified.
Citation assessment: Correct DeskPro product citation.
Personalization assessment: "Hallo David" is too informal for this new-customer service context; prefer "Herr Koch."
Routing assessment: No specific routing objection recorded.
Review notes: Facts are grounded; register needs improvement.

### case_02 — improved
Decision: accept

Supported claims: Monitor capacity up to 12 kg; VESA compatibility 75x75 and 100x100.
Unsupported claims: None identified.
Citation assessment: Correct DeskPro product citation.
Personalization assessment: "Hallo Herr Koch" is appropriate.
Routing assessment: No specific routing objection recorded.
Review notes: Preferred over baseline for form of address.

### case_03 — baseline
Decision: needs-editing

Supported claims: Warranty supported by the captured `Produkt: ErgoChair 3000` source.
Unsupported claims: Return/repair option is unsupported because the captured sources did not include `Rückgabe- und Beschwerdepolitik`. Order-number and video request are procedural additions not supported by captured source text.
Citation assessment: Citation to `Produkt: ErgoChair 3000` supports the warranty claim only. Citation does not support the return/repair or follow-up request claims.
Personalization assessment: Personalization is appropriate for the captured customer context.
Routing assessment: Routing is `requires_human_approval`, consistent with complaint handling and low confidence.
Review notes: Retrieval missed the returns policy. Output is complete, but contains unsupported return/repair framing.

### case_03 — improved
Decision: needs-editing

Supported claims: Honest abstention is supported by the captured sources. Appropriate personalization is supported by the captured customer context.
Unsupported claims: No substantive unsupported factual claim is present; the draft abstains where source support is missing.
Citation assessment: No cited source is used to support an unsupported claim.
Personalization assessment: Personalization is appropriate for the captured customer context.
Routing assessment: Routing is `requires_human_approval`, consistent with complaint handling and low confidence.
Review notes: Output is truncated mid-sentence. Retrieval gap remains.

### case_04 — baseline
Decision: conditional approval

Supported claims: Definitions of Versandt and Zugestellt; tracking number by email; standard delivery 3–5 working days and express delivery 1–2 working days. Acknowledges inability to inspect the actual order status.
Unsupported claims: Spam-folder advice is not in captured source text; reviewer considers it minor unsourced guidance.
Citation assessment: [Bestellstatus-Erklärung] supports status definitions and delivery-time information.
Personalization assessment: Prefer "Herr Koch" to "Hallo David Koch."
Routing assessment: Actual `requires_human_approval` differs from expected `ready_for_review`. Reviewer considers escalation defensible because the actual order status cannot be checked.
Review notes: Visibly ends mid-sentence. Complete the draft and address the noted issues before use. Do not claim a proven token-limit cause.

### case_04 — improved
Decision: conditional approval

Supported claims: Status definitions and delivery times match the captured source; acknowledges inability to inspect actual order status.
Unsupported claims: None identified in the visible text.
Citation assessment: Information maps to Bestellstatus-Erklärung, but an explicit inline source citation is missing.
Personalization assessment: "Sehr geehrter Herr Koch" is appropriate.
Routing assessment: Same actual/expected routing mismatch as baseline; escalation is defensible in the reviewer's judgment.
Review notes: Visibly ends mid-word at "Werkt". Complete the draft and add the missing citation before use. Confidence 0.3 was considered reasonable by the reviewer, not established as calibrated. Preferred over baseline for register and grounded content.

### case_05 — baseline
Decision: conditional approval

Supported claims: ErgoChair 349 EUR each; DeskPro 89 EUR each; 5 chairs = 1,745 EUR, 2 monitor arms = 178 EUR, total = 1,923 EUR. Visible beginning of B2B offer-process statement matches the source.
Unsupported claims: None identified before the cutoff.
Citation assessment: Product and Angebotsanfrage-Prozess citations are present and appropriate.
Personalization assessment: "Sehr geehrter Herr Schmidt" is appropriate.
Routing assessment: `requires_human_approval` matches expected.
Review notes: Visibly ends mid-word at "Lief". Complete the request for required offer information before use.

### case_05 — improved
Decision: conditional approval

Supported claims: Product unit prices; discount starts at 10 units; requested quantities are below that threshold; delivery address and desired delivery date required; offer prepared within one working day.
Unsupported claims: None identified.
Citation assessment: Product citations are present; explicit Angebotsanfrage-Prozess citation is missing for process/discount claims.
Personalization assessment: Opening "Gerne." lacks a personalized greeting for the known premium repeat customer.
Routing assessment: No specific routing objection recorded; use the preserved artifact for actual/expected values.
Review notes: Appears complete despite the automated truncated flag. Add process citation and appropriate greeting before use. Overall comparison with baseline: tie; improved content, baseline tone.

### case_06 — baseline
Decision: needs-editing

Supported claims: Spam classification is correct.
Unsupported claims: Substantive response to spam is inappropriate. Security advice is unsourced. Product names are gratuitously mentioned and irrelevant to the spam inquiry.
Citation assessment: Citations to `Produkt: DeskPro Monitorarm` and `Produkt: ErgoChair 3000` do not support the spam/security response.
Personalization assessment: No meaningful customer personalization is present; customer was not found.
Routing assessment: Routing is `ready_for_review`, consistent with expected spam routing.
Review notes: Spam classification is correct, but response content and citation use are defective.

### case_06 — improved
Decision: needs-editing

Supported claims: Better content with no product leak.
Unsupported claims: No substantive unsupported factual claim is present beyond routing/calibration concerns.
Citation assessment: No irrelevant product citations are present.
Personalization assessment: No meaningful customer personalization is present; customer was not found.
Routing assessment: Routing deviates from expected `ready_for_review`. Confidence `0.1` is implausible for obvious spam.
Review notes: Content improves over baseline, but calibration and routing are defective.

### case_07 — baseline
Decision: accept-with-notes

Supported claims: No substantive factual claims; asks the customer to provide the actual question.
Unsupported claims: None identified.
Citation assessment: No citations needed for this clarification request.
Personalization assessment: Uses customer identity, but prefer "Frau Müller" to "Hallo Anna Müller."
Routing assessment: `unclear` classification and `requires_human_approval` match expected behavior.
Review notes: Appropriate minimal clarification. Reviewer slightly prefers baseline for personalization. Confidence 0.3 was preferred subjectively; this is not a demonstrated calibration advantage.

### case_07 — improved
Decision: accept-with-notes

Supported claims: Asks for the question and states that specific information cannot yet be confirmed.
Unsupported claims: None identified by the reviewer. Conditional forwarding language was judged consistent with the routing.
Citation assessment: No citations needed for the clarification request.
Personalization assessment: No customer name used despite known context.
Routing assessment: `unclear` classification and `requires_human_approval` match expected behavior.
Review notes: Appropriate clarification with a personalization gap. Reviewer questioned confidence 0.6; meaning and calibration of that confidence are not established.

### case_08 — baseline
Decision: accept-with-notes

Supported claims: Schwarz is a listed color; stated delivery time is 3–5 working days.
Unsupported claims: None identified by the reviewer. However, listed color availability must not be treated as confirmed live stock.
Citation assessment: Correct product citation.
Personalization assessment: "Hallo Herr Schmidt" is appropriate.
Routing assessment: `requires_human_approval` matches expected.
Review notes: Interprets "sofort lieferbar" narrowly as same-day delivery. Reviewer accepts the limitation statement but notes that the customer may instead mean current stock availability.

### case_08 — improved
Decision: accept-with-notes

Supported claims: Schwarz is listed; delivery time 3–5 working days; immediate availability cannot be confirmed from the captured source.
Unsupported claims: Forwarding specifically to "Vertrieb" is not supported by the captured source. Reviewer judged this minor, but it remains an unsourced operational promise.
Citation assessment: Correct product citation for product facts.
Personalization assessment: "Sehr geehrter Herr Schmidt" is appropriate.
Routing assessment: No specific routing objection recorded; do not infer that an actual transfer to Vertrieb occurred.
Review notes: Preferred for explicitly distinguishing listed product information from unverified immediate availability.

### case_09 — baseline
Decision: needs-editing

Supported claims: Escalation is supported by the captured `Eskalationsrichtlinie` source.
Unsupported claims: Damage resolution process is unsupported. Invoice-correction process is unsupported.
Citation assessment: `Eskalationsrichtlinie` supports escalation only. Product citations do not support damage resolution or invoice correction.
Personalization assessment: Personalization is appropriate for the captured customer context.
Routing assessment: Routing is `requires_human_approval`, consistent with complaint handling and low confidence.
Review notes: Output is truncated. Damage and invoice claims are unsupported.

### case_09 — improved
Decision: accept

Supported claims: All assertions map to the captured `Eskalationsrichtlinie` source. Correctly abstains on unsupported damage and invoice procedures.
Unsupported claims: None identified in the accepted draft.
Citation assessment: Citation to `Eskalationsrichtlinie` supports the escalation and abstention behavior.
Personalization assessment: Personalization is appropriate for the captured customer context.
Routing assessment: Routing is `requires_human_approval`, consistent with complaint handling and low confidence.
Review notes: Retrieval gap remains, but does not invalidate the draft.

### case_10 — baseline
Decision: conditional approval

Supported claims: Listed colors; quoted 30-day return conditions requiring unused condition and original packaging.
Unsupported claims: None identified by the reviewer. The stronger statement "Rot ist derzeit nicht verfügbar" should be distinguished from the narrower evidence that Rot is not listed.
Citation assessment: Product and returns-policy citations support the quoted information.
Personalization assessment: Prefer "Frau Müller" to "Hallo Anna Müller."
Routing assessment: Abstention compliance is unresolved because the meaning of `abstention_required` is ambiguous for this mixed inquiry.
Review notes: Preserve the original "CONDITIONAL APPROVE / FLAG" judgment. Factual answers are supported, but the draft does not explicitly abstain on subjective office suitability. Do not resolve the rubric ambiguity or rescore history.

### case_10 — improved
Decision: accept-with-notes

Supported claims: Listed colors; Rot is not listed; office suitability cannot be judged from the available information.
Unsupported claims: None identified.
Citation assessment: Correct product citation.
Personalization assessment: No customer name despite known identity.
Routing assessment: Reviewer accepts answering the factual component while explicitly abstaining on subjective suitability. Formal abstention-rubric interpretation remains unresolved.
Review notes: Preferred handling of the mixed factual/subjective inquiry.

### case_11 — baseline
Decision: accept-with-notes

Supported claims: Warranty is 5 years, not 10; listed colors are Schwarz, Grau, Blau.
Unsupported claims: Offer to advise on alternative products lacks supporting captured information; reviewer considers it minor.
Citation assessment: Correct product citation for factual corrections.
Personalization assessment: "Herr Koch" is appropriate.
Routing assessment: Abstention semantics remain unresolved. Reviewer considers correcting false premises preferable to refusing to answer supported factual questions.
Review notes: Preserve approval and the minor unsupported-offer note. Do not silently redefine `abstention_required`.

### case_11 — improved
Decision: accept-with-notes

Supported claims: Warranty is 5 years, not 10; listed colors are Schwarz, Grau, Blau.
Unsupported claims: None identified by the reviewer. Distinguish the source's listed colors from a broader inventory claim about Rot.
Citation assessment: Product citations accompany the corrected claims.
Personalization assessment: "Herr Koch" is appropriate.
Routing assessment: Same unresolved abstention semantics as baseline; reviewer accepts source-backed correction of false premises.
Review notes: Preferred marginally for dropping the unsupported alternative-products offer. Ending near "behilflich sein" has uncertain completeness; do not infer generation-time truncation from the flag.

### case_12 — baseline
Decision: accept-with-notes

Supported claims: Blau is a listed color; price 349 EUR; stated delivery time 3–5 working days.
Unsupported claims: None identified by the reviewer; no live-stock confirmation should be inferred from the listed color.
Citation assessment: "(Quelle: Produkt: ErgoChair 3000)" is present and supports the product facts.
Personalization assessment: Acknowledges the customer's thanks but does not use the known customer name.
Routing assessment: `ready_for_review` matches expected.
Review notes: Slightly preferred for acknowledging the positive feedback.

### case_12 — improved
Decision: accept-with-notes

Supported claims: Blau is a listed color; price 349 EUR; stated delivery time 3–5 working days.
Unsupported claims: None identified.
Citation assessment: Correct product citation.
Personalization assessment: Too terse; no greeting, customer name, or acknowledgment of the customer's thanks.
Routing assessment: `ready_for_review` matches expected.
Review notes: Facts are grounded. A human editor should add a warm acknowledgment, such as thanking Frau Müller for her feedback.

## 7. Evidence qualifications (separate from reviewer notes)

- Visibly incomplete drafts were observed in the historical outputs. Generation-time truncation and its root cause remain unverified; automated truncated flags are not proof of a token-limit cause.
- Confidence and calibration concerns in the review notes are qualitative reviewer opinions, not a measured calibration result or a proven calibration defect.
- Historical complaint-policy retrieval failures for cases 03 and 09 were subsequently addressed in current-code offline checks. Those checks are not an end-to-end rerun of the historical evaluation and do not change historical model outputs.
- Abstention semantics for cases 10 and 11 remain a rubric question. The reviewer's preference for source-backed factual correction over refusal is recorded as judgment, not a resolution of the rubric.
- Reviewer preference counts (improved 9, baseline 2, tie 1) are descriptive for these 12 cases only.
- Listed product colors must not be treated as confirmed live stock or real-time availability.

## 8. Unresolved label discrepancies

- Cases 03, 06, and 09 retain their authoritative decisions exactly as recorded in `docs/evaluation/human-review-decisions-20261022.md`.
- The user's later narrative summary is not present as a separate artifact in the repository. If an external summary uses labels such as "FAIL" or "CONDITIONAL," those should be treated as narrative wording. Where such labels differ from the authoritative decisions above, both should be retained and the discrepancy recorded here.
- Unresolved rubric questions remain for cases 10 and 11 regarding abstention semantics.

## 9. Prioritized defect backlog (not implemented)

1. Output completeness and missing diagnostic evidence: visibly incomplete drafts, missing finish-reason/token evidence, and unclear completeness near cutoffs.
2. Unsupported procedural claims and operational promises: unsourced return/repair, spam/security, damage, invoice, and forwarding promises.
3. Missing claim-level citations: drafts and procedural claims without explicit source support.
4. Confidence semantics and routing expectations: implausible confidence values, routing mismatches, and unclear meaning of confidence scores.
5. Greeting, register, and acknowledgment of customer context: informal or missing greetings, missing customer-name use, and missing acknowledgment of positive or mixed inquiries.

No backlog item has been implemented by this document.

## 10. Provenance summary

- Historical evaluation: `eval-20261022T190411Z`
- Retrieval-fix commit: `d0102c1eebbb661bbad7a943b20ef004cf2bb8fa`
- Current HEAD: `6692ca0530175f88bdcc56f3d69473970e853386` on `main`
- Consolidation recorded-at: `2026-10-23T04:43:06Z`
- Original review packet: `docs/evaluation/human-review-packet.md`
- Existing 3-case review record: `docs/evaluation/human-review-decisions-20261022.md`
- Retrieval verification: `docs/evaluation/retrieval-verification-20261022.md`
