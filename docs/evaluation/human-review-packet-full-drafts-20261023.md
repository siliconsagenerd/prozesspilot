# ProzessPilot Human Review Packet - Full Drafts (separately versioned)

Generated 2026-10-23 from retained historical run/database records. No model calls were made.

## Provenance and matching evidence
- Historical evaluation ID: `eval-20261022T190411Z`
- Raw artifacts: `data/evaluations/eval-20261022T190411Z/raw/*.json`
- Authoritative full drafts: `Draft.original_text` retrieved from the local SQLite database by matching `WorkflowRun.id` to the `run_id` stored in each raw artifact.
- Matching evidence: raw artifact `run_id` equals database `workflow_runs.id`; raw artifact `inquiry_id` equals database `inquiries.id`; inquiry body in the database matches the case body in `data/eval_cases.json`.
- Preview field: `WorkflowStep.output_summary` for the draft step. It is a display preview only and is not authoritative.
- This packet preserves the earlier `human-review-packet.md`. Earlier human decisions were based on 400-character previews for drafts longer than 400 characters; those judgments are flagged below for re-review. No revised human decisions are fabricated.

## Qualification of earlier review
The earlier human-review packet used `WorkflowStep.output_summary`, truncated to 400 characters, as the draft text. For runs where `Draft.original_text` exceeds 400 characters, review judgments based on the earlier packet are preview-limited and should be re-reviewed using this packet.

## case_01

### Synthetic inquiry and customer context
- Body: Hallo, wo kann ich den ErgoChair 3000 in Grau bestellen und wie lange dauert die Lieferung?
- Customer email: anna.mueller@example.de
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: product_question
- Acceptable classifications: 
- Expected routing: ready_for_review
- Deliberate abstention expected: False
- Expected source titles: product.ergochair_3000

### Baseline run
- Run ID: 74e87bba-7371-4456-9ae7-f262e601d065
- Classification: product_question (confidence 0.98)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Full draft length: 144; preview length: 144
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Hallo Anna Müller, der ErgoChair 3000 kostet 349 EUR und ist in den Farben Schwarz, Grau und Blau erhältlich. Quelle: [Produkt: ErgoChair 3000].
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: c7bfe99d-25c5-425a-876d-772efdd3f704
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: False
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Full draft length: 219; preview length: 219
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Hallo Frau Müller,

der ErgoChair 3000 kostet 349 EUR und ist in den Farben Schwarz, Grau und Blau erhältlich. [Produkt: ErgoChair 3000]

Bei weiteren Fragen stehe ich Ihnen gerne zur Verfügung.

Mit freundlichen Grüßen
```

### Human review
- Decision: 
- Notes: 

## case_02

### Synthetic inquiry and customer context
- Body: Mein DeskPro Monitorarm ist nach 2 Wochen kaputt gegangen, ich bin sehr unzufrieden!
- Customer email: clara.weber@example.de
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: complaint
- Acceptable classifications: 
- Expected routing: requires_human_approval
- Deliberate abstention expected: False
- Expected source titles: product.deskpro_monitor_arm, policy.returns_and_complaints, policy.escalation

### Baseline run
- Run ID: 7417d969-f7f1-4da7-a2eb-9e1d8787ef34
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik
- Cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik
- Full draft length: 201; preview length: 201
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Hallo David,

der DeskPro Monitorarm trägt Monitore bis 12 kg und ist VESA-kompatibel (75x75 und 100x100). [Produkt: DeskPro Monitorarm]

Bei weiteren Fragen stehe ich gerne zur Verfügung.

Viele Grüße
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: 058ea51b-f83a-4394-8b51-6c2c8b7718dc
- Classification: product_question (confidence 1.0)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: False
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik
- Cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik
- Full draft length: 165; preview length: 165
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Hallo Herr Koch,

der DeskPro Monitorarm trägt Monitore bis 12 kg und ist VESA-kompatibel (75x75 und 100x100) [Produkt: DeskPro Monitorarm].

Mit freundlichen Grüßen
```

### Human review
- Decision: 
- Notes: 

