# Verification Report, July 10, 2026

**Full visual and factual verification of every artifact built to date. Loop run to clean.**

Prepared for Dennis Lanni | HGF Management Company
Method: six verification agents (scripts) plus page-by-page visual inspection, adapted from the visual-verify loop discipline. Loop repeated until the final sweep returned clean.

---

## Agents run

1. **Agent M, mechanical text:** every PDF and markdown scanned for double numbering, mojibake, formatting leaks, em dashes, and recipient-rule violations.
2. **Agent C, locked-corrections compliance:** banned claim phrasing, PACE framing, school-fee exclusion framing, labeled-estimate rules, and the standard pre-launch disclaimer on every document.
3. **Agent D, data recompute:** Census figures recomputed from the downloaded primary files (103,856 total; 62,372 in 1-4 unit structures: match); market math, BOLD average, note-sizing example, and date arithmetic all re-derived: pass.
4. **Agent L, links:** all 50 cited URLs probed.
5. **Agent T, truth audit:** every checklist "done" item asserted against reality (file existence, verify_map.py pass, 13 brand assets readable).
6. **Agent S, sync integrity:** outputs tree hash-compared against the working tree.

Visual pass: every page of every PDF rasterized into labeled contact sheets (plan set, program set, brand assets) and inspected: bands, tables, lists, and footers render correctly; no overflow, blanks, or broken pages.

## Findings and dispositions

