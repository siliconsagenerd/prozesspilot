# ProzessPilot Human Review Packet (offline, not completed)

Generated from `data/evaluations/eval-20261022T190411Z/` only. No model calls were made.
Source snippets captured in raw artifacts are separated from text reconstructed from the current KB.

## case_01

### Synthetic inquiry and customer context
- Body: Hallo, was kostet der ErgoChair 3000 und welche Farben gibt es?
- Customer: Anna Müller (anna.mueller@example.de), tier=standard
- History: Kaufte Laptop-Tasche 2024. Keine Beschwerden.
- Expected classification: product_question
- Acceptable classifications: product_question
- Expected routing: ready_for_review
- Abstention required: False
- Expected source titles: Produkt: ErgoChair 3000

### Baseline run
- Classification: product_question (confidence 0.98)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Draft:
```text
Hallo Anna Müller, der ErgoChair 3000 kostet 349 EUR und ist in den Farben Schwarz, Grau und Blau erhältlich. Quelle: [Produkt: ErgoChair 3000].
```

### Improved run
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: False
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Draft:
```text
Hallo Frau Müller,

der ErgoChair 3000 kostet 349 EUR und ist in den Farben Schwarz, Grau und Blau erhältlich. [Produkt: ErgoChair 3000]

Bei weiteren Fragen stehe ich Ihnen gerne zur Verfügung.

Mit freundlichen Grüßen
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - Produkt: ErgoChair 3000 (score 1.066): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Produkt: DeskPro Monitorarm (score 0.492): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Eskalationsrichtlinie (score 0.309): Eskalation an menschlichen Agenten bei: Beschwerden, VIP-Kunden, offenen Reklamationen, unklaren Anfragen, oder wenn die KI-Konfidenz unter 0.8 liegt. Der menschliche Agent überprüft Entwurf, Quellen und Kundenkontext.
- improved:
  - Produkt: ErgoChair 3000 (score 1.066): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Produkt: DeskPro Monitorarm (score 0.492): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Eskalationsrichtlinie (score 0.309): Eskalation an menschlichen Agenten bei: Beschwerden, VIP-Kunden, offenen Reklamationen, unklaren Anfragen, oder wenn die KI-Konfidenz unter 0.8 liegt. Der menschliche Agent überprüft Entwurf, Quellen und Kundenkontext.

### Reconstructed source text (current KB; provenance uncertain)
- Eskalationsrichtlinie (`policy.escalation`): Eskalation an menschlichen Agenten bei: Beschwerden, VIP-Kunden, offenen Reklamationen, unklaren Anfragen, oder wenn die KI-Konfidenz unter 0.8 liegt. Der menschliche Agent überprüft Entwurf, Quellen und Kundenkontext.
- Produkt: DeskPro Monitorarm (`product.deskpro_monitor_arm`): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
- Produkt: ErgoChair 3000 (`product.ergochair_3000`): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---

## case_02

### Synthetic inquiry and customer context
- Body: Welche Tragkraft hat der DeskPro Monitorarm und ist er VESA-kompatibel?
- Customer: David Koch (david.koch@example.de), tier=standard
- History: Neukunde.
- Expected classification: product_question
- Acceptable classifications: product_question
- Expected routing: ready_for_review
- Abstention required: False
- Expected source titles: Produkt: DeskPro Monitorarm

### Baseline run
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik
- Draft:
```text
Hallo David,

der DeskPro Monitorarm trägt Monitore bis 12 kg und ist VESA-kompatibel (75x75 und 100x100). [Produkt: DeskPro Monitorarm]

Bei weiteren Fragen stehe ich gerne zur Verfügung.

Viele Grüße
```

### Improved run
- Classification: product_question (confidence 1.0)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: False
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik
- Draft:
```text
Hallo Herr Koch,

der DeskPro Monitorarm trägt Monitore bis 12 kg und ist VESA-kompatibel (75x75 und 100x100) [Produkt: DeskPro Monitorarm].

