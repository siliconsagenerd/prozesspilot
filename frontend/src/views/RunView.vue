<template>
  <section v-if="run">
    <div class="title-row">
      <h2>{{ t('run.workflow') }} <span class="mono">{{ run.id }}</span></h2>
      <span class="badge" :class="statusClass(run.state)">{{ run.state }}</span>
    </div>

    <div class="meta">
      <div class="meta-item"><span class="label">{{ t('run.classification') }}</span><span>{{ run.classification || "—" }}</span></div>
      <div class="meta-item"><span class="label">{{ t('run.confidence') }}</span><span>{{ run.confidence ?? "—" }}</span></div>
      <div class="meta-item"><span class="label">{{ t('run.routing') }}</span><span>{{ run.routing_decision || "—" }}</span></div>
      <div class="meta-item"><span class="label">{{ t('run.cost') }}</span><span class="mono">{{ run.total_cost_usd }} USD</span></div>
      <div class="meta-item"><span class="label">{{ t('run.latency') }}</span><span class="mono">{{ run.total_latency_ms }} ms</span></div>
    </div>

    <div v-if="run.customer" class="card">
      <div class="card-head">{{ t('run.customer') }}</div>
      <div><strong>{{ run.customer.name }}</strong> <span class="badge tier">{{ run.customer.tier }}</span></div>
      <div class="sub">{{ run.customer.email }}</div>
      <div class="history"><em>{{ run.customer.history }}</em></div>
    </div>

    <div class="card">
      <div class="card-head">{{ t('run.inquiry') }}</div>
      <pre>{{ run.inquiry?.body }}</pre>
    </div>

    <h3>{{ t('run.steps') }}</h3>
    <div v-for="st in run.steps" :key="st.index" class="step">
      <div class="step-head">
        <span class="step-num">{{ st.index }}</span>
        <strong>{{ st.name }}</strong>
        <span class="badge" :class="statusClass(st.status)">{{ st.status }}</span>
        <span v-if="st.model_provider" class="mono model">{{ st.model_provider }}/{{ st.model_name }}</span>
      </div>
      <div class="step-metrics mono">{{ t('run.latencyShort') }} {{ st.latency_ms }}ms · {{ t('run.costShort') }} {{ st.cost_usd }}</div>
      <div class="kv"><span class="label">{{ t('run.input') }}</span><span>{{ st.input_summary }}</span></div>
      <div class="kv"><span class="label">{{ t('run.output') }}</span><span>{{ st.output_summary }}</span></div>
      <div v-if="st.citations?.length" class="kv">
        <span class="label">{{ t('run.sources') }}</span>
        <span><span v-for="c in st.citations" :key="c.id" class="cite">[{{ c.title }}]</span></span>
      </div>
      <div v-if="st.error" class="error">Fehler: {{ st.error }}</div>
    </div>

    <div v-if="run.draft" class="card">
      <div class="card-head">{{ t('run.draft') }}</div>
      <pre>{{ run.draft.original_text }}</pre>
      <div class="reasoning"><em>{{ t('run.reasoning') }}</em> {{ run.draft.reasoning }}</div>
      <div v-if="run.draft.edited_text">
        <h4>{{ t('run.edited') }}</h4>
        <pre>{{ run.draft.edited_text }}</pre>
      </div>
    </div>

    <div v-if="run.state === 'AwaitingApproval' || run.state === 'ReadyForReview'" class="card approval">
      <div class="card-head">{{ t('run.approval') }}</div>
      <textarea v-model="edited" rows="6"></textarea>
      <input v-model="reason" :placeholder="t('run.rejectReason')" />
      <div class="actions">
        <button @click="act('approve')" :disabled="acting">{{ t('run.approve') }}</button>
        <button class="secondary" @click="act('edit_approve')" :disabled="acting">{{ t('run.editApprove') }}</button>
        <button class="danger" @click="act('reject')" :disabled="acting">{{ t('run.reject') }}</button>
      </div>
    </div>

    <p v-if="msg" class="success" role="status">{{ msg }}</p>
    <p v-if="error" class="error" role="alert">{{ error }}</p>
  </section>
  <div v-else-if="error" class="error" role="alert" style="padding:1rem 0">
    {{ error }} <router-link to="/">{{ t('run.back') }}</router-link>
  </div>
  <div v-else class="loading">{{ t('run.loading') }}</div>
</template>
<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { API } from "../api";
import { t } from "../i18n";

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
  .title-row { display: flex; align-items: center; gap: .75rem; flex-wrap: wrap; margin-bottom: .5rem; }
  .meta {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: .5rem; margin: 1rem 0 1.25rem;
  }
  .meta-item {
    background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-sm);
    padding: .6rem .85rem; display: flex; flex-direction: column; gap: .15rem;
  }
  .label { font-size: .72rem; color: var(--text-2); text-transform: uppercase; letter-spacing: .06em; font-weight: 600; }
  .card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem; margin: 1rem 0; box-shadow: var(--shadow); }
  .card-head { font-size: .72rem; color: var(--text-2); text-transform: uppercase; letter-spacing: .06em; font-weight: 600; margin-bottom: .5rem; }
  .sub { color: var(--text-2); font-size: .85rem; }
  .history { margin-top: .4rem; color: var(--text-2); font-size: .85rem; }
  .tier { background: #e8e8ed; }
  .step {
    border-left: 3px solid var(--accent); padding: .85rem 1rem; margin: .6rem 0;
    background: var(--surface); border-radius: var(--radius-sm); border: 1px solid var(--border);
    border-left: 3px solid var(--accent); box-shadow: 0 1px 2px rgba(0,0,0,.03);
  }
  .step-head { display: flex; align-items: center; gap: .5rem; flex-wrap: wrap; }
  .step-num {
    width: 22px; height: 22px; border-radius: 50%; background: var(--accent-soft);
    color: var(--accent); font-size: .75rem; font-weight: 700;
    display: inline-flex; align-items: center; justify-content: center;
  }
  .model { color: var(--text-2); }
  .step-metrics { color: var(--text-2); font-size: .8rem; margin: .35rem 0; }
  .kv { display: grid; grid-template-columns: 72px 1fr; gap: .5rem; margin: .25rem 0; font-size: .9rem; }
  .kv .label { text-transform: none; letter-spacing: 0; font-size: .8rem; }
  .cite { color: var(--accent); margin-right: .35rem; }
  .reasoning { margin-top: .75rem; color: var(--text-2); font-size: .9rem; }
  .approval textarea { width: 100%; min-height: 120px; resize: vertical; }
  .approval input { width: 100%; margin: .6rem 0 .8rem; }
  .actions { display: flex; gap: .5rem; flex-wrap: wrap; margin-top: .5rem; }
  .secondary { background: #e8e8ed; color: var(--text); }
  .secondary:hover:not(:disabled) { box-shadow: 0 4px 12px rgba(0,0,0,.08); }
  .danger { background: #d70015; }
  .danger:hover:not(:disabled) { box-shadow: 0 4px 12px rgba(215,0,21,.3); }
  pre { white-space: pre-wrap; word-break: break-word; background: var(--surface-2); padding: .75rem; border-radius: var(--radius-sm); margin: .5rem 0 0; border: 1px solid var(--border); }
  .success { color: #1e7e34; font-weight: 500; }
  .error { color: #d70015; }
  .loading { color: var(--text-2); padding: 2rem 0; text-align: center; }
  .badge.ok { background: #e3f3e8; color: #1e7e34; }
  .badge.warn { background: #fff4e0; color: #9a6700; }
  .badge.bad { background: #fde2e2; color: #c00; }
</style>