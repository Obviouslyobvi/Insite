# INSITE(TM) Build Checklist

Every item in the package, tracked live. Plan control document, companion to the Master Plan.
Legend: [x] done and verified | [~] in progress | [ ] not started | [!] needs Dennis's input (also logged in Build Log)
Updated: July 9, 2026 (rev 2: map corrections)

## 0. Plan and controls (00_PLAN)
- [x] 0.1 Master Plan, markdown source
- [x] 0.2 Master Plan, branded PDF, visually QC'd page by page
- [x] 0.3 Program Structure Map, SVG master (parties, flows 1-8, annexation model, servicing loop)
- [x] 0.4 Program Structure Map, PDF, collision-checked and re-rendered
- [x] 0.5 Build Checklist (this document) + PDF
- [x] 0.6 Standing rule saved: plan is presented before anything is built
- [x] 0.7 Correction (July 9, caught in review): flow 4 was caption text, not a numbered node, and the Specialty Consultants box was orphaned. Both fixed. Added verify_map.py: mechanical audit for unbroken 1..N numbering and box connectivity; now passing and runs before any map ships
- [x] 0.8 Correction (July 9, standing rule from Dennis): documents are prepared for Dennis Lanni only; Gene Palmer is not a company principal and does the build work. Recipient lines corrected across Master Plan, Build Checklist, INS-000, INS-003, INS-004; rule saved as a standing memory
- [x] 0.9 Full verification sweep (July 10): six agents (mechanical, compliance, data recompute, links, truth audit, sync) plus page-by-page visual contact sheets; seven findings fixed; final sweep CLEAN; report filed at 07_BUILDLOG/Verification_Report_2026-07-10
- [x] 0.10 Quarantine event (July 10): seven unknown-provenance documents (INS-002, INS-201, OPERATIONS set) found in the working tree, failed on-arrival scans, moved to 09_QUARANTINE_UNVERIFIED, never synced to outputs; decision queued as Q7
- [x] 0.11 Second full verification loop (July 11, post-completion): zero content findings across all agents; three verification-infrastructure fixes (workbook-defect detector matched relative not absolute references, corrected and defects precisely recorded with staged fixes; stale website screenshots recaptured from the shipped page; human-review contact-sheet pack regenerated at 07_BUILDLOG/qc). Links 48 of 51 clean, remainder bot-blocked and previously verified via second route

## 1. Evidence base (01_EVIDENCE)
- [x] 1.1 Claims Register with verdict per claim (A1-F5), every claim URL-sourced or flagged
- [x] 1.2 Statutes verified: Mello-Roos Act 53311 et seq.; 53345.8 (3:1 statutory value-to-lien); CDIAC appraisal standards
- [x] 1.3 Mitigation Fee Act 66000-66025 + AB 602 transparency rules verified
- [x] 1.4 SB 684 (2023) + SB 1123 (2024) ministerial 10-lot pathway verified
- [x] 1.5 Competitors verified: SCIP (CSCDA; ~$500K typical minimum, ~4-5% issuance costs, pooled ~3x/yr) and BOLD (CMFA; ~$550M, 65+ projects, 12,000+ units since 2020)
- [x] 1.6 Fee burden verified: Terner Center studies ($23,455 avg SF fee 2015, ~3x national; can exceed $150K/unit; LIHTC 2020-23 avg ~$19,806/unit)
- [x] 1.7 Market size verified against Census primary files: CA 2025 = 103,856 total units; 62,372 in 1-4 unit structures (internal figures matched exactly)
- [x] 1.8 County table rebuilt from Census county file; variances vs. earlier internal table logged
- [x] 1.9 Private lending rate range verified (~9.5-15% in 2025-26)
- [x] 1.10 Domain RDAP checks (available: insiteprogram.com, insitecalifornia.com, insitecfd.com; nothing purchased)
- [x] 1.11 Preliminary trademark screen (live INSITE registration exists in software class; counsel clearance flagged)
- [x] 1.12 Final skeptic sweep across all 36 canonical artifacts including table-aware deck text and website text; handout set CLEAN after the primer pilot line was genericized; verify_map PASS