Mit freundlichen Grüßen
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - Produkt: DeskPro Monitorarm (score 1.64): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Produkt: ErgoChair 3000 (score 0.457): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Rückgabe- und Beschwerdepolitik (score 0.424): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.
- improved:
  - Produkt: DeskPro Monitorarm (score 1.64): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Produkt: ErgoChair 3000 (score 0.457): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Rückgabe- und Beschwerdepolitik (score 0.424): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.

### Reconstructed source text (current KB; provenance uncertain)
- Produkt: DeskPro Monitorarm (`product.deskpro_monitor_arm`): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
- Produkt: ErgoChair 3000 (`product.ergochair_3000`): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- Rückgabe- und Beschwerdepolitik (`policy.returns_and_complaints`): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---

## case_03

### Synthetic inquiry and customer context
- Body: Mein ErgoChair 3000 quietscht nach zwei Wochen. Ich moechte ihn zurueckgeben.
- Customer: Anna Müller (anna.mueller@example.de), tier=standard
- History: Kaufte Laptop-Tasche 2024. Keine Beschwerden.
- Expected classification: complaint
- Acceptable classifications: complaint
- Expected routing: requires_human_approval
- Abstention required: False
- Expected source titles: Rueckgabe- und Beschwerdepolitik

### Baseline run
- Classification: complaint (confidence 0.75)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000
- Draft:
```text
Hallo Frau Müller,

es tut uns leid, dass Ihr ErgoChair 3000 nach zwei Wochen quietscht. Laut [Produkt: ErgoChair 3000] hat der Stuhl 5 Jahre Garantie. Wir prüfen gerne eine Rückgabe oder Reparatur; bitte senden Sie uns Ihre Bestellnummer und, falls möglich, ein kurzes Video des Geräuschs. Sobald wir die Angaben haben, melden wir uns mit den nächsten Schritten.

Viele Grüße,
Kundenservice
```

### Improved run
- Classification: complaint (confidence 0.3)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000
- Draft:
```text
Sehr geehrte Frau Müller,

vielen Dank für Ihre Nachricht. Es tut uns leid, dass Ihr ErgoChair 3000 nach zwei Wochen quietscht.

Leider können wir anhand der vorliegenden Informationen keine Rückgabe- oder Garantieabwicklung bestätigen, da hierzu keine passenden Angaben in unserer Wissensdatenbank vorliegen. Wir möchten Ihnen jedoch gerne weiterhelfen und leiten Ihre Anfrage daher an unser Kundens
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - Produkt: ErgoChair 3000 (score 0.609): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- improved:
  - Produkt: ErgoChair 3000 (score 0.609): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.

### Reconstructed source text (current KB; provenance uncertain)
- Produkt: ErgoChair 3000 (`product.ergochair_3000`): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---

## case_04

### Synthetic inquiry and customer context
- Body: Wo ist meine Bestellung #12345? Sie sollte gestern ankommen.
- Customer: David Koch (david.koch@example.de), tier=standard
- History: Neukunde.
- Expected classification: order_status
- Acceptable classifications: order_status
- Expected routing: ready_for_review
- Abstention required: False
- Expected source titles: Bestellstatus-Erklaerung

### Baseline run
- Classification: order_status (confidence 0.72)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Bestellstatus-Erklärung, Produkt: ErgoChair 3000
- Draft:
```text
Hallo David Koch,

ich kann den aktuellen Status Ihrer Bestellung #12345 in dieser Anfrage leider nicht direkt einsehen. Laut [Bestellstatus-Erklärung] erhalten Sie bei Status 'Versandt' eine Trackingnummer per E-Mail; 'Zugestellt' bedeutet, dass das Paket angekommen ist. Die Standardlieferzeit beträgt 3-5 Werktage, Express 1-2 Werktage.

