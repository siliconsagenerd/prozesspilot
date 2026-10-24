<template>
  <section class="landing">
    <div class="hero">
      <h2>{{ t("landing.title") }}</h2>
      <p class="subtitle">{{ t("landing.subtitle") }}</p>
      <p>{{ t("landing.what") }}</p>
      <p class="public-note">{{ t("landing.public") }}</p>
    </div>
    <div class="cards">
      <article class="card">
        <h3>{{ t("nav.demo") }}</h3>
        <p>{{ t("landing.public") }}</p>
        <router-link to="/demo" class="link">{{ t("nav.demo") }} →</router-link>
      </article>
      <article class="card">
        <h3>{{ t("nav.operator") }}</h3>
        <p>{{ t("landing.operator") }}</p>
        <router-link to="/app" class="link">{{ t("nav.operator") }} →</router-link>
      </article>
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
      </ul>
      <p class="muted">{{ t("landing.eval.provenance") }}</p>
      <p class="muted">{{ t("landing.eval.historical") }}</p>
      <p class="muted">{{ t("landing.eval.current") }}</p>
    </section>

    <section class="portfolio">
      <h3>{{ t("landing.portfolio.title") }}</h3>
      <p>{{ t("landing.portfolio.body") }}</p>
      <a class="github" href="https://github.com/siliconsagenerd/securedoc-ai" target="_blank" rel="noopener noreferrer">
        {{ t("landing.portfolio.link") }}
      </a>
      <p class="muted">{{ t("landing.stack") }}</p>
    </section>

    <a class="github" href="https://github.com/siliconsagenerd/prozesspilot" target="_blank" rel="noopener noreferrer">
      {{ t("landing.github") }}
    </a>
  </section>
</template>
<script setup lang="ts">
import { t } from "../i18n";
</script>
<style scoped>
.landing { display: grid; gap: 1.5rem; }
.hero { display: grid; gap: .5rem; }
.subtitle { color: var(--text-2); }
.public-note { font-weight: 600; }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; }
.card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1rem; }
.link { color: var(--accent); text-decoration: none; font-weight: 600; }
.github { color: var(--accent); text-decoration: none; font-weight: 600; width: fit-content; }
.eval-summary, .portfolio { display: grid; gap: .5rem; }
.eval-summary table { width: 100%; border-collapse: collapse; background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; }
.eval-summary th, .eval-summary td { padding: .5rem .75rem; border-bottom: 1px solid var(--border); text-align: left; }
.eval-summary th { background: var(--surface-2); }
.notes { margin: 0; padding-left: 1.25rem; }
.muted { color: var(--text-2); font-size: .9rem; }
</style>
