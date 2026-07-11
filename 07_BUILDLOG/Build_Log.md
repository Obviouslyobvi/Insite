# INSITE Build Log

**Decisions, corrections, cuts, and the consolidated question batch.**

Prepared for Dennis Lanni | HGF Management Company | July 2026

---

## Part 1: The question batch (each with the builder's working answer)

1. **The name.** A software company holds a live federal trademark on "INSITE" in a different industry. Clear the name with a trademark attorney before anything goes public, and keep one backup name ready? Working answer: yes to both; the risk is cheap to retire now and expensive later.
2. **The web address.** Available today: insiteprogram.com, insitecalifornia.com, insitecfd.com. Nothing purchased. Which one? Working answer: insiteprogram.com; cleanest, and still works outside California.
3. **The word "School."** School fees are excluded at launch, so should the public name drop the word until the program can deliver it? Working answer: drop it now; every current document already reads "Development Impact Fee Financing Program."
4. **Talking about the pilot.** Generic ("a small finished-lot subdivision in the Sacramento area") or specific (lot count, city, dates)? And does the landowner need to approve public mention? Working answer: generic in print until documents are signed; the package is built that way.
5. **The company name on documents.** HGF Management Company appears everywhere. Final, or is a new legal entity coming? Working answer: HGF stays on drafts; hold any print run until the entity question settles.
6. **Picking the outside team.** Choose the tax formula consultant, the annual tax roll administrator, and the bond attorney; ask the city and county which firms they already trust so the shortlist starts familiar; confirm the retired county administrator's named advisor role and get a one-page bio. Working answer: familiarity is the whole point, so start with the issuer's own vendor list (selection criteria are in the sourcing and credibility documents).
7. **Sacramento County timing.** Open the county conversation now, in parallel, or after the city pilot closes? Working answer: one informal coffee now, the formal ask after the pilot.
8. **The spreadsheet fix.** The bulk-sale analysis workbook has two formula errors (a wrong-cell reference that triggers the divide-by-zero cascade, and an off-by-one row reference). Fix both in a corrected copy, original untouched? Working answer: yes.
9. **The mystery drafts.** Seven documents of unknown origin (a whitepaper, a developer checklist, five operations manuals) were found mid-build, failed quality scans, and sit in quarantine. Scrub and adopt, or discard and build fresh under the locked rules? Working answer: build fresh; the whitepaper and checklist were already rebuilt clean, so the quarantine now mainly holds the operations manuals.
10. **The minimum deal size.** No verified minimum exists, so the intake form says "determined during feasibility screening." What floor, if any, should be published? Working answer: publish none until pilot economics are real; a made-up floor is exactly the kind of number this program refuses to print.

## Part 2: Decisions log

1. Plan-first discipline enforced after a sequencing error on day one: the Master Plan is now always delivered before any build work, and that rule is saved as a standing memory.
2. Documents are prepared for Dennis Lanni only; the builder is not a recipient or principal (standing rule, applied retroactively across the package).
3. The public program name drops "School" pending question 3; restoring it is a single token swap.
4. The pilot is described generically on every external surface pending question 4.
5. Issuer-neutral drafting everywhere, so a later joint powers authority requires no redrafting (per the issuer strategy memo).
6. The whitepaper and developer checklist were rebuilt fresh rather than salvaged from quarantine (default under question 9).
7. Quarantine over deletion for the unknown-provenance drafts: preserved, labeled, excluded from deliverables.
8. The calculator gained a labeled coverage-cushion input so the website and whitepaper produce the same example figure from the same inputs.
9. Marketing pieces carry a securities-offer sentence in addition to the standard disclaimer; the capital brief leads with what is unproven.
10. Verification posture during the image-viewer outage: mechanical audits (schema validators, token sweeps, unit tests, pixel and structure analysis) plus packaged screenshots and thumbnails for human eyes; nothing shipped on trust.
11. Operations manuals adopted from quarantine at Palmer's direction (July 11): authorship resolved as Dennis Lanni, which reframed the thirteen draft service levels as founder policy pending his confirmation; corrections applied (name, builder reference, disclaimers) with claims verified into the register's new G-series; the project's em dash rule was lifted by Palmer the same day.
12. Workbook corrected on Palmer's go-ahead (July 11), resolving question 8: both defects fixed in v1.1_corrected with the v1 original preserved; 120 cells changed and nothing else (diff-guarded), full recalculation clean, and the fix demonstrated by injecting identical test inputs into both files: the original zeroes hard costs, the corrected copy spreads them over the Development Cost Period and stops.

## Part 3: Corrections log (what was caught, by whom, and what changed)

1. Structure map: flow 4 was caption text and one box was orphaned (caught by the builder's review, credited in checklist 0.7); fixed, and verify_map.py now mechanically enforces unbroken numbering and connectivity.
2. Master Plan delivery sequencing (caught by the builder's review): plan now ships first, always.
3. Markdown converter double-numbered every ordered list (caught by the text sweep); fixed, and affected PDFs rebuilt.
4. County permit table variances against the Census county file (caught by data recompute); table rebuilt from the primary file with a methodology note.
5. Appendix E runs E.1 to E.10, not E.8 as earlier notes said (caught by re-reading the source); INS-201 built to the real structure.
6. wkhtmltopdf silently shrinks SVG text without explicit width/height (caught by structural ASCII audit); logo masters fixed.
7. The rendering engine drops thousands-separators from locale formatting (caught by the JavaScript execution proof); the calculator formats numbers manually.
8. The em dash ban is enforced mechanically across every artifact.
9. The CSCDA policy citation appeared dead to direct fetch; re-verified live through a second route, and the chase yielded two new verified claims (the 2 percent burden cap and the Elk Grove no-liability language).
10. Website contrast defect (caught by the builder's own browser, July 11): the navy who-it-serves band's light text colors cascaded into the white cards, leaving headings white-on-white and bullets at a 1.17 contrast ratio. Root cause of the verification miss: every automated check verified text presence and structure, never rendered legibility, and the ink threshold classified the pale text as background. Fixed with explicit card color rules, and a permanent WCAG contrast agent (tools/contrast_check.py) now runs on every web artifact; it detects all 15 pre-fix failures and passes the fixed set.

## Part 4: Cut list and 80 percent notes

1. INS-001 remains a legacy draft plus the one-page Brand Kit rather than a rebuilt 40-to-60-page manual; consolidation is scheduled, not skipped.
2. The operations manual series (400/500/600) is deferred behind question 9.
3. Word exports are clean but plainly styled (converter output); the branded artifact of record is the PDF.
4. No jurisdiction fee schedules are quoted; the documents point to posted schedules instead.
5. Contact details, domain, and any public deployment are deliberately absent pending questions 1, 2, and 5.
6. Human eyeball passes on the website screenshots, deck thumbnails, and marketing pages are recommended before printing, because the session's image viewer failed and mechanical audits stood in.

*INSITE(TM) is a pre-launch program concept administered by HGF Management Company. Internal record. Not an offer of financing, legal advice, or investment advice.*
