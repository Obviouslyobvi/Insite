# INSITE HANDOFF

**Written July 13, 2026, end of the late session. Paste this to start a new one. It supersedes the earlier July 13 handoff, which carried three stale claims, each corrected below and each named so nobody re-inherits them.**

## Who and what

Palmer is the builder: computer work only, never a principal, never a document recipient. Dennis Lanni is founder and principal of HGF Management Company, Granite Bay, and every document is prepared for him. INSITE finances development impact fees for 2-to-50-lot California subdivisions: one master community facilities district per agency, administrative annexations with unanimous owner approval, one note per project, a single warehouse credit facility (the line and the facility are one instrument), and an optional pooled bond take-out once properties stabilize.

## First action every session

Load 00_PLAN/INSITE_Master_Plan.md before building anything. TODO.txt is the live task list. The Build Log (07_BUILDLOG) holds decisions, corrections, and the question batch. The Delivery Order sequences what Dennis sees.

## Rules

Invent nothing: every claim traces to 01_EVIDENCE/Claims_Register.md (entries A1 through G21, dated and sourced) or carries a founder-estimate label. Documents in prose; chat status in bullets, one item per line; one next action at a time; plain language, no unexplained acronyms. Band PDFs render only through tools/md2pdf.py, whose embedded 12mm top-margin gate hard-fails on ink in the top strip. Word editions embed diagrams as PNGs from 02_PROGRAM/DIAGRAMS. Founder material quarantines in 09_QUARANTINE before adoption; external references file in 01_EVIDENCE/REFERENCE. Nothing is done without visual verification: rasterize pages, check margins and blanks, confirm diagram pages, refresh contact sheets in 07_BUILDLOG/qc. The checklist PDF has its own pipeline (checkbox styling, 12mm margins) and is never regenerated through md2pdf.

## Three corrections to the previous handoff

1. **The DCF workbook was never pending.** Both formula defects were fixed July 11 in v1.1_corrected. Verified July 13 by reading the formulas: DCF Model row 5 points at Market Assumptions B10 (Development Cost Period) across all 60 month columns, row 6 at B11 (Soft Cost Period), and zero references to B9 (Builder Incentives, value 0) survive anywhere in the workbook. The v1 original is preserved untouched in ARCHIVE_ORIGINALS. Nothing is awaiting a go-ahead.
2. **The INS-301 PDF was not clean.** tools/md2pdf.py never handled level-3 headings, so every "###" line printed as literal body text. The shipped guide carried 19 of them, one per chapter and appendix. The tool is patched, the PDF is rebuilt (margin gate passed, 12 pages, rasterized and inspected), and a sweep of every PDF in the repo found INS-301 to be the only casualty. The Word edition was already clean.
3. **Question 11 was never answered.** Its Build Log entry had question 9's school-fee answer pasted into it by error, which is what made the old handoff read as though 11 were settled. Question 9's answer is restored to its own entry; question 11 is recorded as open.

## State

Program decisions 9 and 10 are answered. Question 9: school fees EXCLUDED at launch, definitely; the founder is researching whether pay-then-reimburse avoids the school joint agreement; register entry G7 (Riverside) says a thin agreement survives; bond counsel resolves it if reopened; the mechanics stay documented in the guide as the future path. Question 10: one note per project or annexation; the warehouse line and the credit facility are one instrument, funding everything until the optional take-out at stabilization.

Question 11 is open, worked, and waiting on the founder: INS-007, the Agreement Structure Decision Memo, presents the case for one instrument and the case for two and recommends two, with the Participation Agreement staying the council-approved master (sole discretion over approvals, no general fund obligation, cost recovery, wind-down continuity) and a Program Administration Agreement incorporated by reference carrying the terms that will actually change (fee schedule, service levels, reporting formats, delinquency ladder, insurance, subcontracting, term and termination). The memo names its own weak point: whether an agency may amend a services agreement without returning to council varies by agency, threshold, and charter, and that is reasoning, not a verified claim.

The name is settled for now: Palmer's call on July 13 is to roll with INSITE as is and leave it alone. No Option A memo, no bench-name switch. The trademark attorney's clearance is still the formal gate before public launch, and the TSDR recheck on serial 98837494 stays calendared for about July 26.

Document status: INS-301 Participating Public Agency Guide at v0.99, ten chapters, nine appendices, PDF rebuilt and verified. Whitepaper v1.1 carries the platform as section 11. INS-302 Developer Guide v1.0 shipped. INS-303 Investor Guide v1.0 shipped July 13: ten chapters across four parts, four appendices, every chapter marked PUBLIC or PORTAL, question 10's answer carried throughout, five diagrams embedded, PDF and Word both rendered and visually verified. INS-304 city-staff guide reserved. INS-007 decision memo shipped.

## Open items

Dennis decides question 11 (INS-007). Dennis edits the INS-303 chapter plan and the public-versus-portal split. Dennis still owes: manual policy numbers, entity confirmation, minimum deal size, program email address, and his merge of the INS-301 draft (his Google Doc stays source of truth until adopted). The founder's school-agreement research continues.

Bond counsel carries two questions now, not one: the school-fee reimbursement points if question 9 reopens, and which administrator duties must appear in the council-approved instrument for the agency's authorization to hold. Bench: Brad Neill at Stradling is bond counsel (engaged); Webb Municipal Finance is the special tax consultant candidate; meet Brad first and arrive at Webb with his endorsement.

Chapter 4 and section 5.5 of INS-303 stay bannered bond-counsel gates. They are placeholders on purpose. Filling them before counsel opines would be invention.

## Mechanics

GitHub: github.com/Obviouslyobvi/Insite, public, master. Push flow: git bundle from master only, copied to outputs as insite-pushN.zip; Palmer clones the zip and pushes with his two commands; exactly one push zip lives in outputs at a time. Live pages via raw.githack.com (bust cache with ?v=). The outputs mirror is a full tar copy, and the mount throws intermittent IO errors, so always git-commit first, then retry the mirror, then verify counts. Dennis's export pipeline has produced two blank files; fetch his Google Docs directly when a copy looks empty.
