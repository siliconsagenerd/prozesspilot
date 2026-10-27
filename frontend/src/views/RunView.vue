<template>

  <div class="run-view">
    <div v-if="run" class="run-body">
      <div class="page-head">
        <div>
          <div class="eyebrow">{{ t("run.trace") }}</div>
          <h2>{{ t('run.workflow') }} <span class="mono-run-id">{{ run.id }}</span></h2>
        </div>
        <span class="badge" :class="statusClass(run.state)">{{ lookup("status", run.state) }}</span>

      </div>

      <div class="metric-grid">
        <div class="metric-tile">
          <span class="tile-label">{{ t('run.classification') }}</span>
          <span class="tile-value">{{ lookup("class", run.classification) }}</span>
        </div>
        <div class="metric-tile">
          <span class="tile-label">{{ t('run.confidence') }}</span>
          <span class="tile-value">{{ run.confidence ?? "-" }}</span>
        </div>
        <div class="metric-tile">
          <span class="tile-label">{{ t('run.routing') }}</span>
          <span class="tile-value">{{ lookup("routing", run.routing_decision) }}</span>
        </div>
        <div class="metric-tile">
          <span class="tile-label">{{ t('run.cost') }}</span>
          <span class="tile-value mono">{{ run.total_cost_usd }} USD</span>
        </div>
        <div class="metric-tile">
          <span class="tile-label">{{ t('run.latency') }}</span>
          <span class="tile-value mono">{{ run.total_latency_ms }} ms</span>
        </div>
      </div>

      <div v-if="run.customer" class="panel">
        <div class="panel-head">
          <span class="panel-label">{{ t('run.customer') }}</span>
        </div>
        <div class="customer-line">
          <strong>{{ run.customer.name }}</strong>
          <span class="badge tier">{{ lookup("tier", run.customer.tier) }}</span>
          <span class="customer-email">{{ run.customer.email }}</span>
        </div>
        <div class="history"><em>{{ run.customer.history }}</em></div>
      </div>

      <div class="panel">
        <div class="panel-head">
          <span class="panel-label">{{ t('run.inquiry') }}</span>
        </div>
        <pre class="mono-block">{{ run.inquiry?.body }}</pre>
      </div>

      <h3 class="section-title">{{ t('run.steps') }}</h3>
      <div v-for="st in run.steps" :key="st.index" class="step">
        <div class="step-head">
          <span class="step-num">{{ st.index }}</span>
          <strong class="step-name">{{ st.name }}</strong>
          <span class="badge" :class="statusClass(st.status)">{{ lookup("status", st.status) }}</span>
          <span v-if="st.model_provider" class="step-model mono">{{ st.model_provider }}/{{ st.model_name }}</span>
        </div>
        <div class="step-metrics mono">{{ t('run.latencyShort') }} {{ st.latency_ms }}ms · {{ t('run.costShort') }} {{ st.cost_usd }}</div>
        <div class="kv"><span class="kv-label">{{ t('run.input') }}</span><span class="kv-value">{{ st.input_summary }}</span></div>
        <div class="kv"><span class="kv-label">{{ t('run.output') }}</span><span class="kv-value">{{ st.output_summary }}</span></div>
        <div v-if="st.citations?.length" class="kv">
          <span class="kv-label">{{ t('run.sources') }}</span>
          <span class="kv-value">
            <span v-for="c in st.citations" :key="c.id" class="cite">[{{ c.title }}]</span>
          </span>
        </div>
        <div v-if="st.error" class="error-line">{{ t("run.error") }}: {{ st.error }}</div>
      </div>

      <div v-if="run.draft" class="panel">
        <div class="panel-head">
          <span class="panel-label">{{ t('run.draft') }}</span>
        </div>
        <pre class="mono-block">{{ run.draft.original_text }}</pre>
        <div class="reasoning"><em>{{ t('run.reasoning') }}</em> {{ run.draft.reasoning }}</div>
        <div v-if="run.draft.edited_text">
          <h4 class="edited-title">{{ t('run.edited') }}</h4>
          <pre class="mono-block">{{ run.draft.edited_text }}</pre>
        </div>
      </div>

      <div v-if="run.state === 'AwaitingApproval' || run.state === 'ReadyForReview'" class="panel approval">
        <div class="panel-head">
          <span class="panel-label">{{ t('run.approval') }}</span>
        </div>
        <textarea v-model="edited" rows="6" class="compose-input"></textarea>
        <input v-model="reason" :placeholder="t('run.rejectReason')" class="compose-input" required />
        <div class="approval-actions">
          <button class="btn-approve" @click="act('approve')" :disabled="acting">{{ t('run.approve') }}</button>
          <button class="btn-edit" @click="act('edit_approve')" :disabled="acting">{{ t('run.editApprove') }}</button>
          <button class="btn-reject" @click="act('reject')" :disabled="acting || !reason.trim()">{{ t('run.reject') }}</button>
        </div>
      </div>

      <p v-if="msg" class="success" role="status">{{ msg }}</p>
      <p v-if="error" class="error" role="alert">{{ error }}</p>
    </div>

    <div v-else-if="error" class="error-state" role="alert">
      <p>{{ error }}</p>
      <router-link to="/" class="back-link">{{ t('run.back') }}</router-link>
    </div>
    <div v-else class="loading-state">{{ t('run.loading') }}</div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { API } from "../api";