| # | Finding | Severity | Disposition |
|---|---|---|---|
| 1 | Seven documents of unknown provenance (INS-002 whitepaper, INS-201 checklist, five OPERATIONS manuals) appeared in the working tree at 05:12-05:18, not produced by this run; on-arrival scan showed recipient-rule violations, 100+ em dashes, and unframed school-fee and PACE mentions | HIGH | Quarantined to 09_QUARANTINE_UNVERIFIED with a README; never synced to the deliverable package; adopt-or-discard decision queued as Q7 |
| 2 | Primer heading said "Twelve questions" after Q13 was added | HIGH | Fixed to Thirteen; rebuilt |
| 3 | INS-003, INS-004, INS-005 footers lacked the full "not an offer of financing" disclaimer | HIGH | Standard disclaimer block applied to all three; rebuilt |
| 4 | Claims Register contained 10 em dashes (banned style) | MED | Replaced; register is markdown-only |
| 5 | CSCDA goals-and-policies PDF returned 404 to direct curl (load-bearing 4:1 citation) | HIGH | Re-verified July 10 via search fetch: document live, 4:1 language confirmed verbatim; stable landing page added to citations. Bonus verification captured: CSCDA's 2 percent total-tax-burden cap, added as claim A3b and folded into INS-003 |
| 6 | Link template with a placeholder tripped the checker | LOW | Reworded in the register |
| 7 | Scanner false positives (disclaimer phrase split by line wrap; "do not say" table rows; register's quoted banned claim) | n/a | Scanner corrected: whitespace normalization and context allowlists; documents were already correct |

## Link check results

42 of 50 URLs return 2xx/3xx. Remainder: cscda.org (406) and four sites returning 403 are bot-blocks, each re-verified readable via search fetch this run; planning.lacity.gov returned 200 on retry (content was fetched and logged during the original research pass); the placeholder template was reworded. No citation in the package rests on a dead source.

## New verifications gained during the loop

- CSCDA 2 percent total-tax-burden policy (claim A3b), now citable in RMA sizing discussions.
- Elk Grove staff report: cities in these programs act as intermediaries with "no financial liability or risk" (claim E6), direct precedent language for the city pitch.

## Residuals, intentionally open

1. DCF workbook: the two known formula defects remain in place pending Dennis's go-ahead to fix (logged since the prior session).
2. Quarantined documents: Q7 decision required.
3. Final skeptic re-pass (checklist 1.12) still gates the end-of-run handoff, as planned.

## Second full-package pass, July 11 (post-completion loop)

All agents re-run against the finished 69-file package. Content findings: **zero**. The loop instead caught and fixed three items in the verification infrastructure itself:

1. **Agent W false negative.** The workbook-defect detector matched relative references (!B9) while the actual formulas use absolute notation (!$B$9), so it reported zero known defects. Pattern corrected; it now detects all 120 defect-bearing cells (2 rows across 60 month columns). The defects themselves are confirmed present and precisely recorded: DCF Model row 5 (Remaining Hard Costs) conditions on and divides by Market Assumptions B9, "Builder Incentives" (value 0), which silently zeroes hard costs instead of spreading them over the 12-month Development Cost Period in B10; row 6 (Remaining Soft Costs) uses B10 where the Soft Cost Period in B11 belongs. Corrected formulas are staged, gated on question 8. Hash comparison proves the carried workbook is bit-identical to the original, so package integrity holds.
2. **Stale quality-control screenshots.** The packaged website captures predated the number-formatting fix and showed uncommaed figures. Both recaptured from the shipped page; the rendered text layer again proves the calculator executes and now reads $2,298.
3. **Human-review pack refreshed.** The image viewer remained unavailable this session (two failed attempts on known-good files), so fresh contact sheets of every current document (plan set, program set, marketing set) were regenerated and packaged at 07_BUILDLOG/qc alongside the deck thumbnails and site screenshots. The one-look human pass before printing remains the standing recommendation.

Re-verified this pass: calculator ($2,298 / $250,000 / zero-rate edge), deck schema (All validations PASSED), structure map audit (PASS), Census recompute from primary files (match), outputs hash sync (zero stale), quarantine still excluded from deliverables. Links: 51 checked, 48 clean; the three failures are the same bot-blocked pages (Elk Grove program page, one law-blog explainer, Vacaville program page), each previously verified readable through a second route; no citation rests on a dead source.

## Third pass, July 11: a defect the loop missed, and the agent that now exists because of it

A human browser caught what two automated loops did not: inside the navy who-it-serves band of the website, the white audience cards inherited the band's light text colors, rendering headings white-on-white (contrast ratio 1.00) and bullets at 1.17. Why every prior check was blind to it: the text-layer sweeps verify that words exist regardless of color; the token checks matched every string; and the ink-density audit classified the pale text as background (the text color sums to 715 on a 0-765 scale against a threshold of 650). Presence, structure, and execution were all verified; legibility never was.

The fix is three CSS rules. The lasting fix is tools/contrast_check.py, a contrast agent that injects a script computing the WCAG contrast ratio of every text-bearing element against its effective background and reports through the proven render pipeline. On the pre-fix page it flags all 15 failures; the fixed page and all four other web artifacts pass at 3.0:1 or better. Screenshots recaptured; card-band dark-ink measurement confirms visible text where there was none.
## Package-wide School audit, July 11 (Palmer's directive)

Six extraction agents swept every format in the package for school-fee references: PDFs, markdown, web pages and page sources, the deck including table cells and speaker notes, spreadsheets including headers and document properties, Word documents including tables and headers, SVG text, and even the build scripts. Every hit was classified, because the standing policy makes some mentions mandatory while name-usage is the defect.

The verdict: **zero uses of the retired program name anywhere in the live package.** The 160 total hits break down as: 55 required exclusion notes across 32 files (the "school fees are excluded at launch" language the locked corrections mandate on every audience surface, present exactly where it should be); 61 record and decision-history mentions across 19 files (question 3, correction entries, audit findings, the brand kit's retired-tagline note); 32 hits in 16 archived files (quarantine originals and the archived v1 workbook, preserved as received and exempt by design); and 12 review items that all resolved benign on inspection: two decision-record sentences in the pre-build brief, evidence references to school **districts** as CFD administrators in the sourcing memo (Temecula Valley Unified, from the verified register), the deliberately retained naming open-item in INS-010, and INS-202's school-facilities roadmap line.

The audit's bonus catch: that INS-202 line cites Education Code 17620 and Government Code 65995, two statutes the earlier operations-manual verification never checked because its number pattern matched neither a five-digit section starting with 6 nor an Education Code section at all. Both are now verified against the Treasurer's own Debt Financing Guide (Appendix B.1.4.2) and entered as register claim G5. The statute-scan pattern is corrected accordingly.

**Status: final sweep CLEAN. Package integrity confirmed. The user-visible outputs tree was never contaminated by the quarantined files.**

*INSITE(TM) is a pre-launch program concept administered by HGF Management Company. Internal quality-control record. Not an offer of financing, legal advice, or investment advice.*
