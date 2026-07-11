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

**Status: final sweep CLEAN. Package integrity confirmed. The user-visible outputs tree was never contaminated by the quarantined files.**

*INSITE(TM) is a pre-launch program concept administered by HGF Management Company. Internal quality-control record. Not an offer of financing, legal advice, or investment advice.*
