import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  build: { sourcemap: false },
  server: {
    proxy: {
      "/api": "http://127.0.0.1:18099",
      "/public": "http://127.0.0.1:18099",
    },
  },
  plugins: [vue()],
});
