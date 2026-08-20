# insite-ca.org — putting the static site on the front door, keeping the app

**Prepared** 2026-08-20 · **Approach:** subdomain split

The static site from <https://obviouslyobvi.github.io/Insite/> takes over `insite-ca.org`.
The existing Lovable app moves to `app.insite-ca.org` and keeps running.

| Address | Serves | Lovable project |
|---|---|---|
| `insite-ca.org`, `www.insite-ca.org` | the new static site | **new** project |
| `app.insite-ca.org` | developer portal, admin pipeline, tax roll | **existing** project, untouched |

Nothing is deleted. Nothing is rewritten. No database migration, and no security audit —
the app keeps enforcing its own permissions exactly as it does today.

The cost is that the existing Lovable project stays on a paid plan. That is the trade being
made, and it buys away every irreversible step in the alternative.

---

## Why this beats deleting the app

Reading the code the live site ships to every browser: the browser never touches the
database. Not one query. It uses Supabase for sign-in only — `getUser`, `getSession`,
`onAuthStateChange`, `signOut`.

Everything else goes through a server function:

```js
const m = r({method:"POST"})
  .middleware([e])                                 // permission check
  .handler(a("5995bb8d490f91cfcfaa07e86a6227b3..."));  // logic, server-side
```

That hash is a pointer to code that runs on Lovable's server and was never sent to the
browser. It is not in `10_ARCHIVE/`, and it cannot be recovered from outside the platform.
The same is true for submissions, documents, parcels, pipeline stages and the levy module.

So the app's working half exists in exactly one place. Keeping the project keeps it.

It also sidesteps a live hazard. Because permissions are enforced in those server functions,
the database's own Row Level Security may well be permissive — it never needed to be strict,
since nothing could reach the database except the server. Wiring static pages directly to
Supabase without auditing every table first would publish developer records, uploaded
documents, the admins table and the levy data to anyone who views source. This approach
never goes near that.

---

## Why `app.` and not `portal.`

`portal.insite-ca.org` is available, but it collides. The static site already ships
`portal.html`, and that page is the **Investor Portal** — "Access for capital partners under
review". The Lovable app's `/portal` is the **Developer Portal** — My Projects, submissions.

Two different audiences, one word. Use `app.` and the ambiguity never arises.

---

## Current DNS

Confirmed by lookup, 2026-08-20. Records are held at **name.com**, not by Lovable.

| Record | Value |
|---|---|
| `insite-ca.org` A | `185.158.133.1` |
| `www.insite-ca.org` A | `185.158.133.1` |
| `_lovable.insite-ca.org` TXT | `lovable_verify=8defd88a602bf6d23e4b504c076e24c733619a3e8711e36dbbb5fcaf923673c0` |
| AAAA | none — good, Lovable requires none |
| MX | none (see the loose end at the bottom) |

`185.158.133.1` is Lovable's **shared** edge IP — every Lovable site resolves there. It is
not specific to your project, which is why the apex A records never have to change. What
decides which project answers is the domain attachment inside Lovable, plus the `_lovable`
TXT value.

---

## Where things stand — 2026-08-20

Step numbering changed partway through when downtime stopped being a constraint, so track
progress by this list rather than by the numbers below.

**Done**

- Lovable app source pushed to its own GitHub repository
- `hello@insite-ca.org` mail routing resolved separately
- `app.insite-ca.org` added to the **existing** project (`assess-mint-hub`), A record and
  `_lovable.app` TXT in place at name.com, verified and SSL issued

  It currently 302s to `insite-ca.org`, because the apex is still the project's primary
  domain. Expected, not a fault. It clears when the apex is removed — see the redirect check
  in Step 3.

- The **second** Lovable project exists, connected to
  `github.com/Obviouslyobvi/insite-public-pages`, and the site is pushed (commit
  `1e2a0d3`). Step 1 below describes what was actually done, which differs from the
  original packaging plan.