Bitte prüfen Sie zunächst Ihre E-Mails (auch Spam) auf die 
```

### Improved run
- Classification: order_status (confidence 0.3)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Bestellstatus-Erklärung, Produkt: ErgoChair 3000
- Draft:
```text
Sehr geehrter Herr Koch,

vielen Dank für Ihre Anfrage. Leider kann ich den aktuellen Status Ihrer Bestellung #12345 in den vorliegenden Informationen nicht einsehen. Allgemein gilt: 'Versandt' bedeutet, dass das Paket unterwegs ist und die Trackingnummer per E-Mail versendet wurde; 'Zugestellt' bedeutet, dass das Paket angekommen ist. Die Standardlieferzeit beträgt 3-5 Werktage, Express 1-2 Werkt
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - Produkt: DeskPro Monitorarm (score 0.164): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Bestellstatus-Erklärung (score 0.157): Bestellstatus: 'Eingegangen' = Bestellung erhalten. 'In Bearbeitung' = wird vorbereitet. 'Versandt' = Paket unterwegs, Trackingnummer per E-Mail. 'Zugestellt' = Paket angekommen. Lieferzeit Standard: 3-5 Werktage, Express: 1-2 Werktage.
  - Produkt: ErgoChair 3000 (score 0.152): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- improved:
  - Produkt: DeskPro Monitorarm (score 0.164): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Bestellstatus-Erklärung (score 0.157): Bestellstatus: 'Eingegangen' = Bestellung erhalten. 'In Bearbeitung' = wird vorbereitet. 'Versandt' = Paket unterwegs, Trackingnummer per E-Mail. 'Zugestellt' = Paket angekommen. Lieferzeit Standard: 3-5 Werktage, Express: 1-2 Werktage.
  - Produkt: ErgoChair 3000 (score 0.152): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.

### Reconstructed source text (current KB; provenance uncertain)
- Bestellstatus-Erklärung (`policy.order_status`): Bestellstatus: 'Eingegangen' = Bestellung erhalten. 'In Bearbeitung' = wird vorbereitet. 'Versandt' = Paket unterwegs, Trackingnummer per E-Mail. 'Zugestellt' = Paket angekommen. Lieferzeit Standard: 3-5 Werktage, Express: 1-2 Werktage.
- Produkt: DeskPro Monitorarm (`product.deskpro_monitor_arm`): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
- Produkt: ErgoChair 3000 (`product.ergochair_3000`): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---

## case_05

### Synthetic inquiry and customer context
- Body: Koennen Sie mir ein Angebot fuer 5 ErgoChair 3000 und 2 DeskPro Monitorarme machen?
- Customer: Bernd Schmidt (bernd.schmidt@example.de), tier=premium
- History: Stammkunde seit 2022. Hatte Versandproblem 2023 (gelöst).
- Expected classification: quote_request
- Acceptable classifications: quote_request
- Expected routing: requires_human_approval
- Abstention required: False
- Expected source titles: Angebotsanfrage-Prozess

### Baseline run
- Classification: quote_request (confidence 0.92)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Angebotsanfrage-Prozess
- Draft:
```text
Sehr geehrter Herr Schmidt,

gerne erstellen wir Ihnen ein Angebot für 5 ErgoChair 3000 und 2 DeskPro Monitorarme. Auf Basis der Listenpreise aus [Produkt: ErgoChair 3000] (349 EUR) und [Produkt: DeskPro Monitorarm] (89 EUR) ergibt sich vorläufig: 5 x 349 EUR = 1.745 EUR, 2 x 89 EUR = 178 EUR, Gesamt 1.923 EUR. Gemäß [Angebotsanfrage-Prozess] benötigen wir für B2B-Angebote ab 5 Stück noch die Lief
```