## 2. Program documents (02_PROGRAM)
- [x] 2.0 INS-000 Plain-Language Primer (soup-to-nuts education for stakeholder conversations): md + branded PDF; content mechanically verified; converter double-numbering bug found and fixed, Master Plan PDF rebuilt with the same fix
- [x] 2.0a INS-003 RMA Design and Issuer Strategy memo (md + PDF): zone-per-annexation RMA template design with cited precedents (Escondido, Chula Vista, Roseville, ABAG); JPA decision framed with hybrid recommendation and jurisdiction-three gate; five questions queued for bond counsel; reusable tools/md2pdf.py converter added
- [x] 2.0b INS-004 Sourcing Strategy memo (md + PDF): three-rule split (independence functions never in-house; design bought once and owned; administration contracted with shadow/transition clauses then insourced on four triggers); verified that San Diego, Vacaville, Union City, TVUSD, and ABAG all contract CFD administration; Section 53317(d) cost recovery documented
- [x] 2.0c INS-005 Credibility Plan (md + PDF): direct response to Dennis's July 9 track-record email; five pillars (borrowed tenure, 44-year-old mechanism, policy conservatism, BOLD-from-zero precedent, transparency brand); scripted talk track for city, developer, and capital audiences; consultant selection criteria; primer Q&A extended with Q13
- [x] 2.0d INS-002 Pre-Build Brief (md + PDF): defaults, caveats, and Dennis-needs stated before the whitepaper, per instruction
- [x] 2.1 INS-002 Program Whitepaper, docx: executive summary; the problem (fee burden + capital cost); the mechanism (CFD annexation); structure and roles table (issuer vs. INSITE); underwriting policy (4:1 over 3:1 floor); eligible costs (school fees excluded initially); market analysis with shown arithmetic; competitive landscape (SCIP/BOLD positioning); pilot description; phased JPA/direct-city strategy; risk factors; disclaimers
- [x] 2.2 INS-002 Whitepaper rendered: branded PDF (5 pages, structure map embedded on p.3, confirmed via image extraction), editable docx (pandoc, opens clean: 58 paragraphs, 2 tables), content sweep CLEAN (all locked corrections hold; pilot generic; School dropped; consultant seats marked in progress)
- [x] 2.3 INS-201 Developer Data Package Checklist built fresh from Dennis's Appendix E source (which runs E.1-E.10, correcting the earlier E.1-E.8 note): md + branded PDF + editable docx (12 tables); adds project-info block, submission rules with file-naming convention, eligibility snapshot, per-section purpose note, and an administrator verification box; 65 checkbox rows confirmed in the PDF text layer (55 document items + 10 verification items); sweep CLEAN
- [x] 2.4 Document Library Register built (md + PDF): 15 entries, status and next action for every publication number
- [x] 2.5 INS-102A DCF/Bulk Sale Workbook v1 carried into package (existing asset, reviewed)
- [x] 2.6 Fix list for existing manuals logged inside the Document Library Register (INS-101 cover typo; INS-102 footer mislabel; workbook defects pending question 8)

## 3. Brand (04_BRAND)
- [x] 3.1 Brand kit one-pager (PDF + html source): colors with usage, type system as built (Helvetica headings, Georgia long-form), logo system with clear-space and misuse rules, voice values and writing rules from INS-001, standard disclaimer verbatim; single page confirmed
- [x] 3.2 Logo SVG masters built: INSITE_Mark, INSITE_Logo_Horizontal, INSITE_Logo_Reversed; 4x4 grid with green staircase cluster reconstructed by pixel analysis of the legacy header; tagline drops School per standing decision; legacy Header_2.png marked retired; wkhtmltopdf SVG-text scaling bug found and fixed (explicit width/height), rasters autocropped
- [x] 3.3 Existing icon/asset set carried into package (11 PNGs)
- [x] 3.4 Standard_Disclaimer.md created; identical block verified present in all four new PDFs

## 4. Marketing one-pagers (03_MARKETING)
- [x] 4.1 Developer one-pager PDF: fee-timing squeeze with Terner numbers, four-step process, eligibility box, labeled cost targets, feasibility-screening call to action (contact details deferred to launch); 1 page
- [x] 4.2 City/agency brief PDF: once-only issuer actions (53312.7 policies, master district), never-does list with the Elk Grove "no financial liability or risk" quote (8 words, cited), resident protections incl. 53321(d) and the 2 percent burden benchmark, precedent districts and programs; 1 page
- [x] 4.3 Capital partner brief PDF: security stack (lien, 4:1, zone isolation 53339.3(d), 53321(d)), servicing model, pipeline math with labeled assumption, a read-this-first honesty box, securities-offer disclaimer added; 1 page
- [x] 4.4 Sweep CLEAN on all four PDFs: token checks against the Claims Register, quote-length guard, no banned phrases, School absent from program name. Note: the image viewer was returning blanks this session, so page inspection used mechanical audits (single-page confirmation, embedded-image counts, band and ink-density checks) on the same pipeline visually verified earlier

