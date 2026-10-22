<template>
  <section>
    <div class="card compose">
      <h2>{{ t('inbox.title') }}</h2>
      <textarea v-model="body" :placeholder="t('inbox.bodyPlaceholder')" rows="4"></textarea>
      <input v-model="email" :placeholder="t('inbox.emailPlaceholder')" />
      <div class="actions">
        <button @click="submit" :disabled="loading || !body.trim()" :aria-busy="loading">
          <span v-if="loading" class="spinner"></span>
          {{ loading ? t('inbox.submitting') : t('inbox.submit') }}
        </button>
        <p v-if="error" class="error" role="alert">{{ error }}</p>
      </div>
    </div>

    <h2 style="margin-top:2rem">{{ t('inbox.listTitle') }}</h2>
    <div v-if="loadingList" class="skeleton">{{ t('inbox.loading') }}</div>
    <div v-else-if="!inquiries.length" class="empty">{{ t('inbox.empty') }}</div>
    <div v-else class="list">
      <div v-for="i in inquiries" :key="i.id" class="row">
        <span class="badge" :class="statusClass(i.status)">{{ i.status }}</span>
        <span class="preview">{{ i.body }}</span>
        <router-link v-if="i.run_id" :to="`/runs/${i.run_id}`" class="open">{{ t("inbox.open") }}</router-link>
      </div>
    </div>
  </section>
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
  .card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem; box-shadow: var(--shadow); }
  .compose h2 { margin-bottom: .75rem; }
  textarea { width: 100%; resize: vertical; min-height: 96px; }
  input { width: 100%; margin: .6rem 0 .8rem; }
  .actions { display: flex; align-items: center; gap: .75rem; flex-wrap: wrap; }
  .error { color: #d70015; margin: 0; font-size: .85rem; }
  .spinner {
    display: inline-block; width: 14px; height: 14px; margin-right: .4rem;
    border: 2px solid rgba(255,255,255,.4); border-top-color: #fff;
    border-radius: 50%; animation: spin .7s linear infinite; vertical-align: middle;
  }
  @keyframes spin { to { transform: rotate(360deg); } }
  .skeleton { color: var(--text-2); padding: 1rem 0; }
  .empty { color: var(--text-2); padding: 1.5rem 0; text-align: center; }
  .list { display: flex; flex-direction: column; gap: .5rem; }
  .row {
    display: grid; grid-template-columns: auto 1fr auto; gap: .75rem; align-items: center;
    background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-sm);
    padding: .75rem 1rem; transition: transform .12s var(--ease), box-shadow .15s;
  }
  .row:hover { transform: translateY(-1px); box-shadow: var(--shadow); }
  .preview { color: var(--text); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .open { color: var(--accent); text-decoration: none; font-weight: 500; white-space: nowrap; }
  .open:hover { text-decoration: underline; }
  @media (max-width: 600px) {
    .row { grid-template-columns: 1fr; }
    .open { white-space: normal; }
  }
  .badge.ok { background: #e3f3e8; color: #1e7e34; }
  .badge.warn { background: #fff4e0; color: #9a6700; }
  .badge.bad { background: #fde2e2; color: #c00; }
</style>