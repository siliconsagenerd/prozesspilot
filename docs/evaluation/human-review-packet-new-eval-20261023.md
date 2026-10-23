# ProzessPilot Human Review Packet - New Targeted Evaluation Full Drafts

Generated 2026-10-23 from retained run/database records. No model calls were made for this packet.

## Provenance and matching evidence
- Evaluation ID: `eval-20261023T062145Z`
- Raw artifacts: `data/evaluations/eval-20261023T062145Z/raw/*.json`
- Authoritative full drafts: `Draft.original_text` retrieved from disposable SQLite DB by matching `WorkflowRun.id` to raw artifact `run_id`.
- Cases: E03, E04, E06, E09 (baseline and improved prompt variants)
- Limits recorded before execution: classify 1024, draft 4096 (`docs/evaluation/new-eval-token-limits-20261023.md`)
- Provider-reported upstream model: `Beam-1.0-501B-A23B` (`response_model`); configured model ID `laya-v2/laya-v2`

## E03

### Synthetic inquiry
- Body: Können Sie mir den Status meiner Bestellung #12345 mitteilen?
- Customer email: bernd.schmidt@example.de
- Expected classification: order_status
- Expected routing: ready_for_review
- Deliberate abstention expected: False
- Acceptable sources: policy.order_status

### Baseline run
- Run ID: a7bf8f57-11d9-4dd1-99b9-1606f8339a42
- Predicted: order_status (confidence None)
- Routing: requires_human_approval (state None)
- Draft finish reason: stop
- Draft completion status: complete
- Full draft length: 562
- Full draft:
```text
Vielen Dank für Ihre Anfrage, Herr Schmidt. Ich kann den aktuellen Status Ihrer Bestellung #12345 leider nicht direkt aus den vorliegenden Informationen ablesen. Laut [Bestellstatus-Erklärung] bedeuten die Status: 'Eingegangen' = Bestellung erhalten, 'In Bearbeitung' = wird vorbereitet, 'Versandt' = Paket unterwegs mit Trackingnummer per E-Mail, 'Zugestellt' = Paket angekommen; Standardlieferzeit 3-5 Werktage, Express 1-2 Werktage. Bitte prüfen Sie Ihre E-Mails auf die Trackingnummer oder senden Sie mir weitere Details, damit ich Ihnen gezielt helfen kann.
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: c3a88d10-8e25-4838-b445-263c529ce5ba
- Predicted: order_status (confidence None)
- Routing: requires_human_approval (state None)
- Draft finish reason: stop
- Draft completion status: complete
- Full draft length: 608
- Full draft:
```text
Sehr geehrter Herr Schmidt,

vielen Dank für Ihre Anfrage. Leider kann ich den aktuellen Status Ihrer Bestellung #12345 nicht direkt einsehen. Die möglichen Status sind: 'Eingegangen' (Bestellung erhalten), 'In Bearbeitung' (wird vorbereitet), 'Versandt' (Paket unterwegs, Trackingnummer per E-Mail) und 'Zugestellt' (Paket angekommen). Die Standardlieferzeit beträgt 3-5 Werktage, Express 1-2 Werktage [Bestellstatus-Erklärung].

Gerne leite ich Ihre Anfrage an unser Team weiter, damit der genaue Status für Sie geprüft wird. Möchten Sie, dass ich das veranlasse?

Mit freundlichen Grüßen
Ihr Kundenservice
```

### Human review
- Decision: 
- Notes: 

## E04

### Synthetic inquiry
- Body: Wir benötigen ein Angebot für 20 ErgoChair 3000 für unser Büro, Lieferung nach München.
- Customer email: bernd.schmidt@example.de
- Expected classification: quote_request
- Expected routing: requires_human_approval
- Deliberate abstention expected: False
- Acceptable sources: process.quote_request, product.ergochair_3000

### Baseline run
- Run ID: c3a198bb-7cbe-4f6c-a3c5-d4052f0019b8
- Predicted: quote_request (confidence None)
- Routing: requires_human_approval (state None)
- Draft finish reason: stop
- Draft completion status: complete
- Full draft length: 598
- Full draft:
```text
Sehr geehrter Herr Schmidt,

vielen Dank für Ihre Anfrage. Gerne erstellen wir Ihnen ein Angebot für 20 ErgoChair 3000.

Basierend auf unseren Produktinformationen (Produkt: ErgoChair 3000):
- Preis pro Stuhl: 349 EUR
- Gesamtpreis (20 Stk.): 6.980 EUR
- Lieferzeit: 3-5 Werktage
- Verfügbare Farben: Schwarz, Grau, Blau
- 5 Jahre Garantie

Die Lieferung erfolgt nach München. Bitte teilen Sie uns Ihre gewünschte Farbe mit, damit wir das Angebot finalisieren können.

