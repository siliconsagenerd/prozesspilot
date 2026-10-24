<template>
  <section class="demo">
    <div class="title-row">
      <h2>{{ t("demo.title") }}</h2>
      <span class="badge recorded">{{ t("demo.label") }}</span>
    </div>

    <p v-if="loading" class="muted">{{ t("demo.loading") }}</p>
    <p v-else-if="error" class="error">{{ error }}</p>

    <template v-else-if="data">
      <div class="card">
        <div class="card-head">{{ t("demo.inquiry") }}</div>
        <h3>{{ data.inquiry?.subject }}</h3>
        <pre>{{ data.inquiry?.body }}</pre>
      </div>

      <div class="meta">
        <div class="meta-item"><span class="label">{{ t("demo.classification") }}</span><span>{{ data.classification }}</span></div>
        <div class="meta-item"><span class="label">{{ t("run.confidence") }}</span><span>{{ data.classification_confidence }}</span></div>
        <div class="meta-item"><span class="label">{{ t("demo.approvalState") }}</span><span>{{ data.state }} ({{ data.routing_decision }})</span></div>
      </div>

      <p class="policy-note">{{ t("demo.policyNote") }}</p>
      <div class="card">
        <div class="card-head">{{ t("demo.draft") }}</div>
        <pre>{{ data.draft }}</pre>
      </div>

      <div class="sources">
        <div class="card">
          <div class="card-head">{{ t("demo.retrieved") }}</div>
          <ul>
            <li v-for="(s, i) in data.retrieved_sources" :key="i">{{ s.title }} <span class="mono">{{ s.source_key }}</span></li>
          </ul>
        </div>
        <div class="card">
          <div class="card-head">{{ t("demo.cited") }}</div>
          <ul>
            <li v-for="(s, i) in data.cited_sources" :key="i">{{ s.title }} <span class="mono">{{ s.source_key }}</span></li>
          </ul>
        </div>
      </div>

      <p class="restriction">{{ t("demo.noSending") }}</p>
      <router-link to="/" class="link">{{ t("demo.back") }}</router-link>
    </template>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { t } from "../i18n";
import { API } from "../api";

const data = ref<any>(null);
const error = ref("");
const loading = ref(true);

onMounted(async () => {
  try {
    data.value = await API.getDemoSnapshot();
  } catch (e) {
    error.value = t("demo.error");
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.demo { display: grid; gap: 1rem; }
.title-row { display: flex; align-items: center; gap: .75rem; flex-wrap: wrap; }
.badge.recorded { background: rgba(0,113,227,.12); color: #0071e3; }
.muted { color: var(--text-2); }
.error { color: #b00020; }
.sources { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; }
ul { margin: 0; padding-left: 1.25rem; }
.mono { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .85em; color: var(--text-2); }
.restriction { font-weight: 600; }
.link { color: var(--accent); text-decoration: none; font-weight: 600; }
</style>
