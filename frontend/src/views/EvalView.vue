<template>
  <div class="eval-view">
    <div class="page-head">
      <div>
        <h2>{{ t('eval.title') }}</h2>
      </div>
      <button @click="runEval" :disabled="loading" :aria-busy="loading" class="btn-run">
        <span v-if="loading" class="spinner"></span>
        {{ loading ? t('eval.running') : t('eval.run') }}
      </button>
    </div>

    <p v-if="error" class="error" role="alert">{{ error }}</p>

    <template v-if="agg">
      <div class="metric-grid">
        <div class="metric-tile">
          <span class="tile-label">{{ t('eval.n') }}</span>
          <span class="tile-value mono">{{ agg.n }}</span>
        </div>
        <div class="metric-tile">
          <span class="tile-label">{{ t('eval.provider') }}</span>
          <span class="tile-value">{{ agg.provider }}</span>
        </div>
        <div class="metric-tile accent">
          <span class="tile-label">{{ t('eval.classification') }}</span>
          <span class="tile-value mono">{{ pct(agg.classification_accuracy) }}</span>
        </div>
        <div class="metric-tile accent">
          <span class="tile-label">{{ t('eval.routing') }}</span>
          <span class="tile-value mono">{{ pct(agg.routing_accuracy) }}</span>
        </div>
        <div class="metric-tile accent">
          <span class="tile-label">{{ t('eval.citations') }}</span>
          <span class="tile-value mono">{{ pct(agg.citation_rate) }}</span>
        </div>
        <div class="metric-tile">
          <span class="tile-label">{{ t('eval.latency') }}</span>
          <span class="tile-value mono">{{ agg.avg_latency_ms }} ms</span>
        </div>
        <div class="metric-tile">
          <span class="tile-label">{{ t('eval.cost') }}</span>
          <span class="tile-value mono">{{ agg.total_cost_usd }} USD</span>
        </div>
      </div>

      <div class="table-wrap">
        <div class="table-head">
          <span class="panel-label">{{ t("eval.perCase") }}</span>
          <span class="count-badge">{{ agg.results?.length ?? 0 }}</span>
        </div>
        <table>
          <thead>
            <tr>
              <th>{{ t('eval.case') }}</th>
              <th>{{ t('eval.pred') }}</th>
              <th>{{ t('eval.exp') }}</th>
              <th>{{ t('eval.ok') }}</th>
              <th>{{ t('eval.routingOk') }}</th>
              <th>{{ t('eval.quotes') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="r in agg.results" :key="r.case_id">
              <td class="mono">{{ r.case_id }}</td>
              <td>{{ r.predicted }}</td>
              <td>{{ r.expected }}</td>
              <td :class="r.classification_correct ? 'ok' : 'bad'">{{ r.classification_correct ? 'OK' : '–' }}</td>
              <td :class="r.routing_correct ? 'ok' : 'bad'">{{ r.routing_correct ? 'OK' : '–' }}</td>
              <td :class="r.citations_present ? 'ok' : 'bad'">{{ r.citations_present ? 'OK' : '–' }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </template>

    <div v-else-if="!loading" class="empty-state">
      <p>{{ t("eval.empty") }}</p>
    </div>
  </div>
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
  catch (e: any) { error.value = e?.message || t("eval.error"); }
  finally { loading.value = false; }
}

function pct(v: any) {
  if (v == null) return "-";
  const n = Number(v);
  return isNaN(n) ? v : (n <= 1 ? (n * 100).toFixed(1) + "%" : n + "%");
}
</script>

<style scoped>
.eval-view { display: flex; flex-direction: column; gap: 1.5rem; }

.page-head {
  display: flex; align-items: flex-end; justify-content: space-between;
  gap: 1rem; flex-wrap: wrap;
}
.eyebrow {
  font-size: .72rem; letter-spacing: .12em;
  color: var(--accent); font-weight: 700; margin-bottom: .35rem;
}
.page-head h2 { font-size: 1.6rem; font-weight: 700; color: var(--text); }

.btn-run {
  display: inline-flex; align-items: center; gap: .5rem;
  background: var(--accent); color: var(--inverse); border: none;
  border-radius: var(--radius-md); padding: .7rem 1.4rem;
  font-size: .9rem; font-weight: 600; cursor: pointer;
  box-shadow: none;
  transition: var(--transition);
}
.btn-run:hover:not(:disabled) { background: var(--accent-dark); transform: translateY(-1px); }
.btn-run:disabled { opacity: .5; cursor: not-allowed; }

.spinner {
  width: 14px; height: 14px;
  border: 2px solid var(--border-strong); border-top-color: var(--accent);
  border-radius: 50%; animation: spin .7s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

.error { color: var(--danger); margin: 0; }

.metric-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;
}
.metric-tile {
  background: var(--surface-card); border: 1px solid var(--border);
  border-radius: var(--radius-md); padding: 1rem 1.15rem;
  display: flex; flex-direction: column; gap: .3rem; transition: var(--transition);
}
.metric-tile:hover { border-color: var(--border-active); }
.metric-tile.accent { border-left: 3px solid var(--accent); }
.tile-label {
  font-size: .68rem; letter-spacing: .08em;
  color: var(--text-muted); font-weight: 700;
}
.tile-value { font-size: 1.05rem; font-weight: 700; color: var(--text); }
.mono { font-family: var(--font-mono); }

.table-wrap {
  background: var(--surface-card); border: 1px solid var(--border);
  border-radius: var(--radius-lg); overflow: hidden;
  display: flex; flex-direction: column;
}
.table-head {
  display: flex; align-items: center; justify-content: space-between;
  padding: 1rem 1.5rem; border-bottom: 1px solid var(--border);
}
.panel-label {
  font-size: .68rem; letter-spacing: .1em;
  color: var(--text-muted); font-weight: 700;
}
.count-badge {
  background: var(--bg-deep); color: var(--text-muted);
  font-size: .75rem; font-weight: 700; padding: .15rem .55rem; border-radius: 0;
}

.table-scroll { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; }
th, td {
  padding: .8rem 1rem; text-align: left;
  border-bottom: 1px solid var(--border); font-size: .88rem;
}
th {
  font-size: .7rem; color: var(--text-muted);
  letter-spacing: .08em;
  background: var(--bg-deep); font-weight: 700;
}
tbody tr { transition: var(--transition); }
tbody tr:hover { background: var(--bg-deep); }
tbody tr:last-child td { border-bottom: none; }
td { color: var(--text); }
td.ok { color: var(--success); font-weight: 700; }
td.bad { color: var(--danger); font-weight: 700; }

.empty-state {
  text-align: center; padding: 3rem 1.5rem; color: var(--text-muted);
  background: var(--surface-card); border: 1px dashed var(--border); border-radius: var(--radius-lg);
}
.empty-icon { font-size: 2.5rem; margin-bottom: .75rem; }
</style>
