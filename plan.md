# Updated Veteran's Preference Advisor: Site Development Plan
## (Phase 1 Focus)

This updated plan outlines the phases and Markdown files required to build out the interactive Veteran's Preference Advisor on your Jekyll site, focusing on completing Phase 1 based on the OPM Vet Guide.

## Overall Site Structure Considerations:
(As per your original plan these are good.)

* **Directory**: All decision tree Markdown files will reside in the `/advisor/` directory.
* **Layout**: All advisor pages should use `layout: default` (or a custom advisor layout).
* **Navigation**:
    * Each page will present a question or information and offer choices as links to other Markdown files.
    * Almost every page should include a link back to the start: `[Return to Advisor Start](./start.md)`
* **Disclaimer**: A brief disclaimer should be visible or easily accessible from all advisor pages.
* **Citations**: Markdown files should include markers in the content, linking to relevant sections or page numbers in the OPM Vet Guide (hrdocs.txt). (Citations from hrdocs.txt are incorporated into the content/questions as appropriate).

## Phase 1: Foundational Setup & Initial "Own Service" Path (No Disability, Basic Cases)
This phase establishes the main entry points and the simplest path for veterans claiming preference based on their own service, focusing on common scenarios without immediate disability considerations.

### 1. Review and Standardize Core Files:

* **File**: `advisor/start.md` (Existing)
    * **Title**: Veteran's Preference Advisor - Start
    * **Purpose**: Initial entry point to the advisor.
    * **Content/Question**: "This tool is designed to help you understand potential eligibility for U.S. Federal employment veterans' preference. Please select the primary basis on which you are seeking to determine potential eligibility: (Note: 'Armed Forces' generally means Army, Navy, Air Force, Marine Corps, and Coast Guard as defined in 5 U.S.C. 2101(2). Specific conditions apply for other uniformed services like NOAA and Public Health Service; see OPM Vet Guide Appendix B for details.)"
    * **Choices**:
        * "My own service in the U.S. Armed Forces" -> `advisor/ownservice_intro.md`
        * "The service of a qualifying veteran, if I am a spouse, widow(er), or mother" -> `advisor/derived_intro.md` (File to be created in Phase 3 - Derived Preference)
        * "Neither of the above" -> `advisor/ineligible_general.md`
    * **Notes**: Links updated to new standardized filenames.

* **File**: `advisor/ineligible_general.md` (Replaces `ineligible_start.md`)
    * **Title**: Veteran's Preference Advisor - Initial Ineligibility
    * **Purpose**: Explains general ineligibility if neither main category is chosen.
    * **Content/Question**: "Based on your initial selection, it appears you may not be directly pursuing veteran's preference based on your own service or as a qualifying relative (spouse, widow(er), mother) of a veteran. This advisor focuses on those categories. Veteran's preference is a specific entitlement for those who served in the Armed Forces during certain periods or campaigns, or have service-connected disabilities, and for certain family members (see OPM Vet Guide, 'Why Preference is Given')."
    * **Choices**:
        * "Return to Advisor Start"

### 2. "Own Service" Branch - Introduction & Status:

* **File**: `advisor/ownservice_intro.md` (Replaces `own_service_step1.md`)
    * **Title**: Veteran's Preference Advisor - Based on Your Own Service
    * **Purpose**: Asks about the veteran's current service status.
    * **Content/Question**: "You indicated you are seeking preference based on your own service in the U.S. Armed Forces. To proceed, please select your current status:"
    * **Choices**:
        * "I have been discharged or released from active duty in the Armed Forces." -> `advisor/ownservice_discharged_checkretired.md`
        * "I am currently an active duty service member and expect to be discharged or released from active duty service under honorable conditions within 120 days (and I have or can obtain a certification as described in the VOW Act)." -> `advisor/ownservice_vow_checkretired.md` (See OPM Vet Guide, 'A word about the VOW Act')
        * "None of the above apply to me." -> `advisor/ineligible_ownservice_status.md`
    * **Notes**: Review and potentially update `ineligible_ownservice_status.md`.