### Improved run
- Classification: quote_request (confidence 0.95)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Angebotsanfrage-Prozess
- Draft:
```text
Gerne. Für 5 ErgoChair 3000 (349 EUR/Stück) und 2 DeskPro Monitorarme (89 EUR/Stück) können wir ein Angebot erstellen. Da der Mengenrabatt erst ab 10 Stück gilt, sind diese Stückzahlen ohne Rabatt. Für die Angebotsanfrage benötigen wir noch Ihre Lieferadresse und den gewünschten Liefertermin; das Angebot erhalten Sie innerhalb von 1 Werktag. [Produkt: ErgoChair 3000] [Produkt: DeskPro Monitorarm] 
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - Produkt: ErgoChair 3000 (score 1.218): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Produkt: DeskPro Monitorarm (score 0.656): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Angebotsanfrage-Prozess (score 0.451): Angebotsanfragen für B2B-Kunden ab 5 Stück: bitte Stückzahl, Lieferadresse und gewünschten Liefertermin angeben. Angebote werden innerhalb von 1 Werktag erstellt. Mengenrabatt ab 10 Stück: 5%, ab 50 Stück: 10%.
- improved:
  - Produkt: ErgoChair 3000 (score 1.218): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Produkt: DeskPro Monitorarm (score 0.656): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Angebotsanfrage-Prozess (score 0.451): Angebotsanfragen für B2B-Kunden ab 5 Stück: bitte Stückzahl, Lieferadresse und gewünschten Liefertermin angeben. Angebote werden innerhalb von 1 Werktag erstellt. Mengenrabatt ab 10 Stück: 5%, ab 50 Stück: 10%.

### Reconstructed source text (current KB; provenance uncertain)
- Angebotsanfrage-Prozess (`process.quote_request`): Angebotsanfragen für B2B-Kunden ab 5 Stück: bitte Stückzahl, Lieferadresse und gewünschten Liefertermin angeben. Angebote werden innerhalb von 1 Werktag erstellt. Mengenrabatt ab 10 Stück: 5%, ab 50 Stück: 10%.
- Produkt: DeskPro Monitorarm (`product.deskpro_monitor_arm`): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
- Produkt: ErgoChair 3000 (`product.ergochair_3000`): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---

## case_06

### Synthetic inquiry and customer context
- Body: Sie haben gewonnen! Klicken Sie hier fuer Ihren Preis.
- Customer: None (None), tier=None
- History: None
- Expected classification: spam
- Acceptable classifications: spam
- Expected routing: ready_for_review
- Abstention required: True
- Expected source titles: (none)

### Baseline run
- Classification: spam (confidence 0.97)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000
- Draft:
```text
Vielen Dank für Ihre Nachricht. Diese E-Mail wirkt wie Spam/Phishing; bitte öffnen Sie keine Links und geben Sie keine Daten ein. Für Fragen zu unseren Produkten (z. B. DeskPro Monitorarm, ErgoChair 3000) helfen wir Ihnen gerne weiter.
```

### Improved run
- Classification: spam (confidence 0.1)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: False
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000
- Draft:
```text
Vielen Dank für Ihre Nachricht. Wir können diese Anfrage nicht als legitime Kundenanfrage bestätigen und werden sie nicht weiter bearbeiten. Bei Fragen zu unseren Produkten stehen wir Ihnen gerne zur Verfügung.
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - Produkt: DeskPro Monitorarm (score 0.164): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Produkt: ErgoChair 3000 (score 0.152): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- improved:
  - Produkt: DeskPro Monitorarm (score 0.164): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Produkt: ErgoChair 3000 (score 0.152): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.

### Reconstructed source text (current KB; provenance uncertain)
- Produkt: DeskPro Monitorarm (`product.deskpro_monitor_arm`): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
- Produkt: ErgoChair 3000 (`product.ergochair_3000`): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---

## case_07

