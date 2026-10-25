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

    <section class="eval-summary" aria-labelledby="eval-summary-title">
      <h3 id="eval-summary-title">{{ t("landing.eval.title") }}</h3>
      <p class="muted">{{ t("landing.eval.readonly") }}</p>
      <p class="muted">{{ t("landing.eval.historicalMetrics") }}</p>
      <table>
        <thead>
          <tr>
            <th>{{ t("landing.eval.metric") }}</th>
            <th>Baseline</th>
            <th>Improved</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>{{ t("landing.eval.workflows") }}</td><td>12</td><td>12</td></tr>
          <tr><td>{{ t("landing.eval.classification") }}</td><td>12/12</td><td>12/12</td></tr>
          <tr><td>{{ t("landing.eval.routing") }}</td><td>11/12</td><td>10/12</td></tr>
          <tr><td>{{ t("landing.eval.sources") }}</td><td>9/12</td><td>9/12</td></tr>
          <tr><td>{{ t("landing.eval.truncation") }}</td><td>12/12</td><td>9/12</td></tr>
          <tr><td>{{ t("landing.eval.cost") }}</td><td>0.010177 USD</td><td>0.008665 USD</td></tr>
          <tr><td>{{ t("landing.eval.latency") }}</td><td>94603 ms</td><td>71849 ms</td></tr>
          <tr><td>{{ t("landing.eval.tokens") }}</td><td>37085</td><td>35507</td></tr>
        </tbody>
      </table>
      <p class="muted">{{ t("landing.eval.truncationNote") }}</p>
      <ul class="notes">
        <li>{{ t("landing.eval.mismatches") }}</li>
        <li>{{ t("landing.eval.completion") }}</li>
        <li>{{ t("landing.eval.limits") }}</li>
        <li>{{ t("landing.eval.retrieval") }}</li>
        <li>{{ t("landing.eval.citation") }}</li>
        <li>{{ t("landing.eval.routingPolicy") }}</li>
        <li>{{ t("landing.eval.explicitCitations") }}</li>
      </ul>
      <div class="prov-block">
        <div class="prov-block__label">Provenance</div>
        <p class="muted">{{ t("landing.eval.provenance") }}</p>
        <p class="muted prov-block__line">{{ t("landing.eval.historical") }}</p>
        <p class="muted prov-block__line">{{ t("landing.eval.current") }}</p>
      </div>
    </section>

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
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 5vw, 3.5rem);
  font-weight: 800;
  letter-spacing: -0.035em;
  color: var(--text);
  margin-bottom: 1rem;
  line-height: 1.05;
  position: relative;
  display: inline-block;
}

.doc-title::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -0.15rem;
  width: 3rem;
  height: 3px;
  background: var(--text);
  transition: width var(--transition);
}

.doc-title:hover::after { width: 100%; }

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
  padding-left: 0;
  transition: var(--transition);
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
}

.doc-action::after {
  content: "→";
  opacity: 0;
  transform: translateX(-4px);
  transition: var(--transition);
}

.doc-action:hover {
  border-bottom-color: var(--text);
  background: var(--bg-deep);
  padding-left: 0.4rem;
}

.doc-action:hover::after {
  opacity: 1;
  transform: translateX(0);
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
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 0.75rem;
  letter-spacing: -0.02em;
  padding-left: 0.85rem;
  border-left: 3px solid var(--text);
  line-height: 1.2;
  transition: padding-left var(--transition), border-color var(--transition);
}

.section-h:hover {
  padding-left: 1.1rem;
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
  padding: 0.6rem 0.5rem;
  border-bottom: 1px solid var(--border);
  align-items: baseline;
  transition: background var(--transition), padding-left var(--transition);
  border-radius: 0;
}

.steps li:hover {
  background: var(--bg-deep);
  padding-left: 0.85rem;
}

.steps li:last-child { border-bottom: none; }

.step-n {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--text);
  background: var(--bg-deep);
  min-width: 22px;
  height: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  transition: background var(--transition), color var(--transition);
}

.steps li:hover .step-n {
  background: var(--text);
  color: var(--bg);
}

