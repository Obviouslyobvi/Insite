# insite-ca.org — snapshot of the Lovable production site

**Captured** 2026-08-19, 20:55 PDT (2026-08-20 03:55 UTC)
**Host** Lovable, `185.158.133.1`, fronted by Cloudflare
**Deployment id** `647f70bb408ee52c8ee0a5dc845ab084326aa4b48b23d966a97fb0cb701caf94`

A capture of everything insite-ca.org serves publicly, taken before any discussion of
replacing it. All 20 files returned HTTP 200.

## What is here

| | |
|---|---|
| `index.html` | Home — the eight-stage workflow marketing page |
| `apply.html` | `/apply` — intake page wrapping the Airtable form |
| `login.html` | `/login` — Developer Portal sign-in |
| `admin-login.html` | `/admin-login` — administration sign-in |
| `contact.html` | `/contact` — contact form, hello@insite-ca.org |
| `assets/` | The compiled client bundle: 13 JS/CSS files and the two portal screenshots |

The HTML keeps its original absolute `/assets/...` paths, so the snapshot is faithful to
what the server sent. To browse it, serve the folder at a domain root rather than a
subpath.

## What is NOT here — read before relying on this

This is a snapshot of the **public front end only**. It is not a restorable backup of the
application, and restoring from it would not bring the service back.

insite-ca.org is a full-stack app, not a static site. The bundle contains
`createServerFn`, `auth-middleware`, `admins.functions` and `submissions.functions`,
and `/admin-login` states plainly that it authenticates against Supabase and checks the
caller against an **Admins table**. None of the following is captured here, and none of it
can be captured from outside:

- **The Supabase database** — developer accounts, submitted applications, the admins
  table, and any application history or status tracking. This is the irreplaceable part.
- **Server-function source** — only the compiled client bundle is public.
- **The Lovable project source** — the editable app.
- **Environment configuration** — Supabase keys, Airtable credentials, any other secrets.

## Where the real backups live

1. **Lovable project** — the source of truth for the app. If the project is connected to
   a GitHub repository, that repo is the actual code backup; check the Lovable project
   settings.
2. **Supabase** — take a database backup/export from the Supabase dashboard before any
   change to the site. The account and submission data has no other copy.
3. **Airtable** — the intake base backing `/apply`.

## Why this matters for a replacement

The static site at `05_WEBSITE/theme_insite_ca/` (published to
https://obviouslyobvi.github.io/Insite/) has no equivalent of the developer portal, the
admin sign-in, or the Supabase-backed submission tracking. Its `portal.html` is a
placeholder gate page: no form, no authentication, no database. Pointing insite-ca.org at
GitHub Pages would take those functions offline, because GitHub Pages serves static files
only and cannot run server functions or hold sessions.
