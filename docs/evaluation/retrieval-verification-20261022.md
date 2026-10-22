# Read-only retrieval verification — 2026-10-22

Read-only check. No model calls, no new evaluation run, no artifact overwrite, and no source/config/test changes.

## case_03

### Exact input used
- Inquiry body: `Mein ErgoChair 3000 quietscht nach zwei Wochen. Ich moechte ihn zurueckgeben.`
- Customer context: `{"name": "Anna Müller", "email": "anna.mueller@example.de", "tier": "standard", "history": "Kaufte Laptop-Tasche 2024. Keine Beschwerden."}`

### Current retrieval results
- rank 1: title=Produkt: ErgoChair 3000; source_key=product.ergochair_3000; category=product; score=0.656
- rank 2: title=Rückgabe- und Beschwerdepolitik; source_key=policy.returns_and_complaints; category=policy; score=0.25
- rank 3: title=Eskalationsrichtlinie; source_key=policy.escalation; category=escalation; score=0.25
- `Rückgabe- und Beschwerdepolitik` returned: **True**

### Historical captured results (baseline)
- rank 1: title=Produkt: ErgoChair 3000; id=375d5b64-4611-4465-bd2b-ce61e5e16e51; category=product; score=0.609; snippet=Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- `Rückgabe- und Beschwerdepolitik` returned: **False**

### Historical captured results (improved)
- rank 1: title=Produkt: ErgoChair 3000; id=375d5b64-4611-4465-bd2b-ce61e5e16e51; category=product; score=0.609; snippet=Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- `Rückgabe- und Beschwerdepolitik` returned: **False**

### Changed/unchanged determination
- Current retrieval adds `Rückgabe- und Beschwerdepolitik` and `Eskalationsrichtlinie` to the previously product-only result.
- Historical captured retrieval did not return `Rückgabe- und Beschwerdepolitik` for either baseline or improved.
- Therefore the current retrieval fix **changes** the historical retrieval outcome for both cases.

### Limitations
- This verifies current-code retrieval behavior only.
- It is not a rerun of the historical end-to-end evaluation.
- It does not regenerate LLM drafts or overwrite historical artifacts.

---

## case_09

### Exact input used
- Inquiry body: `Der gelieferte ErgoChair 3000 ist beschädigt und die Rechnung ist falsch.`
- Customer context: `{"name": "Anna Müller", "email": "anna.mueller@example.de", "tier": "standard", "history": "Kaufte Laptop-Tasche 2024. Keine Beschwerden."}`

### Current retrieval results
- rank 1: title=Produkt: ErgoChair 3000; source_key=product.ergochair_3000; category=product; score=0.656
- rank 2: title=Rückgabe- und Beschwerdepolitik; source_key=policy.returns_and_complaints; category=policy; score=0.25
- rank 3: title=Eskalationsrichtlinie; source_key=policy.escalation; category=escalation; score=0.25
- `Rückgabe- und Beschwerdepolitik` returned: **True**

### Historical captured results (baseline)
- rank 1: title=Produkt: ErgoChair 3000; id=375d5b64-4611-4465-bd2b-ce61e5e16e51; category=product; score=1.066; snippet=Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- rank 2: title=Produkt: DeskPro Monitorarm; id=466e4ba1-681c-4b42-b724-a5a757f67cfa; category=product; score=0.656; snippet=Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
- rank 3: title=Eskalationsrichtlinie; id=5ccaba78-46d0-47af-beb8-621b305ee549; category=escalation; score=0.463; snippet=Eskalation an menschlichen Agenten bei: Beschwerden, VIP-Kunden, offenen Reklamationen, unklaren Anfragen, oder wenn die KI-Konfidenz unter 0.8 liegt. Der menschliche Agent überprüft Entwurf, Quellen und Kundenkontext.
- `Rückgabe- und Beschwerdepolitik` returned: **False**

### Historical captured results (improved)
- rank 1: title=Produkt: ErgoChair 3000; id=375d5b64-4611-4465-bd2b-ce61e5e16e51; category=product; score=1.066; snippet=Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- rank 2: title=Produkt: DeskPro Monitorarm; id=466e4ba1-681c-4b42-b724-a5a757f67cfa; category=product; score=0.656; snippet=Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
- rank 3: title=Eskalationsrichtlinie; id=5ccaba78-46d0-47af-beb8-621b305ee549; category=escalation; score=0.463; snippet=Eskalation an menschlichen Agenten bei: Beschwerden, VIP-Kunden, offenen Reklamationen, unklaren Anfragen, oder wenn die KI-Konfidenz unter 0.8 liegt. Der menschliche Agent überprüft Entwurf, Quellen und Kundenkontext.
- `Rückgabe- und Beschwerdepolitik` returned: **False**

### Changed/unchanged determination
- Current retrieval adds `Rückgabe- und Beschwerdepolitik` and `Eskalationsrichtlinie` in place of the second product and changes the escalation score/rank.
- Historical captured retrieval did not return `Rückgabe- und Beschwerdepolitik` for either baseline or improved.
- Therefore the current retrieval fix **changes** the historical retrieval outcome for both cases.

### Limitations
- This verifies current-code retrieval behavior only.
- It is not a rerun of the historical end-to-end evaluation.
- It does not regenerate LLM drafts or overwrite historical artifacts.

---

## Verification commands

- Retrieval regression tests: `tests/backend/test_kb_retrieval.py` — 5 passed, exit code 0.
- HEAD: d0102c1eebbb661bbad7a943b20ef004cf2bb8fa
- Working tree: clean on `main`.