import { t, lookup } from "../i18n";

const route = useRoute();
const run = ref<any>(null);
const edited = ref("");
const reason = ref("");
const msg = ref("");
const error = ref("");
const acting = ref(false);

async function load() {
  error.value = "";
  try {
    run.value = await API.getRun(route.params.id as string);
    if (run.value?.draft?.original_text) edited.value = run.value.draft.original_text;
  } catch (e: any) {
    run.value = null;
    error.value = e?.message || t("run.loadError");
  }
}

async function act(action: string) {
  if (acting.value || !run.value) return;
  acting.value = true; error.value = ""; msg.value = "";
  try {
    await API.approve(run.value.id, action, action === "edit_approve" ? edited.value : undefined, reason.value || undefined);
    msg.value = t("run.saved");
    await load();
  } catch (e: any) {
    error.value = e?.message || t("run.actionError");
  } finally {
    acting.value = false;
  }
}

function statusClass(s: string) {
  const v = (s || "").toLowerCase();
  if (v.includes("approv") || v.includes("ready") || v.includes("done") || v.includes("success")) return "ok";
  if (v.includes("reject") || v.includes("error") || v.includes("fail")) return "bad";
  if (v.includes("await") || v.includes("pend") || v.includes("running")) return "warn";
  return "";
}

onMounted(load);
</script>

<style scoped>
.run-view { display: flex; flex-direction: column; gap: 1.5rem; }

.page-head {
  display: flex; align-items: flex-end; justify-content: space-between;
  gap: 1rem; flex-wrap: wrap;
}
.eyebrow {
  font-size: .72rem; letter-spacing: .12em;
  color: var(--accent); font-weight: 700; margin-bottom: .35rem;
}
.page-head h2 { font-size: 1.6rem; font-weight: 700; color: var(--text); display: flex; align-items: center; gap: .6rem; flex-wrap: wrap; }
.mono-run-id { font-family: var(--font-mono); font-size: .85rem; color: var(--text-muted); background: var(--surface-hover); padding: .1rem .4rem; border-radius: 4px; }

.metric-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;
}
.metric-tile {
  background: var(--surface-card); border: 1px solid var(--border);
  border-radius: var(--radius-md); padding: 1rem 1.15rem;
  display: flex; flex-direction: column; gap: .3rem; transition: var(--transition);
}
.metric-tile:hover { border-color: var(--border-active); }
.tile-label {
  font-size: .68rem; letter-spacing: .08em;
  color: var(--text-muted); font-weight: 700;
}
.tile-value { font-size: 1.05rem; font-weight: 700; color: var(--text); }

.panel {
  background: var(--surface-card); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 1.5rem;
  display: flex; flex-direction: column; gap: .85rem;
}
.panel-head { display: flex; align-items: center; justify-content: space-between; }
.panel-label {
  font-size: .68rem; letter-spacing: .1em;
  color: var(--text-muted); font-weight: 700;
}

