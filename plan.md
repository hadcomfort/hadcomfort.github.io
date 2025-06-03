Phase 2

This plan will define the new Markdown files required for veterans seeking preference based on a service-connected disability or Purple Heart. Each task represents the creation of a specific file and can be worked on independently.

This plan assumes that users arrive at this phase from advisor/ownservice_checkdisability_intro.md (from Phase 1), by selecting "Yes, I have a service-connected disability OR I received a Purple Heart," which should then link to the first file in this phase: advisor/ownservice_disability_details.md.

Veteran's Preference Advisor: Site Development Plan - Phase 2: Disability Path
Overall Goal for Phase 2: To create the decision tree paths for veterans claiming 10-point preference based on their own service due to a service-connected disability or receipt of a Purple Heart.
General Instructions for AI Agent:
* For each task below, create the specified Markdown file in the /advisor/ directory.
* Ensure each file uses layout: default (or the custom advisor layout).
* Include a link back to the start: [Return to Advisor Start](./start.md) on nearly every page.
* Incorporate citations from hrdocs.txt as indicated.
* The content should guide the user to determine potential eligibility for different types of 10-point preference (XP, CP, CPS).

Phase 2 Development Tasks (Asynchronous)
Each task involves creating one Markdown file with the specified attributes.
Task 2.1: Create advisor/ownservice_disability_details.md
* File: advisor/ownservice_disability_details.md (New)
* Title: Own Service: Disability or Purple Heart Details
* Purpose: To gather more specific information about the nature of the disability or Purple Heart to determine the type of 10-point preference.
* Content/Question: Markdown     You indicated you have a service-connected disability or received a Purple Heart. To determine the type of 10-point preference, please select the option that best describes your situation. [cite_start](Remember, if you are claiming 10-point preference, you will typically need to complete an SF-15 form and provide supporting documentation. )
*     
* Choices:
    * "I received a Purple Heart." -> advisor/ownservice_xp_purpleheart.md
    * "I have a service-connected disability rating of 30% or more from the VA or my branch of service." -> advisor/ownservice_cps_details.md 1
    * "I have a service-connected disability rating of 10% or 20% from the VA or my branch of service." -> advisor/ownservice_cp_details.md 2
    * "I have a service-connected disability (rated less than 10% or not yet rated but recognized) OR I am receiving compensation, disability retirement benefits, or pension from the military or VA due to a service-connected disability, but I don't fit the 10-30%+ categories above." -> advisor/ownservice_xp_generaldisability_details.md 3
    * "I'm not sure about the percentage or type." -> advisor/ownservice_disability_clarify_sf15.md
    * "Return to Advisor Start" -> advisor/start.md

Task 2.2: Create advisor/ownservice_xp_purpleheart.md
* File: advisor/ownservice_xp_purpleheart.md (New)
* Title: Own Service: 10-Point Preference (XP) - Purple Heart
* Purpose: Confirms potential eligibility for 10-point XP preference based on Purple Heart.
* Content/Question: Markdown     You indicated you received a Purple Heart. [cite_start]Receipt of a Purple Heart qualifies you for 10-point Veteran's Preference (XP), provided your discharge was (or will be, if VOW Act applies) under honorable conditions and all other general eligibility requirements are met. [cite_start]For disabled veterans, active duty includes training service in the Reserves or National Guard. 
*     
* Choices:
    * "Confirm, proceed to eligibility summary." -> advisor/eligible_xp_10point.md
    * "I made a mistake, review disability/Purple Heart options." -> advisor/ownservice_disability_details.md
    * "Return to Advisor Start" -> advisor/start.md

Task 2.3: Create advisor/ownservice_cps_details.md
* File: advisor/ownservice_cps_details.md (New)
* Title: Own Service: 10-Point Preference (CPS) - 30%+ Disability
* Purpose: Confirms potential eligibility for 10-point CPS preference based on 30%+ disability.
* Content/Question: Markdown     You indicated a service-connected disability rating of 30% or more. [cite_start]This generally qualifies you for 10-point Veteran's Preference (CPS), provided your discharge was (or will be, if VOW Act applies) under honorable conditions and all other general eligibility requirements are met. [cite_start]For disabled veterans, active duty includes training service in the Reserves or National Guard.  [cite_start]Remember to complete the SF-15 form. 
*     
* Choices:
    * "Confirm, proceed to eligibility summary." -> advisor/eligible_cps_10point.md
    * "I made a mistake, review disability/Purple Heart options." -> advisor/ownservice_disability_details.md
    * "Return to Advisor Start" -> advisor/start.md