## case_03

### Synthetic inquiry and customer context
- Body: Können Sie mir den Status meiner Bestellung #12345 mitteilen?
- Customer email: bernd.schmidt@example.de
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: order_status
- Acceptable classifications: 
- Expected routing: ready_for_review
- Deliberate abstention expected: False
- Expected source titles: policy.order_status

### Baseline run
- Run ID: 3c97e5f3-f5d1-475a-8e99-6e8cf97bf368
- Classification: complaint (confidence 0.75)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000
- Cited sources: Produkt: ErgoChair 3000
- Full draft length: 391; preview length: 391
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Hallo Frau Müller,

es tut uns leid, dass Ihr ErgoChair 3000 nach zwei Wochen quietscht. Laut [Produkt: ErgoChair 3000] hat der Stuhl 5 Jahre Garantie. Wir prüfen gerne eine Rückgabe oder Reparatur; bitte senden Sie uns Ihre Bestellnummer und, falls möglich, ein kurzes Video des Geräuschs. Sobald wir die Angaben haben, melden wir uns mit den nächsten Schritten.

Viele Grüße,
Kundenservice
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: c42dbed9-d7d9-459f-ac04-76dabc700df0
- Classification: complaint (confidence 0.3)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000
- Cited sources: Produkt: ErgoChair 3000
- Full draft length: 584; preview length: 400
- Preview-limited earlier judgment: YES (re-review recommended using full draft below)
- Draft review status: full
- Full draft:
```text
Sehr geehrte Frau Müller,

vielen Dank für Ihre Nachricht. Es tut uns leid, dass Ihr ErgoChair 3000 nach zwei Wochen quietscht.

Leider können wir anhand der vorliegenden Informationen keine Rückgabe- oder Garantieabwicklung bestätigen, da hierzu keine passenden Angaben in unserer Wissensdatenbank vorliegen. Wir möchten Ihnen jedoch gerne weiterhelfen und leiten Ihre Anfrage daher an unser Kundenservice-Team weiter, das sich mit den Rückgabe- und Garantiebedingungen für den ErgoChair 3000 vertraut machen und sich bei Ihnen melden wird.

Mit freundlichen Grüßen
Ihr Kundenservice
```

### Human review
- Decision: 
- Notes: 

## case_04

### Synthetic inquiry and customer context
- Body: Wir benötigen ein Angebot für 20 ErgoChair 3000 für unser Büro, Lieferung nach München.
- Customer email: bernd.schmidt@example.de
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: quote_request
- Acceptable classifications: 
- Expected routing: requires_human_approval
- Deliberate abstention expected: False
- Expected source titles: process.quote_request, product.ergochair_3000

### Baseline run
- Run ID: 7f4d5a4d-af9c-4b98-b92f-563a4d2ec883
- Classification: order_status (confidence 0.72)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Bestellstatus-Erklärung, Produkt: ErgoChair 3000
- Cited sources: Produkt: DeskPro Monitorarm, Bestellstatus-Erklärung, Produkt: ErgoChair 3000
- Full draft length: 681; preview length: 400
- Preview-limited earlier judgment: YES (re-review recommended using full draft below)
- Draft review status: full
- Full draft:
```text
Hallo David Koch,

ich kann den aktuellen Status Ihrer Bestellung #12345 in dieser Anfrage leider nicht direkt einsehen. Laut [Bestellstatus-Erklärung] erhalten Sie bei Status 'Versandt' eine Trackingnummer per E-Mail; 'Zugestellt' bedeutet, dass das Paket angekommen ist. Die Standardlieferzeit beträgt 3-5 Werktage, Express 1-2 Werktage.

Bitte prüfen Sie zunächst Ihre E-Mails (auch Spam) auf die Versandbestätigung bzw. Trackingnummer. Wenn Sie keine Trackinginformationen erhalten haben oder das Paket trotz Status 'Zugestellt' nicht bei Ihnen ist, antworten Sie bitte mit Ihrer Bestellnummer und der Lieferadresse, damit wir den Fall prüfen können.

Viele Grüße
Kundenservice
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: 0d7067e9-9f42-45e2-a5e0-0d05d06ed858
- Classification: order_status (confidence 0.3)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Bestellstatus-Erklärung, Produkt: ErgoChair 3000
- Cited sources: Produkt: DeskPro Monitorarm, Bestellstatus-Erklärung, Produkt: ErgoChair 3000
- Full draft length: 657; preview length: 400
- Preview-limited earlier judgment: YES (re-review recommended using full draft below)
- Draft review status: full
- Full draft:
```text
Sehr geehrter Herr Koch,