## 5. Website (05_WEBSITE)
- [x] 5.1 Single-file index.html, self-contained: zero external assets confirmed by scan (system fonts, inline SVG logo, inline CSS/JS); citation links are navigation only
- [x] 5.2 Sections built: pre-launch banner, hero with three sourced stats, how-it-works four steps with annexation strip and protections note, who-it-serves three cards, calculator, evidence table (10 sourced claims), five-question FAQ, contact placeholder, footer
- [x] 5.3 Calculator: cash vs private loan vs land-secured; nine editable inputs, every default labeled with its source or estimate status; formulas printed on the page; unit-tested in node against python ground truth incl. zero-rate edge; coverage-cushion input added so defaults reproduce the whitepaper example ($2,298 vs roughly $2,300); honesty box states future homeowners pay the special tax and developers pay it on unsold lots
- [x] 5.4 Pre-launch banner at top, full standard disclaimer plus securities sentence in footer
- [x] 5.5 Rendered at 1440 and 390 widths with JavaScript on (screenshots in 05_WEBSITE/qc). JS execution proven in the engine: rendered text layer contains the computed values. Honest caveat: the session image viewer is returning blanks, so eyeball inspection is pending; mechanical audits (header/band structure, ink density, anchor integrity) pass and the screenshots are packaged for human review
- [x] 5.6 No trackers, no cookies, no analytics, no external requests; stated on the page and verified by scan; local file only, nothing deployed

## 6. Stakeholder deck (06_DECK)
- [x] 6.1 14-slide deck built with pptxgenjs per the skill constraints: navy sandwich, parcel-grid motif, native county bar chart, embedded structure map, roles and competitive tables, risk slide, status-and-asks close with full disclaimer and speaker notes
- [x] 6.2 Schema validator: All validations PASSED
- [x] 6.3 All 14 slides rendered to a thumbnail grid (06_DECK/qc); table-aware token sweep CLEAN; embedded pictures as designed. Viewer outage: thumbnails packaged for human review

## 7. Build log (07_BUILDLOG)
- [x] 7.1 Decisions log: ten entries (Build_Log Part 2)
- [x] 7.2 Question batch: ten conversational questions, no acronyms, each with a working answer (Build_Log Part 1)
- [x] 7.3 Cut list: six entries (Build_Log Part 4)
- [x] 7.4 Corrections log: nine entries (Build_Log Part 3)

## 8. Red team (08_REDTEAM)
- [x] 8.1 Kill Memo: six attacks argued (legal, credit, competitive, operational, reputational, execution/key-person), each with survivors, casualties, and residual risk
- [x] 8.2 Casualties table in the memo; global sweep confirms every casualty absent from handout surfaces
- [x] 8.3 Completeness table in the Kill Memo: all ten plan deliverables verified done

## 9. Packaging and handoff
- [x] 9.1 Root README written: reading order, directory map, standing rules, disclaimer
- [x] 9.2 Local git repository initialized and committed (push left to the owner; no credentials used)
- [x] 9.3 Full canonical tree synced to outputs; quarantine preserved in the repo, clearly labeled, excluded from deliverables
- [x] 9.4 Final handoff message delivered with the question batch

## Open items needing Dennis's input [!] (will also appear in the Build Log question batch)
- [!] Q1 Trademark: proceed with INSITE pending counsel clearance, or clear alternates first?
- [!] Q2 Domain preference among available options (insiteprogram.com / insitecalifornia.com / insitecfd.com)?
- [!] Q3 Public naming: "Development Impact & School Fee Financing Program" vs. dropping "School" until school fees are in scope (materials currently drop it)?
- [!] Q4 Pilot facts for external use: can the 27-lot City of Sacramento project be described publicly, and at what specificity?
- [!] Q5 Entity on external materials: HGF Management Company LLC as-is, or pending NV/CA entity decision?
- [!] Q6 Consultant selection (INS-005): shortlist and interview the special tax consultant and tax roll administrator (criteria in INS-005), select bond counsel, and confirm the named advisor role and one-page bios for the credibility bench
- [!] Q7 Quarantined drafts (see 09_QUARANTINE_UNVERIFIED/QUARANTINE_README): run INS-002/INS-201/OPERATIONS set through full verification and adopt, or discard and rebuild fresh under the locked corrections?
- [!] Q8 Minimum financing size: no verified minimum exists, so INS-201 says "determined during feasibility screening." What floor does Dennis want to publish, if any?