Task 2.4: Create advisor/ownservice_cp_details.md
* File: advisor/ownservice_cp_details.md (New)
* Title: Own Service: 10-Point Preference (CP) - 10-20% Disability
* Purpose: Confirms potential eligibility for 10-point CP preference based on 10-20% disability.
* Content/Question: Markdown     You indicated a service-connected disability rating of 10% or 20%. [cite_start]This generally qualifies you for 10-point Veteran's Preference (CP), provided your discharge was (or will be, if VOW Act applies) under honorable conditions and all other general eligibility requirements are met. [cite_start]For disabled veterans, active duty includes training service in the Reserves or National Guard.  [cite_start]Remember to complete the SF-15 form. 
*     
* Choices:
    * "Confirm, proceed to eligibility summary." -> advisor/eligible_cp_10point.md
    * "I made a mistake, review disability/Purple Heart options." -> advisor/ownservice_disability_details.md
    * "Return to Advisor Start" -> advisor/start.md

Task 2.5: Create advisor/ownservice_xp_generaldisability_details.md
* File: advisor/ownservice_xp_generaldisability_details.md (New)
* Title: Own Service: 10-Point Preference (XP) - General Disability
* Purpose: Confirms potential eligibility for 10-point XP preference based on a general service-connected disability or receipt of related benefits.
* Content/Question: Markdown     You indicated you have a present service-connected disability OR are receiving compensation, disability retirement benefits, or pension from the military or the Department of Veterans Affairs, not specifically categorized as 10-20% (CP) or 30%+ (CPS). [cite_start]This may qualify you for 10-point Veteran's Preference (XP), provided your discharge was (or will be, if VOW Act applies) under honorable conditions and all other general eligibility requirements are met. [cite_start]For disabled veterans, active duty includes training service in the Reserves or National Guard.  [cite_start]Remember to complete the SF-15 form. 
*     
* Choices:
    * "Confirm, proceed to eligibility summary." -> advisor/eligible_xp_10point.md
    * "I made a mistake, review disability/Purple Heart options." -> advisor/ownservice_disability_details.md
    * "Return to Advisor Start" -> advisor/start.md

Task 2.6: Create advisor/ownservice_disability_clarify_sf15.md
* File: advisor/ownservice_disability_clarify_sf15.md (New)
* Title: Own Service: Disability Preference - Clarification Needed
* Purpose: Advises users unsure of their disability status to check documentation and the SF-15.
* Content/Question: Markdown     Understanding your specific disability rating and type is important for determining 10-point preference. Please review your documentation from the Department of Veterans Affairs (VA) or your branch of service. [cite_start]The Standard Form 15 (SF-15), 'Application for 10-Point Veteran Preference,' also provides details on required documentation.  Once you have more information, you can select the appropriate option from the previous page.
*     
* Choices:
    * "Return to disability/Purple Heart options." -> advisor/ownservice_disability_details.md
    * "Return to Advisor Start" -> advisor/start.md