* **File**: `advisor/ineligible_ownservice_status.md` (Existing, review content)
    * **Title**: Veteran's Preference Advisor - Ineligible Service Status
    * **Purpose**: Explains ineligibility if current service status doesn't fit primary categories for own service.
    * **Content/Question**: "To claim preference based on your own service, you generally need to have been discharged/released from active duty or be an active duty member covered by the VOW Act (expected discharge within 120 days with certification). (See OPM Vet Guide, 'A word about the VOW Act'). If neither of these applies, you may not be eligible for preference at this time through this path."
    * **Choices**:
        * "Return to Advisor Start"

### 3. "Own Service" - Discharged Path (Initial Checks):
(The "VOW Act Path" will mirror these checks, starting with `ownservice_vow_checkretired.md`)

* **File**: `advisor/ownservice_discharged_checkretired.md`
    * **Title**: Own Service: Discharged - Check Retiree Status
    * **Purpose**: Checks if the discharged veteran is a high-ranking retiree, which affects preference.
    * **Content/Question**: "Are you a military retiree at the rank of Major, Lieutenant Commander, or higher? (This generally does not apply to Reservists who will not begin drawing military retired pay until age 60. See OPM Vet Guide, 'Types of Preference' and Appendix C for rank equivalents)."
    * **Choices**:
        * "Yes, I am a retiree at Major/Lt. Commander or higher." -> `advisor/ownservice_discharged_retiredmajor_isdisabled.md`
        * "No, I am not a retiree at that rank, OR I am a Reservist not yet drawing retired pay until age 60." -> `advisor/ownservice_discharged_honorableconditions.md`

* **File**: `advisor/ownservice_discharged_retiredmajor_isdisabled.md`
    * **Title**: Own Service: Retired Major/Lt. Cmdr+ - Check Disability
    * **Purpose**: High-ranking retirees are only eligible for preference if disabled.
    * **Content/Question**: "Military retirees at the rank of Major, Lieutenant Commander, or higher are generally not eligible for preference in appointment unless they are disabled veterans. (OPM Vet Guide, 'Types of Preference'). Do you have a service-connected disability recognized by the Department of Veterans Affairs (VA) or your branch of service?"
    * **Choices**:
        * "Yes, I am a disabled veteran." -> `advisor/ownservice_discharged_honorableconditions.md` (Disability preference will be key, but other conditions like honorable discharge are still checked first).
        * "No, I am not a disabled veteran." -> `advisor/ineligible_retiredmajor_notdisabled.md`

* **File**: `advisor/ineligible_retiredmajor_notdisabled.md`
    * **Title**: Own Service: Ineligible - Retired Officer Not Disabled
    * **Purpose**: Explains ineligibility for non-disabled high-ranking retirees.
    * **Content/Question**: "Military retirees at the rank of Major, Lieutenant Commander, or higher are not eligible for preference in appointment unless they are disabled veterans. (OPM Vet Guide, 'Types of Preference'). Based on your responses, you may not be eligible for veteran's preference under this condition."
    * **Choices**:
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_discharged_honorableconditions.md`
    * **Title**: Own Service: Discharged - Character of Service
    * **Purpose**: Checks for honorable discharge condition.
    * **Content/Question**: "To receive preference, a veteran must have been discharged or released from active duty in the Armed Forces under honorable conditions. This typically means an Honorable or General discharge. (OPM Vet Guide, 'Types of Preference'). What was the character of your discharge?"
    * **Choices**:
        * "Honorable or General Discharge." -> `advisor/ownservice_checkdisability_intro.md` (Routing to check disability first, then sole survivor, then service periods)
        * "Other than Honorable/General (e.g., Undesirable, Bad Conduct, Dishonorable)." -> `advisor/ineligible_discharge_type.md`
        * "I'm not sure / Need to check my DD Form 214." -> `advisor/ownservice_discharged_checkdd214_discharge.md`

* **File**: `advisor/ineligible_discharge_type.md`
    * **Title**: Own Service: Ineligible - Discharge Not Under Honorable Conditions
    * **Purpose**: Explains ineligibility due to discharge type.
    * **Content/Question**: "Veteran's preference requires a discharge or release under honorable conditions (i.e., an Honorable or General discharge). (OPM Vet Guide, 'Types of Preference'). If your discharge was of a different character, you may not be eligible."
    * **Choices**:
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_discharged_checkdd214_discharge.md`
    * **Title**: Own Service: Discharged - Check DD Form 214 for Discharge
    * **Purpose**: Advises user to check their documentation.
    * **Content/Question**: "Your DD Form 214 (Certificate of Release or Discharge from Active Duty) will state the character of your service. Please review this document. Once you have this information, you can restart or continue."
    * **Choices**:
        * "I have checked, and it was Honorable or General." -> `advisor/ownservice_checkdisability_intro.md`
        * "I have checked, and it was other than Honorable/General." -> `advisor/ineligible_discharge_type.md`
        * "Return to Advisor Start"

