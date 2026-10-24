<template>
  <div class="app-shell">
    <header class="site-header">
      <div class="header-inner">
        <a class="brand" href="/">
          <span class="brand-mark">P</span>
          <span class="brand-name">ProzessPilot</span>
        </a>
        <nav class="primary-nav" aria-label="Primary">
          <router-link to="/" class="nav-link">{{ t('nav.landing') }}</router-link>
          <router-link to="/demo" class="nav-link">{{ t('nav.demo') }}</router-link>
          <router-link to="/app" class="nav-link">{{ t('nav.operator') }}</router-link>
          <router-link to="/eval" class="nav-link">{{ t('nav.eval') }}</router-link>
        </nav>
        <div class="header-controls">
          <div class="segmented-control lang-switch" role="group" :aria-label="t('lang.toggle')">
            <button
              type="button"
              class="segmented-btn"
              :class="{ active: locale === 'de' }"
              @click="setLocale('de')"
              aria-label="Deutsch"
            >DE</button>
            <button
              type="button"
              class="segmented-btn"
              :class="{ active: locale === 'en' }"
              @click="setLocale('en')"
              aria-label="English"
            >EN</button>
          </div>
          <div class="segmented-control theme-switch" role="group" aria-label="Theme">
            <button
              type="button"
              class="segmented-btn"
              :class="{ active: theme === 'light' }"
              @click="setTheme('light')"
              :title="t('theme.light')"
              aria-label="Light mode"
            >
              <span class="theme-icon">☼</span>
              <span class="theme-text">{{ t('theme.light') }}</span>
            </button>
            <button
              type="button"
              class="segmented-btn"
              :class="{ active: theme === 'dark' }"
              @click="setTheme('dark')"
              :title="t('theme.dark')"
              aria-label="Dark mode"
            >
              <span class="theme-icon">☾</span>
              <span class="theme-text">{{ t('theme.dark') }}</span>
            </button>
          </div>
        </div>
      </div>
    </header>

    <main class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="page-fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <footer class="site-footer">
      <div class="footer-inner">
        <span>Vishrut Pandey · Bewerbungsprojekt · EUROKEY Software GmbH</span>
        <span class="tech">FastAPI · Vue 3 · SQLite · OpenAI/Laya</span>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { t, locale, setLocale } from "./i18n";

const theme = ref<"light" | "dark">("light");

function applyTheme(tVal: string) {
  document.documentElement.setAttribute("data-theme", tVal);
}

function setTheme(tVal: "light" | "dark") {
  theme.value = tVal;
  applyTheme(tVal);
  try { localStorage.setItem("pp-theme", tVal); } catch {}
}

onMounted(() => {
  let saved = "light";
  try { saved = (localStorage.getItem("pp-theme") as "light" | "dark") || "light"; } catch {}
  theme.value = saved === "dark" ? "dark" : "light";
  applyTheme(theme.value);
});
</script>

<style>
:root {
  --bg: #FFFFFF;
  --bg-deep: #F4F4F4;
  --header-bg: rgba(255, 255, 255, 0.88);
  --surface: #FFFFFF;
  --surface-hover: #F4F4F4;
  --surface-solid: #FFFFFF;
  --surface-card: #FFFFFF;
  --border: #D9D9D9;
  --border-strong: #1A1A1A;
  --border-active: #1A1A1A;
  --text: #1A1A1A;
  --text-muted: #595959;
  --text-subtle: #8C8C8C;
  --accent: #1A1A1A;
  --accent-dark: #000000;
  --accent-soft: #F4F4F4;
  --inverse: #FFFFFF;
  --success: #1F6F3F;
  --warning: #8A5A0B;
  --danger: #9F1C1C;
  --success-soft: #EAF4EE;
  --warning-soft: #F7F0E2;
  --danger-soft: #FBE9E9;
  --radius-lg: 0px;
  --radius-md: 0px;
  --radius-sm: 0px;
  --font-display: "IBM Plex Sans", system-ui, sans-serif;
  --font-sans: "IBM Plex Sans", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
  --transition: 120ms linear;
  --maxw: 1480px;
}

