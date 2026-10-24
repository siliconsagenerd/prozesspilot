<template>
  <div class="doc">
    <header class="doc-header">
      <div class="doc-header-left">
        <div class="doc-id">{{ t("landing.docid") }}</div>
        <h1 class="doc-title">ProzessPilot</h1>
      </div>
      <div class="doc-header-right">
        <p class="doc-lede">{{ t("landing.lede") }}</p>
        <div class="doc-actions">
          <router-link to="/demo" class="doc-action">{{ t("landing.action.demo") }}</router-link>
          <router-link to="/app" class="doc-action">{{ t("landing.action.operator") }}</router-link>
          <router-link to="/eval" class="doc-action">{{ t("landing.action.eval") }}</router-link>
        </div>
      </div>
    </header>

    <div class="kpi-strip">
      <div class="kpi">
        <span class="kpi-label">{{ t("landing.eval.workflows") }}</span>
        <span class="kpi-value mono">12</span>
      </div>
      <div class="kpi">
        <span class="kpi-label">{{ t("landing.eval.classification") }}</span>
        <span class="kpi-value mono">12/12</span>
      </div>
      <div class="kpi">
        <span class="kpi-label">{{ t("landing.eval.latency") }}</span>
        <span class="kpi-value mono">−24.1%</span>
      </div>
      <div class="kpi">
        <span class="kpi-label">{{ t("landing.eval.tokens") }}</span>
        <span class="kpi-value mono">−1578</span>
      </div>
    </div>

    <hr class="rule" />

    <div class="layout">
      <main class="main">
        <section class="doc-section">
          <h2 class="section-h">{{ t("landing.section.what") }}</h2>
          <p>{{ t("landing.what") }}</p>
          <p class="muted">
            {{ t("landing.public") }} {{ t("landing.operator") }}
          </p>
        </section>

        <hr class="rule" />

        <section class="doc-section">
          <h2 class="section-h">{{ t("landing.section.workflow") }}</h2>
          <p>{{ t("landing.workflow.intro") }}</p>
          <ol class="steps">
            <li v-for="n in 6" :key="n"><span class="step-n">{{ n }}</span><div><strong>{{ t('landing.step.'+n).replace(/:.*/, '') }}</strong>: {{ t('landing.step.'+n).replace(/^[^:]*: /, '') }}</div></li>
          </ol>

          <figure class="trace">
            <div class="trace-row">
              <div class="trace-label">{{ t("landing.trace.inquiry.label") }}</div>
              <blockquote>„{{ t("landing.trace.inquiry.text") }}“</blockquote>
            </div>
            <div class="trace-row">
              <div class="trace-label">{{ t("landing.trace.result.label") }}</div>
              <div class="trace-meta">{{ t("landing.trace.result.meta") }}</div>
            </div>
            <div class="trace-row">
              <div class="trace-label">{{ t("landing.trace.draft.label") }}</div>
              <p>{{ t("landing.trace.draft.text") }}</p>
              <div class="cites">
                <span class="cite">{{ t("landing.trace.cite.1") }}</span>
                <span class="cite">{{ t("landing.trace.cite.2") }}</span>
              </div>
            </div>
          </figure>
        </section>

        <hr class="rule" />

        <section class="doc-section">
          <h2 class="section-h">{{ t("landing.section.capabilities") }}</h2>
          <dl class="deflist">
            <div class="def">
              <dt>{{ t("landing.cap.structured") }}</dt>
              <dd>{{ t("landing.cap.structured.desc") }}</dd>
            </div>
            <div class="def">
              <dt>{{ t("landing.cap.citations") }}</dt>
              <dd>{{ t("landing.cap.citations.desc") }}</dd>
            </div>
            <div class="def">
              <dt>{{ t("landing.cap.approval") }}</dt>
              <dd>{{ t("landing.cap.approval.desc") }}</dd>
            </div>
            <div class="def">
              <dt>{{ t("landing.cap.audit") }}</dt>
              <dd>{{ t("landing.cap.audit.desc") }}</dd>
            </div>
            <div class="def">
              <dt>{{ t("landing.cap.eval") }}</dt>
              <dd>{{ t("landing.cap.eval.desc") }}</dd>
            </div>
          </dl>
        </section>

        <hr class="rule" />

        <section class="doc-section eval-section">
          <h2 class="section-h">4. Evaluation</h2>
          <p class="muted">{{ t("landing.eval.historicalMetrics") }}</p>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>{{ t("landing.eval.metric") }}</th>
                  <th>Baseline</th>
                  <th>ProzessPilot</th>
                  <th>Delta</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{{ t("landing.eval.workflows") }}</td>
                  <td class="mono">12</td>
                  <td class="mono">12</td>
                  <td class="mono">0</td>
                </tr>
                <tr>
                  <td>{{ t("landing.eval.classification") }}</td>
                  <td class="mono">12/12</td>
                  <td class="mono">12/12</td>
                  <td class="mono">0</td>
                </tr>
                <tr>
                  <td>{{ t("landing.eval.routing") }}</td>
                  <td class="mono">11/12</td>
                  <td class="mono">10/12</td>
                  <td class="mono">−1</td>
                </tr>
                <tr>
                  <td>{{ t("landing.eval.sources") }}</td>
                  <td class="mono">9/12</td>
                  <td class="mono">9/12</td>
                  <td class="mono">0</td>
                </tr>
                <tr>
                  <td>{{ t("landing.eval.truncation") }}</td>
                  <td class="mono">12/12</td>
                  <td class="mono">9/12</td>
                  <td class="mono">−3</td>
                </tr>
                <tr>
                  <td>{{ t("landing.eval.cost") }}</td>
                  <td class="mono">0.010177 USD</td>
                  <td class="mono">0.008665 USD</td>
                  <td class="mono">−14.9%</td>
                </tr>
                <tr>
                  <td>{{ t("landing.eval.latency") }}</td>
                  <td class="mono">94603 ms</td>
                  <td class="mono">71849 ms</td>
                  <td class="mono">−24.1%</td>
                </tr>
                <tr>
                  <td>{{ t("landing.eval.tokens") }}</td>
                  <td class="mono">37085</td>
                  <td class="mono">35507</td>
                  <td class="mono">−1578</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
      </main>

      <aside class="side">
        <section class="side-block try-block">
          <h3 class="side-h">{{ t("landing.side.try") }}</h3>
          <div class="try-links">
            <router-link to="/demo" class="try-link">{{ t("landing.action.demo") }} →</router-link>
            <router-link to="/app" class="try-link">{{ t("landing.action.operator") }} →</router-link>
            <router-link to="/eval" class="try-link">{{ t("landing.action.eval") }} →</router-link>
          </div>
        </section>

        <section class="side-block">
          <h3 class="side-h">{{ t("landing.side.metrics") }}</h3>
          <dl class="side-metrics">
            <div><dt>{{ t("landing.eval.workflows") }}</dt><dd class="mono">12</dd></div>
            <div><dt>{{ t("landing.eval.classification") }}</dt><dd class="mono">12/12</dd></div>
            <div><dt>{{ t("landing.eval.latency") }}</dt><dd class="mono">−24.1%</dd></div>
            <div><dt>{{ t("landing.eval.tokens") }}</dt><dd class="mono">−1578</dd></div>
          </dl>
        </section>

        <section class="side-block">
          <h3 class="side-h">{{ t("landing.prov.run") }}</h3>
          <ul class="side-list">
            <li>{{ t("landing.eval.truncationNote") }}</li>
            <li>{{ t("landing.eval.mismatches") }}</li>
            <li>{{ t("landing.eval.completion") }}</li>
            <li>{{ t("landing.eval.historical") }}</li>
            <li>{{ t("landing.eval.current") }}</li>
          </ul>
        </section>

        <section class="side-block">
          <h3 class="side-h">{{ t("landing.prov.limits") }}</h3>
          <ul class="side-list">
            <li>{{ t("landing.eval.limits") }}</li>
            <li>{{ t("landing.eval.retrieval") }}</li>
            <li>{{ t("landing.eval.citation") }}</li>
            <li>{{ t("landing.eval.routingPolicy") }}</li>
            <li>{{ t("landing.eval.citationsSubset") }}</li>
          </ul>
        </section>

        <section class="side-block">
          <h3 class="side-h">{{ t("landing.prov.provenance") }}</h3>
          <p class="mono side-prov">{{ t("landing.eval.provenance") }}</p>
        </section>

        <section class="side-block related-side">
          <div class="related-badge">{{ t("landing.prov.related") }}</div>
          <h3 class="related-title">SecureDoc-AI</h3>
          <p class="related-desc">{{ t("landing.portfolio.body") }}</p>
          <div class="stack-chips">
            <span class="chip">FastAPI</span>
            <span class="chip">Vue 3</span>
            <span class="chip">SQLAlchemy</span>
            <span class="chip">RAG</span>
            <span class="chip">Spring Boot</span>
          </div>
          <div class="related-links">
            <a href="https://github.com/siliconsagenerd/securedoc-ai" target="_blank" rel="noopener" class="related-link">{{ t("landing.eval.github") }}: securedoc-ai ↗</a>
            <a href="https://github.com/siliconsagenerd/prozesspilot" target="_blank" rel="noopener" class="related-link">{{ t("landing.eval.github") }}: prozesspilot ↗</a>
          </div>
        </section>

        <section class="side-block">
          <h3 class="side-h">{{ t("landing.section.limits") }}</h3>
          <ul class="side-list">
            <li>{{ t("landing.limits.1") }}</li>
            <li>{{ t("landing.limits.2") }}</li>
            <li>{{ t("landing.limits.3") }}</li>
            <li>{{ t("landing.limits.4") }}</li>
          </ul>
        </section>
      </aside>
    </div>
  </div>