.steps strong {
  font-weight: 700;
}

.eval-summary {
  background: var(--bg-deep);
  border: 1px solid var(--border);
  padding: 1.5rem 1.75rem;
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
}

.eval-summary::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: var(--text);
}

.eval-summary h3 {
  font-size: 1.1rem;
  font-weight: 800;
  letter-spacing: -0.01em;
  margin-bottom: 0.75rem;
}

.eval-summary table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.75rem 0 1rem;
  font-size: 0.85rem;
}

.eval-summary th,
.eval-summary td {
  padding: 0.5rem 0.6rem;
  border-bottom: 1px solid var(--border);
  text-align: left;
}

.eval-summary thead th {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-muted);
  border-bottom: 2px solid var(--border-strong);
  background: var(--bg);
}

.eval-summary tbody tr {
  transition: background var(--transition);
}

.eval-summary tbody tr:hover {
  background: var(--surface-hover);
}

.eval-summary tbody td.mono {
  font-family: var(--font-mono);
}

.notes {
  list-style: none;
  padding: 0;
  margin: 0.75rem 0 1rem;
  display: grid;
  gap: 0.35rem;
}

.notes li {
  font-size: 0.85rem;
  color: var(--text-muted);
  padding: 0.35rem 0 0.35rem 1.25rem;
  position: relative;
  line-height: 1.5;
  transition: color var(--transition), padding-left var(--transition);
}

.notes li::before {
  content: "—";
  position: absolute;
  left: 0;
  color: var(--text-subtle);
  transition: color var(--transition);
}

.notes li:hover {
  color: var(--text);
  padding-left: 1.5rem;
}

.notes li:hover::before {
  color: var(--text);
}

.prov-block {
  margin-top: 1rem;
  padding: 1rem 1.1rem;
  border: 1px solid var(--border);
  background: var(--bg);
  position: relative;
}

.prov-block__label {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--bg);
  background: var(--text);
  display: inline-block;
  padding: 0.1rem 0.4rem;
  margin-bottom: 0.6rem;
}

.prov-block__line {
  margin-top: 0.4rem;
  padding-top: 0.4rem;
  border-top: 1px dashed var(--border);
}

.prov-block__line:first-of-type {
  border-top: none;
  margin-top: 0;
  padding-top: 0;
}
.trace {
  border: 1px solid var(--border-strong);
  padding: 1.25rem;
  margin-top: 1.25rem;
  background: var(--bg);
  transition: border-color var(--transition);
}

.trace:hover {
  border-color: var(--text);
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
  transition: var(--transition);
  cursor: default;
}

.cite:hover {
  background: var(--text);
  color: var(--bg);
  border-color: var(--text);
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
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  font-weight: 800;
  color: var(--text);
  letter-spacing: -0.03em;
  line-height: 1;
}

.chip {
  font-family: var(--font-sans);
  font-size: 0.78rem;
  padding: 0.15rem 0.5rem;
  border: 1px solid var(--border);
  background: var(--bg-deep);
  color: var(--text);
  border-radius: 0;
  transition: var(--transition);
  cursor: default;
}

.chip:hover {
  background: var(--text);
  color: var(--bg);
  border-color: var(--text);
  transform: translateY(-1px);
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
  top: 5rem;
  animation: slideInLeft 0.6s ease-out both;
}

.side-block { padding: 0; }

.side-h {
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--text);
  margin: 0 0 0.5rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  position: relative;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid var(--border);
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

@keyframes slideInLeft {
  from { opacity: 0; transform: translateX(-24px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}


@media (max-width: 960px) {
  .layout { grid-template-columns: 1fr; }
  .side { position: static; }
}









@media (max-width: 720px) {
  .prov { grid-template-columns: 1fr; }
  .deflist { grid-template-columns: 1fr; gap: 0; }
  .doc { padding: 0 0.75rem; }
  .eval-section { margin: 0; }
  .related-card { grid-template-columns: 1fr; }
  .related-badge { writing-mode: horizontal-tb; transform: none; }
  .cap-grid { grid-template-columns: 1fr; }
}
</style>