### 3a. "Own Service" - VOW Act Path (Initial Checks):
(This section mirrors section 3 but for those under the VOW Act, starting from `ownservice_intro.md`)

* **File**: `advisor/ownservice_vow_checkretired.md` (New)
    * **Title**: Own Service (VOW Act): Check Retiree Status
    * **Purpose**: Checks if the service member expecting discharge will be a high-ranking retiree.
    * **Content/Question**: "Regarding your upcoming discharge/release: Are you a military retiree (or will you be upon discharge/release) at the rank of Major, Lieutenant Commander, or higher? (This generally does not apply to Reservists who will not begin drawing military retired pay until age 60. See OPM Vet Guide, 'Types of Preference' and Appendix C for rank equivalents.)"
    * **Choices**:
        * "Yes, I expect to be a retiree at Major/Lt. Commander or higher." -> `advisor/ownservice_vow_retiredmajor_isdisabled.md`
        * "No, I do not expect to be a retiree at that rank, OR I am a Reservist not anticipating drawing retired pay until age 60." -> `advisor/ownservice_vow_honorableconditions.md`

* **File**: `advisor/ownservice_vow_retiredmajor_isdisabled.md` (New)
    * **Title**: Own Service (VOW Act): Retired Major/Lt. Cmdr+ - Check Disability
    * **Purpose**: High-ranking retirees are only eligible if disabled.
    * **Content/Question**: "Military retirees at the rank of Major, Lieutenant Commander, or higher are generally not eligible for preference unless they are disabled veterans. (OPM Vet Guide, 'Types of Preference'). Do you currently have a service-connected disability, or do you anticipate being recognized as a disabled veteran upon discharge?"
    * **Choices**:
        * "Yes, I am (or expect to be) a disabled veteran." -> `advisor/ownservice_vow_honorableconditions.md`
        * "No, I am not (and do not expect to be) a disabled veteran." -> `advisor/ineligible_vow_retiredmajor_notdisabled.md`

