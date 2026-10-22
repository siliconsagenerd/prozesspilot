export const API = {
  base: "/api",
  async listInquiries() {
    const r = await fetch(`${this.base}/inquiries`);
    return r.json();
  },
  async createInquiry(body: string, subject = "", customer_email: string | null = null) {
    const r = await fetch(`${this.base}/inquiries`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ subject, body, customer_email }),
    });
    return r.json();
  },
  async run(inquiryId: string, promptVariant = "improved") {
    const r = await fetch(`${this.base}/inquiries/${inquiryId}/run?prompt_variant=${promptVariant}`, { method: "POST" });
    return r.json();
  },
  async getRun(id: string) {
    const r = await fetch(`${this.base}/runs/${id}`);
    return r.json();
  },
  async approve(runId: string, action: string, edited_text?: string, reason?: string) {
    const r = await fetch(`${this.base}/runs/${runId}/approve`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action, edited_text, reason }),
    });
    return r.json();
  },
  async evalRun(promptVariant = "improved") {
    const r = await fetch(`${this.base}/eval/run?prompt_variant=${promptVariant}`, { method: "POST" });
    return r.json();
  },
  async evalResults() {
    const r = await fetch(`${this.base}/eval/results`);
    return r.json();
  },
};