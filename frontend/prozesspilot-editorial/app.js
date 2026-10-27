/* ProzessPilot editorial prototype — app logic */
const T = {
  de: {
    "nav.overview":"Übersicht","companion.title":"★ Verwandtes Projekt","companion.desc":"SecureDoc-AI nutzt einen separaten Spring-Boot-Java-Validator fuer Upload-Validierung neben einer FastAPI-Pipeline.","nav.demo":"Demo","nav.operator":"Operator","nav.eval":"Evaluation",
    "nav.kb":"Wissensbasis","nav.customers":"Kunden",
    "common.loading":"Lade…","common.error":"Fehler","common.empty":"Keine Daten","common.back":"Zurück",
    "common.approve":"Freigeben","common.editApprove":"Bearbeiten & Freigeben","common.reject":"Ablehnen",
    "common.open":"Öffnen →","common.run":"Lauf starten",
    "overview.title":"ProzessPilot","overview.lede":"Human-in-the-loop Workflow-Copilot für synthetische Kundenanfragen: Klassifikation, Retrieval mit Zitaten, Entwurf, konfidenzbasierte Freigabe. Keine echten Schreibvorgänge.",
    "overview.cta.demo":"Aufgezeichnete Demo →","overview.cta.operator":"Operator-Konsole →","overview.cta.eval":"Evaluation →","overview.cta.kb":"Wissensbasis →",
    "overview.hist.title":"4. Evaluation",
    "overview.hist.note":"Diese Metriken beschreiben den historischen synthetischen Evaluationslauf, nicht die aktuelle Live-Laya-Konfiguration.",
    "overview.hist.readonly":"Nur synthetische Evaluationsartefakte. Keine neue Inferenz.",
    "overview.hist.metric":"METRIK","overview.hist.baseline":"BASELINE","overview.hist.improved":"ProzessPilot","overview.hist.delta":"Delta",
    "overview.hist.workflows":"Workflows (12 Fälle × 2 Varianten)","overview.hist.classification":"Klassifikationsübereinstimmung",
    "overview.hist.routing":"Routing-Übereinstimmung mit eingefrorenen erwarteten Labels","overview.hist.sources":"Erwartete Quellen abgerufen",
    "overview.hist.flags":"Automatisierte Flags für unvollständige Ausgaben","overview.hist.cost":"Gesamtkosten",
    "overview.hist.tokens":"Gesamttokens","overview.hist.latency":"Gesamtlatenz","overview.kpi.classification":"Klassifikation","overview.kpi.latency":"Latenz","overview.kpi.tokens":"Token-Einsparung",
    "overview.kpi.classificationSub":"beide Varianten","overview.kpi.latencySub":"94603 → 71849 ms","overview.kpi.tokensSub":"37085 → 35507",
    "overview.what.title":"1. Was ProzessPilot macht","overview.what.p1":"ProzessPilot klassifiziert Anfragen, sucht Wissen, erstellt zitierte Entwürfe und routet unsichere Fälle zur Freigabe.",
    "overview.what.p2":"Öffentliche Demo: kuratiertes, bereinigtes Beispiel aus einem abgeschlossenen Live-Run. Geschützter Operator-Zugang für Live-Inferenz, Freigabe und Evaluation.",
    "overview.wf.title":"2. Der Workflow","overview.wf.subtitle":"Eine Anfrage durchläuft sechs Schritte. Jeder Schritt ist einzeln nachvollziehbar und gespeichert.",
    "overview.wf.step1Title":"Klassifikation","overview.wf.step1Desc":"Kategorie und Konfidenz. Bei niedriger Konfidenz: manuelle Freigabe.",
    "overview.wf.step2Title":"Kunden-Lookup","overview.wf.step2Desc":"Kunde und offene Bestellungen werden aus der lokalen Datenbank geladen.",
    "overview.wf.step3Title":"Wissenssuche","overview.wf.step3Desc":"Relevante Quellen werden abgerufen; explizit zitiert.",
    "overview.wf.step4Title":"Entwurf","overview.wf.step4Desc":"Antwortentwurf wird generiert, inkl. Token- und Kostenangabe.",
    "overview.wf.step5Title":"Routing","overview.wf.step5Desc":"Konfidenzbasiert: automatisch oder zur Freigabe.",
    "overview.wf.step6Title":"Freigabe","overview.wf.step6Desc":"Mensch prüft, bearbeitet, gibt frei oder lehnt ab.",
    "overview.wf.inquiryLabel":"Anfrage","overview.wf.inquiryText":"\"Guten Tag, unsere Lieferung vom 12.03. ist noch nicht angekommen. Können Sie den Status prüfen? Bestellnummer 4711.\"",
    "overview.wf.resultLabel":"Ergebnis","overview.wf.resultMeta":"Klassifikation: Lieferstatus · Konfidenz 0.92 · Routing: automatisch · 3 Quellen · 2 zitiert · 412 Tokens · 0.0009 USD",
    "overview.wf.draftLabel":"Entwurf","overview.wf.draftText":"Sehr geehrte/r Kunde/in, vielen Dank für Ihre Anfrage. Ihre Bestellung 4711 befindet sich derzeit in der Versandvorbereitung und wird voraussichtlich am 15.03. zugestellt.",
    "overview.wf.cite1":"Versandrichtlinien v2","overview.wf.cite2":"Bestellstatus-FAQ",
    "overview.wf.title":"2. Der Workflow","overview.wf.subtitle":"Eine Anfrage durchläuft sechs Schritte. Jeder Schritt ist einzeln nachvollziehbar und gespeichert.",
    "overview.wf.step1Title":"Klassifikation","overview.wf.step1Desc":"Kategorie und Konfidenz. Bei niedriger Konfidenz: manuelle Freigabe.",
    "overview.wf.step2Title":"Kunden-Lookup","overview.wf.step2Desc":"Kunde und offene Bestellungen werden aus der lokalen Datenbank geladen.",
    "overview.wf.step3Title":"Wissenssuche","overview.wf.step3Desc":"Relevante Quellen werden abgerufen; explizit zitiert.",
    "overview.wf.step4Title":"Entwurf","overview.wf.step4Desc":"Antwortentwurf wird generiert, inkl. Token- und Kostenangabe.",
    "overview.wf.step5Title":"Routing","overview.wf.step5Desc":"Konfidenzbasiert: automatisch oder zur Freigabe.",
    "overview.wf.step6Title":"Freigabe","overview.wf.step6Desc":"Mensch prüft, bearbeitet, gibt frei oder lehnt ab.",
    "overview.wf.inquiryLabel":"Anfrage","overview.wf.inquiryText":"„Guten Tag, unsere Lieferung vom 12.03. ist noch nicht angekommen. Können Sie den Status prüfen? Bestellnummer 4711.“",
    "overview.wf.resultLabel":"Ergebnis","overview.wf.resultMeta":"Klassifikation: Lieferstatus · Konfidenz 0.92 · Routing: automatisch · 3 Quellen · 2 zitiert · 412 Tokens · 0.0009 USD",
    "overview.wf.draftLabel":"Entwurf","overview.wf.draftText":"Sehr geehrte/r Kunde/in, vielen Dank für Ihre Anfrage. Ihre Bestellung 4711 befindet sich derzeit in der Versandvorbereitung und wird voraussichtlich am 15.03. zugestellt.",
    "overview.wf.cite1":"Versandrichtlinien v2","overview.wf.cite2":"Bestellstatus-FAQ",
    "overview.provenance.title":"Provenienz","overview.provenance.content":"Provenienz: synthetischer Datensatz, 12 Fälle, Run eval-20261022T190411Z; Manifest-Fall-Hash ceb819418b6afab2d05bd54752f444314a2d62021b773e4f3ce96d0dc60afd9. Historische Evaluation: OpenAI-kompatible Route, Modell laya-v2/laya-v2 (OmniRoute). Aktuelle Live-Konfiguration: Laya, Modell laya-v3.",
    "overview.capabilities.title":"3. Fähigkeiten","overview.capabilities.structured":"Strukturierte Workflows","overview.capabilities.structuredDesc":"Jeder Schritt einzeln nachvollziehbar, mit Input und Output.",
    "overview.capabilities.retrieval":"Retrieval mit Zitaten","overview.capabilities.retrievalDesc":"Antworten verweisen explizit auf Quellen. Keine unbelegten Behauptungen.",
    "overview.capabilities.confidence":"Konfidenzbasierte Freigabe","overview.capabilities.confidenceDesc":"Niedrige Konfidenz oder Beschwerden gehen zur manuellen Prüfung.",
    "overview.capabilities.audit":"Audit-Trail","overview.capabilities.auditDesc":"Jeder Modellaufruf, jede Tool-Eingabe und -Ausgabe, Latenz, Token und Kosten werden gespeichert.",
    "overview.capabilities.eval":"Evaluation","overview.capabilities.evalDesc":"12 synthetische Fälle, Baseline gegen verbesserten Prompt, automatische Metriken.",
    "overview.limits5.title":"5. Grenzen","overview.limits5.1":"Alle ausgehenden Aktionen sind Mocks. Keine echten E-Mails, CRM- oder Kundendaten.",
    "overview.limits5.2":"Die Demo zeigt einen aufgezeichneten Run, keine neue Inferenz.",
    "overview.limits5.3":"Operator-Zugang ist geschützt; keine echte Authentifizierung in dieser Version.",
    "overview.limits5.4":"Keine mehrsprachige Verarbeitung. Eingaben werden auf Deutsch erwartet.",
    "overview.ledeLong":"Human-in-the-loop Workflow-Copilot für synthetische Kundenanfragen. Ein lokaler, auditierbarer Workflow-Copilot für synthetische Kundenanfragen: Klassifikation, Retrieval mit Zitaten, Entwurf, konfidenzbasierte Freigabe. Keine echten Schreibvorgänge.",
    "overview.workflows":"Workflows","overview.what.title":"Was ProzessPilot tut",
    "overview.what.p1":"ProzessPilot ist ein human-in-the-loop Workflow-Copilot für strukturierte Kundenanfragen. Er nimmt E-Mails oder Support-Tickets entgegen, klassifiziert das Anliegen, ruft relevante Wissensbasis-Artikel mit Zitaten ab, generiert einen Antwortentwurf und steuert die konfidenzbasierte Freigabe (automatisch bei hoher Konfidenz oder an den menschlichen Operator bei Unklarheiten).",
    "overview.what.p2":"Um absolute Datensicherheit zu gewährleisten, führt das System keine echten Schreibvorgänge oder externen Versandaktionen aus; alle Entwürfe und Freigaben verbleiben in der kontrollierten Operator-Konsole.",
    "overview.limits.title":"Bekannte Grenzen & Methode",
    "overview.limits.content":"Bekannte Grenzen: ausgeführte Token-Limits 1024/2048 statt freigegebener 128/384. Abruf ist tokenbasiertes Overlap-Heuristik, keine semantische Relevanzmessung. Menschliche Zitatprüfung für die 9/12 abgerufenen erwarteten Quellen ausstehend. Tatsächliche Generierungsabbrüche wurden nicht verifiziert, weil Finish-Reason-Evidenz nicht erfasst wurde. Historische Evaluation: OpenAI-kompatible Route, Modell laya-v2/laya-v2 (OmniRoute). Aktuelle Live-Konfiguration: Laya, Modell laya-v3.",
    "overview.notes.title":"Anmerkungen & Provenienz",
    "overview.notes.content":"Routing-Abweichungen: Fall 04 in beiden Varianten; Fall 06 nur improved. Abschlussstatus: 24/24 Workflows im erfolgreichen Lauf. Erster Lauf scheiterte vollständig.",
    "overview.live.title":"Live-Status","overview.live.inquiries":"Anfragen","overview.live.kb":"KB-Einträge","overview.live.customers":"Kunden","overview.live.evalruns":"Eval-Läufe",
    "demo.title":"Öffentliche Demo","demo.subtitle":"Aufgezeichnetes Beispiel aus einem abgeschlossenen Live-Run. Keine neue Inferenz.",
    "demo.loading":"Lade aufgezeichneten Run…","demo.inquiry":"Kundenanfrage","demo.classification":"Klassifikation",
    "demo.confidence":"Konfidenz","demo.routing":"Freigabestatus","demo.rationale":"Begründung","demo.draft":"Generierter Antwortentwurf",
    "demo.sources":"Abgerufene Quellen","demo.noSources":"Keine Quellen",
    "operator.title":"Operator Console","operator.submit":"Kundenanfrage einreichen","operator.submitBtn":"Einreichen & Workflow starten",
    "operator.subject":"Betreff","operator.body":"Nachricht","operator.email":"Kunden-E-Mail (optional)","operator.variant":"Prompt-Variante",
    "operator.inbox":"Inbox","operator.entries":"Einträge","operator.empty":"Keine Anfragen vorhanden.","operator.noSubject":"(kein Betreff)","status.awaitingApproval":"Zur Freigabe","status.readyForReview":"Zur Prüfung","status.failed":"Fehlgeschlagen","status.approved":"Freigegeben","status.rejected":"Abgelehnt","status.processing":"In Bearbeitung","status.drafting":"Entwurf","status.done":"Fertig","status.skipped":"Übersprungen",
    "run.title":"Workflow Trace","run.workflow":"Workflow","run.state":"Status","run.classification":"Klassifikation","run.confidence":"Konfidenz",
    "run.routing":"Routing","run.cost":"Kosten","run.latency":"Latenz","run.input":"EINGABE","run.output":"AUSGABE","run.tokens":"Tokens","step.classify":"Klassifikation","step.customer_lookup":"Kundensuche","step.kb_search":"Wissenssuche","step.draft":"Entwurf","step.routing":"Routing","step.route":"Routing","run.inquiry":"Anfrage",
    "run.steps":"Schritte","run.draft":"Entwurf","run.reasoning":"Begründung","run.sources":"Quellen","run.approvals":"Freigaben",
    "run.traceLink":"Trace (HTML) öffnen ↗","run.noDraft":"Kein Entwurf vorhanden.","run.approveOk":"Freigegeben.",
    "run.rejectReason":"Ablehnungsgrund","run.editPlaceholder":"Entwurf bearbeiten…",
    "kb.title":"Wissensbasis","kb.entries":"Einträge","kb.empty":"Keine KB-Einträge.",
    "customers.title":"Kunden","customers.empty":"Keine Kunden.",
    "eval.title":"Evaluation","eval.subtitle":"12 synthetische Fälle, Baseline gegen verbesserten Prompt, automatische Metriken.",
    "eval.runBtn":"Eval (improved prompt) starten","eval.running":"Evaluation läuft…","eval.noResults":"Noch keine Evaluation.",
    "eval.case":"Fall","eval.predicted":"Vorhergesagt","eval.expected":"Erwartet","eval.cls":"Klassifikation ok",
    "eval.routing":"Routing ok","eval.cites":"Zitate","eval.latency":"Latenz","eval.cost":"Kosten",
    "eval.summary.n":"Workflows","eval.summary.cls":"Klassifikationsübereinstimmung","eval.summary.route":"Routing-Übereinstimmung",
    "eval.summary.cite":"Zitate vorhanden","eval.summary.latency":"Gesamtlatenz","eval.summary.tokens":"Gesamttokens","eval.summary.cost":"Gesamtkosten",
    "toast.created":"Anfrage erstellt, Workflow gestartet.","toast.approved":"Freigegeben.","toast.rejected":"Abgelehnt.",
    "toast.edited":"Bearbeitet & freigegeben.","toast.evalDone":"Evaluation abgeschlossen.","toast.error":"Fehler bei der Anfrage.",
    "overview.hist.note1":"Tatsächliche Generierungsabbrüche wurden nicht verifiziert, weil Finish-Reason-Evidenz nicht erfasst wurde.",
    "overview.hist.note2":"Routing-Abweichungen: Fall 04 in beiden Varianten; Fall 06 nur improved.",
    "overview.hist.note3":"Abschlussstatus: 24/24 Workflows im erfolgreichen Lauf eval-20261022T190411Z; erster Lauf scheiterte vollständig.",
    "overview.hist.note4":"Bekannte Grenzen: ausgeführte Token-Limits 1024/2048 statt freigegebener 128/384.",
    "overview.hist.note5":"Abruf ist tokenbasiertes Overlap-Heuristik, keine semantische Relevanzmessung.",
    "overview.hist.note6":"Menschliche Zitatprüfung für die 12-Fälle-Synthesevaluation abgeschlossen; keine Produktionsprüfung.",
    "overview.hist.note7":"Routing-Metriken vergleichen Übereinstimmung mit eingefrorenen erwarteten Labels, nicht Routing-Policy-Konformität.",
    "overview.hist.note8":"Explizite Zitate sind die im Entwurf markierte Teilmenge der abgerufenen Quellen; abgerufene Quellen werden nicht als Zitate dargestellt.",
    "overview.provenance.title":"Provenienz",
    "overview.provenance.p1":"Provenienz: synthetischer Datensatz, 12 Fälle, Run eval-20261022T190411Z; Manifest-Fall-Hash ceb819418b6afab2d05bd54752f444314a2d62021b773e4f3ce96d0dc60afd9.",
    "overview.provenance.p2":"Historische Evaluation: OpenAI-kompatible Route, Modell laya-v2/laya-v2 (OmniRoute).",
    "overview.provenance.p3":"Aktuelle Live-Konfiguration: Laya, Modell laya-v3.",

  },
  en: {
    "nav.overview":"Overview","nav.demo":"Demo","nav.operator":"Operator","nav.eval":"Evaluation","companion.title":"★ Related project","companion.desc":"SecureDoc-AI uses a separate Spring-Boot Java validator for upload validation alongside a FastAPI pipeline.",
    "nav.kb":"Knowledge base","nav.customers":"Customers",
    "common.loading":"Loading…","common.error":"Error","common.empty":"No data","common.back":"Back",
    "common.approve":"Approve","common.editApprove":"Edit & Approve","common.reject":"Reject",
    "common.open":"Open →","common.run":"Run workflow",
    "overview.title":"ProzessPilot","overview.lede":"Human-in-the-loop workflow copilot for synthetic customer inquiries: classification, retrieval with citations, drafting, confidence-based approval. No real writes.",
    "overview.cta.demo":"Recorded demo →","overview.cta.operator":"Operator console →","overview.cta.eval":"Evaluation →","overview.cta.kb":"Knowledge base →",
    "overview.hist.title":"Historical evaluation (eval-20261022T190411Z)",
    "overview.hist.note":"These metrics describe the historical synthetic evaluation run, not the current live Laya configuration.",
    "overview.hist.readonly":"Synthetic evaluation artifacts only. No new inference.",
    "overview.hist.metric":"METRIC","overview.hist.baseline":"BASELINE","overview.hist.improved":"ProzessPilot","overview.hist.delta":"Delta",
    "overview.hist.workflows":"Workflows (12 cases × 2 variants)","overview.hist.classification":"Classification match",
    "overview.hist.routing":"Routing match against frozen expected labels","overview.hist.sources":"Expected sources retrieved",
    "overview.hist.flags":"Automated flags for incomplete outputs","overview.hist.cost":"Total cost",
    "overview.hist.tokens":"Total tokens","overview.hist.latency":"Total latency","overview.kpi.classification":"Classification","overview.kpi.latency":"Latency","overview.kpi.tokens":"Token savings",
    "overview.kpi.classificationSub":"both variants","overview.kpi.latencySub":"94603 → 71849 ms","overview.kpi.tokensSub":"37085 → 35507",
    "overview.what.title":"1. What ProzessPilot does","overview.what.p1":"ProzessPilot classifies inquiries, searches knowledge, drafts cited replies, and routes uncertain cases for approval.",
    "overview.what.p2":"Public demo: a curated, sanitized example from a completed live run. Protected operator access for live inference, approval, and evaluation.",
    "overview.wf.title":"2. The workflow","overview.wf.subtitle":"An inquiry passes through six steps. Each step is individually traceable and stored.",
    "overview.wf.step1Title":"Classification","overview.wf.step1Desc":"Category and confidence. Low confidence: manual approval.",
    "overview.wf.step2Title":"Customer lookup","overview.wf.step2Desc":"Customer and open orders are loaded from the local database.",
    "overview.wf.step3Title":"Knowledge search","overview.wf.step3Desc":"Relevant sources are retrieved and explicitly cited.",
    "overview.wf.step4Title":"Draft","overview.wf.step4Desc":"Answer draft is generated, including token and cost figures.",
    "overview.wf.step5Title":"Routing","overview.wf.step5Desc":"Confidence-based: automatic or for approval.",
    "overview.wf.step6Title":"Approval","overview.wf.step6Desc":"Human reviews, edits, approves or rejects.",
    "overview.wf.inquiryLabel":"Inquiry","overview.wf.inquiryText":"\"Hello, our delivery from 12.03. has not arrived yet. Can you check the status? Order number 4711.\"",
    "overview.wf.resultLabel":"Result","overview.wf.resultMeta":"Classification: delivery status · confidence 0.92 · routing: automatic · 3 sources · 2 cited · 412 tokens · 0.0009 USD",
    "overview.wf.draftLabel":"Draft","overview.wf.draftText":"Dear customer, thank you for your inquiry. Your order 4711 is currently in shipping preparation and is expected to be delivered on 15.03.",
    "overview.wf.cite1":"Shipping policy v2","overview.wf.cite2":"Order status FAQ",
    "overview.cap.title":"3. Capabilities","overview.cap.workflowsTitle":"Structured workflows","overview.cap.workflowsDesc":"Each step individually traceable, with input and output.",
    "overview.cap.retrievalTitle":"Retrieval with citations","overview.cap.retrievalDesc":"Answers explicitly reference sources. No unsubstantiated claims.",
    "overview.cap.approvalTitle":"Confidence-based approval","overview.cap.approvalDesc":"Low confidence or complaints go to manual review.",
    "overview.cap.auditTitle":"Audit trail","overview.cap.auditDesc":"Every model call, tool input and output, latency, token and cost is stored.",
    "overview.cap.evalTitle":"Evaluation","overview.cap.evalDesc":"12 synthetic cases, baseline vs improved prompt, automatic metrics.",
    "overview.provenance.title":"Provenance","overview.provenance.content":"Provenance: synthetic dataset, 12 cases, run eval-20261022T190411Z; manifest case hash ceb819418b6afab2d05bd54752f444314a2d62021b773e4f3ce96d0dc60afd9. Historical evaluation: OpenAI-compatible route, model laya-v2/laya-v2 (OmniRoute). Current live configuration: Laya, model laya-v3.",
    "overview.capabilities.title":"3. Capabilities","overview.capabilities.structured":"Structured workflows","overview.capabilities.structuredDesc":"Each step individually traceable, with input and output.",
    "overview.capabilities.retrieval":"Retrieval with citations","overview.capabilities.retrievalDesc":"Replies explicitly reference sources. No unsupported claims.",
    "overview.capabilities.confidence":"Confidence-based approval","overview.capabilities.confidenceDesc":"Low confidence or complaints go to manual review.",
    "overview.capabilities.audit":"Audit trail","overview.capabilities.auditDesc":"Every model call, tool input and output, latency, tokens and cost are stored.",
    "overview.capabilities.eval":"Evaluation","overview.capabilities.evalDesc":"12 synthetic cases, baseline vs. improved prompt, automatic metrics.",
    "overview.limits5.title":"5. Limits","overview.limits5.1":"All outgoing actions are mocks. No real emails, CRM or customer data.",
    "overview.limits5.2":"The demo shows a recorded run, not a new inference.",
    "overview.limits5.3":"Operator access is protected; no real authentication in this version.",
    "overview.limits5.4":"No multilingual processing. Inputs are expected in German.",
    "overview.ledeLong":"Human-in-the-loop workflow copilot for synthetic customer inquiries. A local, auditable workflow copilot for synthetic customer inquiries: classification, retrieval with citations, drafting, confidence-based approval. No real writes.",
    "overview.workflows":"Workflows","overview.what.title":"What ProzessPilot does",
    "overview.what.p1":"ProzessPilot is a human-in-the-loop workflow copilot for structured customer inquiries. It takes in emails or support tickets, classifies the request, retrieves relevant knowledge-base articles with citations, generates a reply draft, and manages confidence-based approval (automatic at high confidence or routed to the human operator when uncertain).",
    "overview.what.p2":"To guarantee absolute data security, the system performs no real writes or external sending actions; all drafts and approvals remain in the controlled operator console.",
    "overview.limits.title":"Known limits & method",
    "overview.limits.content":"Known limitations: executed token limits 1024/2048 instead of approved 128/384. Retrieval is token overlap heuristic, not semantic relevance. Human citation check for 9/12 retrieved expected sources pending. Actual generation truncations unverified due to lack of finish-reason telemetry. Historical evaluation: OpenAI-compatible route, model laya-v2/laya-v2 (OmniRoute). Current live configuration: Laya, model laya-v3.",
    "overview.notes.title":"Notes & provenance",
    "overview.notes.content":"Routing anomalies: Case 04 in both variants; Case 06 improved only. Completion status: 24/24 workflows in successful run. Initial run failed completely.",
    "overview.live.title":"Live status","overview.live.inquiries":"Inquiries","overview.live.kb":"KB entries","overview.live.customers":"Customers","overview.live.evalruns":"Eval runs",
    "demo.title":"Public demo","demo.subtitle":"Recorded example from a completed live run. No new inference.",
    "demo.loading":"Loading recorded run…","demo.inquiry":"Customer inquiry","demo.classification":"Classification",
    "demo.confidence":"Confidence","demo.routing":"Approval status","demo.rationale":"Rationale","demo.draft":"Generated reply draft",
    "demo.sources":"Retrieved sources","demo.noSources":"No sources",
    "operator.title":"Operator Console","operator.submit":"Submit inquiry","operator.submitBtn":"Submit & start workflow",
    "operator.subject":"Subject","operator.body":"Message","operator.email":"Customer email (optional)","operator.variant":"Prompt variant",
    "operator.inbox":"Inbox","operator.entries":"entries","operator.empty":"No inquiries yet.","operator.noSubject":"(no subject)","status.awaitingApproval":"Awaiting approval","status.readyForReview":"Ready for review","status.failed":"Failed","status.approved":"Approved","status.rejected":"Rejected","status.processing":"Processing","status.drafting":"Drafting","status.done":"Done","status.skipped":"Skipped",
    "run.title":"Workflow Trace","run.workflow":"Workflow","run.state":"Status","run.classification":"Classification","run.confidence":"Confidence",
    "run.routing":"Routing","run.cost":"Cost","run.latency":"Latency","run.input":"INPUT","run.output":"OUTPUT","run.tokens":"Tokens","step.classify":"Classification","step.customer_lookup":"Customer lookup","step.kb_search":"Knowledge search","step.draft":"Draft","step.routing":"Routing","step.route":"Routing","run.inquiry":"Inquiry",
    "run.steps":"Steps","run.draft":"Draft","run.reasoning":"Rationale","run.sources":"Sources","run.approvals":"Approvals",
    "run.traceLink":"Open trace (HTML) ↗","run.noDraft":"No draft available.","run.approveOk":"Approved.",
    "run.rejectReason":"Rejection reason","run.editPlaceholder":"Edit draft…",
    "kb.title":"Knowledge base","kb.entries":"entries","kb.empty":"No KB entries.",
    "customers.title":"Customers","customers.empty":"No customers.",
    "eval.title":"Evaluation","eval.subtitle":"12 synthetic cases, baseline vs. improved prompt, automated metrics.",
    "eval.runBtn":"Run eval (improved prompt)","eval.running":"Running evaluation…","eval.noResults":"No evaluation yet.",
    "eval.case":"Case","eval.predicted":"Predicted","eval.expected":"Expected","eval.cls":"Classification ok",
    "eval.routing":"Routing ok","eval.cites":"Citations","eval.latency":"Latency","eval.cost":"Cost",
    "eval.summary.n":"Workflows","eval.summary.cls":"Classification agreement","eval.summary.route":"Routing agreement",
    "eval.summary.cite":"Citations present","eval.summary.latency":"Total latency","eval.summary.tokens":"Total tokens","eval.summary.cost":"Total cost",
    "toast.created":"Inquiry created, workflow started.","toast.approved":"Approved.","toast.rejected":"Rejected.",
    "toast.edited":"Edited & approved.","toast.evalDone":"Evaluation complete.","toast.error":"Request failed.",
    "overview.hist.note1":"Actual generation-time truncation was not verified because finish-reason evidence was not captured.",
    "overview.hist.note2":"Routing mismatches: case 04 in both variants; case 06 in improved only.",
    "overview.hist.note3":"Completion status: 24/24 workflows in successful run eval-20261022T190411Z; first run failed all classify steps.",
    "overview.hist.note4":"Known limits: executed token limits 1024/2048 instead of approved 128/384.",
    "overview.hist.note5":"Retrieval is token-overlap heuristic, not semantic relevance.",
    "overview.hist.note6":"Human citation review completed for the 12-case synthetic evaluation; not a production audit.",
    "overview.hist.note7":"Routing metrics compare agreement with frozen expected labels, not routing policy compliance.",
    "overview.hist.note8":"Explicit citations are the subset of retrieved sources marked in the draft; retrieved sources are not displayed as citations.",
    "overview.provenance.title":"Provenance",
    "overview.provenance.p1":"Provenance: synthetic dataset, 12 cases, run eval-20261022T190411Z; manifest case hash ceb819418b6afab2d05bd54752f444314a2d62021b773e4f3ce96d0dc60afd9.",
    "overview.provenance.p2":"Historical evaluation: OpenAI-compatible route, model laya-v2/laya-v2 (OmniRoute).",
    "overview.provenance.p3":"Current live configuration: Laya, model laya-v3.",

  }
};

