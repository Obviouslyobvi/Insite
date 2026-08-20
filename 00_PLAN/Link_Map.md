# insite-ca.org — complete link map

**Compiled** 2026-08-20, from the deployed page sources. Two hosts share the domain after
the cutover: the public site on the apex, the app on `app.`.

## Public site — `insite-ca.org` (project `happy-public-view`)

`/` issues a 301 to `/index.html`. Every page except the three utility pages carries the
shared nav: Home, Developers, Fee Estimator, Do I Qualify?, Apply, Manual.

| URL | Page | Links out (beyond the shared nav) |
|---|---|---|
| `/index.html` | Home — fee explanation, calculator, FAQ, evidence table | 9 external evidence sources (see below) |
| `/developers.html` | Developer-facing program page | apply CTAs |
| `/builders.html` | Builder framing — "Paid at the Permit Counter" | apply + fee estimator CTAs. **Reachable only by direct URL — no page links to it** |
| `/investors.html` | The security stack, for capital partners | `portal.html` ×2, `tey_calculator.html`, 2 document links on raw.githack (see warning) |
| `/qualify.html` | "Do you qualify? Three numbers tell you" | apply ×4, fee estimator, developers |
| `/qualify2.html` | Variant of qualify with v2 graphics | same as qualify. **Unlinked — direct URL only** |
| `/fee_estimator.html` | Fee estimator with worked 10-lot example | qualify, apply |
| `/tey_calculator.html` | Tax-equivalent yield calculator | `index.html#how`. No nav bar. **Linked only from investors.html** |
| `/developer_application.html` | Application page | embeds + links the Airtable form |
| `/manual.html` | Developer manual (HTML edition) | no nav bar |
| `/portal.html` | **Investor** Portal gate page | no nav bar. Linked only from investors.html |

Assets: `/assets_ins002_types.png`, `/assets_ins002_factors.png` (qualify, manual),
`/assets_ins002_types_v2.jpg`, `/assets_ins002_factors_v2.jpg` (qualify2),
`/fonts/inter-latin-var.woff2` (every page), `/manual.pdf` (unlinked, direct URL only).

## The app — `app.insite-ca.org` (project `assess-mint-hub` / "INSITE Finance Hub")

Verified serving directly (no redirect) after the cutover.

| URL | What it is |
|---|---|
| `/` | App homepage — the old marketing front |
| `/login` | **Developer** Portal sign-in |
| `/portal` | "My Projects" — the authenticated developer view |
| `/admin-login` | Administration sign-in |
| `/admin` | "Pipeline" — the operations console |
| `/admin/tax-roll` | Annual Levy Submission module |
| `/admin/notifications` | Notifications console |
| `/apply` → `/apply/success` | Airtable intake wrap + confirmation |
| `/contact` | Contact form (publishes hello@insite-ca.org) |
| `/methodology` | Underwriting methodology + financing calculator |

## Old apex URLs that no longer exist there

Anything circulated with these paths now 404s on the apex. The content lives on `app.`:

| Dead on apex | Now at |
|---|---|
| `insite-ca.org/login` | `app.insite-ca.org/login` |
| `insite-ca.org/portal` | `app.insite-ca.org/portal` (note: apex `/portal.html` is the *Investor* page — different audience) |
| `insite-ca.org/admin`, `/admin-login`, `/admin/...` | same paths on `app.` |
| `insite-ca.org/apply`, `/apply/success` | `app.insite-ca.org/apply` — or the static `/developer_application.html` |
| `insite-ca.org/contact` | `app.insite-ca.org/contact` |
| `insite-ca.org/methodology` | `app.insite-ca.org/methodology` — or the static `/fee_estimator.html` |

## External links the public site depends on

From `index.html` (evidence table): treasurer.ca.gov (2 incl. the debt guide), cscda.org (2),
cmfa-ca.com/bold, elkgrove.gov staff report PDF, ftb.ca.gov, abag.ca.gov,
northcoastfinancialinc.com. From `developer_application.html`: the Airtable form
(`airtable.com/appVwwLQvMkhsebB1/...`), also embedded as an iframe.

## ⚠ Two links that break if the Insite repo goes private

`investors.html` links to documents served **straight out of the `Obviouslyobvi/Insite`
GitHub repo** via raw.githack.com:

- `.../Insite/master/03_MARKETING/src/INSITE_Capital_Partner_Brief.html`
- `.../Insite/master/02_PROGRAM/INS-303_Investor_Guide_PUBLIC_EDITION.pdf`

Making that repository private — recommended elsewhere in the runbook because it exposes
the Kill Memo and payment records — kills both links. Before flipping visibility, copy
those two files into the `insite-public-pages` repo's `public/` and repoint the two hrefs
to local paths. That also removes the last runtime dependency on the old repo.
