# Porting the GitHub site into the Lovable app

**Prepared** 2026-08-19, 21:58 PDT

Goal: get the content and styling of `05_WEBSITE/theme_insite_ca/` (published at
https://obviouslyobvi.github.io/Insite/) onto insite-ca.org **without** moving the domain
off Lovable, so the developer portal, admin pipeline and tax-roll module keep running.

No DNS change. No hosting change. The pages become routes in the existing app.

## Why this is a port, not a file copy

insite-ca.org is a TanStack Start app on Lovable: React routes, server functions, Supabase
auth. Our pages are standalone HTML with inline `<style>` and inline `<script>`. Lovable's
router and its AI editor both operate on React routes, so loose HTML files dropped into
`public/` would be reachable but unmanageable — outside the editor, outside the app's nav
and auth, and colliding with the app shell at the root path. Each page needs to become a
route.

The styling side is the easy half: the theme in `theme_insite_ca/` was lifted verbatim
from insite-ca.org's own stylesheet — same tokens, same `--radius`, same Inter stack. It
drops into the app's existing design system rather than fighting it.

## Content gap

### Genuinely new — no equivalent on the live site

| Page | Words | What it is |
|---|---|---|
| `qualify.html` | ~937 | "Do you qualify? Three numbers tell you" — the self-screening flow |
| `manual.html` | ~1,207 | Developer manual, also published as a PDF |
| `builders.html` | ~487 | Builder-facing framing of the same program |
| `investors.html` | ~361 | The security stack, for capital partners |
| `tey_calculator.html` | ~271 | Tax-equivalent yield calculator |

Roughly 3,250 words with no home on insite-ca.org today. This is the bulk of the value.

`qualify2.html` is a second variant of the qualify page; pick one before porting.

### Overlapping — needs a merge decision, not a copy

| Ours | Live | Note |
|---|---|---|
| `index.html` (~1,421w) | `/` | Both are homepages. Live has Developer benefits / The workflow / Financing process; ours has the fee explanation, per-parcel sizing, calculator, FAQ and the evidence table. Ours is substantially longer. |
| `fee_estimator.html` | `/methodology` | Same subject. `/methodology` already covers finished lot value, the 2% tax ceiling, and per-parcel capacity. Ours adds a worked 10-lot example and the day-one comparison. |
| `developer_application.html` | `/apply` | Both embed the same Airtable form. Live also has `/apply/success`, which ours lacks. Drop ours and keep `/apply`. |

### Naming conflict — resolve before porting

Our `portal.html` is the **Investor** portal: a gate page for capital partners.
The live `/portal` is the **Developer** portal: "My Projects", Supabase-backed.

Same path, different audiences. Ours needs a different route — `/investors/access` or
similar — or the live one does. This will silently break things if it is missed.

## Sequence

1. **Connect the Lovable project to GitHub** (in Lovable: GitHub → Create Repository).
   This is the blocker; the app source exists only inside Lovable today, and no repo on
   the account matches it.
2. Add that repo to the working session.
3. Port the five new pages first — they add content without touching anything live.
4. Then resolve the three overlaps, homepage last since it is the most contested.
5. Rename the investor portal route.
6. Verify each route at 1440 and 390, as with the static build.

## What is explicitly not changing

Auth, the developer portal, the ten-stage admin pipeline, documents, parcels, the Annual
Levy Submission module, and notifications all stay exactly as they are. This work is
additive: pages and styling only.