### Synthetic inquiry and customer context
- Body: Ich habe eine Frage.
- Customer: Anna Müller (anna.mueller@example.de), tier=standard
- History: Kaufte Laptop-Tasche 2024. Keine Beschwerden.
- Expected classification: unclear
- Acceptable classifications: unclear
- Expected routing: requires_human_approval
- Abstention required: True
- Expected source titles: (none)

### Baseline run
- Classification: unclear (confidence 0.3)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: 
- Draft:
```text
Hallo Anna Müller, gerne helfen wir Ihnen. Bitte teilen Sie uns Ihre Frage mit, damit wir sie beantworten können.
```

### Improved run
- Classification: unclear (confidence 0.6)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: 
- Draft:
```text
Gerne. Bitte teilen Sie uns Ihre Frage mit; dann prüfen wir das gerne. Ohne weitere Details kann ich keine spezifischen Angaben bestätigen und leite bei Bedarf an den zuständigen Bereich weiter.
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - (none captured)
- improved:
  - (none captured)

### Reconstructed source text (current KB; provenance uncertain)

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---

## case_08

### Synthetic inquiry and customer context
- Body: Ist der ErgoChair 3000 in Schwarz sofort lieferbar?
- Customer: Bernd Schmidt (bernd.schmidt@example.de), tier=premium
- History: Stammkunde seit 2022. Hatte Versandproblem 2023 (gelöst).
- Expected classification: product_question
- Acceptable classifications: product_question
- Expected routing: requires_human_approval
- Abstention required: False
- Expected source titles: Produkt: ErgoChair 3000

### Baseline run
- Classification: product_question (confidence 0.8)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Draft:
```text
Hallo Herr Schmidt, laut [Produkt: ErgoChair 3000] ist der ErgoChair 3000 in Schwarz als Farbe verfügbar; die angegebene Lieferzeit beträgt 3-5 Werktage. Eine Lieferung am selben Tag können wir auf Basis dieser Angaben nicht garantieren.
```

### Improved run
- Classification: product_question (confidence 0.65)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Draft:
```text
Sehr geehrter Herr Schmidt,

laut [Produkt: ErgoChair 3000] ist der ErgoChair 3000 in Schwarz erhältlich; die Lieferzeit beträgt 3–5 Werktage. Ob er sofort lieferbar ist, kann ich aus den vorliegenden Informationen nicht bestätigen. Ich leite Ihre Anfrage gerne an den Vertrieb weiter.

Mit freundlichen Grüßen
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - Produkt: ErgoChair 3000 (score 1.066): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Produkt: DeskPro Monitorarm (score 0.328): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Rückgabe- und Beschwerdepolitik (score 0.282): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.
- improved:
  - Produkt: ErgoChair 3000 (score 1.066): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Produkt: DeskPro Monitorarm (score 0.328): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Rückgabe- und Beschwerdepolitik (score 0.282): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.

### Reconstructed source text (current KB; provenance uncertain)
- Produkt: DeskPro Monitorarm (`product.deskpro_monitor_arm`): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
- Produkt: ErgoChair 3000 (`product.ergochair_3000`): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- Rückgabe- und Beschwerdepolitik (`policy.returns_and_complaints`): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---

## case_09

### Synthetic inquiry and customer context
- Body: Der gelieferte ErgoChair 3000 ist beschädigt und die Rechnung ist falsch.
- Customer: Anna Müller (anna.mueller@example.de), tier=standard
- History: Kaufte Laptop-Tasche 2024. Keine Beschwerden.
- Expected classification: complaint
- Acceptable classifications: complaint
- Expected routing: requires_human_approval
- Abstention required: False
- Expected source titles: Rueckgabe- und Beschwerdepolitik

### Baseline run
- Classification: complaint (confidence 0.65)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Draft:
```text
Sehr geehrte Frau Müller,

vielen Dank für Ihre Nachricht. Es tut uns sehr leid zu hören, dass Ihr ErgoChair 3000 beschädigt geliefert wurde und die Rechnung nicht korrekt ist.

Wir nehmen Ihre Beschwerde ernst und leiten diese gemäß unserer Eskalationsrichtlinie an einen unserer Mitarbeiter weiter, der sich umgehend mit Ihnen in Verbindung setzen wird, um die Schadensregulierung und die Korrektur
```