* **File**: `advisor/ineligible_vow_retiredmajor_notdisabled.md` (New)
    * **Title**: Own Service (VOW Act): Ineligible - Retired Officer Not Disabled
    * **Purpose**: Explains ineligibility for non-disabled high-ranking retirees under VOW Act path.
    * **Content/Question**: "Military retirees at the rank of Major, Lieutenant Commander, or higher are not eligible for preference unless they are disabled veterans. (OPM Vet Guide, 'Types of Preference'). Based on your responses, you may not be eligible for veteran's preference if you retire at this rank without a disability."
    * **Choices**:
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_vow_honorableconditions.md` (New)
    * **Title**: Own Service (VOW Act): Expected Character of Service
    * **Purpose**: Checks for expected honorable discharge via VOW Act certification.
    * **Content/Question**: "To receive preference, discharge must be under honorable conditions. Does your VOW Act certification state you are expected to be discharged/released under honorable conditions (i.e., an Honorable or General discharge)? (See OPM Vet Guide, 'A word about the VOW Act' regarding certification requirements)."
    * **Choices**:
        * "Yes, my certification indicates an expected Honorable or General discharge." -> `advisor/ownservice_checkdisability_intro.md` (Routing to check disability first, then sole survivor, then service periods; wording on subsequent pages may need to remind user this is based on certification until DD214 issued)
        * "No, my certification indicates otherwise, or I cannot obtain such certification." -> `advisor/ineligible_vow_discharge_type.md`
        * "Return to Advisor Start"

* **File**: `advisor/ineligible_vow_discharge_type.md` (New)
    * **Title**: Own Service (VOW Act): Ineligible - Discharge Not Expected to be Honorable
    * **Purpose**: Explains ineligibility if VOW certification doesn't indicate honorable discharge.
    * **Content/Question**: "Veteran's preference requires eventual discharge or release under honorable conditions. If your VOW Act certification does not indicate an expected honorable discharge, you may not proceed with a claim for preference at this time under the VOW Act. (See OPM Vet Guide, 'A word about the VOW Act')."
    * **Choices**:
        * "Return to Advisor Start"

### 4. "Own Service" - Routing for Preference Type (Disability, Sole Survivor, 5-Point):
(This sequence begins after honorable conditions are confirmed for either Discharged or VOW Act paths)

* **File**: `advisor/ownservice_checkdisability_intro.md` (New - Placeholder for Phase 2 start, but needed for routing in Phase 1)
    * **Title**: Veteran's Preference Advisor - Check for Service-Connected Disability or Purple Heart
    * **Purpose**: To determine if the veteran might be eligible for 10-point preference due to disability or Purple Heart.
    * **Content/Question**: "Next, we'll check if you might be eligible for 10-point preference. Do you have a service-connected disability recognized by the Department of Veterans Affairs (VA) or your branch of service, OR have you received a Purple Heart? (See OPM Vet Guide, '10-Point Disability Preference (XP)' for Purple Heart)."
    * **Choices**:
        * "Yes, I have a service-connected disability OR I received a Purple Heart." -> `advisor/ownservice_disability_details.md` (File to be created in Phase 2 - Disability Path)
        * "No." -> `advisor/ownservice_discharged_checkfirst_solesurvivor.md`
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_discharged_checkfirst_solesurvivor.md` (Existing, content adjusted for flow)
    * **Title**: Own Service: Check for Sole Survivorship Preference
    * **Purpose**: Checks for 0-point Sole Survivorship Preference (SSP) before checking 5-point criteria.
    * **Content/Question**: "You've indicated no current claim to disability/Purple Heart preference. Now we need to determine other types of preference you might be eligible for. Were you released or discharged from active duty after August 29, 2008, by reason of a 'sole survivorship discharge'? (See OPM Vet Guide, '0-point Preference (SSP)')."
    * **Choices**:
        * "Yes, I believe I had a sole survivorship discharge." -> `advisor/ownservice_ssp_eligible.md` (File to be created in Phase 4 - Sole Survivor Path)
        * "No, or I'm not sure." -> `advisor/ownservice_nodisability_nossps_checkserviceperiod.md` (Renamed from `ownservice_nodisability_checkserviceperiod.md` for clarity of this path)
        * "Return to Advisor Start"

### 5. "Own Service" - Path for 5-Point Preference (TP Basic Cases):
(This path is for those who are not claiming/eligible for disability or SSP at this stage of the advisor flow)

* **File**: `advisor/ownservice_nodisability_nossps_checkserviceperiod.md` (Replaces `ownservice_nodisability_checkserviceperiod.md`)
    * **Title**: Own Service: Check Service Periods for 5-Point Preference (TP)
    * **Purpose**: Asks about qualifying service periods for 5-point preference (TP).
    * **Content/Question**: "Since you haven't indicated eligibility for disability or sole survivorship preference at this stage, let's check if your service meets criteria for 5-point preference (TP). Did your active service (not solely for training, if you are non-disabled) include any of the following periods or events? (Select all that apply, or the one that best fits. We will address the 24-month service requirement later if applicable. See OPM Vet Guide, '5-Point Preference (TP)' for details on qualifying periods.)"
    * **Choices**:
        * "Service during a declared war (specifically World War II: December 7, 1941 - April 28, 1952)." -> `advisor/ownservice_tp_wartime_wwii.md`
        * "Service during the period April 28, 1952, through July 1, 1955." -> `advisor/ownservice_tp_period_1952_1955.md`
        * "Service for more than 180 consecutive days (other than for training), any part of which occurred after January 31, 1955, and before October 15, 1976." -> `advisor/ownservice_tp_period_1955_1976.md`
        * "Service during the Gulf War from August 2, 1990, through January 2, 1992." -> `advisor/ownservice_tp_period_gulfwar1.md`
        * "Service for more than 180 consecutive days (other than for training), any part of which occurred during the period beginning September 11, 2001, and ending on August 31, 2010 (the last day of Operation Iraqi Freedom)." -> `advisor/ownservice_tp_period_post911_oif.md`
        * "Service in a campaign or expedition for which a campaign medal has been authorized (e.g., Armed Forces Expeditionary Medal)." (Refer to OPM Vet Guide Appendix A for a list) -> `advisor/ownservice_tp_campaignmedal.md`
        * "None of the above service periods or medals apply to me." -> `advisor/ineligible_ownservice_noqualifyingperiod.md`