let lang = localStorage.getItem("pp2.lang") || "de";
let theme = localStorage.getItem("pp2.theme") || "light";

function t(key){ return (T[lang] && T[lang][key]) || key; }

function applyTheme(){
  document.documentElement.classList.toggle("dark", theme === "dark");
  const btn = document.getElementById("themeToggle");
  if(btn) btn.textContent = theme === "dark" ? "☾" : "☼";
}
function applyLang(){
  document.documentElement.setAttribute("lang", lang);
  const btn = document.getElementById("langToggle");
  if(btn) btn.textContent = lang.toUpperCase();
  document.querySelectorAll("[data-i18n]").forEach(el => { el.textContent = t(el.getAttribute("data-i18n")); });
}

function toast(msg, kind){
  const el = document.getElementById("toast");
  el.textContent = msg;
  el.classList.remove("is-error","is-ok");
  if(kind === "error") el.classList.add("is-error");
  if(kind === "ok") el.classList.add("is-ok");
  el.hidden = false;
  clearTimeout(el._t);
  el._t = setTimeout(()=>{ el.hidden = true; }, 3200);
}

async function api(path, opts){
  opts = opts || {};
  const res = await fetch(path, {
    headers: Object.assign({"Content-Type":"application/json", "X-ProzessPilot-Operator":"1"}, opts.headers || {}),
    method: opts.method || "GET",
    body: opts.body ? JSON.stringify(opts.body) : undefined,
  });
  if(!res.ok){
    let detail = res.statusText;
    try { const j = await res.json(); detail = j.detail || detail; } catch(e){}
    throw new Error(detail);
  }
  const ct = res.headers.get("content-type") || "";
  if(ct.includes("application/json")) return res.json();
  return res.text();
}