### Improved run
- Classification: complaint (confidence 0.4)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Draft:
```text
Sehr geehrte Frau Müller,

vielen Dank für Ihre Nachricht. Zu Schaden und Rechnung können wir leider keine bestätigten Angaben machen. Gemäß [Eskalationsrichtlinie] leiten wir Ihre Beschwerde an einen menschlichen Agenten weiter, der Entwurf, Quellen und Kundenkontext prüft.

Mit freundlichen Grüßen
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - Produkt: ErgoChair 3000 (score 1.066): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Produkt: DeskPro Monitorarm (score 0.656): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Eskalationsrichtlinie (score 0.463): Eskalation an menschlichen Agenten bei: Beschwerden, VIP-Kunden, offenen Reklamationen, unklaren Anfragen, oder wenn die KI-Konfidenz unter 0.8 liegt. Der menschliche Agent überprüft Entwurf, Quellen und Kundenkontext.
- improved:
  - Produkt: ErgoChair 3000 (score 1.066): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Produkt: DeskPro Monitorarm (score 0.656): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Eskalationsrichtlinie (score 0.463): Eskalation an menschlichen Agenten bei: Beschwerden, VIP-Kunden, offenen Reklamationen, unklaren Anfragen, oder wenn die KI-Konfidenz unter 0.8 liegt. Der menschliche Agent überprüft Entwurf, Quellen und Kundenkontext.

### Reconstructed source text (current KB; provenance uncertain)
- Eskalationsrichtlinie (`policy.escalation`): Eskalation an menschlichen Agenten bei: Beschwerden, VIP-Kunden, offenen Reklamationen, unklaren Anfragen, oder wenn die KI-Konfidenz unter 0.8 liegt. Der menschliche Agent überprüft Entwurf, Quellen und Kundenkontext.
- Produkt: DeskPro Monitorarm (`product.deskpro_monitor_arm`): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
- Produkt: ErgoChair 3000 (`product.ergochair_3000`): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---

## case_10

### Synthetic inquiry and customer context
- Body: Kann ich den ErgoChair 3000 auch in Rot bekommen? Ich bin mir nicht sicher, ob das zu meinem Buero passt.
- Customer: Anna Müller (anna.mueller@example.de), tier=standard
- History: Kaufte Laptop-Tasche 2024. Keine Beschwerden.
- Expected classification: product_question
- Acceptable classifications: product_question
- Expected routing: ready_for_review
- Abstention required: True
- Expected source titles: Produkt: ErgoChair 3000

### Baseline run
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik, Bestellstatus-Erklärung
- Draft:
```text
Hallo Anna Müller, der ErgoChair 3000 ist laut [Produkt: ErgoChair 3000] in Schwarz, Grau und Blau erhältlich; Rot ist derzeit nicht verfügbar. Wenn Sie unsicher sind, ob der Stuhl zu Ihrem Büro passt, können Sie ihn nach [Rückgabe- und Beschwerdepolitik] innerhalb von 30 Tagen unbenutzt und in Originalverpackung zurückgeben.
```

### Improved run
- Classification: product_question (confidence 0.9)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik, Bestellstatus-Erklärung
- Draft:
```text
Vielen Dank für Ihre Anfrage. Der ErgoChair 3000 ist laut unseren Angaben in Schwarz, Grau und Blau erhältlich; Rot ist nicht aufgeführt [Produkt: ErgoChair 3000]. Ob eine Farbe zu Ihrem Büro passt, können wir leider nicht beurteilen.
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - Produkt: ErgoChair 3000 (score 0.609): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Rückgabe- und Beschwerdepolitik (score 0.424): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.
  - Bestellstatus-Erklärung (score 0.157): Bestellstatus: 'Eingegangen' = Bestellung erhalten. 'In Bearbeitung' = wird vorbereitet. 'Versandt' = Paket unterwegs, Trackingnummer per E-Mail. 'Zugestellt' = Paket angekommen. Lieferzeit Standard: 3-5 Werktage, Express: 1-2 Werktage.