- Verified live at `https://happy-public-view.lovable.app`: `/` 301s to `/index.html`, all
  11 pages and all 6 assets return 200, and the served HTML is byte-identical to the
  GitHub Pages source. The gate before cutover is passed.

- **The cutover is done — 2026-08-20, verified live.** `insite-ca.org` serves the static
  site: `/` 301s to `/index.html`, all 11 pages and all 6 assets return 200, served HTML
  byte-identical to source, `www` 302s to the apex. The domain moved via Lovable's own
  "Move and connect" dialog, which handled the release-and-claim in one action and updated
  the `_lovable` TXT verification. `app.insite-ca.org` self-promoted to primary on the old
  project and serves the portal directly — `/`, `/login`, `/portal` all 200, no redirect.

**Remaining**

- Test a real sign-in and a **password reset** on `app.insite-ca.org` — the reset email
  must land back on `app.`, not the apex. Supabase dashboard access is unavailable, so if
  the reset misroutes, the fix lives in the app project's backend settings inside Lovable.
- Post-cutover tidy-up: see `Link_Map.md` for the two investors.html links that must be
  relocalized **before** making the Insite repo private; then retire the gh-pages workflow
  and consider repo visibility.

---

## The one rule that still holds

Downtime is acceptable, so the steps below run in a single sitting rather than waiting for
each address to settle before starting the next.

One constraint survives that relaxation, and it is not about downtime: **do not release the
apex until the new site is built and confirmed working on its own `*.lovable.app` URL.**
Release it first and the domain points at nothing while you have no verified target to hand
it to — a paid-plan block or a rejected verification then turns a planned outage into an
open-ended one. Steps 1 and 2 change nothing live, so there is no cost to doing them first.

---

## Step 1 — Build the new site (nothing live changes)

Touches no DNS and no existing project. Can be done at any time, including right now.

This is a **second, separate Lovable project**, alongside the existing `assess-mint-hub`
one. The app stays where it is; this new project exists only to serve the static site.

1. Create a second Lovable project.

   This does **not** mean a second subscription. Lovable bills per account, not per
   project: one paid plan covers the whole account, and custom domains are a plan-level
   feature rather than a per-project purchase. The metered resource is credits, which are
   spent on AI editing — this project is pushed from GitHub and never edited in Lovable, so
   it burns effectively none. Lovable's docs do not publish a cap on custom domains per
   plan; two is unlikely to approach one, but it is undocumented rather than confirmed.
2. Connect it to GitHub so it has a repo.
3. Get the site into that repo — **done, and done differently than first planned.**

   The original plan was to replace the repo contents with `05_WEBSITE/lovable_site/`, the
   standalone Vite package. On inspection, Lovable's GitHub connect had scaffolded a full
   TanStack Start app and stamped the project's template into `.lovable/project.json` —
   the same machinery its build pipeline is keyed to. Gutting that risked a fight with the
   deploy side that could not be tested from outside.

   What shipped instead, in `Obviouslyobvi/insite-public-pages` commit `1e2a0d3`:
   - the scaffold left intact, so Lovable's pipeline and editor keep working;
   - all 11 pages, 4 diagrams, the Inter font and manual.pdf placed in `public/`, which is
     served verbatim at the site root — byte-identical to the GitHub Pages copy, no build
     step touching the pages at all;
   - one source change: the index route 301s `/` to `/index.html`, where every internal
     link on the site already points.

   Verified against a local build and dev server: all 19 files carried into the build
   output unchanged; `/` redirects 301; all 11 pages and all 6 assets return 200 with the
   expected titles.

   `05_WEBSITE/lovable_site/` remains in this repository as the standalone fallback — if
   Lovable's pipeline ever objects to serving from `public/`, that package is the verified
   plan B, at the cost of leaving Lovable's template.
4. Open the project's `*.lovable.app` preview URL and click through the pages. A **Publish**
   click in Lovable may be needed before the `*.lovable.app` URL reflects the push.

