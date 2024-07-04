import { fileURLToPath, URL } from "node:url";
import path from "path";

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const PORT = 5000;

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  
  build: {
    target: "esnext", //browsers can handle the latest ES features
  }, 
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
      "~bootstrap": path.resolve(__dirname, "node_modules/bootstrap"),
    },
  },
  server: {
    port: PORT,
    //strictPort: true,
    //host: true,
    //origin: "http://0.0.0.0:5000",
  },
  preview: {
    port: PORT,
    strictPort: true,
    host: true,
    origin: "http://0.0.0.0:5000",
  }
})