async function openTrace(id){
  try {
    const res = await fetch("/api/runs/" + id + "/trace.html?lang=" + encodeURIComponent(lang), { headers: {"X-ProzessPilot-Operator":"1"} });
    if(!res.ok) throw new Error(res.statusText);
    const html = await res.text();
    const w = window.open("", "_blank");
    if(w){ w.document.open(); w.document.write(html); w.document.close(); }
  } catch(e){ toast(e.message || "error", "error"); }
}

function statusLabel(state){
  const key = "status." + String(state||"").charAt(0).toLowerCase() + String(state||"").slice(1);
  if(T[lang] && T[lang][key]) return t(key);
  return state || "—";
}
function stepLabel(name){
  const key = "step." + String(name||"");
  if(T[lang] && T[lang][key]) return t(key);
  return name || "—";
}
function badge(state){
  const s = (state || "").toLowerCase();
  let cls = "text-secondary";
  if(["approved","readyforreview","done","classified"].includes(s)) cls = "text-tertiary";
  else if(["awaitingapproval","running","pending"].includes(s)) cls = "text-primary";
  else if(["failed","rejected","error"].includes(s)) cls = "text-error";
  return `<span class="badge ${cls}">${escapeHtml(statusLabel(state))}</span>`;
}

function fmtNum(n){ return (n == null) ? "—" : Number(n).toLocaleString(); }
function fmtMoney(n){ return (n == null) ? "—" : Number(n).toFixed(6) + " USD"; }
function fmtMs(n){ return (n == null) ? "—" : Number(n).toLocaleString() + " ms"; }
function escapeHtml(s){ return String(s==null?"":s).replace(/[&<>"']/g, c=>({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c])); }
const DATA_TR = {
  "Rückgabe ErgoChair 3000": "Return ErgoChair 3000",
  "Ist der ErgoChair 3000 für Personen über 120 kg geeignet?": "Is the ErgoChair 3000 suitable for people over 120 kg?",
  "Das Produkt kam beschädigt an, ich möchte Ersatz.": "The product arrived damaged, I would like a replacement.",
  "Kann ich den ErgoChair zurückgeben, wenn er mir nicht gefällt?": "Can I return the ErgoChair if I don't like it?",
  "Anfrage für 50 DeskPro Monitorarme mit Mengenrabatt für Firma XY.": "Request for 50 DeskPro monitor arms with volume discount for company XY.",
  "Wann kommt meine Lieferung an, ich habe Express gewählt?": "When will my delivery arrive, I chose express?",
  "Die Rücksendung meines Monitorarms hat nicht funktioniert, ich warte seit 3 Wochen auf Erstattung.": "The return of my monitor arm didn't work, I've been waiting 3 weeks for a refund.",
  "Hallo, ich weiß nicht genau was ich brauche, können Sie mich beraten?": "Hello, I'm not sure what I need, can you advise me?",
  "GEWINNEN SIE EIN IPHONE!!! Klicken Sie hier: http://spam.example": "WIN AN IPHONE!!! Click here: http://spam.example",
  "Wir benötigen ein Angebot für 20 ErgoChair 3000 für unser Büro, Lieferung nach München.": "We need a quote for 20 ErgoChair 3000 for our office, delivery to Munich.",
  "Können Sie mir den Status meiner Bestellung #12345 mitteilen?": "Can you tell me the status of my order #12345?",
  "Mein DeskPro Monitorarm ist nach 2 Wochen kaputt gegangen, ich bin sehr unzufrieden!": "My DeskPro monitor arm broke after 2 weeks, I am very dissatisfied!",
  "Hallo, wo kann ich den ErgoChair 3000 in Grau bestellen und wie lange dauert die Lieferung?": "Hello, where can I order the ErgoChair 3000 in grey and how long does delivery take?",
  "Mein ErgoChair 3000 quietscht nach zwei Wochen. Ich moechte ihn zurueckgeben.": "My ErgoChair 3000 squeaks after two weeks. I would like to return it.",
  "Rückgabe ErgoChair 3000": "Return ErgoChair 3000",
  "Rückgabe- und Beschwerdepolitik": "Return and complaints policy",
  "Eskalationsrichtlinie": "Escalation policy",
  "Produkt: ErgoChair 3000": "Product: ErgoChair 3000",
  "Sehr geehrte Frau Beispiel,\n\nvielen Dank f\u00fcr Ihre Nachricht. Es tut mir leid zu h\u00f6ren, dass Sie Probleme mit Ihrem ErgoChair 3000 haben. Da das Produkt anscheinend einen Defekt aufweist, k\u00f6nnen wir Ihnen entweder einen Ersatz oder eine Reparatur anbieten, gem\u00e4\u00df unserer R\u00fcckgabe- und Beschwerdepolitik [R\u00fcckgabe- und Beschwerdepolitik]. \n\nBitte lassen Sie uns wissen, wie Sie fortfahren m\u00f6chten. Wenn Sie eine R\u00fcckgabe w\u00fcnschen, beachten Sie bitte, dass diese innerhalb von 30 Tagen m\u00f6glich ist, sofern das Produkt unbenutzt und in Originalverpackung ist [R\u00fcckgabe- und Beschwerdepolitik]. \n\nFalls Sie weitere Unterst\u00fctzung ben\u00f6tigen, kann ich Ihre Anfrage auch an einen menschlichen Agenten eskalieren.\n\nMit freundlichen Gr\u00fc\u00dfen,\nIhr Kundenservice-Team": "Dear Ms. Example,\n\nThank you for your message. I am sorry to hear that you are having problems with your ErgoChair 3000. Since the product appears to be defective, we can offer you either a replacement or a repair, in accordance with our return and complaints policy [Return and complaints policy]. \n\nPlease let us know how you would like to proceed. If you wish to return the item, please note that this is possible within 30 days, provided the product is unused and in its original packaging [Return and complaints policy]. \n\nIf you need further assistance, I can also escalate your request to a human agent.\n\nKind regards,\nYour customer service team",
};
function td(s){ if(lang !== "en" || !s) return s; return Object.prototype.hasOwnProperty.call(DATA_TR, s) ? DATA_TR[s] : s; }


function parseRoute(){
  const h = (location.hash || "#/").replace(/^#/, "");
  const parts = h.split("/").filter(Boolean);
  if(parts.length === 0) return {name:"overview"};
  if(parts[0] === "demo") return {name:"demo"};
  if(parts[0] === "kb") return {name:"kb"};
  if(parts[0] === "customers") return {name:"customers"};
  if(parts[0] === "eval") return {name:"eval"};
  if(parts[0] === "app"){
    if(parts[1] === "run" && parts[2]) return {name:"run", id: parts[2]};
    return {name:"app"};
  }
  return {name:"overview"};
}

function navigate(){ render(); updateNav(); }
window.addEventListener("hashchange", navigate);

function updateNav(){
  const r = parseRoute().name;
  document.querySelectorAll(".nav__links a").forEach(a => {
    const route = a.getAttribute("data-route");
    const active = (route === r) || (route === "app" && r === "run");
    a.classList.toggle("text-primary", active);
    a.classList.toggle("border-b-2", active);
    a.classList.toggle("border-primary", active);
  });
}

async function render(){
  const view = document.getElementById("view");
  view.innerHTML = `<div class="state"><span class="spinner"></span><div class="mt-2">${t("common.loading")}</div></div>`;
  const r = parseRoute();
  try {
    if(r.name === "overview") await renderOverview(view);
    else if(r.name === "demo") await renderDemo(view);
    else if(r.name === "app") await renderOperator(view);
    else if(r.name === "run") await renderRun(view, r.id);
    else if(r.name === "kb") await renderKB(view);
    else if(r.name === "customers") await renderCustomers(view);
    else if(r.name === "eval") await renderEval(view);
    else await renderOverview(view);
  } catch(e){
    view.innerHTML = `<div class="state"><div class="font-bold text-error">${t("common.error")}</div><p class="muted">${escapeHtml(e.message)}</p></div>`;
  }
}

async function renderOverview(view){
  const [inquiries, kb, customers, evalResults] = await Promise.all([
    api("/api/inquiries").catch(()=>[]),
    api("/api/kb").catch(()=>[]),
    api("/api/customers").catch(()=>[]),
    api("/api/eval/results").catch(()=>[]),
  ]);
  const clsAgg = evalResults.length ? (evalResults.filter(x=>x.classification_correct).length / evalResults.length) : 0;
  const routeAgg = evalResults.length ? (evalResults.filter(x=>x.routing_correct).length / evalResults.length) : 0;
  const citeAgg = evalResults.length ? (evalResults.filter(x=>x.citations_present).length / evalResults.length) : 0;
  view.innerHTML = `
    <section class="mb-10">
      <div class="flex flex-wrap items-baseline justify-between gap-2 border-b-2 border-on-surface dark:border-inverse-on-surface pb-2 mb-4">
        <h1 class="font-headline text-4xl sm:text-5xl font-black tracking-tight">${t("overview.title")}</h1>
        <span class="font-label text-xs uppercase tracking-widest text-secondary">Broadsheet · Editorial Prototype</span>
      </div>
      <p class="font-serif text-lg leading-relaxed max-w-3xl dropcap">${t("overview.lede")}</p>
      <div class="flex flex-wrap gap-3 mt-6">
        <a class="btn" href="#/demo">${t("overview.cta.demo")}</a>
        <a class="btn btn--ghost" href="#/app">${t("overview.cta.operator")}</a>
        <a class="btn btn--ghost" href="#/kb">${t("overview.cta.kb")}</a>
        <a class="btn btn--ghost" href="#/eval">${t("overview.cta.eval")}</a>
      </div>
    </section>

    <section class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10">
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("overview.workflows")}</div><div class="font-headline text-3xl font-black">12</div><div class="text-xs text-secondary">eval-20261022T190411Z</div></div>
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("overview.kpi.classification")}</div><div class="font-headline text-3xl font-black">12/12</div><div class="text-xs text-secondary">${t("overview.kpi.classificationSub")}</div></div>
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("overview.kpi.latency")}</div><div class="font-headline text-3xl font-black">−24.1%</div><div class="text-xs text-secondary">${t("overview.kpi.latencySub")}</div></div>
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("overview.kpi.tokens")}</div><div class="font-headline text-3xl font-black">−1578</div><div class="text-xs text-secondary">${t("overview.kpi.tokensSub")}</div></div>
    </section>

    <section class="card mb-10">
      <h2 class="font-headline text-2xl font-bold mb-3">${t("overview.what.title")}</h2>
      <p class="font-serif text-base leading-relaxed mb-3">${t("overview.what.p1")}</p>
      <p class="font-serif text-base leading-relaxed">${t("overview.what.p2")}</p>
    </section>

    <section class="card mb-10">
      <h2 class="font-headline text-2xl font-bold mb-3">${t("overview.wf.title")}</h2>
      <p class="muted mb-4">${t("overview.wf.subtitle")}</p>
      <ol class="steps">
        <li><span class="step-n">1</span><div><strong>${t("overview.wf.step1Title")}</strong>: ${t("overview.wf.step1Desc")}</div></li>
        <li><span class="step-n">2</span><div><strong>${t("overview.wf.step2Title")}</strong>: ${t("overview.wf.step2Desc")}</div></li>
        <li><span class="step-n">3</span><div><strong>${t("overview.wf.step3Title")}</strong>: ${t("overview.wf.step3Desc")}</div></li>
        <li><span class="step-n">4</span><div><strong>${t("overview.wf.step4Title")}</strong>: ${t("overview.wf.step4Desc")}</div></li>
        <li><span class="step-n">5</span><div><strong>${t("overview.wf.step5Title")}</strong>: ${t("overview.wf.step5Desc")}</div></li>
        <li><span class="step-n">6</span><div><strong>${t("overview.wf.step6Title")}</strong>: ${t("overview.wf.step6Desc")}</div></li>
      </ol>
      <div class="demo-inquiry mt-6">
        <div class="text-xs uppercase tracking-widest text-secondary mb-1">${t("overview.wf.inquiryLabel")}</div>
        <p class="font-serif italic">${t("overview.wf.inquiryText")}</p>
      </div>
      <div class="demo-meta">
        <div class="text-xs uppercase tracking-widest text-secondary mb-1">${t("overview.wf.resultLabel")}</div>
        <span class="text-sm">${t("overview.wf.resultMeta")}</span>
      </div>
      <div class="draft">
        <div class="text-xs uppercase tracking-widest text-secondary mb-1">${t("overview.wf.draftLabel")}</div>
        <p class="font-serif">${t("overview.wf.draftText")}</p>
      </div>
      <div class="sources mt-3">
        <span class="source-chip">${t("overview.wf.cite1")}</span>
        <span class="source-chip">${t("overview.wf.cite2")}</span>
      </div>
    </section>

    <section class="card mb-10">
      <h2 class="font-headline text-2xl font-bold mb-3">${t("overview.capabilities.title")}</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="card card--flat">
          <h3 class="font-headline font-bold text-lg mb-1">${t("overview.capabilities.structured")}</h3>
          <p class="text-sm muted">${t("overview.capabilities.structuredDesc")}</p>
        </div>
        <div class="card card--flat">
          <h3 class="font-headline font-bold text-lg mb-1">${t("overview.capabilities.retrieval")}</h3>
          <p class="text-sm muted">${t("overview.capabilities.retrievalDesc")}</p>
        </div>
        <div class="card card--flat">
          <h3 class="font-headline font-bold text-lg mb-1">${t("overview.capabilities.confidence")}</h3>
          <p class="text-sm muted">${t("overview.capabilities.confidenceDesc")}</p>
        </div>
        <div class="card card--flat">
          <h3 class="font-headline font-bold text-lg mb-1">${t("overview.capabilities.audit")}</h3>
          <p class="text-sm muted">${t("overview.capabilities.auditDesc")}</p>
        </div>
        <div class="card card--flat md:col-span-2">
          <h3 class="font-headline font-bold text-lg mb-1">${t("overview.capabilities.eval")}</h3>
          <p class="text-sm muted">${t("overview.capabilities.evalDesc")}</p>
        </div>
      </div>
    </section>

    <section class="card mb-10">
      <h2 class="font-headline text-2xl font-bold mb-2">${t("overview.hist.title")}</h2>
      <p class="muted mb-4">${t("overview.hist.note")}</p>
      <div class="table-wrap">
        <table>
          <thead><tr>
            <th>${t("overview.hist.metric")}</th><th>${t("overview.hist.baseline")}</th><th>${t("overview.hist.improved")}</th><th>${t("overview.hist.delta")}</th>
          </tr></thead>
          <tbody>${histRows()}</tbody>
        </table>
      </div>
      <div class="eval-notes">
        <p>${t("overview.hist.note1")}</p>
        <p>${t("overview.hist.note2")}</p>
        <p>${t("overview.hist.note3")}</p>
        <p>${t("overview.hist.note4")}</p>
        <p>${t("overview.hist.note5")}</p>
        <p>${t("overview.hist.note6")}</p>
        <p>${t("overview.hist.note7")}</p>
        <p>${t("overview.hist.note8")}</p>
      </div>
    </section>

        <section class="card mb-10">
          <h2 class="font-headline text-2xl font-bold mb-3">${t("overview.provenance.title")}</h2>
          <div class="space-y-2 text-sm leading-relaxed">
            <p>${t("overview.provenance.p1")}</p>
            <p>${t("overview.provenance.p2")}</p>
            <p>${t("overview.provenance.p3")}</p>
          </div>
        </section>

    <section class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-10">
      <div class="card">
        <h2 class="font-headline text-xl font-bold mb-3">${t("overview.limits5.title")}</h2>
        <ul class="list-disc list-inside text-sm leading-relaxed space-y-2">
          <li>${t("overview.limits5.1")}</li>
          <li>${t("overview.limits5.2")}</li>
          <li>${t("overview.limits5.3")}</li>
          <li>${t("overview.limits5.4")}</li>
        </ul>
      </div>
      <div class="card">
        <h2 class="font-headline text-xl font-bold mb-3">${t("overview.live.title")}</h2>
        <div class="grid grid-cols-2 gap-3">
          <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("overview.live.inquiries")}</div><div class="font-headline text-2xl font-black">${inquiries.length}</div></div>
          <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("overview.live.kb")}</div><div class="font-headline text-2xl font-black">${kb.length}</div></div>
          <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("overview.live.customers")}</div><div class="font-headline text-2xl font-black">${customers.length}</div></div>
          <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("overview.live.evalruns")}</div><div class="font-headline text-2xl font-black">${evalResults.length}</div><div class="text-xs text-secondary">cls ${Math.round(clsAgg*100)}% · route ${Math.round(routeAgg*100)}% · cite ${Math.round(citeAgg*100)}%</div></div>
        </div>
      </div>
    </section>
  `;
}

function histRows(){
  const rows = [
    [t("overview.hist.workflows"),"12","12","0"],
    [t("overview.hist.classification"),"12/12","12/12","0"],
    [t("overview.hist.routing"),"11/12","10/12","−1"],
    [t("overview.hist.sources"),"9/12","9/12","0"],
    [t("overview.hist.flags"),"12/12","9/12","−3"],
    [t("overview.hist.cost"),"0.010177 USD","0.008665 USD","−0.001512 USD"],
    [t("overview.hist.latency"),"94603 ms","71849 ms","−22754 ms"],
    [t("overview.hist.tokens"),"37085","35507","−1578"],
  ];
  return rows.map(r=>`<tr><td>${r[0]}</td><td class="mono">${r[1]}</td><td class="mono">${r[2]}</td><td class="mono">${r[3]}</td></tr>`).join("");
}
async function renderDemo(view){
  view.innerHTML = `<div class="card"><h1 class="font-headline text-3xl font-black mb-2">${t("demo.title")}</h1><p class="muted mb-4">${t("demo.subtitle")}</p><div class="state"><span class="spinner"></span><div class="mt-2">${t("demo.loading")}</div></div></div>`;
  const snap = await api("/public/demo-snapshot");
  const inq = snap.inquiry || {};
  const cls = snap.classification;
  const conf = snap.classification_confidence;
  const routing = snap.routing_decision;
  const rationale = snap.rationale || (typeof snap.draft === "object" ? snap.draft?.reasoning : null);
  const draft = (typeof snap.draft === "string") ? snap.draft : (snap.draft?.original_text || snap.draft_text || "");
  const sources = snap.retrieved_sources || snap.cited_sources || (typeof snap.draft === "object" ? snap.draft?.citations : []) || [];
  const cited = snap.cited_sources || [];
  view.innerHTML = `
    <div class="card mb-6">
      <div class="flex flex-wrap items-baseline justify-between gap-2 border-b border-outline-variant pb-2 mb-3">
        <h1 class="font-headline text-3xl font-black">${t("demo.title")}</h1>
        <span class="badge text-secondary">Recorded Snapshot</span>
      </div>
      <p class="muted">${t("demo.subtitle")}</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("demo.classification")}</div><div class="font-headline text-2xl font-black">${escapeHtml(cls || "—")}</div></div>
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("demo.confidence")}</div><div class="font-headline text-2xl font-black">${conf != null ? Number(conf).toFixed(2) : "—"}</div></div>
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("demo.routing")}</div><div class="font-headline text-lg font-black">${escapeHtml(routing || "—")}</div></div>
    </div>
    <div class="card mb-6">
      <div class="text-xs uppercase tracking-widest text-secondary mb-2">${t("demo.inquiry")} · 01</div>
      <div class="font-headline text-xl font-bold mb-1">${escapeHtml(td(inq.subject || ""))}</div>
      <div class="font-serif text-base leading-relaxed">${escapeHtml(td(inq.body || ""))}</div>
    </div>
    ${rationale ? `<div class="card mb-6"><div class="font-headline text-lg font-bold mb-2">${t("demo.rationale")}</div><p class="font-serif text-base leading-relaxed">${escapeHtml(rationale)}</p></div>` : ""}
    <div class="card mb-6">
      <div class="font-headline text-lg font-bold mb-2">${t("demo.draft")} · 02</div>
      <div class="draft">${escapeHtml(td(draft))}</div>
      <div class="mt-3 text-xs text-secondary">draft_confidence: ${snap.draft_confidence != null ? Number(snap.draft_confidence).toFixed(2) : "—"}</div>
    </div>
    <div class="card">
      <div class="font-headline text-lg font-bold mb-2">${t("demo.sources")} · ${sources.length}</div>
      <div>${sources.length ? sources.map(s=>`<span class="source-chip">${escapeHtml(td(s.title || s.source_key || s))}</span>`).join("") : `<span class="muted">${t("demo.noSources")}</span>`}</div>
      ${cited.length ? `<div class="mt-3"><div class="text-xs uppercase tracking-widest text-secondary mb-1">Cited</div>${cited.map(s=>`<span class="source-chip">${escapeHtml(td(s.title || s.source_key))}</span>`).join("")}</div>` : ""}
    </div>
  `;
}

async function renderOperator(view){
  const inquiries = await api("/api/inquiries");
  view.innerHTML = `
    <div class="flex flex-wrap items-baseline justify-between gap-2 border-b-2 border-on-surface dark:border-inverse-on-surface pb-2 mb-6">
      <h1 class="font-headline text-3xl font-black">${t("operator.title")}</h1>
      <span class="text-xs uppercase tracking-widest text-secondary">${inquiries.length} ${t("operator.entries")}</span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="card">
        <h2 class="font-headline text-xl font-bold mb-3">${t("operator.submit")}</h2>
        <form id="submitForm">
          <div class="field"><label>${t("operator.subject")}</label><input name="subject" required /></div>
          <div class="field"><label>${t("operator.body")}</label><textarea name="body" required rows="4"></textarea></div>
          <div class="field"><label>${t("operator.email")}</label><input name="customer_email" type="email" /></div>
          <div class="field"><label>${t("operator.variant")}</label>
            <select name="prompt_variant"><option value="improved">improved</option><option value="baseline">baseline</option></select>
          </div>
          <button class="btn" type="submit">${t("operator.submitBtn")}</button>
        </form>
      </div>
      <div class="card">
        <h2 class="font-headline text-xl font-bold mb-3">${t("operator.inbox")}</h2>
        <div id="inboxList" class="stack" style="max-height:560px;overflow:auto"></div>
      </div>
    </div>
  `;
  const list = document.getElementById("inboxList");
  if(!inquiries.length){
    list.innerHTML = `<div class="state">${t("operator.empty")}</div>`;
  } else {
    list.innerHTML = inquiries.map(inq => `
      <div class="inbox-item" data-id="${inq.run_id || inq.id}" tabindex="0" role="button">
        <div>${badge(inq.state || inq.status)}</div>
        <div>
          <div class="font-semibold">${escapeHtml(inq.subject || t("operator.noSubject"))}</div>
          <div class="text-xs text-secondary">${escapeHtml(td((inq.body||"")).slice(0,90))}</div>
        </div>
        <div class="text-primary font-semibold text-sm">${t("common.open")}</div>
      </div>
    `).join("");
    list.querySelectorAll(".inbox-item").forEach(el => {
      const open = () => { location.hash = "#/app/run/" + el.getAttribute("data-id"); };
      el.addEventListener("click", open);
      el.addEventListener("keydown", e => { if(e.key==="Enter"||e.key===" "){ e.preventDefault(); open(); }});
    });
  }
  document.getElementById("submitForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const fd = new FormData(e.target);
    const body = { subject: fd.get("subject"), body: fd.get("body"), customer_email: fd.get("customer_email") || null };
    const variant = fd.get("prompt_variant");
    const btn = e.target.querySelector("button[type=submit]");
    btn.disabled = true;
    try {
      const inq = await api("/api/inquiries", {method:"POST", body});
      const runRes = await api(`/api/inquiries/${inq.id}/run?prompt_variant=${variant}`, {method:"POST"});
      toast(t("toast.created"), "ok");
      location.hash = "#/app/run/" + (runRes.run_id || runRes.id || inq.id);
    } catch(err){ toast(err.message || t("toast.error"), "error"); }
    finally { btn.disabled = false; }
  });
}

async function renderRun(view, id){
  view.innerHTML = `<div class="state"><span class="spinner"></span></div>`;
  const run = await api("/api/runs/" + id);
  const inq = run.inquiry || {};
  const draft = run.draft;
  const steps = run.steps || [];
  const approvals = run.approvals || [];
  const sources = (draft && draft.citations) ? draft.citations : [];
  view.innerHTML = `
    <div class="mb-4"><a class="text-primary font-semibold text-sm" href="#/app">← ${t("common.back")}</a></div>
    <div class="flex flex-wrap items-baseline justify-between gap-2 border-b-2 border-on-surface dark:border-inverse-on-surface pb-2 mb-6">
      <h1 class="font-headline text-3xl font-black">${t("run.title")}</h1>
      <div class="flex items-center gap-2">
        ${badge(run.state)}
        <button class="btn btn--ghost btn--sm" onclick="openTrace('${run.id}')">${t("run.traceLink")}</button>
      </div>
    </div>
    <section class="grid grid-cols-2 md:grid-cols-6 gap-3 mb-6">
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("run.workflow")}</div><div class="font-mono text-sm">${run.id.slice(0,8)}…</div></div>
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("run.classification")}</div><div class="font-headline text-xl font-black">${escapeHtml(run.classification || "—")}</div><div class="text-xs text-secondary">${t("run.confidence")} ${run.confidence != null ? Number(run.confidence).toFixed(2) : "—"}</div></div>
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("run.routing")}</div><div class="text-sm font-semibold">${escapeHtml(run.routing_decision || "—")}</div></div>
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("run.cost")}</div><div class="font-headline text-lg font-black">${fmtMoney(run.total_cost_usd)}</div></div>
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("run.latency")}</div><div class="font-headline text-lg font-black">${fmtMs(run.total_latency_ms)}</div></div>
      <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("run.tokens")}</div><div class="font-headline text-lg font-black">${fmtNum(run.total_tokens)}</div></div>
    </section>
    <section class="card mb-6">
      <div class="font-headline text-lg font-bold mb-2">${t("run.inquiry")}</div>
      <div class="font-semibold mb-1">${escapeHtml(td(inq.subject || ""))}</div>
      <div class="font-serif text-base leading-relaxed whitespace-pre-wrap">${escapeHtml(td(inq.body || ""))}</div>
      ${run.error ? `<div class="badge text-error mt-2">${escapeHtml(run.error)}</div>` : ""}
    </section>
    <section class="card mb-6">
      <div class="font-headline text-lg font-bold mb-2">${t("run.steps")} · ${steps.length}</div>
      ${steps.map(s => `
        <div class="step">
          <div class="flex flex-wrap items-center gap-2 mb-1">
            <span class="font-semibold">${s.index}. ${escapeHtml(stepLabel(s.name))}</span>
            ${badge(s.status)}
            ${s.model_name ? `<span class="text-xs text-secondary">${escapeHtml(s.model_provider)}/${escapeHtml(s.model_name)}</span>` : ""}
            <span class="text-xs text-secondary">${fmtMs(s.latency_ms)} · ${fmtMoney(s.cost_usd)}</span>
            ${s.confidence != null ? `<span class="text-xs text-secondary">conf ${Number(s.confidence).toFixed(2)}</span>` : ""}
            ${s.finish_reason ? `<span class="text-xs text-secondary">${escapeHtml(s.finish_reason)}</span>` : ""}
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
            <div><span class="uppercase tracking-widest text-secondary">${t("run.input")}</span><div class="font-mono mt-1">${escapeHtml(s.input_summary || "—")}</div></div>
            <div><span class="uppercase tracking-widest text-secondary">${t("run.output")}</span><div class="font-mono mt-1">${escapeHtml(s.output_summary || "—")}</div></div>
          </div>
          ${s.citations && s.citations.length ? `<div class="mt-2">${s.citations.map(c=>`<span class="source-chip">${escapeHtml(c.title||c.source_key)}</span>`).join("")}</div>` : ""}
        </div>
      `).join("")}
    </section>
    <section class="card mb-6">
      <div class="font-headline text-lg font-bold mb-2">${t("run.draft")}</div>
      ${draft ? `
        <div class="draft">${escapeHtml(draft.edited_text || draft.original_text || "")}</div>
        <div class="flex flex-wrap gap-2 mt-2">
          <span class="badge text-secondary">conf ${draft.draft_confidence != null ? Number(draft.draft_confidence).toFixed(2) : "—"}</span>
          ${draft.citation_format_issues && draft.citation_format_issues.length ? `<span class="badge text-primary">${draft.citation_format_issues.length} citation issues</span>` : ""}
        </div>
        ${draft.reasoning ? `<div class="mt-3"><div class="text-xs uppercase tracking-widest text-secondary mb-1">${t("run.reasoning")}</div><p class="font-serif text-base leading-relaxed">${escapeHtml(draft.reasoning)}</p></div>` : ""}
        <div class="mt-3"><div class="text-xs uppercase tracking-widest text-secondary mb-1">${t("run.sources")} · ${sources.length}</div>
          <div>${sources.length ? sources.map(s=>`<span class="source-chip">${escapeHtml(s.title || s.source_key)}</span>`).join("") : `<span class="muted">${t("demo.noSources")}</span>`}</div>
        </div>
        ${approvals.length ? `<div class="mt-3"><div class="text-xs uppercase tracking-widest text-secondary mb-1">${t("run.approvals")}</div>${approvals.map(a=>`<div class="text-xs text-secondary">${escapeHtml(a.action)} · ${escapeHtml(a.actor)} · ${a.created_at || ""}${a.reason ? " · " + escapeHtml(a.reason) : ""}</div>`).join("")}</div>` : ""}
        ${renderApprovalControls(run, draft)}
      ` : `<div class="state">${t("run.noDraft")}</div>`}
    </section>
  `;
  wireApproval(run);
}

function renderApprovalControls(run, draft){
  if(run.state === "Approved" || run.state === "Rejected") return "";
  const original = draft.original_text || "";
  return `
    <div class="rule my-4"></div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div>
        <button id="approveBtn" class="btn">${t("common.approve")}</button>
        <button id="rejectBtn" class="btn btn--danger ml-2">${t("common.reject")}</button>
        <div class="field mt-3"><label>${t("run.rejectReason")}</label><input id="rejectReason" /></div>
      </div>
      <div>
        <div class="field"><label>${t("run.editPlaceholder")}</label><textarea id="editDraft" rows="6">${escapeHtml(original)}</textarea></div>
        <button id="editApproveBtn" class="btn btn--ghost">${t("common.editApprove")}</button>
      </div>
    </div>
  `;
}
function wireApproval(run){
  const approveBtn = document.getElementById("approveBtn");
  if(approveBtn) approveBtn.addEventListener("click", async () => {
    try { await api(`/api/runs/${run.id}/approve`, {method:"POST", body:{action:"approve"}}); toast(t("toast.approved"), "ok"); render(); }
    catch(e){ toast(e.message || t("toast.error"), "error"); }
  });
  const rejectBtn = document.getElementById("rejectBtn");
  if(rejectBtn) rejectBtn.addEventListener("click", async () => {
    const reason = (document.getElementById("rejectReason")?.value || "").trim();
    try { await api(`/api/runs/${run.id}/approve`, {method:"POST", body:{action:"reject", reason}}); toast(t("toast.rejected"), "ok"); render(); }
    catch(e){ toast(e.message || t("toast.error"), "error"); }
  });
  const editBtn = document.getElementById("editApproveBtn");
  if(editBtn) editBtn.addEventListener("click", async () => {
    const text = (document.getElementById("editDraft")?.value || "").trim();
    if(!text){ toast(t("toast.error"), "error"); return; }
    try { await api(`/api/runs/${run.id}/approve`, {method:"POST", body:{action:"edit_approve", edited_text: text}}); toast(t("toast.edited"), "ok"); render(); }
    catch(e){ toast(e.message || t("toast.error"), "error"); }
  });
}

async function renderKB(view){
  const kb = await api("/api/kb");
  view.innerHTML = `
    <div class="flex flex-wrap items-baseline justify-between gap-2 border-b-2 border-on-surface dark:border-inverse-on-surface pb-2 mb-6">
      <h1 class="font-headline text-3xl font-black">${t("kb.title")}</h1>
      <span class="text-xs uppercase tracking-widest text-secondary">${kb.length} ${t("kb.entries")}</span>
    </div>
    ${kb.length ? `
      <div class="card">
        <table>
          <thead><tr><th>Key</th><th>Title</th><th>Category</th></tr></thead>
          <tbody>
            ${kb.map(k => `<tr>
              <td class="mono">${escapeHtml(k.source_key || k.key || k.id)}</td>
              <td class="font-semibold">${escapeHtml(k.title || "—")}</td>
              <td class="text-sm">${escapeHtml(k.category || "—")}</td>
            </tr>`).join("")}
          </tbody>
        </table>
      </div>
    ` : `<div class="state">${t("kb.empty")}</div>`}
  `;
}

async function renderCustomers(view){
  const customers = await api("/api/customers");
  view.innerHTML = `
    <div class="flex flex-wrap items-baseline justify-between gap-2 border-b-2 border-on-surface dark:border-inverse-on-surface pb-2 mb-6">
      <h1 class="font-headline text-3xl font-black">${t("customers.title")}</h1>
      <span class="text-xs uppercase tracking-widest text-secondary">${customers.length}</span>
    </div>
    ${customers.length ? `
      <div class="card">
        <table>
          <thead><tr><th>Name</th><th>Email</th><th>Tier</th></tr></thead>
          <tbody>
            ${customers.map(c => `<tr>
              <td class="font-semibold">${escapeHtml(c.name || "—")}</td>
              <td class="mono">${escapeHtml(c.email || "—")}</td>
              <td>${escapeHtml(c.tier || "—")}</td>
            </tr>`).join("")}
          </tbody>
        </table>
      </div>
    ` : `<div class="state">${t("customers.empty")}</div>`}
  `;
}

async function renderEval(view){
  const results = await api("/api/eval/results").catch(()=>[]);
  const agg = computeEvalAgg(results);
  view.innerHTML = `
    <div class="flex flex-wrap items-baseline justify-between gap-2 border-b-2 border-on-surface dark:border-inverse-on-surface pb-2 mb-6">
      <h1 class="font-headline text-3xl font-black">${t("eval.title")}</h1>
      <button id="runEvalBtn" class="btn">${t("eval.runBtn")}</button>
    </div>
    <p class="muted mb-4">${t("eval.subtitle")}</p>
    <div id="evalProgress" class="muted mb-4" style="display:none">${t("eval.running")} <span class="spinner"></span></div>
    <section class="card">
      <div class="font-headline text-lg font-bold mb-3">${t("overview.live.evalruns")} · ${results.length}</div>
      ${results.length ? `
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
          <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("eval.summary.n")}</div><div class="font-headline text-2xl font-black">${agg.n}</div></div>
          <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("eval.summary.cls")}</div><div class="font-headline text-2xl font-black">${Math.round(agg.cls*100)}%</div></div>
          <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("eval.summary.route")}</div><div class="font-headline text-2xl font-black">${Math.round(agg.route*100)}%</div></div>
          <div class="kpi"><div class="text-xs uppercase tracking-widest text-secondary">${t("eval.summary.cite")}</div><div class="font-headline text-2xl font-black">${Math.round(agg.cite*100)}%</div></div>
        </div>
        <div style="overflow:auto">
        <table>
          <thead><tr>
            <th>${t("eval.case")}</th><th>${t("eval.predicted")}</th><th>${t("eval.expected")}</th>
            <th>${t("eval.cls")}</th><th>${t("eval.routing")}</th><th>${t("eval.cites")}</th>
            <th>${t("eval.latency")}</th><th>${t("eval.cost")}</th>
          </tr></thead>
          <tbody>
            ${results.slice(0,80).map(r=>`<tr>
              <td class="mono">${escapeHtml(r.case_id)}</td>
              <td>${escapeHtml(r.predicted)}</td>
              <td>${escapeHtml(r.expected)}</td>
              <td>${r.classification_correct ? "✓" : "✗"}</td>
              <td>${r.routing_correct ? "✓" : "✗"}</td>
              <td>${r.citations_present ? "✓" : "—"}</td>
              <td class="num">${fmtMs(r.latency_ms)}</td>
              <td class="num">${fmtMoney(r.cost_usd)}</td>
            </tr>`).join("")}
          </tbody>
        </table>
        </div>
      ` : `<div class="state">${t("eval.noResults")}</div>`}
    </section>
  `;
  document.getElementById("runEvalBtn").addEventListener("click", async () => {
    const btn = document.getElementById("runEvalBtn");
    const prog = document.getElementById("evalProgress");
    btn.disabled = true; prog.style.display = "block";
    try {
      await api("/api/eval/run?prompt_variant=improved", {method:"POST"});
      toast(t("toast.evalDone"), "ok");
      await renderEval(view);
    } catch(e){ toast(e.message || t("toast.error"), "error"); }
    finally { btn.disabled = false; prog.style.display = "none"; }
  });
}

