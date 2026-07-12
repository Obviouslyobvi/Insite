# The INSITE Fee Database: schema and workflow

**Purpose.** One statewide table of development impact fees, per jurisdiction and category, feeding the fee estimator and, later, Airtable automation. Built to the same standard as the Claims Register: no row without a source.

**Legal basis.** Government Code 65940.1 (added by AB 1483, effective January 1, 2020; strengthened by AB 1820 in 2024) requires every California city, county, and special district with a website to post its current schedule of fees, present it so the fees applying to each parcel are clear, post the written schedule or a direct link to it, update within 30 days of any change, and archive impact fee nexus studies from 2018 forward. That is what makes a statewide compile feasible: the data is required to be public, jurisdiction by jurisdiction.

**Workflow, per jurisdiction.** Find the agency's fee schedule or AB 1483 transparency page; transcribe each residential impact fee as one row in the template; paste the exact source URL and the schedule's effective date; date and initial the verification; import to Airtable (fields map one-to-one with the CSV header); export the estimator's JSON from Airtable when rows change. A row without a source URL does not ship, ever.

**Field dictionary.** jurisdiction and county identify the agency; agency_type is city, county, or special district; fee_category matches the estimator's nine categories; amount is dollars; unit_basis is per unit, per square foot, or per acre; housing_type distinguishes single-family detached, attached, and multifamily where schedules do; effective_date is the schedule's own date; source_url and source_title point at the posted schedule; verified_date and verified_by close the loop; notes carries anything odd.

**Cadence.** Agencies must update within 30 days of changes, so a quarterly re-verification pass per active jurisdiction keeps the table honest; the pilot jurisdiction gets re-verified before every external use.
