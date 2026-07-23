# INSITE(TM) Airtable Base Design

**Prepared for Dennis Lanni, HGF Management Company**

**July 23, 2026. One base, three layers: what each layer does, what data lives in it, and which layers sit inside the existing agreement.**

## The shape of it

Everything discussed so far fits in a single Airtable base with three layers that share data instead of duplicating it. The fee database is the reference layer: facts about jurisdictions and their fees, maintained as cities change their schedules. The pipeline is the working layer: projects and people, moving through stages. The document framework is the output layer: automations that assemble program documents from the data the first two layers already hold. A project record links to its jurisdiction, so a fee lookup, a pipeline view, and a generated document all draw from the same underlying facts, entered once.

## Layer one: the fee database

Two tables. Jurisdictions holds one record per city or county: name, county, participation status, and the link to the agency's posted fee schedule required by Government Code 65940.1. Fees holds one record per fee, in the fourteen-field structure already built and populated for the Sacramento pilot: fee name, category, amount, unit basis, housing type, effective date, source link, source title, verification date, verifier, and notes, each fee linked to its jurisdiction. Views come preconfigured: fees by jurisdiction, fees by category, and a maintenance view that surfaces any fee whose verification date has gone stale, with an automation that flags those records on a schedule. That flag is the automation component of the contracted database line. This layer is part of Milestone 2 under the existing agreement, at no additional cost, and gets built the day the HGF account exists.

## Layer two: the pipeline

Two tables. Entities holds people and companies: name, company, role, contact details, source of the relationship, and a stage field carrying the five stages as defined: Lead, a person or company identified but whose interest and qualifications are not confirmed; Prospect, a more serious potential client in active communication about a specific opportunity; Applicant, someone who has submitted an application or requested formal approval; Borrower, an active relationship with services being provided; Closed, an engagement or transaction that has concluded. Projects holds one record per deal: project name, linked entity, linked jurisdiction, lot count, lot status, estimated fees, screening result, and dates for each stage transition. Views show the pipeline by stage, projects by jurisdiction, and a simple activity log. This layer is outside the six milestones of the existing agreement and proceeds on written approval.

## Layer three: the document framework

Automations that assemble documents from record data: when a project reaches a stage, the base generates the corresponding document from a template filled with that project's fields. Built gradually as the first transactions define what the documents actually are, which is the right order, because automating a document that has never been through a live deal hardens guesses instead of facts. The layer starts with one working example wired end to end so the pattern is proven, and grows one document at a time. This layer is outside the six milestones of the existing agreement and is scoped per document set once the first transaction defines it.

## Scope summary

Layer one is contracted work under Milestone 2, included, no new approval needed. Layers two and three are new scope under the agreement's terms, which require written approval before work begins for the work to be billable. A one-line reply approving a layer and its price is sufficient writing. Nothing in this design commits either party; it exists so the discussion starts from a drawn picture instead of a blank page.

*INSITE(TM) is a pre-launch program concept administered by HGF Management Company. This material is not an offer of financing, legal advice, or investment advice. Program structure, eligibility, costs, and pricing are subject to issuer approval, bond counsel review, and program underwriting. Figures identified as targets or estimates are the founder's working numbers, not commitments.*
