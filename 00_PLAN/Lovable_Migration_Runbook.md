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

## Step 1 — Give the app its new address first

Do this before touching the apex. The app gains `app.insite-ca.org` while still serving
`insite-ca.org`, so it is never unreachable.

1. Existing Lovable project → Settings → Domains → add `app.insite-ca.org`.
2. At name.com, add the records Lovable shows you:
   - **A** record, host `app`, value `185.158.133.1`
   - **TXT** record, host `_lovable.app`, value the `lovable_verify=...` string Lovable
     generates for this subdomain — a new one, not the value in the table above
3. Wait for verification and SSL.
4. Load `https://app.insite-ca.org`, sign in, confirm the portal works.

Do not continue until that sign-in succeeds.

---

## Step 2 — Build the new site, still without touching the apex

1. Create a second Lovable project, on a paid plan.
2. Connect it to GitHub so it has a repo.
3. Push the contents of `05_WEBSITE/lovable_site/` into that repo. That folder is the site
   already packaged with the build config Lovable needs; its README covers the layout.
   Verified: 11 pages, every link and asset resolving, Inter loading, no console errors, no
   overflow at 1440 px and 390 px.
4. Confirm it works on the project's own `*.lovable.app` preview URL.

Still nothing changed on the live domain.

---

## Step 3 — Hand the apex over

Lovable will not hold the same domain on two projects, so the old project has to let go
before the new one can take it. This is the only step with downtime, and it only affects the
apex — `app.insite-ca.org` keeps serving throughout.

1. **Old** project → Settings → Domains → remove `insite-ca.org` and `www.insite-ca.org`.
   Leave `app.insite-ca.org` in place.
2. **New** project → Settings → Domains → add `insite-ca.org` and `www.insite-ca.org`.
3. Replace the `_lovable.insite-ca.org` TXT value at name.com with the one the new project
   generates. The old value belongs to the old project and will not verify the new one.
4. Leave both apex A records exactly as they are.
5. Wait for verification and SSL, then load `https://insite-ca.org`.

Pick a quiet hour. Between 1 and 5 the front door serves nothing.

---

## Step 4 — Check it over

- `insite-ca.org` and `www.insite-ca.org` serve the new static site
- `app.insite-ca.org` still signs in and loads the portal
- the Airtable form on `/developer_application.html` loads — the one thing that could not be
  verified from the sandbox
- run the calculators on `index.html`, `fee_estimator.html` and `tey_calculator.html`

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

## Two things left open

**Routes that move.** Anything pointing at the old apex paths needs its link updated to the
`app.` subdomain — `/login`, `/admin-login`, `/portal`, `/admin`, `/apply`, `/apply/success`,
`/contact`, `/methodology`. They will 404 on the apex after cutover, because the static site
does not use those paths. Check email signatures, the Airtable form's confirmation message,
and any circulated documents.

**No MX records.** The old contact page publishes `hello@insite-ca.org`, but nothing at this
domain is set up to receive mail there. Not caused by this migration and not fixed by it,
but worth settling before putting a contact address on the new site.