vielen Dank für Ihre Anfrage. Leider kann ich den aktuellen Status Ihrer Bestellung #12345 in den vorliegenden Informationen nicht einsehen. Allgemein gilt: 'Versandt' bedeutet, dass das Paket unterwegs ist und die Trackingnummer per E-Mail versendet wurde; 'Zugestellt' bedeutet, dass das Paket angekommen ist. Die Standardlieferzeit beträgt 3-5 Werktage, Express 1-2 Werktage [Bestellstatus-Erklärung].

Da ich den konkreten Status Ihrer Bestellung nicht bestätigen kann, leite ich Ihre Anfrage gerne an unser Serviceteam weiter, das den aktuellen Stand prüfen und Sie informieren kann.

Mit freundlichen Grüßen
Ihr Kundenservice
```

### Human review
- Decision: 
- Notes: 

## case_05

### Synthetic inquiry and customer context
- Body: GEWINNEN SIE EIN IPHONE!!! Klicken Sie hier: http://spam.example
- Customer email: None
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: spam
- Acceptable classifications: 
- Expected routing: requires_human_approval
- Deliberate abstention expected: True
- Expected source titles: 

### Baseline run
- Run ID: 3ec1ca60-c21b-43df-8ec0-56d13f5bd01f
- Classification: quote_request (confidence 0.92)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Angebotsanfrage-Prozess
- Cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Angebotsanfrage-Prozess
- Full draft length: 697; preview length: 400
- Preview-limited earlier judgment: YES (re-review recommended using full draft below)
- Draft review status: full
- Full draft:
```text
Sehr geehrter Herr Schmidt,

gerne erstellen wir Ihnen ein Angebot für 5 ErgoChair 3000 und 2 DeskPro Monitorarme. Auf Basis der Listenpreise aus [Produkt: ErgoChair 3000] (349 EUR) und [Produkt: DeskPro Monitorarm] (89 EUR) ergibt sich vorläufig: 5 x 349 EUR = 1.745 EUR, 2 x 89 EUR = 178 EUR, Gesamt 1.923 EUR. Gemäß [Angebotsanfrage-Prozess] benötigen wir für B2B-Angebote ab 5 Stück noch die Lieferadresse und den gewünschten Liefertermin. Mengenrabatte gelten ab 10 Stück (5%) bzw. 50 Stück (10%); bei den genannten Mengen ist aktuell kein Mengenrabatt vorgesehen. Nach Eingang der fehlenden Angaben erhalten Sie das Angebot innerhalb von 1 Werktag.

Mit freundlichen Grüßen
Ihr Kundenservice
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: c6fc283c-5fd8-4997-8bf4-c32b9c85a9fd
- Classification: quote_request (confidence 0.95)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Angebotsanfrage-Prozess
- Cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Angebotsanfrage-Prozess
- Full draft length: 425; preview length: 400
- Preview-limited earlier judgment: YES (re-review recommended using full draft below)
- Draft review status: full
- Full draft:
```text
Gerne. Für 5 ErgoChair 3000 (349 EUR/Stück) und 2 DeskPro Monitorarme (89 EUR/Stück) können wir ein Angebot erstellen. Da der Mengenrabatt erst ab 10 Stück gilt, sind diese Stückzahlen ohne Rabatt. Für die Angebotsanfrage benötigen wir noch Ihre Lieferadresse und den gewünschten Liefertermin; das Angebot erhalten Sie innerhalb von 1 Werktag. [Produkt: ErgoChair 3000] [Produkt: DeskPro Monitorarm] [Angebotsanfrage-Prozess]
```