</template>


<script setup lang="ts">
import { t } from "../i18n";
</script>

<style scoped>
.doc {
  max-width: var(--maxw, 1320px);
  margin: 0 auto;
  font-size: 0.95rem;
  line-height: 1.6;
  padding: 0;
}

.doc-header {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  align-items: end;
  padding: 0 0 1.5rem;
  border-bottom: 1px solid var(--border-strong);
  margin-bottom: 2rem;
}

.doc-header > div:first-child { }

.doc-header .doc-lede { max-width: 60ch; }

@media (max-width: 720px) {
  .doc-header { grid-template-columns: 1fr; gap: 1rem; }
}

.doc-id {
  font-family: var(--font-sans);
  font-size: 0.85rem;
  color: var(--text-muted);
  letter-spacing: 0;
  margin-bottom: 1rem;
  text-transform: none;
  font-weight: 500;
}

.doc-title {
  font-family: var(--font-sans);
  font-size: 3rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text);
  margin-bottom: 1rem;
  line-height: 1.1;
}

.doc-lede {
  color: var(--text-muted);
  max-width: 62ch;
  margin-bottom: 1.25rem;
}

.doc-actions {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
  margin-top: 0.5rem;
}

.doc-action {
  color: var(--text);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  border-bottom: 1px solid var(--border-strong);
  padding-bottom: 1px;
  transition: var(--transition);
}

