# Replacing insite-ca.org with the static site — runbook

**Prepared** 2026-08-20

Goal, in your words: back up what Lovable is hosting, store the backup, delete it from
Lovable, and put the site from <https://obviouslyobvi.github.io/Insite/> there instead,
keeping the domain.

The domain part is easier than expected. The backup part has a hole in it that has to be
closed before anything gets deleted. Both are explained below.

---

## Read this first: what the existing backup does and does not cover

`10_ARCHIVE/insite-ca.org_2026-08-19/` holds 33 files — every public page plus the
compiled JS/CSS bundle. It is committed and pushed to GitHub, so it is stored off the
Lovable platform. That much is done.

It is a copy of the **public front end only**. It is not a restorable backup. Four things
are not in it, and none of them can be captured from outside the platform:

| Not backed up | Where it lives | Recoverable after deletion? |
|---|---|---|
| The Supabase database | Supabase project | **No** |
| Server-function source | Lovable project | **No** |
| The editable app source | Lovable project | **No** |
| Environment secrets (Supabase keys, Airtable creds) | Lovable project settings | **No** |

The database is the one that matters. Read out of the shipped bundle, Supabase currently
holds developer accounts and sessions, the admins table, project submissions, uploaded
documents, parcels, the ten-stage pipeline, and the Annual Levy Submission records — the
county tax roll module. Deleting the Lovable project does not by itself delete the
Supabase project, but it deletes the only application that knows how to read any of it.

**So: the site being replaced is not only a marketing site.** Swapping in the static pages
retires the developer portal, the operations console, the pipeline and the levy module.
The static site has no equivalent of any of them — its `portal.html` is a gate page with
no form, no auth and no database behind it.

If that is the intent, fine — this runbook does it. If any of that data or workflow is
still in use, export it before Step 4, because Step 4 is the irreversible one.

---

## Step 1 — Close the backup gap

Only you can do these; they are all behind logins I have no access to.

1. **Export the Supabase database.** Supabase dashboard → your project → Database →
   Backups, or from a terminal:
   ```bash
   supabase db dump -f insite_supabase_2026-08-20.sql --db-url "<connection string>"
   ```
   This is the irreplaceable one.
2. **Get the Lovable app source out.** In the Lovable project: GitHub → Create Repository.
   That pushes the full editable source to a repo you own, which is the only real backup of
   the app. Do this **before** deleting — the project is the only copy today.
3. **Export the Airtable base** behind `/apply` (Airtable → base → Download CSV).
4. **Copy the environment variables** out of Lovable project settings into your password
   manager. Supabase URL and keys at minimum.

Store 1, 3 and 4 somewhere durable. Committing them to this repo is **not** appropriate —
the SQL dump holds personal data and the env file holds live secrets. A password manager or
an encrypted drive.

---

## Step 2 — Stand the replacement up first, before deleting anything

Do not delete, then rebuild. Build the new one alongside, confirm it works, then cut over.

1. Create a new Lovable project.
2. Connect it to GitHub so it has a repo.
3. Push the contents of `05_WEBSITE/lovable_site/` into that repo — that folder is this
   site already packaged with the build config Lovable needs. Its README explains the
   layout. The build is verified: 11 pages, all links and assets resolving, Inter loading,
   no console errors, no overflow at 1440 px and 390 px.
4. Confirm the site works on the project's own `*.lovable.app` preview URL.

Nothing has changed on the live domain at this point, and nothing is deleted.

---

## Step 3 — Move the domain

The good news: **the DNS records do not need to change.**

Current state, confirmed by lookup on 2026-08-20:

| Record | Value |
|---|---|
| `insite-ca.org` A | `185.158.133.1` |
| `www.insite-ca.org` A | `185.158.133.1` |
| `_lovable.insite-ca.org` TXT | `lovable_verify=8defd88a602bf6d23e4b504c076e24c733619a3e8711e36dbbb5fcaf923673c0` |
| AAAA | none — good, Lovable requires none |
| MX | **none** (see the note at the end) |
| Nameservers | `ns1hwy` / `ns2fln` / `ns3fqs` / `ns4jnz.name.com` |

`185.158.133.1` is Lovable's shared edge IP, not an address specific to your project, and
the records are held at name.com rather than by Lovable. So the A records stay exactly as
they are, and deleting the project does not touch them.

What has to change is the **domain attachment inside Lovable**, and Lovable will not let the
same domain sit on two projects at once. That forces this order:

1. Old project → Settings → Domains → remove `insite-ca.org` (and `www`).
2. New project → Settings → Domains → add `insite-ca.org` (and `www`).
3. Lovable will issue a **new** `_lovable` TXT verification value. Replace the existing TXT
   record at name.com with the new one — the value above belongs to the old project and will
   not verify the new one.
4. Wait for verification and SSL issuance.

There is a short window between 1 and 4 where the domain serves nothing. It is the only
unavoidable downtime in the whole exercise, so do this at a quiet hour.

**The new project must be on a paid Lovable plan.** Custom domains are not available on the
free plan; a free project cannot hold `insite-ca.org` at all.

---

## Step 4 — Delete the old project

Only once Step 1 is genuinely done and Step 3 is verified serving the new site.

Lovable project → Settings → Delete project.

This is the irreversible step. After it, the app source, the server functions and the
secrets are gone. The Supabase project survives unless you delete it separately — leave it
alone until you are sure you will not need the data.

---

## What breaks on cutover, and what to do about it

The two sites do not share URLs. These live paths stop existing:

| Live path today | After the swap |
|---|---|
| `/methodology` | gone — nearest is `/fee_estimator.html` |
| `/apply` | gone — nearest is `/developer_application.html` |
| `/apply/success` | gone, no equivalent |
| `/contact` | gone, no equivalent |
| `/login`, `/admin-login` | gone, no equivalent |
| `/portal` | **different meaning** — `/portal.html` is the investor gate page, not the developer portal |
| `/admin`, `/admin/tax-roll`, `/admin/notifications` | gone, no equivalent |

Anything linking to those — bookmarks, email signatures, documents, the Airtable form's
confirmation — will 404. Worth a redirect pass afterwards if any of them were circulated.

The `/portal` collision is the one that will confuse people rather than just 404: the same
URL will start serving a page aimed at a completely different audience.

## One loose end found while checking DNS

There are **no MX records** on insite-ca.org. The live contact page publishes
`hello@insite-ca.org`, but nothing at this domain is set up to receive mail there. Either it
was never wired up, or it forwards through a service that does not require MX at the apex.
Nothing in this migration causes it and nothing here fixes it, but it is worth knowing
before you make a contact address prominent on the new site.