- improved:
  - Produkt: ErgoChair 3000 (score 0.609): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Rückgabe- und Beschwerdepolitik (score 0.424): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.
  - Bestellstatus-Erklärung (score 0.157): Bestellstatus: 'Eingegangen' = Bestellung erhalten. 'In Bearbeitung' = wird vorbereitet. 'Versandt' = Paket unterwegs, Trackingnummer per E-Mail. 'Zugestellt' = Paket angekommen. Lieferzeit Standard: 3-5 Werktage, Express: 1-2 Werktage.

### Reconstructed source text (current KB; provenance uncertain)
- Bestellstatus-Erklärung (`policy.order_status`): Bestellstatus: 'Eingegangen' = Bestellung erhalten. 'In Bearbeitung' = wird vorbereitet. 'Versandt' = Paket unterwegs, Trackingnummer per E-Mail. 'Zugestellt' = Paket angekommen. Lieferzeit Standard: 3-5 Werktage, Express: 1-2 Werktage.
- Produkt: ErgoChair 3000 (`product.ergochair_3000`): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- Rückgabe- und Beschwerdepolitik (`policy.returns_and_complaints`): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---

## case_11

### Synthetic inquiry and customer context
- Body: Hat der ErgoChair 3000 eine 10-jaehrige Garantie und ist er in Rot erhaeltlich?
- Customer: David Koch (david.koch@example.de), tier=standard
- History: Neukunde.
- Expected classification: product_question
- Acceptable classifications: product_question
- Expected routing: ready_for_review
- Abstention required: True
- Expected source titles: Produkt: ErgoChair 3000

### Baseline run
- Classification: product_question (confidence 0.98)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Draft:
```text
Vielen Dank für Ihre Anfrage, Herr Koch. Laut [Produkt: ErgoChair 3000] bietet der ErgoChair 3000 eine Garantie von 5 Jahren (nicht 10 Jahre) und ist in den Farben Schwarz, Grau und Blau erhältlich – Rot ist leider nicht im Sortiment. Gern beraten wir Sie zu den verfügbaren Farben oder alternativen Produkten.
```