### Human review
- Decision: 
- Notes: 

## case_06

### Synthetic inquiry and customer context
- Body: Hallo, ich weiß nicht genau was ich brauche, können Sie mich beraten?
- Customer email: david.koch@example.de
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: unclear
- Acceptable classifications: 
- Expected routing: requires_human_approval
- Deliberate abstention expected: True
- Expected source titles: 

### Baseline run
- Run ID: 02921e30-a7fc-4720-8fb7-3627a34d2e09
- Classification: spam (confidence 0.97)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000
- Cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000
- Full draft length: 235; preview length: 235
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Vielen Dank für Ihre Nachricht. Diese E-Mail wirkt wie Spam/Phishing; bitte öffnen Sie keine Links und geben Sie keine Daten ein. Für Fragen zu unseren Produkten (z. B. DeskPro Monitorarm, ErgoChair 3000) helfen wir Ihnen gerne weiter.
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: c684f5ff-390e-4a88-8c38-2389ab43778a
- Classification: spam (confidence 0.1)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: False
- Retrieved/cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000
- Cited sources: Produkt: DeskPro Monitorarm, Produkt: ErgoChair 3000
- Full draft length: 210; preview length: 210
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Vielen Dank für Ihre Nachricht. Wir können diese Anfrage nicht als legitime Kundenanfrage bestätigen und werden sie nicht weiter bearbeiten. Bei Fragen zu unseren Produkten stehen wir Ihnen gerne zur Verfügung.
```

### Human review
- Decision: 
- Notes: 

## case_07

### Synthetic inquiry and customer context
- Body: Ist der ErgoChair 3000 für Personen über 120 kg geeignet?
- Customer email: anna.mueller@example.de
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: product_question
- Acceptable classifications: 
- Expected routing: ready_for_review
- Deliberate abstention expected: False
- Expected source titles: product.ergochair_3000

### Baseline run
- Run ID: f792d05b-5906-47d0-a9aa-6dd7f5c5d198
- Classification: unclear (confidence 0.3)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: 
- Cited sources: 
- Full draft length: 113; preview length: 113
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Hallo Anna Müller, gerne helfen wir Ihnen. Bitte teilen Sie uns Ihre Frage mit, damit wir sie beantworten können.
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: 8103f36e-4f63-4aea-aa41-3034ed7f4a73
- Classification: unclear (confidence 0.6)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: 
- Cited sources: 
- Full draft length: 194; preview length: 194
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Gerne. Bitte teilen Sie uns Ihre Frage mit; dann prüfen wir das gerne. Ohne weitere Details kann ich keine spezifischen Angaben bestätigen und leite bei Bedarf an den zuständigen Bereich weiter.
```

### Human review
- Decision: 
- Notes: 

## case_08

### Synthetic inquiry and customer context
- Body: Die Rücksendung meines Monitorarms hat nicht funktioniert, ich warte seit 3 Wochen auf Erstattung.
- Customer email: clara.weber@example.de
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: complaint
- Acceptable classifications: 
- Expected routing: requires_human_approval
- Deliberate abstention expected: False
- Expected source titles: policy.returns_and_complaints, product.deskpro_monitor_arm, policy.escalation

### Baseline run
- Run ID: 0aa1f3be-dde2-4402-9f7e-4ddc4f2a774e
- Classification: product_question (confidence 0.8)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Full draft length: 237; preview length: 237
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Hallo Herr Schmidt, laut [Produkt: ErgoChair 3000] ist der ErgoChair 3000 in Schwarz als Farbe verfügbar; die angegebene Lieferzeit beträgt 3-5 Werktage. Eine Lieferung am selben Tag können wir auf Basis dieser Angaben nicht garantieren.
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: 1864fd40-e74a-4654-99f8-5cf385cf9d0c
- Classification: product_question (confidence 0.65)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Full draft length: 310; preview length: 310
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Sehr geehrter Herr Schmidt,

