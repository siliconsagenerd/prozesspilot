<template>
  <div class="demo-view">
    <div class="page-head">
      <div>
        <div class="eyebrow">Recorded Snapshot</div>
        <h2>{{ t("demo.title") }}</h2>
      </div>
      <span class="chip-recorded">
        <span class="chip-dot"></span>
        {{ t("demo.label") }}
      </span>
    </div>

    <p v-if="loading" class="state muted">{{ t("demo.loadingSnapshot") }}</p>
    <p v-else-if="error" class="state error" role="alert">{{ error }}</p>

    <template v-else-if="data">
      <div class="demo-grid">
        <div class="panel panel-primary">
          <div class="panel-head">
            <span class="panel-label">{{ t("demo.inquiryLabel") }}</span>
            <span class="panel-num">01</span>
          </div>
          <h3 class="inquiry-subject">{{ data.inquiry?.subject }}</h3>
          <pre class="mono-block">{{ data.inquiry?.body }}</pre>
        </div>

        <div class="side-stack">
          <div class="metric-tile">
            <span class="tile-label">{{ t("demo.classification") }}</span>
            <span class="tile-value">{{ data.classification }}</span>
          </div>
          <div class="metric-tile">
            <span class="tile-label">{{ t("run.confidence") }}</span>
            <span class="tile-value mono">{{ data.classification_confidence }}</span>
          </div>
          <div class="metric-tile">
            <span class="tile-label">{{ t("demo.approvalState") }}</span>
            <span class="tile-value">{{ data.state }} <span class="dim">· {{ data.routing_decision }}</span></span>
          </div>
        </div>
      </div>

      <div class="notice-bar">
        <span>{{ t("demo.policyNote") }}</span>
      </div>

      <div class="panel">
        <div class="panel-head">
          <span class="panel-label">{{ t("demo.draftLabel") }}</span>
          <span class="panel-num">02</span>
        </div>
        <pre class="mono-block">{{ data.draft }}</pre>
      </div>

      <div class="sources-grid">
        <div class="panel">
          <div class="panel-head">
            <span class="panel-label">{{ t("demo.retrieved") }}</span>
            <span class="count-badge">{{ data.retrieved_sources?.length ?? 0 }}</span>
          </div>
          <div v-if="!data.retrieved_sources?.length" class="empty-note">{{ t("demo.noSources") }}</div>
          <ul v-else class="source-list">
            <li v-for="(s, i) in data.retrieved_sources" :key="i">
              <span class="source-title">{{ s.title }}</span>
              <span class="source-key mono">{{ s.source_key }}</span>
            </li>
          </ul>
        </div>
        <div class="panel">
          <div class="panel-head">
            <span class="panel-label">{{ t("demo.citedLabel") }}</span>
            <span class="count-badge accent">{{ data.cited_sources?.length ?? 0 }}</span>
          </div>
          <div v-if="!data.cited_sources?.length" class="empty-note">{{ t("demo.noCitations") }}</div>
          <ul v-else class="source-list cited">
            <li v-for="(s, i) in data.cited_sources" :key="i">
              <span class="source-title">{{ s.title }}</span>
              <span class="source-key mono">{{ s.source_key }}</span>
            </li>
          </ul>
        </div>
      </div>

      <p class="restriction">
        <span>{{ t("demo.noSending") }}</span>
      </p>
      <router-link to="/" class="back-link">← {{ t("demo.back") }}</router-link>
    </template>
  </div>
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
  } catch {
    error.value = t("demo.error");
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.demo-view { display: flex; flex-direction: column; gap: 1.5rem; }

.page-head {
  display: flex; align-items: flex-end; justify-content: space-between;
  gap: 1rem; flex-wrap: wrap; margin-bottom: 0.5rem;
}
.eyebrow {
  font-size: .72rem; letter-spacing: .12em;
  color: var(--accent); font-weight: 700; margin-bottom: .35rem;
}
.page-head h2 { font-size: 1.6rem; font-weight: 700; color: var(--text); }

.chip-recorded {
  display: inline-flex; align-items: center; gap: .4rem;
  background: var(--accent-soft); color: var(--accent);
  border: 1px solid var(--accent); border-radius: 30px;
  padding: .35rem .85rem; font-size: .78rem; font-weight: 600;
}
.chip-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--accent); box-shadow: 0 0 6px var(--accent);
}

