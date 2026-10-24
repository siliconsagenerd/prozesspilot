<template>
  <div class="inbox-view">
    <div class="page-head">
      <div>
        <div class="eyebrow">Operator Console</div>
        <h2>{{ t("inbox.title") }}</h2>
      </div>
      <span class="chip-count">{{ inquiries.length }} {{ t("inbox.entries") }}</span>
    </div>

    <div class="panel compose">
      <div class="panel-head">
        <span class="panel-label">{{ t("inbox.composeLabel") }}</span>
      </div>
      <textarea
        v-model="body"
        :placeholder="t('inbox.bodyPlaceholder')"
        rows="4"
        class="compose-input"
      ></textarea>
      <input
        v-model="email"
        :placeholder="t('inbox.emailPlaceholder')"
        class="compose-input"
      />
      <div class="compose-actions">
        <button @click="submit" :disabled="loading || !body.trim()" :aria-busy="loading" class="btn-run">
          <span v-if="loading" class="spinner"></span>
          {{ loading ? t('inbox.submitting') : t('inbox.submit') }}
        </button>
        <p v-if="error" class="error" role="alert">{{ error }}</p>
      </div>
    </div>

    <div class="list-section">
      <h3 class="list-title">{{ t('inbox.listTitle') }}</h3>
      <div v-if="loadingList" class="state muted">{{ t("inbox.loading") }}</div>
      <div v-else-if="!inquiries.length" class="empty-state">
        <p>{{ t('inbox.empty') }}</p>
      </div>
      <div v-else class="inbox-list">
        <div v-for="i in inquiries" :key="i.id" class="inbox-row">
          <span class="badge" :class="statusClass(i.status)">{{ i.status }}</span>
          <span class="preview">{{ i.body }}</span>
          <router-link v-if="i.run_id" :to="`/runs/${i.run_id}`" class="open-link">
            {{ t("inbox.open") }} →
          </router-link>
          <span v-else class="no-run">-</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { API } from "../api";
import { t } from "../i18n";

const body = ref("");
const email = ref("");
const loading = ref(false);
const loadingList = ref(false);
const error = ref("");
const inquiries = ref<any[]>([]);

function statusClass(s: string) {
  const v = (s || "").toLowerCase();
  if (v.includes("approv") || v.includes("ready") || v.includes("done")) return "ok";
  if (v.includes("reject") || v.includes("error") || v.includes("fail")) return "bad";
  if (v.includes("await") || v.includes("pend")) return "warn";
  return "";
}

async function load() {
  loadingList.value = true;
  try { inquiries.value = await API.listInquiries(); }
  catch (e: any) { error.value = e.message; }
  finally { loadingList.value = false; }
}

async function submit() {
  if (!body.value.trim() || loading.value) return;
  loading.value = true; error.value = "";
  try {
    const r = await API.createInquiry(body.value, "", email.value || null);
    await API.run(r.id);
    body.value = ""; email.value = "";
    await load();
  } catch (e: any) { error.value = e.message; }
  finally { loading.value = false; }
}

onMounted(load);
</script>

<style scoped>
.inbox-view { display: flex; flex-direction: column; gap: 1.5rem; }

.page-head {
  display: flex; align-items: flex-end; justify-content: space-between;
  gap: 1rem; flex-wrap: wrap;
}
.eyebrow {
  font-size: .72rem; letter-spacing: .12em;
  color: var(--accent); font-weight: 700; margin-bottom: .35rem;
}
.page-head h2 { font-size: 1.6rem; font-weight: 700; color: var(--text); }

.chip-count {
  background: var(--surface-hover); border: 1px solid var(--border);
  color: var(--text-muted); font-size: .8rem; font-weight: 600;
  padding: .3rem .8rem; border-radius: 0;
}

.panel {
  background: var(--surface-card); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 1.5rem;
  display: flex; flex-direction: column; gap: 1rem;
}
.panel-label {
  font-size: .7rem; letter-spacing: .1em;
  color: var(--text-muted); font-weight: 700;
}
.panel-head { display: flex; align-items: center; justify-content: space-between; }

.compose-input {
  width: 100%; background: var(--bg-deep); border: 1px solid var(--border);
  border-radius: var(--radius-sm); padding: .85rem 1rem;
  color: var(--text); font-size: .9rem; font-family: var(--font-sans);
  transition: var(--transition); resize: vertical; min-height: 96px;
}
.compose-input:focus {
  outline: none; border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-soft);
}
.compose-input::placeholder { color: var(--text-subtle); }

.compose-actions { display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; }

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

.error { color: var(--danger); margin: 0; font-size: .85rem; }

.state { padding: 1.25rem; border-radius: var(--radius-md); color: var(--text-muted); background: var(--surface-card); border: 1px solid var(--border); }

.list-title { font-size: 1.1rem; font-weight: 700; color: var(--text); margin: 0; }

.empty-state {
  text-align: center; padding: 3rem 1.5rem; color: var(--text-muted);
  background: var(--surface-card); border: 1px dashed var(--border); border-radius: var(--radius-lg);
}
.empty-icon { font-size: 2.5rem; margin-bottom: .75rem; }

.inbox-list { display: flex; flex-direction: column; gap: .5rem; }
.inbox-row {
  display: grid; grid-template-columns: auto 1fr auto; gap: .9rem; align-items: center;
  background: var(--surface-card); border: 1px solid var(--border);
  border-radius: var(--radius-md); padding: .85rem 1.1rem;
  transition: var(--transition);
}
.inbox-row:hover { border-color: var(--border-active); background: var(--surface-hover); }
.preview { color: var(--text); font-size: .9rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.no-run { color: var(--text-subtle); }

.badge {
  font-size: .72rem; font-weight: 700; padding: .2rem .55rem;
  border-radius: 4px; letter-spacing: .04em;
  white-space: nowrap;
}
.badge.ok { background: var(--success-soft); color: var(--success); }
.badge.warn { background: var(--warning-soft); color: var(--warning); }
.badge.bad { background: var(--danger-soft); color: var(--danger); }

.open-link {
  color: var(--accent); text-decoration: none; font-weight: 600;
  font-size: .85rem; white-space: nowrap; transition: var(--transition);
}
.open-link:hover { color: var(--accent); }

@media (max-width: 600px) {
  .inbox-row { grid-template-columns: 1fr; gap: .4rem; }
}
</style>
