Phase 4

Okay, here is a multi-step asynchronous plan for Phase 4: Sole Survivor Preference Path. This phase focuses on users who are seeking 0-point preference based on a "sole survivorship discharge."
This plan assumes users arrive from advisor/ownservice_discharged_checkfirst_solesurvivor.md (from Phase 1) by selecting "Yes, I believe I had a sole survivorship discharge," which should then link to the first file in this phase: advisor/ownservice_ssp_dischargedate.md.

Veteran's Preference Advisor: Site Development Plan - Phase 4: Sole Survivor Preference Path
Overall Goal for Phase 4: To create the decision tree path for veterans claiming 0-point Sole Survivor Preference (SSP).
General Instructions for AI Agent:
* For each task below, create the specified Markdown file in the /advisor/ directory.
* Ensure each file uses layout: default (or the custom advisor layout).
* Include a link back to the start: [Return to Advisor Start](./start.md) on nearly every page.
* Incorporate citations from hrdocs.txt as indicated, using the format ``.
* Content should guide the user to determine potential eligibility for 0-point SSP.

Phase 4 Development Tasks (Asynchronous)
Each task involves creating one Markdown file with the specified attributes.
Task 4.1: Create advisor/ownservice_ssp_dischargedate.md
* File: advisor/ownservice_ssp_dischargedate.md (New)
* Title: Sole Survivor Preference: Date of Discharge
* Purpose: To verify if the veteran's discharge date meets the statutory requirement for SSP (after August 29, 2008).
* Content/Question: Markdown     You indicated you believe you had a 'sole survivorship discharge.' [cite_start]To be eligible for Sole Survivor Preference (SSP), your release or discharge from the relevant period of active duty must have occurred *after August 29, 2008*. 
* 
* When were you released or discharged from this period of active duty?
*     
* Choices:
    * "On or before August 29, 2008." -> advisor/ineligible_ssp_dischargedate.md
    * "After August 29, 2008." -> advisor/ownservice_ssp_discharge_reason.md
    * "I'm not sure / I need to check my DD Form 214." -> advisor/ownservice_ssp_checkdd214_date.md
    * "[Return to previous question (Own Service: Check for Sole Survivorship Preference)]" -> advisor/ownservice_discharged_checkfirst_solesurvivor.md
    * "[Return to Advisor Start]" -> advisor/start.md

Task 4.2: Create advisor/ownservice_ssp_discharge_reason.md
* File: advisor/ownservice_ssp_discharge_reason.md (New)
* Title: Sole Survivor Preference: Reason for Discharge
* Purpose: To verify if the specific reason for discharge was "sole survivorship."
* Content/Question: Markdown     You indicated your discharge was after August 29, 2008. Was the specific reason stated for your release or discharge from that period of active duty a 'sole survivorship discharge'? [cite_start]This should be documented on your DD Form 214 or other official separation papers. 
*     
* Choices:
    * "Yes, the reason documented was a 'sole survivorship discharge'." -> advisor/ownservice_ssp_familycriteria_info.md
    * "No, the reason documented was different." -> advisor/ineligible_ssp_reason.md
    * "I'm not sure / I need to check my DD Form 214." -> advisor/ownservice_ssp_checkdd214_reason.md
    * "[Return to previous question (Date of Discharge)]" -> advisor/ownservice_ssp_dischargedate.md
    * "[Return to Advisor Start]" -> advisor/start.md

Task 4.3: Create advisor/ownservice_ssp_familycriteria_info.md
* File: advisor/ownservice_ssp_familycriteria_info.md (New)
* Title: Sole Survivor Preference: Basis for Discharge (Information)
* Purpose: To provide context on the family circumstances that typically lead to a "sole survivorship discharge."
* Content/Question: Markdown     You've indicated you received a 'sole survivorship discharge' after August 29, 2008. This type of discharge is typically granted to protect 'the only surviving child in a family' where a parent or one or more siblings served in the U.S. Armed Forces AND:
* 
* * Was killed, died as a result of wounds, accident, or disease; OR
* * Is in a captured or missing in action status; OR
* * [cite_start]Is permanently 100 percent disabled or hospitalized on a continuing basis (and is not gainfully employed because of the disability or hospitalization). 
* 
* [cite_start]And, the death, status, or disability did not result from the intentional misconduct or willful neglect of the parent or sibling and was not incurred during a period of unauthorized absence. 
* 
* If your 'sole survivorship discharge' was granted based on these family circumstances, you may be eligible for 0-point Sole Survivor Preference (SSP).
*     
* Choices:
    * "Yes, this aligns with the basis for my discharge. Proceed to eligibility summary." -> advisor/eligible_ssp_0point.md
    * "No, this does not sound like the basis for my discharge, or my discharge was different." -> advisor/ineligible_ssp_reason.md
    * "[I need to re-check the reason for my discharge]" -> advisor/ownservice_ssp_checkdd214_reason.md
    * "[Return to previous question (Reason for Discharge)]" -> advisor/ownservice_ssp_discharge_reason.md
    * "[Return to Advisor Start]" -> advisor/start.md