### Improved run
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Draft:
```text
Vielen Dank für Ihre Anfrage, Herr Koch. Laut unserer Produktinformationen hat der ErgoChair 3000 eine Garantie von 5 Jahren, nicht 10 Jahren [Produkt: ErgoChair 3000]. Zudem ist der Stuhl in den Farben Schwarz, Grau und Blau erhältlich; Rot ist leider nicht im Sortiment [Produkt: ErgoChair 3000]. Gerne können wir Ihnen bei weiteren Fragen oder bei der Auswahl einer passenden Farbe behilflich sein
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - Produkt: ErgoChair 3000 (score 1.218): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Produkt: DeskPro Monitorarm (score 0.656): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Rückgabe- und Beschwerdepolitik (score 0.565): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.
- improved:
  - Produkt: ErgoChair 3000 (score 1.218): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Produkt: DeskPro Monitorarm (score 0.656): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
  - Rückgabe- und Beschwerdepolitik (score 0.565): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.

### Reconstructed source text (current KB; provenance uncertain)
- Produkt: DeskPro Monitorarm (`product.deskpro_monitor_arm`): Der DeskPro Monitorarm trägt Monitore bis 12 kg, ist VESA-kompatibel (75x75 und 100x100) und höhenverstellbar. Preis: 89 EUR. Montage ohne Werkzeug möglich.
- Produkt: ErgoChair 3000 (`product.ergochair_3000`): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- Rückgabe- und Beschwerdepolitik (`policy.returns_and_complaints`): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---

## case_12

### Synthetic inquiry and customer context
- Body: Anna, danke fuer den schnellen Versand letzte Woche. Kann ich den ErgoChair 3000 in Blau nachbestellen?
- Customer: Anna Müller (anna.mueller@example.de), tier=standard
- History: Kaufte Laptop-Tasche 2024. Keine Beschwerden.
- Expected classification: product_question
- Acceptable classifications: product_question
- Expected routing: ready_for_review
- Abstention required: False
- Expected source titles: Produkt: ErgoChair 3000

### Baseline run
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Bestellstatus-Erklärung, Rückgabe- und Beschwerdepolitik
- Draft:
```text
Danke für Ihr Feedback. Ja, der ErgoChair 3000 ist in Blau verfügbar; Preis 349 EUR, Lieferzeit 3-5 Werktage. (Quelle: Produkt: ErgoChair 3000)
```

### Improved run
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Bestellstatus-Erklärung, Rückgabe- und Beschwerdepolitik
- Draft:
```text
Ja, der ErgoChair 3000 ist in Blau erhältlich. Preis: 349 EUR, Lieferzeit: 3-5 Werktage. [Produkt: ErgoChair 3000]
```

### Captured source snippets (from raw kb_search tool output)
- baseline:
  - Produkt: ErgoChair 3000 (score 0.761): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Bestellstatus-Erklärung (score 0.157): Bestellstatus: 'Eingegangen' = Bestellung erhalten. 'In Bearbeitung' = wird vorbereitet. 'Versandt' = Paket unterwegs, Trackingnummer per E-Mail. 'Zugestellt' = Paket angekommen. Lieferzeit Standard: 3-5 Werktage, Express: 1-2 Werktage.
  - Rückgabe- und Beschwerdepolitik (score 0.141): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.
- improved:
  - Produkt: ErgoChair 3000 (score 0.761): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
  - Bestellstatus-Erklärung (score 0.157): Bestellstatus: 'Eingegangen' = Bestellung erhalten. 'In Bearbeitung' = wird vorbereitet. 'Versandt' = Paket unterwegs, Trackingnummer per E-Mail. 'Zugestellt' = Paket angekommen. Lieferzeit Standard: 3-5 Werktage, Express: 1-2 Werktage.
  - Rückgabe- und Beschwerdepolitik (score 0.141): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.

### Reconstructed source text (current KB; provenance uncertain)
- Bestellstatus-Erklärung (`policy.order_status`): Bestellstatus: 'Eingegangen' = Bestellung erhalten. 'In Bearbeitung' = wird vorbereitet. 'Versandt' = Paket unterwegs, Trackingnummer per E-Mail. 'Zugestellt' = Paket angekommen. Lieferzeit Standard: 3-5 Werktage, Express: 1-2 Werktage.
- Produkt: ErgoChair 3000 (`product.ergochair_3000`): Der ErgoChair 3000 ist ein ergonomischer Bürostuhl mit verstellbarer Lendenstütze, atmungsaktivem Mesh-Rücken und 5 Jahren Garantie. Preis: 349 EUR. Lieferzeit: 3-5 Werktage. Farben: Schwarz, Grau, Blau.
- Rückgabe- und Beschwerdepolitik (`policy.returns_and_complaints`): Rückgabe innerhalb von 30 Tagen möglich, sofern das Produkt unbenutzt und in Originalverpackung ist. Beschwerden werden innerhalb von 2 Werktagen bearbeitet. Bei Defekt wird Ersatz oder Reparatur angeboten. Erstattung erfolgt auf das ursprüngliche Zahlungsmittel.

### Blank reviewer fields
- Unsupported claims: ___
- Citation support: ___
- Personalization: ___
- Final reviewer judgment: ___

---