Als Stammkunde mit Premium-Status stehen wir Ihnen gerne für Rückfragen zur Verfügung.

Mit freundlichen Grüßen
Ihr Kundenservice
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: fcf938c9-6549-4aca-89ff-019801425ec9
- Predicted: quote_request (confidence None)
- Routing: requires_human_approval (state None)
- Draft finish reason: stop
- Draft completion status: complete
- Full draft length: 499
- Full draft:
```text
Vielen Dank für Ihre Anfrage, Herr Schmidt. Auf Basis der vorliegenden Informationen können wir Ihnen den ErgoChair 3000 zum Stückpreis von 349 EUR anbieten; für 20 Stück ergibt sich ein Warenwert von 6.980 EUR. Die Lieferzeit beträgt 3-5 Werktage. Verfügbare Farben: Schwarz, Grau, Blau. Versandkosten und weitere Lieferdetails nach München können wir aus den vorliegenden Informationen nicht bestätigen; gern leiten wir Ihre Anfrage zur finalen Angebotserstellung weiter. [Produkt: ErgoChair 3000]
```

### Human review
- Decision: 
- Notes: 

## E06

### Synthetic inquiry
- Body: Hallo, ich weiß nicht genau was ich brauche, können Sie mich beraten?
- Customer email: david.koch@example.de
- Expected classification: unclear
- Expected routing: requires_human_approval
- Deliberate abstention expected: True
- Acceptable sources: 

### Baseline run
- Run ID: 84ca452c-bfb4-455b-b6ab-b51316ef1261
- Predicted: unclear (confidence None)
- Routing: requires_human_approval (state None)
- Draft finish reason: stop
- Draft completion status: complete
- Full draft length: 313
- Full draft:
```text
Hallo David, gerne berate ich Sie. Um passende Empfehlungen zu geben, brauche ich ein paar Infos: Wofür suchen Sie etwas (z. B. Produktkategorie oder Anwendung)? Welches Budget haben Sie? Gibt es wichtige Anforderungen (Größe, Farbe, Marke, Lieferzeit)? Antworten Sie kurz, dann schlage ich passende Optionen vor.
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: 32355e61-7d89-427e-b375-dc486471f392
- Predicted: product_question (confidence None)
- Routing: requires_human_approval (state None)
- Draft finish reason: stop
- Draft completion status: complete
- Full draft length: 187
- Full draft:
```text
Hallo Herr Koch, leider liegen mir keine passenden Informationen vor, um Sie konkret zu beraten. Bitte beschreiben Sie Ihr Anliegen genauer oder ich leite Sie an einen Fachberater weiter.
```

### Human review
- Decision: 
- Notes: 

## E09

### Synthetic inquiry
- Body: Wann kommt meine Lieferung an, ich habe Express gewählt?
- Customer email: bernd.schmidt@example.de
- Expected classification: order_status
- Expected routing: ready_for_review
- Deliberate abstention expected: False
- Acceptable sources: policy.order_status

### Baseline run
- Run ID: a204ef4a-0825-48bc-b569-b055ad1b91c6
- Predicted: order_status (confidence None)
- Routing: requires_human_approval (state None)
- Draft finish reason: stop
- Draft completion status: complete
- Full draft length: 255
- Full draft:
```text
Hallo Bernd Schmidt,

bei Express-Lieferung beträgt die Lieferzeit laut [Bestellstatus-Erklärung] 1-2 Werktage. Sobald Ihre Bestellung versandt wurde, erhalten Sie die Trackingnummer per E-Mail und können den Status über 'Versandt' verfolgen.

Viele Grüße
```

### Human review
- Decision: 
- Notes: 

### Improved run
- Run ID: 92e21751-3d1d-4e7c-9794-ed6f05e2a96e
- Predicted: order_status (confidence None)
- Routing: requires_human_approval (state None)
- Draft finish reason: stop
- Draft completion status: complete
- Full draft length: 540
- Full draft:
```text
Hallo Herr Schmidt,

vielen Dank für Ihre Anfrage. Laut unserer Bestellstatus-Erklärung beträgt die Lieferzeit bei Express-Versand 1–2 Werktage. Sobald Ihre Bestellung versandt wurde, erhalten Sie die Trackingnummer per E-Mail, um den Sendungsstatus zu verfolgen.

Für den genauen Status Ihrer aktuellen Bestellung kann ich leider keine spezifischen Angaben machen, da mir die Bestelldetails nicht vorliegen. Gerne können wir das für Sie prüfen – möchten Sie, dass ich Ihre Anfrage an unser Versandteam weiterleite?

Mit freundlichen Grüßen
```

### Human review
- Decision: 
- Notes: 
