# insite-ca.org — snapshot of the Lovable production site

**Captured** 2026-08-19, 20:55–21:45 PDT (2026-08-20 03:55–04:45 UTC)
**Host** Lovable, `185.158.133.1`, fronted by Cloudflare
**Deployment id** `647f70bb408ee52c8ee0a5dc845ab084326aa4b48b23d966a97fb0cb701caf94`

A capture of everything insite-ca.org serves publicly, taken before any discussion of
replacing it. 33 files, all fetched HTTP 200.

## What is here

| | |
|---|---|
| `index.html` | Home — the eight-stage workflow marketing page |
| `methodology.html` | `/methodology` — underwriting methodology and financing calculator |
| `apply.html` | `/apply` — intake page wrapping the Airtable form |
| `apply_success.html` | `/apply/success` — post-submission confirmation |
| `login.html` | `/login` — Developer Portal sign-in |
| `admin-login.html` | `/admin-login` — administration sign-in |
| `contact.html` | `/contact` — contact form, hello@insite-ca.org |
| `portal.html` | `/portal` — "My Projects", the authenticated developer view (shell only) |
| `admin.html` | `/admin` — "Pipeline", the authenticated operations console (shell only) |
| `assets/` | The compiled client bundle: 23 JS/CSS files and two portal illustrations |

`portal.html` and `admin.html` are the unauthenticated shells. Their contents render
client-side after Supabase sign-in, so only the frame is captured.

The HTML keeps its original absolute `/assets/...` paths, so the snapshot is faithful to
what the server sent. To browse it, serve the folder at a domain root, not a subpath.

## What Supabase actually does

Airtable is the intake form only — the front door at `/apply`. **Supabase runs everything
after intake.** Read out of the bundle:

**Authentication** — `supabase-js` with GoTrue: developer sign-up and sign-in, admin
sign-in, sessions, `onAuthStateChange`, sign-out. `/admin-login` checks the caller against
an **Admins table**. There is a "Claim admin role (first user)" bootstrap path.

**Developer portal** (`/portal`, gated) — "My projects", "New submission", "Submit a
project", "Documents", "Parcels", "Status".

**Operations console** (`/admin`, gated) — "Pipeline", "Set stage or delete", "Docs to
review", "In underwriting", "Active servicing", "Received", "Parcels", "Notifications".

**A ten-stage pipeline** (`stages-Gnsvj1Oe.js`), each project moving through:

> New Submission → Intake Review → Entitlement Review → Due Diligence → Underwriting →
> Legal Review → Assessment Formation → Funding Coordination → Servicing → Tax Roll

with map/build milestones alongside: Tentative Map, Final Map, Finished Lots,
Finished Houses.

**Tax roll** (`/admin/tax-roll/`) — labelled "Annual Levy Submission", the annual special
tax levy filed with the county.

**Notifications** — `/admin/notifications` and an `/api/broadcast` endpoint, plus Supabase
Edge Functions.

So Airtable captures the first form; Supabase holds the accounts, the deal pipeline, the
documents, the parcels and the levy administration. They are not alternatives to each
other — one feeds the other.

How much real data sits behind that is not visible from outside; these routes are
auth-gated. The capture shows the features exist, not how heavily they are used.

## What is NOT here — read before relying on this

This is a snapshot of the **public front end only**. It is not a restorable backup, and
restoring from it would not bring the service back. Not captured, and not capturable from
outside:

- **The Supabase database** — developer accounts, submissions, the admins table, pipeline
  stages, documents, parcels, levy records. This is the irreplaceable part.
- **Server-function source** — the bundle ships only hashed handler ids
  (`createServerFn`, `auth-middleware`, `admins.functions`, `submissions.functions`); the
  logic runs server-side.
- **The Lovable project source** — the editable app.
- **Environment configuration** — Supabase keys, Airtable credentials, other secrets.

## Where the real backups live

1. **Supabase** — export the database from the Supabase dashboard before any change to the
   site. The account, pipeline and levy data has no other copy.
2. **Lovable project** — the source of truth for the app. If it is connected to a GitHub
   repository, that repo is the actual code backup; check the Lovable project settings.
3. **Airtable** — the intake base backing `/apply`.

## Why this matters for a replacement

The static site at `05_WEBSITE/theme_insite_ca/` (published to
https://obviouslyobvi.github.io/Insite/) has no equivalent of the developer portal, the
operations console, the pipeline, or the tax-roll module. Its `portal.html` is a
placeholder gate page: no form, no authentication, no database. GitHub Pages serves static
files only and cannot run server functions or hold sessions, so pointing insite-ca.org at
it would take all of the above offline.

Worth noting the two sites overlap on content but not on function: `/methodology` on the
live site covers the same underwriting constraints and calculator as the static site's
homepage and fee estimator.
