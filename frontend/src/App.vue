<template>
  <div class="app">
    <header class="topbar">
      <div class="brand">
        <span class="brand-mark" aria-hidden="true"></span>
        <h1>ProzessPilot</h1>
      </div>
      <div class="topbar-right">
        <nav>
          <router-link to="/" class="nav-link">{{ t('nav.inbox') }}</router-link>
          <router-link to="/eval" class="nav-link">{{ t('nav.eval') }}</router-link>
        </nav>
        <button class="lang-toggle" @click="toggleLocale" :aria-label="t('lang.toggle')">
          {{ t('lang.label') }}
        </button>
      </div>
    </header>
    <main>
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
  </div>
</template>
<script setup lang="ts">
import { t, toggleLocale } from "./i18n";
</script>
<style>
  :root {
    --bg: #f5f5f7;
    --surface: #ffffff;
    --surface-2: #fbfbfd;
    --text: #1d1d1f;
    --text-2: #6e6e73;
    --accent: #0071e3;
    --accent-soft: rgba(0, 113, 227, 0.12);
    --border: rgba(0, 0, 0, 0.08);
    --shadow: 0 1px 2px rgba(0,0,0,.04), 0 8px 24px rgba(0,0,0,.06);
    --radius: 12px;
    --radius-sm: 8px;
    --ease: cubic-bezier(.2,.8,.2,1);
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; }
  body {
    font-family: -apple-system, "SF Pro Text", "Helvetica Neue", system-ui, sans-serif;
    background: var(--bg);
    color: var(--text);
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    line-height: 1.5;
  }
  .app { max-width: 1120px; margin: 0 auto; padding: 1.25rem 1.5rem 3rem; }
  .topbar {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 1.5rem; padding: .75rem 1rem;
    background: rgba(255,255,255,.72);
    backdrop-filter: saturate(180%) blur(20px);
    -webkit-backdrop-filter: saturate(180%) blur(20px);
    border: 1px solid var(--border); border-radius: var(--radius);
    position: sticky; top: .75rem; z-index: 10;
  }
  .brand { display: flex; align-items: center; gap: .6rem; }
  .brand-mark {
    width: 26px; height: 26px; border-radius: 7px;
    background: linear-gradient(135deg, #0071e3, #409cff);
    box-shadow: 0 2px 6px rgba(0,113,227,.35);
  }
  .brand h1 { font-size: 1.05rem; font-weight: 600; margin: 0; letter-spacing: -.01em; }
  nav { display: flex; gap: .25rem; }
  .nav-link {
    padding: .4rem .85rem; border-radius: 8px; text-decoration: none;
    color: var(--text); font-size: .9rem; font-weight: 500;
    transition: background .15s var(--ease), color .15s var(--ease);
  }
  .nav-link:hover { background: var(--accent-soft); color: var(--accent); }
  .topbar-right { display: flex; align-items: center; gap: .75rem; }
  .lang-toggle {
    padding: .4rem .7rem; border-radius: 999px; background: rgba(255,255,255,.72);
    border: 1px solid var(--border); color: var(--text); font-weight: 600; font-size: .8rem;
    backdrop-filter: saturate(180%) blur(20px); -webkit-backdrop-filter: saturate(180%) blur(20px);
    cursor: pointer; transition: transform .12s var(--ease), box-shadow .15s var(--ease);
  }
  .lang-toggle:hover { box-shadow: 0 2px 8px rgba(0,0,0,.08); }
  .lang-toggle:active { transform: scale(.96); }
  .lang-toggle:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
  main { margin-top: 1rem; }
  h2 { font-size: 1.5rem; font-weight: 600; letter-spacing: -.02em; margin: 0 0 .75rem; }
  h3 { font-size: 1.05rem; font-weight: 600; margin: 1.25rem 0 .5rem; }
  .mono { font-family: "SF Mono", ui-monospace, monospace; font-size: .85rem; }
  .card {
    background: var(--surface); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 1.25rem; margin: 1rem 0;
    box-shadow: var(--shadow);
  }
  .badge {
    display: inline-block; padding: .18rem .55rem; border-radius: 999px;
    font-size: .72rem; font-weight: 600; letter-spacing: .02em;
    background: #e8e8ed; color: var(--text);
  }
  button {
    padding: .55rem 1.1rem; background: var(--accent); color: #fff;
    border: none; border-radius: 9px; cursor: pointer; font-weight: 500;
    font-size: .9rem; transition: transform .12s var(--ease), box-shadow .15s var(--ease), opacity .15s;
  }
  button:hover:not(:disabled) { box-shadow: 0 4px 12px rgba(0,113,227,.3); }
  button:active:not(:disabled) { transform: scale(.98); }
  button:disabled { opacity: .5; cursor: not-allowed; }
  button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
  textarea, input {
    padding: .6rem .75rem; border: 1px solid var(--border); border-radius: 9px;
    font: inherit; background: var(--surface); transition: border-color .15s, box-shadow .15s;
  }
  textarea:focus, input:focus {
    outline: none; border-color: var(--accent);
    box-shadow: 0 0 0 3px var(--accent-soft);
  }
  .fade-enter-active, .fade-leave-active { transition: opacity .18s var(--ease); }
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
  }
  .fade-enter-from, .fade-leave-to { opacity: 0; }
  @media (max-width: 640px) {
    .app { padding: 1rem; }
    .topbar { flex-direction: column; gap: .5rem; align-items: flex-start; }
  }
</style>