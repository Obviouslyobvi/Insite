# insite-ca.org — static site, packaged for Lovable hosting

This is the site published at <https://obviouslyobvi.github.io/Insite/>, wrapped in the
minimum build config Lovable needs in order to host it. The page content is unmodified:
same HTML, same inline CSS, same calculator scripts, same logo SVGs.

Push the contents of this folder to the GitHub repository that a Lovable project is
connected to, and Lovable will build and serve it.

## What's here

| | |
|---|---|
| 11 `.html` pages | `index`, `developers`, `builders`, `investors`, `qualify`, `qualify2`, `fee_estimator`, `tey_calculator`, `developer_application`, `manual`, `portal` |
| 4 images | the two `qualify`/`manual` diagrams (`.png`) and the two `qualify2` variants (`_v2.jpg`) |
| `public/fonts/` | Inter variable, latin subset, 48 KB |
| `public/manual.pdf` | the developer manual, unlinked but published today |
| `vite.config.js` | multi-page build config |
| `package.json` | one dev dependency, Vite |

## Why Vite and not a plain file copy

Lovable builds and serves projects rather than serving a folder, so the site needs a
`build` script that emits a `dist/`. Vite is what Lovable's own projects use, so it is the
one that is certain to work there.

The config is deliberately thin. Every `.html` file in the project root is registered as
its own build entry, so the output keeps the flat filenames the site already uses
(`/qualify.html`, `/manual.html`) and every relative link between pages carries over
untouched. No page was rewritten to make this work.

## The one layout rule worth knowing

Images sit in the project root; the font sits in `public/fonts/`.

That split is not arbitrary. Vite rewrites `<img src>` at build time and fingerprints the
file, which is why the images can live at the root. It does **not** rewrite URLs inside an
inline `<style>` block, and every page pulls Inter in through an inline `@font-face`:

```css
src: url("fonts/inter-latin-var.woff2") format("woff2");
```

Nothing rewrites that string, so the file has to still be at that exact path after the
build. `public/` is copied verbatim into `dist/`, so it is. Moving the font out of
`public/` will build cleanly and then silently fall back to system fonts in the browser.

Vite prints a warning about this font on every build — `didn't resolve at build time, it
will remain unchanged to be resolved at runtime`. That is the intended behaviour, not a
problem to fix.

## Build

```bash
npm install
npm run build     # -> dist/
npm run preview   # serve the build locally
```

## Verified

Built with Vite 5.4.21: 11 pages, 4 images fingerprinted.

Served from `dist/` and checked in Chromium at 1440 px and 390 px:

- all 11 pages return 200
- every internal link and asset reference across every built page resolves 200
- Inter reports `status: loaded` on all 11 pages at both widths
- no horizontal overflow on any page at either width
- no console errors, with one exception below

`developer_application.html` embeds the Airtable form in an iframe. That request fails when
the page is served from `127.0.0.1` in a sandbox; the same embed is on the live GitHub
Pages copy today and loads there. Re-check it once on the real domain after deploying.