Task 4.4: Create advisor/eligible_ssp_0point.md
* File: advisor/eligible_ssp_0point.md (Replaces placeholder ownservice_ssp_eligible.md from previous plan's outline)
* Title: Veteran's Preference Advisor - Potential 0-Point Sole Survivor Preference (SSP)
* Purpose: Informs the user they may be eligible for 0-point SSP and its benefits.
* Content/Question: Markdown     Based on your responses, you appear to meet the criteria for 0-point Sole Survivor Preference (SSP). [cite_start]This is because you indicated you received a 'sole survivorship discharge' after August 29, 2008, based on qualifying family member service and loss/disability. 
* 
* Key aspects of 0-point Sole Survivor Preference (SSP) include:
* * [cite_start]You do *not* receive additional points added to your passing score or rating. 
* * [cite_start]You *are* entitled to be listed ahead of non-preference eligibles who have the same score on an examination, or listed ahead of non-preference eligibles in the same quality category when agencies use category rating. 
* * [cite_start]You *are* entitled to receive the same pass-over rights as other preference eligibles. 
* * [cite_start]You *are* entitled to credit experience in the armed forces to meet the qualification requirements for Federal jobs. 
* 
* This is an initial assessment and not a final determination of preference. Ensure your DD Form 214 or other official separation documents clearly indicate a 'sole survivorship discharge' and the date of discharge.
*     
* Choices:
    * "Learn more about veteran's preference procedures" (Link to a general info page or OPM guidance)
    * "[Return to Advisor Start]" -> advisor/start.md

Task 4.5: Create advisor/ineligible_ssp_dischargedate.md
* File: advisor/ineligible_ssp_dischargedate.md (New)
* Title: Sole Survivor Preference: Potentially Ineligible - Discharge Date Not Met
* Purpose: Explains potential ineligibility if the discharge date does not meet the SSP requirement.
* Content/Question: Markdown     [cite_start]To be eligible for 0-point Sole Survivor Preference (SSP) under the Hubbard Act, your release or discharge from active duty must have occurred *after August 29, 2008*. 
* 
* Based on your response, your discharge date does not meet this requirement for SSP. You may still be eligible for other types of veteran's preference based on your service.
*     
* Choices:
    * "[Re-check discharge date information]" -> advisor/ownservice_ssp_dischargedate.md
    * "[Explore other preference types (e.g., 5-point, disability)]" -> advisor/ownservice_checkdisability_intro.md
    * "[Return to Advisor Start]" -> advisor/start.md

Task 4.6: Create advisor/ineligible_ssp_reason.md
* File: advisor/ineligible_ssp_reason.md (New)
* Title: Sole Survivor Preference: Potentially Ineligible - Reason for Discharge Not Met
* Purpose: Explains potential ineligibility if the discharge was not a "sole survivorship discharge."
* Content/Question: Markdown     [cite_start]Eligibility for 0-point Sole Survivor Preference (SSP) requires that the specific reason for your discharge (after August 29, 2008) was a 'sole survivorship discharge'. 
* 
* If your discharge was for other reasons, you would not qualify for SSP. However, you might be eligible for other types of veteran's preference (e.g., 5-point preference based on service period or campaign medal, or 10-point preference if disabled).
*     
* Choices:
    * "[Re-check reason for discharge information]" -> advisor/ownservice_ssp_discharge_reason.md
    * "[Explore other preference types (e.g., 5-point, disability)]" -> advisor/ownservice_checkdisability_intro.md
    * "[Return to Advisor Start]" -> advisor/start.md

Task 4.7: Create advisor/ownservice_ssp_checkdd214_date.md
* File: advisor/ownservice_ssp_checkdd214_date.md (New)
* Title: Sole Survivor Preference: Check DD Form 214 for Discharge Date
* Purpose: Advises the user to check their DD Form 214 for the discharge date.
* Content/Question: Markdown     Your DD Form 214 (Certificate of Release or Discharge from Active Duty) will state your date of discharge for the relevant period of service. Please review this document to confirm if your discharge occurred *after August 29, 2008*.
* 
* Once you have this information, please select an option:
*     
* Choices:
    * "My discharge was after August 29, 2008." -> advisor/ownservice_ssp_discharge_reason.md
    * "My discharge was on or before August 29, 2008." -> advisor/ineligible_ssp_dischargedate.md
    * "[Return to Advisor Start]" -> advisor/start.md

Task 4.8: Create advisor/ownservice_ssp_checkdd214_reason.md
* File: advisor/ownservice_ssp_checkdd214_reason.md (New)
* Title: Sole Survivor Preference: Check DD Form 214 for Discharge Reason
* Purpose: Advises the user to check their DD Form 214 for the specific reason for discharge.
* Content/Question: Markdown     Your DD Form 214 (Certificate of Release or Discharge from Active Duty) or other official separation documents should state the specific reason or authority for your discharge. Please review these documents to confirm if the reason was explicitly a 'sole survivorship discharge'.
* 
* Once you have this information, please select an option:
*     
* Choices:
    * "Yes, the reason documented was 'sole survivorship discharge'." -> advisor/ownservice_ssp_familycriteria_info.md
    * "No, the reason documented was different or unclear regarding sole survivorship." -> advisor/ineligible_ssp_reason.md
    * "[Return to Advisor Start]" -> advisor/start.md

This concludes the development plan for Phase 4, focusing on Sole Survivor Preference. If there are other "complex cases" to be added to Phase 4, they would need their own set of tasks and file definitions.