.customer-line {
  display: flex; align-items: center; gap: .7rem; flex-wrap: wrap;
  color: var(--text); font-weight: 700;
}
.customer-email { color: var(--text-muted); font-size: .85rem; font-weight: 500; }
.history { color: var(--text-muted); font-size: .85rem; }
.badge.tier { background: var(--accent-soft); color: var(--accent); }

.mono-block {
  font-family: var(--font-mono); font-size: .85rem; line-height: 1.6;
  white-space: pre-wrap; word-break: break-word; color: var(--text);
  background: var(--bg-deep); border: 1px solid var(--border);
  border-radius: var(--radius-sm); padding: 1rem; margin: 0;
}

.section-title { font-size: 1.1rem; font-weight: 700; color: var(--text); margin: 0; }

.step {
  border-left: 3px solid var(--accent);
  background: var(--surface-card); border: 1px solid var(--border);
  border-radius: var(--radius-md); padding: 1.1rem 1.25rem;
  display: flex; flex-direction: column; gap: .5rem;
}
.step-head { display: flex; align-items: center; gap: .65rem; flex-wrap: wrap; }
.step-num {
  width: 24px; height: 24px; border-radius: 50%;
  background: var(--accent-soft); color: var(--accent);
  font-size: .78rem; font-weight: 700;
  display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.step-name { color: var(--text); font-weight: 600; }
.step-model { color: var(--text-muted); font-size: .78rem; }
.step-metrics { color: var(--text-muted); font-size: .78rem; }

.kv { display: grid; grid-template-columns: 90px 1fr; gap: .75rem; font-size: .88rem; }
.kv-label { color: var(--text-muted); font-weight: 600; }
.kv-value { color: var(--text); }
.cite { color: var(--accent); margin-right: .35rem; }

.error-line { color: var(--danger); font-size: .85rem; }

.reasoning { color: var(--text-muted); font-size: .88rem; }
.edited-title { font-size: .95rem; font-weight: 700; color: var(--text); margin: 0; }

.compose-input {
  width: 100%; background: var(--bg-deep); border: 1px solid var(--border);
  border-radius: var(--radius-sm); padding: .8rem .95rem;
  color: var(--text); font-size: .88rem; font-family: var(--font-sans);
  transition: var(--transition); resize: vertical;
}
.compose-input:focus {
  outline: none; border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-soft);
}
.compose-input::placeholder { color: var(--text-subtle); }

.approval { border-color: var(--warning); }
.approval .panel-label { color: var(--warning); }
.approval-actions { display: flex; gap: .65rem; flex-wrap: wrap; }

.btn-approve, .btn-edit, .btn-reject {
  border: none; border-radius: var(--radius-md);
  padding: .6rem 1.2rem; font-size: .88rem; font-weight: 600;
  cursor: pointer; transition: var(--transition); color: var(--text);
}
.btn-approve { background: var(--success); box-shadow: none; }
.btn-approve:hover:not(:disabled) { background: var(--success); transform: translateY(-1px); }
.btn-edit { background: var(--accent); box-shadow: none; }
.btn-edit:hover:not(:disabled) { background: var(--accent-dark); transform: translateY(-1px); }
.btn-reject { background: var(--danger); box-shadow: none; }
.btn-reject:hover:not(:disabled) { background: var(--danger); transform: translateY(-1px); }
.btn-approve:disabled, .btn-edit:disabled, .btn-reject:disabled { opacity: .5; cursor: not-allowed; }

.success { color: var(--success); font-weight: 600; margin: 0; }
.error { color: var(--danger); margin: 0; }

.loading-state { color: var(--text-muted); text-align: center; padding: 3rem 0; }
.error-state { display: flex; flex-direction: column; gap: .75rem; color: var(--danger); }
.back-link {
  color: var(--accent); text-decoration: none; font-weight: 600;
  font-size: .9rem; transition: var(--transition);
}
.back-link:hover { color: var(--accent); }

.badge {
  font-size: .72rem; font-weight: 700; padding: .25rem .6rem;
  border-radius: 4px; letter-spacing: .04em;
}
.badge.ok { background: var(--success-soft); color: var(--success); }
.badge.warn { background: var(--warning-soft); color: var(--warning); }
.badge.bad { background: var(--danger-soft); color: var(--danger); }
</style>
