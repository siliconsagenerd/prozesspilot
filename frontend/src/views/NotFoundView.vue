<template>
  <div class="notfound">
    <h1 class="doc-title">404</h1>
    <p class="muted">{{ t('notfound.body') }}</p>
    <router-link to="/" class="btn-run">{{ t('notfound.home') }}</router-link>
  </div>
</template>

<script setup lang="ts">
import { t } from "../i18n";
</script>

<style scoped>
.notfound { max-width: 640px; margin: 4rem auto; text-align: center; display: grid; gap: 1rem; justify-items: center; }
.notfound .btn-run { text-decoration: none; }
</style>