html[data-theme="dark"] {
  --bg: #0A0A0A;
  --bg-deep: #141414;
  --header-bg: rgba(10, 10, 10, 0.88);
  --surface: #0A0A0A;
  --surface-hover: #1A1A1A;
  --surface-solid: #141414;
  --surface-card: #141414;
  --border: #2A2A2A;
  --border-strong: #F5F5F5;
  --border-active: #FFFFFF;
  --text: #F5F5F5;
  --text-muted: #A3A3A3;
  --text-subtle: #737373;
  --accent: #F5F5F5;
  --accent-dark: #FFFFFF;
  --accent-soft: #262626;
  --inverse: #0A0A0A;
  --success: #4ADE80;
  --warning: #FBBF24;
  --danger: #F87171;
  --success-soft: #14261A;
  --warning-soft: #2A2414;
  --danger-soft: #2A1515;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html { background: var(--bg); overflow-x: hidden; }

body {
  font-family: var(--font-sans);
  background-color: var(--bg);
  color: var(--text);
  min-height: 100vh;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

.app-shell {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid var(--border);
  background: var(--header-bg);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  transition: background 120ms linear, border-color 120ms linear;
}

.header-inner {
  max-width: var(--maxw);
  margin: 0 auto;
  padding: 0.75rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  color: var(--text);
}

.brand-mark {
  width: 22px;
  height: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: var(--text);
  color: var(--bg);
  font-family: var(--font-mono);
  font-weight: 600;
  font-size: 0.8rem;
  border-radius: 0;
}

.brand-name {
  font-family: var(--font-sans);
  font-weight: 600;
  font-size: 1rem;
  letter-spacing: -0.01em;
}

.primary-nav {
  display: flex;
  gap: 0.25rem;
}

.nav-link {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 500;
  padding: 0.4rem 0.85rem;
  border-bottom: 2px solid transparent;
  transition: var(--transition);
}

.nav-link:hover {
  color: var(--text);
}

.nav-link.router-link-active {
  color: var(--text);
  border-bottom-color: var(--text);
  font-weight: 600;
}

.header-controls {
  display: flex;
  align-items: center;
  gap: 0.65rem;
}

.segmented-control {
  display: inline-flex;
  align-items: center;
  background: var(--bg-deep);
  border: 1px solid var(--border-strong);
  padding: 1px;
  gap: 1px;
}

.segmented-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.35rem;
  background: transparent;
  border: none;
  color: var(--text-muted);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 500;
  padding: 0.28rem 0.55rem;
  cursor: pointer;
  transition: var(--transition);
  line-height: 1;
  user-select: none;
}

.segmented-btn .theme-icon {
  font-size: 0.85rem;
  line-height: 1;
}

.segmented-btn .theme-text {
  font-size: 0.72rem;
  letter-spacing: -0.01em;
}

.segmented-btn:hover:not(.active) {
  color: var(--text);
  background: var(--surface-hover);
}

.segmented-btn.active {
  background: var(--text);
  color: var(--bg);
  font-weight: 700;
}

.main-content {
  flex: 1;
  max-width: var(--maxw);
  width: 100%;
  margin: 0 auto;
  padding: 2rem 2rem 3.5rem;
}

.site-footer {
  border-top: 1px solid var(--border);
  background: var(--bg);
  padding: 1rem 0;
  margin-top: auto;
}

.footer-inner {
  max-width: var(--maxw);
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.78rem;
  color: var(--text-muted);
  flex-wrap: wrap;
  gap: 1rem;
  font-family: var(--font-mono);
}

.tech {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text-muted);
}

.page-fade-enter-active, .page-fade-leave-active {
  transition: opacity 120ms linear;
}

.page-fade-enter-from { opacity: 0; }
.page-fade-leave-to { opacity: 0; }

@media (max-width: 860px) {
  .header-inner {
    flex-wrap: wrap;
    gap: 0.75rem;
    padding: 0.75rem 1rem;
  }
  .header-controls {
    margin-left: auto;
  }
  .main-content {
    padding: 1.5rem 1rem 2.5rem;
  }
  .footer-inner {
    padding: 0 1rem;
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