laut [Produkt: ErgoChair 3000] ist der ErgoChair 3000 in Schwarz erhältlich; die Lieferzeit beträgt 3–5 Werktage. Ob er sofort lieferbar ist, kann ich aus den vorliegenden Informationen nicht bestätigen. Ich leite Ihre Anfrage gerne an den Vertrieb weiter.

Mit freundlichen Grüßen
```

### Human review
- Decision: 
- Notes: 

## case_09

### Synthetic inquiry and customer context
- Body: Wann kommt meine Lieferung an, ich habe Express gewählt?
- Customer email: bernd.schmidt@example.de
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: order_status
- Acceptable classifications: 
- Expected routing: ready_for_review
- Deliberate abstention expected: False
- Expected source titles: policy.order_status

### Baseline run
- Run ID: 33bfe249-d720-476f-9a2b-713567f2e338
- Classification: complaint (confidence 0.65)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Full draft length: 513; preview length: 400
- Preview-limited earlier judgment: YES (re-review recommended using full draft below)
- Draft review status: full
- Full draft:
```text
Sehr geehrte Frau Müller,

vielen Dank für Ihre Nachricht. Es tut uns sehr leid zu hören, dass Ihr ErgoChair 3000 beschädigt geliefert wurde und die Rechnung nicht korrekt ist.

Wir nehmen Ihre Beschwerde ernst und leiten diese gemäß unserer Eskalationsrichtlinie an einen unserer Mitarbeiter weiter, der sich umgehend mit Ihnen in Verbindung setzen wird, um die Schadensregulierung und die Korrektur der Rechnung zu veranlassen.

Bitte haben Sie noch etwas Geduld.

Mit freundlichen Grüßen
Ihr Kundenservice-Team
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: f680c791-877b-4fef-b6c6-841d1d575831
- Classification: complaint (confidence 0.4)
- Routing: requires_human_approval (state AwaitingApproval)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Eskalationsrichtlinie
- Full draft length: 300; preview length: 300
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Sehr geehrte Frau Müller,

vielen Dank für Ihre Nachricht. Zu Schaden und Rechnung können wir leider keine bestätigten Angaben machen. Gemäß [Eskalationsrichtlinie] leiten wir Ihre Beschwerde an einen menschlichen Agenten weiter, der Entwurf, Quellen und Kundenkontext prüft.

Mit freundlichen Grüßen
```

### Human review
- Decision: 
- Notes: 

## case_10

### Synthetic inquiry and customer context
- Body: Anfrage für 50 DeskPro Monitorarme mit Mengenrabatt für Firma XY.
- Customer email: bernd.schmidt@example.de
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: quote_request
- Acceptable classifications: 
- Expected routing: requires_human_approval
- Deliberate abstention expected: False
- Expected source titles: process.quote_request, product.deskpro_monitor_arm

### Baseline run
- Run ID: 1d11c222-2821-47e1-b7a8-9df4a0039b6d
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik, Bestellstatus-Erklärung
- Cited sources: Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik, Bestellstatus-Erklärung
- Full draft length: 327; preview length: 327
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Hallo Anna Müller, der ErgoChair 3000 ist laut [Produkt: ErgoChair 3000] in Schwarz, Grau und Blau erhältlich; Rot ist derzeit nicht verfügbar. Wenn Sie unsicher sind, ob der Stuhl zu Ihrem Büro passt, können Sie ihn nach [Rückgabe- und Beschwerdepolitik] innerhalb von 30 Tagen unbenutzt und in Originalverpackung zurückgeben.
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: b3383548-5044-4cc7-8ead-df6d97aa4e28
- Classification: product_question (confidence 0.9)
- Routing: ready_for_review (state Approved)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik, Bestellstatus-Erklärung
- Cited sources: Produkt: ErgoChair 3000, Rückgabe- und Beschwerdepolitik, Bestellstatus-Erklärung
- Full draft length: 234; preview length: 234
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Vielen Dank für Ihre Anfrage. Der ErgoChair 3000 ist laut unseren Angaben in Schwarz, Grau und Blau erhältlich; Rot ist nicht aufgeführt [Produkt: ErgoChair 3000]. Ob eine Farbe zu Ihrem Büro passt, können wir leider nicht beurteilen.
```