.state { padding: 1.25rem; border-radius: var(--radius-md); }
.state.muted { color: var(--text-muted); background: var(--surface-card); border: 1px solid var(--border); }
.state.error { color: var(--danger); background: var(--danger-soft); border: 1px solid var(--danger); }

.demo-grid {
  display: grid; grid-template-columns: 1.6fr 1fr; gap: 1.5rem;
}
.side-stack { display: flex; flex-direction: column; gap: 1rem; }

.metric-tile {
  background: var(--surface-card); border: 1px solid var(--border);
  border-radius: var(--radius-md); padding: 1.1rem 1.25rem;
  display: flex; flex-direction: column; gap: .35rem; flex: 1;
  transition: var(--transition);
}
.metric-tile:hover { border-color: var(--border-active); }
.tile-label {
  font-size: .7rem; letter-spacing: .08em;
  color: var(--text-muted); font-weight: 600;
}
.tile-value { font-size: 1.1rem; font-weight: 700; color: var(--text); }
.tile-value .dim { color: var(--text-muted); font-weight: 500; font-size: .9rem; }

.panel {
  background: var(--surface-card); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 1.5rem;
  display: flex; flex-direction: column; gap: 1rem;
}
.panel-primary { border-color: var(--border-active); }
.panel-head {
  display: flex; align-items: center; justify-content: space-between;
  gap: .75rem;
}
.panel-label {
  font-size: .7rem; letter-spacing: .1em;
  color: var(--text-muted); font-weight: 700;
}
.panel-num { font-family: var(--font-mono); font-size: .75rem; color: var(--text-subtle); }
.count-badge {
  background: var(--bg-deep); color: var(--text-muted);
  font-size: .75rem; font-weight: 700; padding: .15rem .55rem; border-radius: 0;
}
.count-badge.accent { background: var(--accent-soft); color: var(--accent); }

.inquiry-subject { font-size: 1.15rem; font-weight: 700; color: var(--text); }

.mono-block {
  font-family: var(--font-mono); font-size: .85rem; line-height: 1.6;
  white-space: pre-wrap; word-break: break-word; color: var(--text);
  background: var(--bg-deep); border: 1px solid var(--border);
  border-radius: var(--radius-sm); padding: 1rem; margin: 0;
}

.notice-bar {
  display: flex; align-items: center; gap: .75rem;
  background: var(--warning-soft); border: 1px solid var(--border-strong);
  border-radius: var(--radius-md); padding: .9rem 1.1rem;
  font-size: .88rem; color: var(--warning);
}
.notice-icon { font-size: 1rem; }

.sources-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }

.source-list {
  list-style: none; padding: 0; margin: 0;
  display: flex; flex-direction: column; gap: .5rem;
}
.source-list li {
  display: flex; flex-direction: column; gap: .2rem;
  background: var(--bg-deep); border: 1px solid var(--border);
  border-radius: var(--radius-sm); padding: .7rem .9rem;
}
.source-list.cited li { border-left: 3px solid var(--accent); }
.source-title { font-weight: 600; font-size: .9rem; color: var(--text); }
.source-key { font-size: .78rem; color: var(--text-muted); }

.empty-note { color: var(--text-muted); font-size: .88rem; font-style: italic; }

.restriction {
  display: flex; align-items: center; gap: .5rem;
  font-weight: 600; font-size: .9rem; color: var(--warning);
  background: var(--warning-soft); border: 1px solid var(--border-strong);
  border-radius: var(--radius-md); padding: .85rem 1.1rem; margin: 0;
}
.back-link {
  color: var(--accent); text-decoration: none; font-weight: 600;
  font-size: .9rem; transition: var(--transition);
}
.back-link:hover { color: var(--accent); transform: translateX(-3px); }

@media (max-width: 900px) {
  .demo-grid { grid-template-columns: 1fr; }
  .sources-grid { grid-template-columns: 1fr; }
}
</style>
