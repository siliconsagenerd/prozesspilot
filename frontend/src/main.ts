import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import InboxView from "./views/InboxView.vue";
import RunView from "./views/RunView.vue";
import EvalView from "./views/EvalView.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: InboxView },
    { path: "/runs/:id", component: RunView },
    { path: "/eval", component: EvalView },
  ],
});

createApp(App).use(router).mount("#app");