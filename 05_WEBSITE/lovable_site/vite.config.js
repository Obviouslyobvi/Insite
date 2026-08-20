import { defineConfig } from 'vite'
import { fileURLToPath } from 'node:url'
import { readdirSync } from 'node:fs'
import { resolve } from 'node:path'

const root = fileURLToPath(new URL('.', import.meta.url))

// Multi-page build: every .html file in the project root is its own entry, so
// the output keeps the same flat filenames the site already uses
// (/qualify.html, /manual.html, ...) and the relative links between pages
// carry over unchanged.
const input = Object.fromEntries(
  readdirSync(root)
    .filter((f) => f.endsWith('.html'))
    .map((f) => [f.replace(/\.html$/, ''), resolve(root, f)])
)

export default defineConfig({
  // The font is pulled in by an inline @font-face inside each page's <style>
  // block, which Vite does not rewrite. It lives in public/fonts/ so it stays
  // reachable at exactly the path the CSS asks for.
  build: {
    outDir: 'dist',
    rollupOptions: { input },
  },
})
