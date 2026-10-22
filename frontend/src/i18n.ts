import { ref } from "vue";

export type Locale = "de" | "en";

const STORAGE_KEY = "pp_locale";

function initialLocale(): Locale {
  const stored = localStorage.getItem(STORAGE_KEY);
  return stored === "en" ? "en" : "de";
}

export const locale = ref<Locale>(initialLocale());

const messages: Record<Locale, Record<string, string>> = {
  de: {
    "nav.inbox": "Inbox",
    "nav.eval": "Evaluation",
    "lang.toggle": "Sprache wechseln",
    "lang.label": "DE",
    "inbox.title": "Neue Anfrage",
    "inbox.bodyPlaceholder": "Anfrage-Text (Deutsch)…",
    "inbox.emailPlaceholder": "Kunden-E-Mail (optional)",
    "inbox.submit": "Einreichen & Workflow starten",
    "inbox.submitting": "Startet…",
    "inbox.listTitle": "Inbox",
    "inbox.loading": "Laden…",
    "inbox.empty": "Keine Anfragen. Reiche oben eine ein.",
    "inbox.open": "Öffnen →",
    "eval.title": "Evaluation",
    "eval.run": "Eval (improved prompt) starten",
    "eval.running": "Läuft…",
    "eval.n": "N",
    "eval.provider": "Provider",
    "eval.classification": "Klassifikation",
    "eval.routing": "Routing",
    "eval.citations": "Zitierquote",
    "eval.latency": "Ø Latenz",
    "eval.cost": "Gesamtkosten",
    "eval.case": "Case",
    "eval.pred": "Pred",
    "eval.exp": "Exp",
    "eval.ok": "OK",
    "eval.routingOk": "Routing OK",
    "eval.quotes": "Zitate",
    "run.workflow": "Workflow",
    "run.classification": "Klassifikation",
    "run.confidence": "Konfidenz",
    "run.routing": "Routing",
    "run.cost": "Kosten",
    "run.latency": "Latenz",
    "run.customer": "Kunde",
    "run.inquiry": "Anfrage",
    "run.steps": "Schritte",
    "run.latencyShort": "latenz",
    "run.costShort": "kosten",
    "run.input": "Input",
    "run.output": "Output",
    "run.sources": "Quellen",
    "run.draft": "Entwurf",
    "run.reasoning": "Begründung:",
    "run.edited": "Bearbeitet",
    "run.approval": "Freigabe",
    "run.approve": "Freigeben",
    "run.editApprove": "Bearbeiten & Freigeben",
    "run.reject": "Ablehnen",
    "run.rejectReason": "Ablehnungsgrund (bei Reject)",
    "run.saved": "Aktion gespeichert.",
    "run.loading": "Laden…",
    "run.loadError": "Lauf konnte nicht geladen werden.",
    "run.actionError": "Aktion fehlgeschlagen.",
    "run.back": "Zurück zur Inbox",
  },
  en: {
    "nav.inbox": "Inbox",
    "nav.eval": "Evaluation",
    "lang.toggle": "Switch language",
    "lang.label": "EN",
    "inbox.title": "New inquiry",
    "inbox.bodyPlaceholder": "Inquiry text (German)…",
    "inbox.emailPlaceholder": "Customer email (optional)",
    "inbox.submit": "Submit & start workflow",
    "inbox.submitting": "Starting…",
    "inbox.listTitle": "Inbox",
    "inbox.loading": "Loading…",
    "inbox.empty": "No inquiries. Submit one above.",
    "inbox.open": "Open →",
    "eval.title": "Evaluation",
    "eval.run": "Run eval (improved prompt)",
    "eval.running": "Running…",
    "eval.n": "N",
    "eval.provider": "Provider",
    "eval.classification": "Classification",
    "eval.routing": "Routing",
    "eval.citations": "Citation rate",
    "eval.latency": "Avg latency",
    "eval.cost": "Total cost",
    "eval.case": "Case",
    "eval.pred": "Pred",
    "eval.exp": "Exp",
    "eval.ok": "OK",
    "eval.routingOk": "Routing OK",
    "eval.quotes": "Quotes",
    "run.workflow": "Workflow",
    "run.classification": "Classification",
    "run.confidence": "Confidence",
    "run.routing": "Routing",
    "run.cost": "Cost",
    "run.latency": "Latency",
    "run.customer": "Customer",
    "run.inquiry": "Inquiry",
    "run.steps": "Steps",
    "run.latencyShort": "latency",
    "run.costShort": "cost",
    "run.input": "Input",
    "run.output": "Output",
    "run.sources": "Sources",
    "run.draft": "Draft",
    "run.reasoning": "Reasoning:",
    "run.edited": "Edited",
    "run.approval": "Approval",
    "run.approve": "Approve",
    "run.editApprove": "Edit & approve",
    "run.reject": "Reject",
    "run.rejectReason": "Rejection reason (on reject)",
    "run.saved": "Action saved.",
    "run.loading": "Loading…",
    "run.loadError": "Could not load run.",
    "run.actionError": "Action failed.",
    "run.back": "Back to inbox",
  },
};

export function t(key: string): string {
  return messages[locale.value][key] ?? messages.de[key] ?? key;
}

export function setLocale(next: Locale) {
  locale.value = next;
  localStorage.setItem(STORAGE_KEY, next);
  document.documentElement.lang = next;
}

export function toggleLocale() {
  setLocale(locale.value === "de" ? "en" : "de");
}

// initial
document.documentElement.lang = locale.value;
