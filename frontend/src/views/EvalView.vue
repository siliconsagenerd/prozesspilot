<template>
  <section>
    <div class="title-row">
      <h2>{{ t('eval.title') }}</h2>
      <button @click="runEval" :disabled="loading" :aria-busy="loading">
        <span v-if="loading" class="spinner"></span>
        {{ loading ? t('eval.running') : t('eval.run') }}
      </button>
    </div>
    <p v-if="error" class="error" role="alert">{{ error }}</p>

    <div v-if="agg" class="card">
      <div class="metrics">
        <div class="metric"><span class="label">{{ t('eval.n') }}</span><span>{{ agg.n }}</span></div>
        <div class="metric"><span class="label">{{ t('eval.provider') }}</span><span>{{ agg.provider }}</span></div>
        <div class="metric"><span class="label">{{ t('eval.classification') }}</span><span>{{ pct(agg.classification_accuracy) }}</span></div>
        <div class="metric"><span class="label">{{ t('eval.routing') }}</span><span>{{ pct(agg.routing_accuracy) }}</span></div>
        <div class="metric"><span class="label">{{ t('eval.citations') }}</span><span>{{ pct(agg.citation_rate) }}</span></div>
        <div class="metric"><span class="label">{{ t('eval.latency') }}</span><span class="mono">{{ agg.avg_latency_ms }} ms</span></div>
        <div class="metric"><span class="label">{{ t('eval.cost') }}</span><span class="mono">{{ agg.total_cost_usd }} USD</span></div>
      </div>
    </div>

    <div v-if="agg" class="table-wrap">
      <table>
        <thead><tr><th>{{ t('eval.case') }}</th><th>{{ t('eval.pred') }}</th><th>{{ t('eval.exp') }}</th><th>{{ t('eval.ok') }}</th><th>{{ t('eval.routingOk') }}</th><th>{{ t('eval.quotes') }}</th></tr></thead>
        <tbody>
          <tr v-for="r in agg.results" :key="r.case_id">
            <td class="mono">{{ r.case_id }}</td>
            <td>{{ r.predicted }}</td>
            <td>{{ r.expected }}</td>
            <td :class="r.classification_correct ? 'ok' : 'bad'">{{ r.classification_correct ? "✓" : "✗" }}</td>
            <td :class="r.routing_correct ? 'ok' : 'bad'">{{ r.routing_correct ? "✓" : "✗" }}</td>
            <td :class="r.citations_present ? 'ok' : 'bad'">{{ r.citations_present ? "✓" : "✗" }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>
<script setup lang="ts">
import { ref } from "vue";
import { API } from "../api";
import { t } from "../i18n";

const loading = ref(false);
const agg = ref<any>(null);
const error = ref("");

async function runEval() {
  if (loading.value) return;
  loading.value = true; error.value = "";
  try { agg.value = await API.evalRun("improved"); }
  catch (e: any) { error.value = e?.message || "Evaluation fehlgeschlagen."; }
  finally { loading.value = false; }
}

function pct(v: any) {
  if (v == null) return "—";
  const n = Number(v);
  return isNaN(n) ? v : (n <= 1 ? (n * 100).toFixed(1) + "%" : n + "%");
}
</script>
<style scoped>
  .title-row { display: flex; align-items: center; justify-content: space-between; gap: .75rem; flex-wrap: wrap; margin-bottom: .5rem; }
  .card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem; margin: 1rem 0; box-shadow: var(--shadow); }
  .metrics { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: .6rem; }
  .metric {
    background: var(--surface-2); border: 1px solid var(--border); border-radius: var(--radius-sm);
    padding: .6rem .8rem; display: flex; flex-direction: column; gap: .15rem;
  }
  .label { font-size: .72rem; color: var(--text-2); text-transform: uppercase; letter-spacing: .06em; font-weight: 600; }
  .table-wrap { overflow-x: auto; background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow); }
  table { width: 100%; border-collapse: collapse; }
  th, td { padding: .6rem .75rem; text-align: left; border-bottom: 1px solid var(--border); font-size: .88rem; }
  th { font-size: .72rem; color: var(--text-2); text-transform: uppercase; letter-spacing: .06em; background: var(--surface-2); }
  tr:last-child td { border-bottom: none; }
  td.ok { color: #1e7e34; font-weight: 600; }
  td.bad { color: #d70015; font-weight: 600; }
  .spinner {
    display: inline-block; width: 14px; height: 14px; margin-right: .4rem;
    border: 2px solid rgba(255,255,255,.4); border-top-color: #fff;
    border-radius: 50%; animation: spin .7s linear infinite; vertical-align: middle;
  }
  @keyframes spin { to { transform: rotate(360deg); } }
</style>