.doc-action:hover {
  border-bottom-color: var(--text);
  background: var(--bg-deep);
}

.rule {
  border: none;
  border-top: 1px solid var(--border);
  margin: 2rem 0;
}

.doc-section {
  margin: 0;
}

.section-h {
  font-family: var(--font-sans);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 0.75rem;
  letter-spacing: -0.01em;
}

.doc-section p {
  margin-bottom: 0.75rem;
  color: var(--text);
}

.muted {
  color: var(--text-muted);
  font-size: 0.88rem;
}

.steps {
  list-style: none;
  padding: 0;
  margin: 1rem 0 1.5rem;
  counter-reset: step;
}

.steps li {
  display: flex;
  gap: 0.9rem;
  padding: 0.55rem 0;
  border-bottom: 1px solid var(--border);
  align-items: baseline;
}

.steps li:last-child { border-bottom: none; }

.step-n {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--text-subtle);
  min-width: 18px;
}

.steps strong {
  font-weight: 600;
}

.trace {
  border: 1px solid var(--border-strong);
  padding: 1.25rem;
  margin-top: 1.25rem;
  background: var(--bg);
}

.trace-row {
  padding: 0.6rem 0;
  border-bottom: 1px solid var(--border);
}

.trace-row:last-child { border-bottom: none; }

