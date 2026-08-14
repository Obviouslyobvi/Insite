# INSITE website — insite-ca.org theme variant

A complete, self-contained copy of `05_WEBSITE/` restyled with the theme and colors from
[insite-ca.org](https://insite-ca.org). **Every file in the parent `05_WEBSITE/` folder is
untouched.** This folder is an addition, not a replacement — the two versions can be served
side by side.

All 10 pages, all copy, all markup structure, and all calculator logic are identical to the
originals. Only presentation changed: the palette, the typography, and the card/button/table
treatment.

## What's here

| | |
|---|---|
| Pages | `index`, `developers`, `builders`, `investors`, `qualify`, `fee_estimator`, `tey_calculator`, `developer_application`, `manual`, `portal` (`.html`) |
| Assets | `assets_ins002_factors.*`, `assets_ins002_types.*`, `manual.pdf` |
| Font | `fonts/inter-latin-var.woff2` — Inter variable, latin subset, 48 KB |
| QC | `qc/` — full-page screenshots of every page at 1440 px and 390 px |

Links between pages are all relative, so the folder works opened straight from disk
(`file://`) or served from any static host. There are no CDN dependencies.

## The logo is not themed

The INSITE mark keeps its own navy `#1A3E6C`, green `#8DB87A`, and grey tagline exactly as
in the original. It is brand identity, not site chrome. The build skips every `<svg>`
element wholesale, so all 11 logo instances are byte-identical to the originals and no
future palette change can reach them.

## Theme source

Tokens were lifted verbatim from `https://insite-ca.org/assets/styles-BOjQD-ta.css`
(a Tailwind/shadcn build). The reference site declares Inter but ships no webfont, so it
falls back to system UI fonts; this copy self-hosts Inter instead, which keeps the package
offline-capable and renders the intended typeface consistently.

## Color mapping

Applied to site chrome only — never inside the logo.

| Role | Original site | insite-ca.org token | New value |
|---|---|---|---|
| Headings, body ink, dark buttons | `--navy` `#153A5B` | `--foreground` | `#101828` |
| Accent, links, kickers, step badges | `--green` `#3E7C59` | `--primary` / `--accent` | `#0964F8` |
| Secondary text, captions | `--slate` `#6B7280` | `--muted-foreground` | `#57657A` |
| Panel and band surfaces | `--light` `#F5F7FA` | `--secondary` / `--muted` | `#F5F8FB` |
| Hairlines, inputs | `--line` `#D3DAE3` | `--border` / `--input` | `#E2E8F0` |
| Warning rule | `#B45309` | `--chart-1` | `#F05100` |
| Pre-launch notice bar | `#7A4A12` | `--foreground` | `#101828` |

The `--navy` and `--green` variable names are kept so the diff against the original stays
readable; only their values changed.

## Presentation changes

- **Typography** — Inter throughout at `--font-sans`, replacing Helvetica and the Georgia
  serif used for lede paragraphs. Tighter heading tracking (`-0.02em`), 600/700 weights.
- **Radius** — `--radius: .75rem`, matching the reference. Cards and tables get 12 px
  corners, buttons and inputs 8 px.
- **Cards** — the original's 4 px navy/green top accents are flattened to a uniform 1 px
  hairline, which is how the reference styles every card.
- **Nav** — sticky translucent bar with a 12 px backdrop blur and a hairline bottom border,
  replacing the 2 px navy rule. Nav links get a rounded hover background.
- **Buttons** — `.btn` is foreground-dark on white, `.btn.alt` is primary blue, both rounded
  with an opacity hover, matching the reference's "Start Intake" treatment.
- **Tables** — tinted header row, hairline grid, clipped rounded corners.
- **Inputs** — rounded, hairline border, 3 px focus ring in primary blue.

## Verification

Rendered in headless Chromium at 1440×900 and 390×844. All 10 pages return HTTP 200 with no
console errors, no broken assets, and zero horizontal overflow at either viewport. Page
heights track the originals within about 1 percent, confirming layout was preserved. The
per-parcel calculator, fee estimator, and TEY calculator were exercised and return the same
figures as the originals.

Two pre-existing conditions are unchanged from the original site and are not theme defects:
the pages ship no `favicon.ico`, and the Airtable form embedded in
`developer_application.html` cannot load in a sandboxed browser without network access.

Text content was diffed against the originals page by page: identical on all 10.

## Contrast

All foreground/background pairs clear WCAG AA for body text: `#0964F8` on white is 5.0:1,
`#57657A` on white is 5.8:1, and `#57657A` on `#F5F8FB` is 5.5:1.
