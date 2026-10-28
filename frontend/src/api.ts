const OPERATOR_TOKEN = (import.meta as any).env?.VITE_OPERATOR_TOKEN || "1";

export const API = {
  base: "/api",
  async getDemoSnapshot() {
    const response = await fetch("/public/demo-snapshot");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  },

  async listInquiries() {
    return requestJson<any[]>(`${this.base}/inquiries`);
  },

  async createInquiry(body: string, subject = "", customer_email: string | null = null) {
    return requestJson<any>(`${this.base}/inquiries`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ subject, body, customer_email }),
    });
  },

  async run(inquiryId: string, promptVariant = "improved") {
    return requestJson<any>(`${this.base}/inquiries/${inquiryId}/run?prompt_variant=${promptVariant}`, {
      method: "POST",
    });
  },

  async getRun(id: string) {
    return requestJson<any>(`${this.base}/runs/${id}`, {
      headers: { "X-ProzessPilot-Operator": OPERATOR_TOKEN },
    });
  },

  async approve(runId: string, action: string, edited_text?: string, reason?: string) {
    return requestJson<any>(`${this.base}/runs/${runId}/approve`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action, edited_text, reason }),
    });
  },

  async evalRun(promptVariant = "improved") {
    return requestJson<any>(`${this.base}/eval/run?prompt_variant=${promptVariant}`, {
      method: "POST",
    });
  },

  async evalResults() {
    return requestJson<any>(`${this.base}/eval/results`);
  },

  async listCustomers() {
    return requestJson<any[]>(`${this.base}/customers`);
  },
};

class ApiError extends Error {
  status: number;

  constructor(message: string, status: number) {
    super(message);
    this.name = "ApiError";
    this.status = status;
  }
}

async function requestJson<T>(url: string, init?: RequestInit): Promise<T> {
  const headers = new Headers(init?.headers ?? {});
  if (!headers.has("x-prozesspilot-operator")) {
    headers.set("x-prozesspilot-operator", OPERATOR_TOKEN);
  }
  const mergedInit = { ...init, headers };
  let response: Response;
  try {
    response = await fetch(url, mergedInit);
  } catch {
    throw new ApiError("Netzwerkfehler beim Aufruf der API.", 0);
  }

  const contentType = response.headers.get("content-type") ?? "";
  const text = await response.text();

  if (!response.ok) {
    const detail = extractSafeDetail(text, contentType);
    const suffix = detail ? `: ${detail}` : "";
    throw new ApiError(`Anfrage fehlgeschlagen (HTTP ${response.status})${suffix}`, response.status);
  }

  if (text.trim() === "") {
    throw new ApiError(`Leere Serverantwort (HTTP ${response.status}).`, response.status);
  }

  if (!contentType.toLowerCase().includes("application/json")) {
    throw new ApiError(`Unerwartete Serverantwort (HTTP ${response.status}).`, response.status);
  }

  try {
    return JSON.parse(text) as T;
  } catch {
    throw new ApiError(`Ungültige JSON-Antwort (HTTP ${response.status}).`, response.status);
  }
}

function extractSafeDetail(text: string, contentType: string): string {
  if (!contentType.toLowerCase().includes("application/json") || text.trim() === "") {
    const plain = text.replace(/\s+/g, " ").trim();
    return plain.length > 500 ? `${plain.slice(0, 500)}…` : plain;
  }

  try {
    const data = JSON.parse(text);
    const detail = (data as { detail?: unknown })?.detail;
    if (typeof detail === "string") {
      const clean = detail.replace(/[\r\n\t]+/g, " ").trim();
      return clean.length > 500 ? `${clean.slice(0, 500)}…` : clean;
    }
    if (Array.isArray(detail)) {
      const messages = detail
        .map((item) => {
          if (!item || typeof item !== "object") return "";
          const location = Array.isArray((item as { loc?: unknown }).loc)
            ? (item as { loc: unknown[] }).loc.join(".")
            : "";
          const message = typeof (item as { msg?: unknown }).msg === "string"
            ? (item as { msg: string }).msg
            : "";
          return location && message ? `${location}: ${message}` : message;
        })
        .filter(Boolean)
        .join("; ");
      return messages.length > 500 ? `${messages.slice(0, 500)}…` : messages;
    }
  } catch {
    // Fall through to the plain-text handling below.
  }

  const plain = text.replace(/\s+/g, " ").trim();
  return plain.length > 500 ? `${plain.slice(0, 500)}…` : plain;
}