.trace-label {
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 0.35rem;
  text-transform: none;
  letter-spacing: 0;
}

.trace blockquote {
  font-size: 0.92rem;
  color: var(--text);
  margin: 0;
  font-style: italic;
  border: none;
}

.trace-meta {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--text-muted);
}

.trace p {
  font-size: 0.92rem;
  color: var(--text);
  margin: 0 0 0.5rem;
}

.cites {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-top: 0.5rem;
}

.cite {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text);
  border: 1px solid var(--border);
  padding: 0.1rem 0.45rem;
}

.deflist {
  margin: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0 2rem;
}

.eval-section {
  background: var(--bg-deep);
  padding: 1.5rem;
  border-radius: 8px;
  margin: 0 -1.5rem;
}

.kpi-strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  padding: 1.25rem 0;
  border-bottom: 1px solid var(--border);
  margin-bottom: 2rem;
}

.kpi {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.kpi-label {
  font-family: var(--font-sans);
  font-size: 0.85rem;
  color: var(--text-muted);
  text-transform: none;
  letter-spacing: 0;
}

.kpi-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.02em;
}

.related-section {
  margin: 0;
}

.related-card {
  background: var(--bg-deep);
  padding: 2rem;
  position: relative;
}

.related-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 3px;
  height: 100%;
  background: var(--text);
}

.related-badge {
  font-family: var(--font-sans);
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-muted);
  padding-top: 0.25rem;
}

.related-body { min-width: 0; }

.related-title {
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 0.5rem;
  color: var(--text);
}

.related-desc {
  color: var(--text-muted);
  font-size: 0.92rem;
  line-height: 1.6;
  max-width: 90ch;
  margin: 0 0 1rem;
}

.stack-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1rem;
}

.chip {
  font-family: var(--font-sans);
  font-size: 0.78rem;
  padding: 0.15rem 0.5rem;
  border: 1px solid var(--border);
  background: var(--bg-deep);
  color: var(--text);
  border-radius: 0;
}

.related-links {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.related-link {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--text);
  text-decoration: none;
  border-bottom: 1px solid var(--border-strong);
  padding-bottom: 1px;
  transition: var(--transition);
}

.related-link:hover {
  border-bottom-color: var(--text);
  background: var(--bg-deep);
}

@media (max-width: 720px) {
  .related-card { grid-template-columns: 1fr; }
  .related-badge { writing-mode: horizontal-tb; transform: none; }
}

.def {
  padding: 0.6rem 0;
  border-bottom: 1px solid var(--border);
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 1rem;
  align-items: baseline;
}

.def:last-child { border-bottom: none; }

.def dt {
  font-weight: 600;
  color: var(--text);
  font-size: 0.9rem;
}

.def dd {
  color: var(--text-muted);
  font-size: 0.9rem;
  margin: 0;
}

.table-wrap {
  border: 1px solid var(--border);
  margin-top: 0.75rem;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 0.6rem 0.75rem;
  text-align: left;
  border-bottom: 1px solid var(--border);
  font-size: 0.85rem;
}