Task 2.7: Create advisor/eligible_xp_10point.md
* File: advisor/eligible_xp_10point.md (New)
* Title: Veteran's Preference Advisor - Potential 10-Point Eligibility (XP)
* Purpose: Informs the user they may be eligible for 10-point preference (XP) based on Purple Heart or general disability criteria.
* Content/Question: Markdown     [cite_start]Based on your responses, you appear to meet the criteria for 10-point veteran's preference (XP).  This is an initial assessment and not a final determination of preference.
* 
* Key considerations for XP preference:
* * [cite_start]It can be based on receiving a Purple Heart OR having a service-connected disability (or receiving compensation/pension for it) that doesn't fall into the specific CP (10-20%) or CPS (30%+) categories. 
* * [cite_start]You must have been discharged or released from active duty under honorable conditions (or expect to be if applying under the VOW Act). 
* * [cite_start]Applicants claiming 10-point preference must typically complete Standard Form (SF) 15, Application for 10-Point Veteran Preference, and submit required documentation. 
* * [cite_start]For disabled veterans, "active duty" includes training service in the Reserves or National Guard. 
* * [cite_start]The 24-month minimum active duty service requirement that applies to some 5-point preference situations generally does not apply to those eligible for 10-point preference due to a separation for disability incurred or aggravated in the line of duty. 
* 
* Remember to claim preference when applying for Federal jobs and be prepared to provide documentation.
*     
* Choices:
    * "Learn more about applying with 10-point preference (SF-15)" (Link to OPM guidance on SF-15 or a future detailed info page)
    * "Return to Advisor Start" -> advisor/start.md

Task 2.8: Create advisor/eligible_cp_10point.md
* File: advisor/eligible_cp_10point.md (New)
* Title: Veteran's Preference Advisor - Potential 10-Point Eligibility (CP)
* Purpose: Informs the user they may be eligible for 10-point preference (CP) based on a 10-20% disability.
* Content/Question: Markdown     [cite_start]Based on your responses, you appear to meet the criteria for 10-point veteran's preference (CP) due to a service-connected disability rating of at least 10 percent but less than 30 percent.  This is an initial assessment and not a final determination of preference.
* 
* Key considerations for CP preference:
* * [cite_start]You must have been discharged or released from active duty under honorable conditions (or expect to be if applying under the VOW Act). 
* * [cite_start]Applicants claiming 10-point preference must typically complete Standard Form (SF) 15, Application for 10-Point Veteran Preference, and submit required documentation (like your VA rating decision). 
* * [cite_start]For disabled veterans, "active duty" includes training service in the Reserves or National Guard. 
* * [cite_start]The 24-month minimum active duty service requirement that applies to some 5-point preference situations generally does not apply to those eligible for 10-point preference due to a separation for disability incurred or aggravated in the line of duty. 
* 
* Remember to claim preference when applying for Federal jobs and be prepared to provide documentation.
*     
* Choices:
    * "Learn more about applying with 10-point preference (SF-15)" (Link to OPM guidance on SF-15 or a future detailed info page)
    * "Return to Advisor Start" -> advisor/start.md

Task 2.9: Create advisor/eligible_cps_10point.md
* File: advisor/eligible_cps_10point.md (New)
* Title: Veteran's Preference Advisor - Potential 10-Point Eligibility (CPS)
* Purpose: Informs the user they may be eligible for 10-point preference (CPS) based on a 30%+ disability.
* Content/Question: Markdown     [cite_start]Based on your responses, you appear to meet the criteria for 10-point veteran's preference (CPS) due to a service-connected disability rating of 30 percent or more.  This is an initial assessment and not a final determination of preference.
* 
* Key considerations for CPS preference:
* * [cite_start]You must have been discharged or released from active duty under honorable conditions (or expect to be if applying under the VOW Act). 
* * [cite_start]Applicants claiming 10-point preference must typically complete Standard Form (SF) 15, Application for 10-Point Veteran Preference, and submit required documentation (like your VA rating decision). 
* * [cite_start]For disabled veterans, "active duty" includes training service in the Reserves or National Guard. 
* * [cite_start]The 24-month minimum active duty service requirement that applies to some 5-point preference situations generally does not apply to those eligible for 10-point preference due to a separation for disability incurred or aggravated in the line of duty. 
* 
* Remember to claim preference when applying for Federal jobs and be prepared to provide documentation.
*     
* Choices:
    * "Learn more about applying with 10-point preference (SF-15)" (Link to OPM guidance on SF-15 or a future detailed info page)
    * "Return to Advisor Start" -> advisor/start.md

This concludes the development plan for Phase 2. Once these files are created, the next step would be a QA plan similar to the one you previously generated for Phase 1, to check these new Phase 2 files.
