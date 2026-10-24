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

    <aside
      class="float-widget"
      :class="{ 'is-expanded': floatExpanded || floatHovered }"
      aria-label="Companion project"
      @click="toggleFloat"
      @mouseenter="floatHovered = true"
      @mouseleave="floatHovered = false"
      tabindex="0"
      @keydown.enter="toggleFloat"
      @keydown.space.prevent="toggleFloat"
    >
      <div class="float-widget__monogram" aria-hidden="true">SD</div>
      <div class="float-widget__body">
        <div class="float-widget__eyebrow">★ {{ t("landing.prov.related") }}</div>
        <h3 class="float-widget__title">SecureDoc-AI</h3>
        <a
          href="https://github.com/siliconsagenerd/securedoc-ai"
          target="_blank"
          rel="noopener"
          class="float-widget__primary-link"
          @click.stop
        >Open SecureDoc-AI ↗</a>
        <div class="float-widget__extra" v-show="floatExpanded || floatHovered">
          <p class="float-widget__desc">{{ t("landing.portfolio.body") }}</p>
          <div class="float-widget__chips">
            <span class="chip">FastAPI</span>
            <span class="chip">Vue 3</span>
            <span class="chip">SQLAlchemy</span>
            <span class="chip">RAG</span>
            <span class="chip">Spring Boot</span>
          </div>
          <div class="float-widget__links">
            <a href="https://github.com/siliconsagenerd/securedoc-ai" target="_blank" rel="noopener" class="float-widget__link" @click.stop>SecureDoc-AI ↗</a>
            <a href="https://github.com/siliconsagenerd/prozesspilot" target="_blank" rel="noopener" class="float-widget__link" @click.stop>ProzessPilot ↗</a>
          </div>
        </div>
        <div class="float-widget__hint" v-show="!(floatExpanded || floatHovered)">tap to expand</div>
      </div>
    </aside>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { t, locale, setLocale } from "./i18n";

const theme = ref<"light" | "dark">("light");
const floatExpanded = ref(false);
const floatHovered = ref(false);
const toggleFloat = () => { floatExpanded.value = !floatExpanded.value; };

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
::selection {
  background: var(--text);
  color: var(--bg);
}

html { scroll-behavior: smooth; }

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-sans);
  color: var(--text);
  letter-spacing: -0.02em;
  line-height: 1.15;
  font-weight: 700;
  margin: 0;
}

h1 { font-size: clamp(2rem, 4vw, 3rem); letter-spacing: -0.03em; }
h2 { font-size: clamp(1.5rem, 3vw, 2.25rem); letter-spacing: -0.025em; }
h3 { font-size: clamp(1.15rem, 2vw, 1.5rem); letter-spacing: -0.02em; }
h4 { font-size: 1.05rem; letter-spacing: -0.01em; font-weight: 600; }

a {
  color: inherit;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.18em;
  transition: color var(--transition), text-decoration-color var(--transition);
}

a:focus-visible,
button:focus-visible,
[role="button"]:focus-visible {
  outline: 2px solid var(--text);
  outline-offset: 2px;
}

button { font-family: inherit; }

::placeholder { color: var(--text-subtle); }

.muted { color: var(--text-muted); }

.float-widget {
  position: fixed;
  bottom: 1.25rem;
  right: 1.25rem;
  z-index: 40;
  width: 300px;
  max-width: calc(100vw - 2.5rem);
  background: var(--text);
  color: var(--bg);
  border: none;
  box-shadow: 0 12px 40px rgba(0,0,0,0.25);
  padding: 1rem 1.15rem 1.1rem;
  display: flex;
  gap: 0.85rem;
  align-items: flex-start;
  animation: slideUp 0.5s ease-out both;
  overflow: hidden;
  cursor: pointer;
  transition: transform var(--transition), box-shadow var(--transition);
}

.float-widget:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(0,0,0,0.3);
}

.float-widget::before {
  content: "";
  position: absolute;
  top: -30%;
  right: -20%;
  width: 140px;
  height: 140px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 70%);
  pointer-events: none;
}

.float-widget__monogram {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 700;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg);
  color: var(--text);
  flex-shrink: 0;
  letter-spacing: 0.02em;
}

.float-widget__body { min-width: 0; flex: 1; }

.float-widget__eyebrow {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--bg);
  opacity: 0.7;
  margin-bottom: 0.2rem;
}

.float-widget__title {
  font-size: 1.05rem;
  font-weight: 800;
  letter-spacing: -0.01em;
  color: var(--bg);
  margin-bottom: 0.5rem;
}

.float-widget__desc {
  font-size: 0.8rem;
  line-height: 1.5;
  color: var(--bg);
  opacity: 0.85;
  margin-bottom: 0.6rem;
}

.float-widget__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
  margin-bottom: 0.6rem;
}

.float-widget__chips .chip {
  font-size: 0.68rem;
  padding: 0.1rem 0.4rem;
  border: 1px solid rgba(255,255,255,0.3);
  background: transparent;
  color: var(--bg);
}

.float-widget__primary-link {
  display: inline-block;
  color: var(--bg);
  font-weight: 700;
  font-size: 0.85rem;
  text-decoration: none;
  border-bottom: 1px solid rgba(255,255,255,0.5);
  padding-bottom: 1px;
  transition: var(--transition);
}

.float-widget__primary-link:hover {
  border-bottom-color: var(--bg);
}

.float-widget__hint {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: var(--bg);
  opacity: 0.5;
  margin-top: 0.5rem;
  letter-spacing: 0.04em;
}

.float-widget.is-expanded .float-widget__hint { display: none; }

.float-widget__extra {
  margin-top: 0.6rem;
  padding-top: 0.6rem;
  border-top: 1px solid rgba(255,255,255,0.2);
}

.float-widget__links {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
}

.float-widget__link {
  color: var(--bg);
  font-size: 0.78rem;
  text-decoration: none;
  opacity: 0.85;
  transition: var(--transition);
}

.float-widget__link:hover { opacity: 1; text-decoration: underline; }

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 720px) {
  .float-widget {
    bottom: 0.75rem;
    right: 0.75rem;
    left: 0.75rem;
    width: auto;
    max-width: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
</style>