th {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-subtle);
  font-weight: 600;
  background: var(--bg-deep);
}

tbody tr:last-child td { border-bottom: none; }
tbody tr:hover { background: var(--bg-deep); }
td { color: var(--text); }
td.mono { font-family: var(--font-mono); }

.highlight-row td { background: var(--bg-deep); font-weight: 600; }

.limits {
  list-style: none;
  padding: 0;
  margin: 0;
}

.limits li {
  padding: 0.45rem 0;
  border-bottom: 1px solid var(--border);
  color: var(--text-muted);
  font-size: 0.9rem;
  padding-left: 1rem;
  position: relative;
}

.limits li::before {
  content: "-";
  position: absolute;
  left: 0;
  color: var(--text-subtle);
}

.limits li:last-child { border-bottom: none; }

.prov {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 1.25rem;
}

.prov-group {
  padding: 0;
  border: none;
  background: transparent;
  border-radius: 0;
}

.prov-h {
  font-family: var(--font-sans);
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: var(--text);
  margin: 0 0 0.5rem;
  text-transform: none;
}

.prov-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.prov-list li {
  padding: 0.4rem 0;
  border-bottom: 1px solid var(--border);
  color: var(--text-muted);
  font-size: 0.85rem;
  line-height: 1.5;
}

.prov-list li:last-child { border-bottom: none; }

.prov-list li.mono { font-family: var(--font-mono); font-size: 0.78rem; word-break: break-all; }

.prov-list a { color: var(--accent); text-decoration: none; border-bottom: 1px solid transparent; }
.prov-list a:hover { border-bottom-color: var(--accent); }

.doc-section > p,
.doc-section > ol,
.doc-section > figure,
.doc-section > dl,
.doc-section > ul.limits {
  max-width: 90ch;
}

.cap-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  max-width: 100%;
}

.layout {
  display: grid;
  grid-template-columns: 1fr 360px;
  gap: 2rem;
  align-items: start;
  margin-top: 0;
}

.main { min-width: 0; }

.side {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  position: sticky;
  top: 1.5rem;
}

.side-block { padding: 0; }

.side-h {
  font-family: var(--font-sans);
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text);
  margin: 0 0 0.5rem;
  letter-spacing: -0.01em;
}

.side-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.side-list li {
  font-size: 0.85rem;
  color: var(--text-muted);
  line-height: 1.5;
}

.side-prov {
  font-size: 0.78rem;
  color: var(--text-muted);
  word-break: break-all;
  margin: 0;
}

.try-links {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.try-link {
  font-size: 0.85rem;
  color: var(--text);
  text-decoration: none;
  padding: 0.35rem 0.5rem;
  background: var(--bg);
  border: 1px solid var(--border);
  transition: var(--transition);
}

.try-link:hover {
  background: var(--bg-deep);
  border-color: var(--border-strong);
}

.side-metrics {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem 1rem;
  margin: 0;
}

.side-metrics div {
  display: flex;
  flex-direction: column;
  gap: 0.1rem;
}

.side-metrics dt {
  font-size: 0.75rem;
  color: var(--text-muted);
}

.side-metrics dd {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text);
  margin: 0;
}

.related-side {
  background: var(--bg-deep);
  padding: 1.25rem;
  border-left: 3px solid var(--text);
}

@media (max-width: 960px) {
  .layout { grid-template-columns: 1fr; }
  .side { position: static; }
}

@media (max-width: 720px) {
  .kpi-strip { grid-template-columns: repeat(2, 1fr); }
  .prov { grid-template-columns: 1fr; }
  .deflist { grid-template-columns: 1fr; gap: 0; }
  .doc { padding: 0 0.75rem; }
  .eval-section { margin: 0; }
  .related-card { grid-template-columns: 1fr; }
  .related-badge { writing-mode: horizontal-tb; transform: none; }
  .cap-grid { grid-template-columns: 1fr; }
}
</style>
