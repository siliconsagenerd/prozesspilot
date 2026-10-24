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
</style>