* **File**: `advisor/ownservice_tp_wartime_wwii.md`
    * **Title**: Own Service: WWII Service for 5-Point Preference
    * **Purpose**: Confirms WWII service for 5-point TP. The 24-month rule generally doesn't apply here.
    * **Content/Question**: "You indicated service during World War II (December 7, 1941 - April 28, 1952). This service qualifies for 5-point preference (TP), provided your discharge was honorable and other general conditions are met. The 24-month minimum service rule generally does not apply to this period for establishing preference eligibility (OPM Vet Guide, '5-Point Preference (TP)')."
    * **Choices**:
        * "Confirm, proceed to eligibility summary." -> `advisor/eligible_tp_5point.md`
        * "I made a mistake, check other service periods." -> `advisor/ownservice_nodisability_nossps_checkserviceperiod.md`
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_tp_period_1952_1955.md`
    * **Title**: Own Service: Service April 1952 - July 1955 for 5-Point Preference
    * **Purpose**: Confirms service for 5-point TP. The 24-month rule generally doesn't apply here.
    * **Content/Question**: "You indicated service during the period April 28, 1952, through July 1, 1955. This service qualifies for 5-point preference (TP), provided your discharge was honorable and other general conditions are met. The 24-month minimum service rule generally does not apply to this period for establishing preference eligibility (OPM Vet Guide, '5-Point Preference (TP)')."
    * **Choices**:
        * "Confirm, proceed to eligibility summary." -> `advisor/eligible_tp_5point.md`
        * "I made a mistake, check other service periods." -> `advisor/ownservice_nodisability_nossps_checkserviceperiod.md`
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_tp_period_1955_1976.md`
    * **Title**: Own Service: Service 1955-1976 (>180 days) for 5-Point Preference
    * **Purpose**: Confirms service and checks applicability of 24-month rule.
    * **Content/Question**: "You indicated service for more than 180 consecutive days (other than for training), with some part after January 31, 1955, and before October 15, 1976. This service generally qualifies for 5-point preference (TP). The 24-month minimum active duty service requirement typically applies only to veterans who originally enlisted after September 7, 1980, or first began active duty on or after October 14, 1982 (see 38 U.S.C. 5303A(d) and OPM Vet Guide, '5-Point Preference (TP)'). For your service in the 1955-1976 period, did your original enlistment in the Armed Forces occur after September 7, 1980, OR did you first begin any period of active duty on or after October 14, 1982?"
    * **Choices**:
        * "No, my original enlistment/active duty for the qualifying service started before those dates." -> `advisor/eligible_tp_5point.md`
        * "Yes, my original enlistment/active duty started on or after those dates." -> `advisor/ownservice_tp_24month_rule_check.md`
        * "I made a mistake, check other service periods." -> `advisor/ownservice_nodisability_nossps_checkserviceperiod.md`
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_tp_period_gulfwar1.md`
    * **Title**: Own Service: Gulf War Service (1990-1992) for 5-Point Preference
    * **Purpose**: Confirms service during Gulf War; leads to 24-month rule check.
    * **Content/Question**: "You indicated service during the Gulf War (August 2, 1990, through January 2, 1992). This service can qualify for 5-point preference (TP) if other conditions, including a minimum service duration for some, are met. (OPM Vet Guide, '5-Point Preference (TP)' and 'A word about Gulf War Preference')."
    * **Choices**:
        * "Continue to check service duration requirements." -> `advisor/ownservice_tp_24month_rule_check.md`
        * "I made a mistake, check other service periods." -> `advisor/ownservice_nodisability_nossps_checkserviceperiod.md`
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_tp_period_post911_oif.md`
    * **Title**: Own Service: Post-9/11 Service / OIF (>180 days) for 5-Point Preference
    * **Purpose**: Confirms service post-9/11; leads to 24-month rule check.
    * **Content/Question**: "You indicated service for more than 180 consecutive days (other than for training), with some part occurring from September 11, 2001, through August 31, 2010 (Operation Iraqi Freedom). This service can qualify for 5-point preference (TP) if other conditions, including a minimum service duration for some, are met. (OPM Vet Guide, '5-Point Preference (TP)')."
    * **Choices**:
        * "Continue to check service duration requirements." -> `advisor/ownservice_tp_24month_rule_check.md`
        * "I made a mistake, check other service periods." -> `advisor/ownservice_nodisability_nossps_checkserviceperiod.md`
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_tp_campaignmedal.md`
    * **Title**: Own Service: Campaign Medal for 5-Point Preference
    * **Purpose**: Confirms service in a campaign/expedition; leads to 24-month rule check.
    * **Content/Question**: "You indicated service in a campaign or expedition for which a campaign medal has been authorized (e.g., Armed Forces Expeditionary Medal). This service can qualify for 5-point preference (TP) if other conditions, including a minimum service duration for some, are met. (Refer to OPM Vet Guide Appendix A for a list of qualifying medals/campaigns)."
    * **Choices**:
        * "Continue to check service duration requirements." -> `advisor/ownservice_tp_24month_rule_check.md`
        * "I made a mistake, check other service periods." -> `advisor/ownservice_nodisability_nossps_checkserviceperiod.md`
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_tp_24month_rule_check.md`
    * **Title**: Own Service: 5-Point Preference - Minimum Service Enlistment Date Check
    * **Purpose**: Checks if the 24-month service requirement potentially applies based on original enlistment date.
    * **Content/Question**: 
        > For some service periods (like Gulf War, Post-9/11 OIF, or Campaign Medal service), a minimum service duration applies if you originally enlisted after September 7, 1980, OR began active duty on or after October 14, 1982. This rule generally requires 24 months of continuous active duty OR serving the full period for which you were called/ordered to active duty, unless certain exceptions apply (e.g., disability separation for 10-point preference, hardship separation; see OPM Vet Guide, '5-Point Preference (TP)'). 
        >
        > Did you originally enlist after September 7, 1980, OR first begin any period of active duty on or after October 14, 1982?
    * **Choices**:
        * "Yes, my original enlistment/active duty started on or after those dates." -> `advisor/ownservice_tp_24month_duration.md`
        * "No, my original enlistment/active duty for the qualifying service period started before those dates." -> `advisor/eligible_tp_5point.md` (24-month rule does not apply to them for this service)
        * "I made a mistake, check other service periods." -> `advisor/ownservice_nodisability_nossps_checkserviceperiod.md`
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_tp_24month_duration.md` (New)
    * **Title**: Own Service: 5-Point Preference - Minimum Service Duration Fulfilled
    * **Purpose**: Checks if the 24-month/full period active duty requirement was met.
    * **Content/Question**: "You indicated your relevant original enlistment or start of active duty was after September 7, 1980, or on/after October 14, 1982, respectively. Did you complete at least 24 months of continuous active duty, OR the full period for which you were called or ordered to active duty (if less than 24 months)? (OPM Vet Guide, '5-Point Preference (TP)')"
    * **Choices**:
        * "Yes, I served 24 months continuously OR the full period for which I was called/ordered." -> `advisor/eligible_tp_5point.md`
        * "No, I did not complete 24 months OR the full period." -> `advisor/ownservice_tp_24month_exceptions.md`
        * "I made a mistake with my enlistment date." -> `advisor/ownservice_tp_24month_rule_check.md`
        * "Return to Advisor Start"

* **File**: `advisor/ownservice_tp_24month_exceptions.md` (New)
    * **Title**: Own Service: 5-Point Preference - Minimum Service Duration Exceptions
    * **Purpose**: Checks for exceptions if the 24-month/full period active duty was not met.
    * **Content/Question**: "The 24-month minimum service rule (or full period if shorter) generally applies if you originally enlisted after September 7, 1980, or began active duty on or after October 14, 1982. However, this rule does not apply if you were separated for a service-connected disability (which would typically make you eligible for 10-point preference) or for hardship (under 10 U.S.C. 1171 or 1173). (OPM Vet Guide, '5-Point Preference (TP)'). Do either of these exceptions apply to your situation for the period of service in question?"
    * **Choices**:
        * "Yes, I was separated due to a service-connected disability." -> `advisor/ownservice_disability_details.md` (Link to Phase 2 - Disability Path, as this is a 10-point preference condition)
        * "Yes, I was separated for hardship under 10 U.S.C. 1171 or 1173." -> `advisor/eligible_tp_5point.md`
        * "No, neither of these exceptions apply." -> `advisor/ineligible_tp_minduration.md`
        * "I made a mistake with my service duration." -> `advisor/ownservice_tp_24month_duration.md`
        * "Return to Advisor Start"

### 6. Outcome Files for Phase 1 (5-Point Path):

* **File**: `advisor/eligible_tp_5point.md` (New)
    * **Title**: Veteran's Preference Advisor - Potential 5-Point Eligibility (TP)
    * **Purpose**: Informs the user they may be eligible for 5-point preference (TP).
    * **Content/Question**: "Based on your responses, you appear to meet the criteria for 5-point veteran's preference (TP), provided your discharge was (or will be, if VOW Act applies) under honorable conditions and all other general eligibility requirements are met. This is an initial assessment and not a final determination of preference. Remember to claim preference when applying for Federal jobs and be prepared to provide necessary documentation (like your DD Form 214 or VOW Act certification)."
    * **Choices**:
        * "Learn more about what to do next" (Link to a general info page, or OPM guidance)
        * "Return to Advisor Start"

* **File**: `advisor/ineligible_tp_minduration.md` (New)
    * **Title**: Veteran's Preference Advisor - Ineligible for 5-Point Preference (Minimum Service Not Met)
    * **Purpose**: Explains ineligibility for 5-point TP due to not meeting minimum service duration without applicable exceptions.
    * **Content/Question**: "To qualify for 5-point preference based on your service period and original enlistment/active duty start date (after Sep 7, 1980/Oct 14, 1982), you generally must have served continuously for 24 months OR the full period for which you were called or ordered to active duty, unless specific exceptions apply (like a separation for service-connected disability qualifying for 10-point preference, or a hardship separation). (OPM Vet Guide, '5-Point Preference (TP)'). Based on your responses, it appears you may not meet this minimum service requirement for 5-point preference under this specific service path."
    * **Choices**:
        * "Review service duration or exception choices." -> `advisor/ownservice_tp_24month_duration.md`
        * "Review service period choices again." -> `advisor/ownservice_nodisability_nossps_checkserviceperiod.md`
        * "Return to Advisor Start"

* **File**: `advisor/ineligible_ownservice_noqualifyingperiod.md` (New)
    * **Title**: Veteran's Preference Advisor - Potentially Ineligible for 5-Point Preference (No Qualifying Period Indicated)
    * **Purpose**: Explains potential ineligibility if no qualifying service periods for 5-point preference are selected by a non-disabled veteran not claiming SSP.
    * **Content/Question**: "Based on your responses, it appears your service does not fall into the specified periods or involve a qualifying campaign medal for 5-point preference (TP) as a veteran who, in this path, has not indicated a service-connected disability or sole survivorship discharge. (See OPM Vet Guide, '5-Point Preference (TP)'). If you made an error or wish to explore other preference types (like based on disability), please return to the relevant section."
    * **Choices**:
        * "I want to re-check for disability preference (10-point) or sole survivorship." -> `advisor/ownservice_checkdisability_intro.md`
        * "Review service period choices again." -> `advisor/ownservice_nodisability_nossps_checkserviceperiod.md`
        * "Return to Advisor Start"

This updated Phase 1 plan provides a more detailed structure for the "Own Service (No Disability, Basic Cases)" path, with clear routing and endpoints. Remember that Phases 2 (Disability), 3 (Derived Preference), and 4 (Sole Survivor, other complex cases) will build upon this foundation.