Do not start Step 3 until that preview looks right.

---

## Step 2 — Widen the Supabase allowlist (nothing live changes)

Additive only. The app keeps working exactly as it does now.

In the Supabase dashboard → **Authentication → URL Configuration**, add
`https://app.insite-ca.org/**` to **Redirect URLs**. Leave `https://insite-ca.org/**` in
place and leave **Site URL** alone for now — both are still in use until the switchover.

### Why this matters more than it looks

The app builds its auth redirect URLs from `window.location.origin`. Read out of the
bundle: 23 uses of `redirectTo`, 5 of `emailRedirectTo`, and **no hardcoded domain
anywhere**. So the app adapts to a new address on its own, with no code change.

Supabase does not. It keeps its own allowlist, rejects any redirect URL not on it, and
falls back silently to whatever **Site URL** says.

Miss this and the failure is nastier than an outright error. Sign-in looks fine, then every
password reset and email confirmation link drops the user on `insite-ca.org` — by then the
static site, with no portal and no session. It reads as "the reset link is broken", and the
cause is nowhere near where it appears.

---

## Step 3 — The switchover (the site is down through this)

All of it in one sitting. Order within the step does not matter much now, but this sequence
means the least waiting.

**In Lovable, old project** → Settings → Domains:
1. Add `app.insite-ca.org`. Note the `lovable_verify=...` value it generates.
2. Remove `insite-ca.org` and `www.insite-ca.org`.

**In Lovable, new project** → Settings → Domains:
3. Add `insite-ca.org` and `www.insite-ca.org`. Note the new `lovable_verify=...` value.

**At name.com** → DNS records:
4. **Add** an A record — host `app`, value `185.158.133.1`.
5. **Add** a TXT record — host `_lovable.app`, value the string from (1).
6. **Replace** the existing `_lovable` TXT value with the string from (3). The current
   value belongs to the old project and will not verify the new one.
7. **Leave both apex A records alone.** They already point at the right place.

Host fields at name.com are relative — enter `app`, not `app.insite-ca.org`.

The two verification records live at different hostnames — `_lovable.insite-ca.org` and
`_lovable.app.insite-ca.org` — so they do not collide.

8. Wait for both projects to verify and issue SSL. Minutes usually, up to an hour.

### Then check the redirect cleared

Lovable marks one domain per project as **primary** — the starred one in Settings → Domains
— and 302s every other domain on that project to it. While the old project held both, this
was live and harmless:

```
https://app.insite-ca.org/  →  302  →  https://insite-ca.org/
```

Once the apex is removed, `app.insite-ca.org` is the only domain left on that project and
should become primary on its own. Confirm it rather than assume it:

```bash
curl -sI https://app.insite-ca.org/ | head -1     # want: HTTP/2 200, not 302
```

A 302 still pointing at `insite-ca.org` after the apex is gone means the portal is bouncing
visitors to the static site. Fix it by starring `app.insite-ca.org` as primary in the old
project's domain settings.

Do not star `app.` *before* removing the apex — that flips the redirect the other way and
sends the live site to the subdomain early.

---

## Step 4 — Point Supabase at the new home

Once `app.insite-ca.org` loads, go back to **Authentication → URL Configuration** and set
**Site URL** to `https://app.insite-ca.org`.

Then sign in, and run **one password reset**. The plain sign-in path does not exercise the
redirect allowlist; the reset does. That is the test that actually proves Step 2 worked.

---

## Step 5 — Check it over

- `insite-ca.org` and `www.insite-ca.org` serve the new static site
- `app.insite-ca.org` returns **200, not a 302** — see the redirect check in Step 3
- `app.insite-ca.org` signs in and loads the portal
- a **password reset** email lands back on `app.insite-ca.org`, not on the static site
- the Airtable form on `/developer_application.html` loads — the one thing that could not be
  verified from the sandbox