### Human review
- Decision: 
- Notes: 

## case_11

### Synthetic inquiry and customer context
- Body: Kann ich den ErgoChair zurückgeben, wenn er mir nicht gefällt?
- Customer email: anna.mueller@example.de
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: product_question
- Acceptable classifications: 
- Expected routing: ready_for_review
- Deliberate abstention expected: False
- Expected source titles: policy.returns_and_complaints, product.ergochair_3000

### Baseline run
- Run ID: a8ee1d94-ad3c-4d91-af5d-ae13d80a30bc
- Classification: product_question (confidence 0.98)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Full draft length: 310; preview length: 310
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Vielen Dank für Ihre Anfrage, Herr Koch. Laut [Produkt: ErgoChair 3000] bietet der ErgoChair 3000 eine Garantie von 5 Jahren (nicht 10 Jahre) und ist in den Farben Schwarz, Grau und Blau erhältlich – Rot ist leider nicht im Sortiment. Gern beraten wir Sie zu den verfügbaren Farben oder alternativen Produkten.
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: 8e4720ba-eb6a-4d54-8419-b1618daabf33
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Cited sources: Produkt: ErgoChair 3000, Produkt: DeskPro Monitorarm, Rückgabe- und Beschwerdepolitik
- Full draft length: 401; preview length: 400
- Preview-limited earlier judgment: YES (re-review recommended using full draft below)
- Draft review status: full
- Full draft:
```text
Vielen Dank für Ihre Anfrage, Herr Koch. Laut unserer Produktinformationen hat der ErgoChair 3000 eine Garantie von 5 Jahren, nicht 10 Jahren [Produkt: ErgoChair 3000]. Zudem ist der Stuhl in den Farben Schwarz, Grau und Blau erhältlich; Rot ist leider nicht im Sortiment [Produkt: ErgoChair 3000]. Gerne können wir Ihnen bei weiteren Fragen oder bei der Auswahl einer passenden Farbe behilflich sein.
```

### Human review
- Decision: 
- Notes: 

## case_12

### Synthetic inquiry and customer context
- Body: Das Produkt kam beschädigt an, ich möchte Ersatz.
- Customer email: david.koch@example.de
- Customer context: from synthetic seed data (see data/eval_cases.json)
- Expected classification: complaint
- Acceptable classifications: 
- Expected routing: requires_human_approval
- Deliberate abstention expected: False
- Expected source titles: policy.returns_and_complaints, policy.escalation

### Baseline run
- Run ID: c3d17eec-6ad8-41a7-8926-31fa001348b9
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state ReadyForReview)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Bestellstatus-Erklärung, Rückgabe- und Beschwerdepolitik
- Cited sources: Produkt: ErgoChair 3000, Bestellstatus-Erklärung, Rückgabe- und Beschwerdepolitik
- Full draft length: 143; preview length: 143
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Danke für Ihr Feedback. Ja, der ErgoChair 3000 ist in Blau verfügbar; Preis 349 EUR, Lieferzeit 3-5 Werktage. (Quelle: Produkt: ErgoChair 3000)
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: 0f971598-c155-471f-8c0f-e76ccf469250
- Classification: product_question (confidence 0.95)
- Routing: ready_for_review (state Approved)
- Automated truncated flag: True
- Retrieved/cited sources: Produkt: ErgoChair 3000, Bestellstatus-Erklärung, Rückgabe- und Beschwerdepolitik
- Cited sources: Produkt: ErgoChair 3000, Bestellstatus-Erklärung, Rückgabe- und Beschwerdepolitik
- Full draft length: 114; preview length: 114
- Preview-limited earlier judgment: no
- Draft review status: full
- Full draft:
```text
Ja, der ErgoChair 3000 ist in Blau erhältlich. Preis: 349 EUR, Lieferzeit: 3-5 Werktage. [Produkt: ErgoChair 3000]
```

### Human review
- Decision: 
- Notes: 