function computeEvalAgg(results){
  const n = results.length;
  const cls = n ? results.filter(x=>x.classification_correct).length / n : 0;
  const route = n ? results.filter(x=>x.routing_correct).length / n : 0;
  const cite = n ? results.filter(x=>x.citations_present).length / n : 0;
  return {n, cls, route, cite};
}

document.getElementById("langToggle").addEventListener("click", () => {
  lang = lang === "de" ? "en" : "de";
  localStorage.setItem("pp2.lang", lang);
  applyLang();
  render();
});
document.getElementById("themeToggle").addEventListener("click", () => {
  theme = theme === "dark" ? "light" : "dark";
  localStorage.setItem("pp2.theme", theme);
  applyTheme();
});

// Float widget behavior
(function(){
  const w = document.getElementById("floatWidget");
  if(!w) return;
  const saved = localStorage.getItem("pp2.widgetPos") || "br";
  setPosition(saved);
  w.addEventListener("click", (e) => {
    const target = e.target;
    if(target.closest("a,button")) return;
    w.classList.toggle("is-expanded");
  });
  w.addEventListener("keydown", (e) => {
    if(e.key === "Enter" || e.key === " ") { e.preventDefault(); w.classList.toggle("is-expanded"); }
    if(e.key === "Escape") w.classList.remove("is-expanded");
  });
  w.querySelectorAll(".float-widget__positions button").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      setPosition(btn.getAttribute("data-pos"));
      localStorage.setItem("pp2.widgetPos", btn.getAttribute("data-pos"));
    });
  });
  function setPosition(pos){
    w.classList.remove("pos-tl","pos-tr","pos-bl","pos-br");
    w.classList.add("pos-" + pos);
    w.querySelectorAll(".float-widget__positions button").forEach(b => {
      b.classList.toggle("active", b.getAttribute("data-pos") === pos);
    });
  }
})();

applyTheme();
applyLang();
navigate();