- run the calculators on `index.html`, `fee_estimator.html` and `tey_calculator.html`

Then tidy up: remove `https://insite-ca.org/**` from the Supabase redirect allowlist, now
that nothing should be redirecting there.

---

## Backups — still worth doing, just no longer urgent

Nothing here deletes anything, so none of this is now load-bearing. It is ordinary hygiene,
and the first item is the one to actually do.

1. **Push the Lovable app to GitHub.** In the existing project: GitHub → Create Repository.
   One click, no effect on the live site, and it turns the app source from
   single-copy-inside-a-vendor into something you hold. Worth doing today regardless of any
   of the above.
2. **Export the Supabase database** — dashboard → Database → Backups, or
   `supabase db dump -f insite_supabase_2026-08-20.sql --db-url "<connection string>"`.
   Project ref `diictbhvwszujxplobsz`.
3. **Export the Airtable base** behind the application form.
4. **Copy the environment variables** out of Lovable settings into a password manager.

Do not commit 2 or 4 to this repository. The dump holds personal data; the env file holds
live credentials.

`10_ARCHIVE/insite-ca.org_2026-08-19/` stays as-is: a faithful record of what the public
site looked like on that date, and useful as a reference for the old page copy.

---

## Decided: the public site does not link to the portal

Developers reach it at `app.insite-ca.org` directly. All 11 pages stay byte-identical to
what is published at github.io, and no nav copy changes.

A "Developer Login" nav item was tried and backed out. The nav has no slack: measured at
1440 px, the header is 86 px tall, and a seventh item wraps it to a second row at 145 px on
every page. If this is revisited, these are the combinations that were measured to fit:

| Change | Header height |
|---|---|
| "Fee Estimator" → "Fees", add **Login** | 86 px — fits |
| "Do I Qualify?" → "Qualify", add **Login** | 86 px — fits |
| Both shortened, add **Developer Login** | 86 px — fits |
| Labels unchanged, add **Developer Login** | 145 px — wraps |

A footer link is the other route, and needs no nav copy change, but only 5 of the 11 pages
carry a `<footer>` element today — `index`, `developers`, `investors`, `qualify`,
`qualify2` — so it would either cover those five or mean adding a footer to the other six.

## Unrelated, and more urgent than any of the above: the repo is public

`github.com/Obviouslyobvi/Insite` is readable without a login. Verified 2026-08-20 — all
returned 200 unauthenticated:

- `00_PLAN/Payment_Summary_2026-07-29.md`
- `00_PLAN/Whats_Missing.md`
- `00_PLAN/HANDOFF.md`
- `01_EVIDENCE/Claims_Register.md`
- `07_BUILDLOG/Quarantine_Audit.md`

`08_REDTEAM/Kill_Memo.md` is in the same tree.

The gh-pages workflow deliberately excludes the evidence register, red-team memo, build log
and quarantine from what it publishes to the website branch. That precaution is moot while
the repository itself is public: everything on `master` is readable regardless.

Not changed here, because it is a judgement call with a side effect. Making the repository
private stops GitHub Pages serving `obviouslyobvi.github.io/Insite` unless the account is on
a plan that allows Pages from private repositories. If the static site has moved to Lovable
by then, that no longer matters — which makes the cutover the natural moment to close this.

## Two things left open

**Routes that move.** Anything pointing at the old apex paths needs its link updated to the
`app.` subdomain — `/login`, `/admin-login`, `/portal`, `/admin`, `/apply`, `/apply/success`,
`/contact`, `/methodology`. They will 404 on the apex after cutover, because the static site
does not use those paths. Check email signatures, the Airtable form's confirmation message,
and any circulated documents.

**No MX records.** The old contact page publishes `hello@insite-ca.org`, but nothing at this
domain is set up to receive mail there. Not caused by this migration and not fixed by it,
but worth settling before putting a contact address on the new site.
