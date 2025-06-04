---
layout: default
title: Veteran's Preference Advisor Audit Report
---

# Veteran's Preference Advisor Audit Report

## Introduction

This report details the findings of an audit of the Veteran's Preference Advisor tool. The purpose of this audit is to compare the logic and content of the advisor's interactive paths with the official U.S. Office of Personnel Management (OPM) Veteran's Guide for HR Professionals (`hrdocs.txt`). This audit aims to identify discrepancies, content gaps, areas needing clarification, and citation issues to ensure the advisor provides accurate and comprehensive guidance to users.

## Methodology

The audit was conducted by systematically reviewing the advisor's question and answer flows, as represented in the `advisor/*.md` files and visualized in `advisor/advisor_diagram.md`. Each path and decision point within the advisor was compared against relevant sections of the OPM Vet Guide (`hrdocs.txt`).

The process involved:
1.  Identifying key topics and rules outlined in the OPM Vet Guide relevant to veteran's preference.
2.  Tracing corresponding paths within the advisor.
3.  Comparing the advisor's questions, guidance, and outcomes against the specific language and rules in the OPM Vet Guide.
4.  Noting any deviations, omissions, or areas where clarity could be improved.
5.  Verifying citations for accuracy and completeness, where present.

## Findings

This section details the specific observations and discrepancies found during the audit.

### General Observations

*   **Overall Structure:** The advisor attempts to cover a wide range of scenarios for both veterans and their family members. The flow is generally logical, but some complex rules are difficult to represent in a simple question-answer format, leading to potential simplifications or omissions.
*   **Citation Use:** Citations are present in many files but are not consistently applied to every decision point or piece of guidance derived from the OPM Vet Guide. Some citations are general references to page numbers, which can be broad. (Further detail on specific citation issues will be covered in a dedicated review task - Task 1.2).
*   **User Experience:** The advisor often uses direct quotes or paraphrases from the OPM Vet Guide, which is good for accuracy but can sometimes be dense for users. Opportunities may exist to simplify language while retaining accuracy.

### Specific Path Discrepancies

#### 1. Clarity of "Honorable Conditions" for Discharge

*   **Advisor Files Involved:**
    *   `advisor/ownservice_intro.md`
    *   `advisor/ownservice_discharged_honorableconditions.md`
    *   `advisor/ineligible_discharge_type.md`
    *   `advisor/ownservice_vow_honorableconditions.md`
    *   `advisor/ineligible_vow_discharge_type.md`
*   **Advisor Logic:**
    *   `ownservice_intro.md` correctly directs users who are discharged to `ownservice_discharged_checkretired.md` and VOW Act candidates to `ownservice_vow_checkretired.md`.
    *   `ownservice_discharged_honorableconditions.md` asks "What was the character of your discharge?" with options: "Honorable or General Discharge," "Other than Honorable/General," and "I'm not sure." It correctly states, "To receive preference, a veteran must have been discharged or released from active duty in the Armed Forces under honorable conditions. This typically means an Honorable or General discharge."
    *   `ineligible_discharge_type.md` is the end point for "Other than Honorable/General" and correctly states "Veteran's preference requires a discharge or release under honorable conditions (i.e., an Honorable or General discharge)."
    *   `ownservice_vow_honorableconditions.md` asks "Does your VOW Act certification state you are expected to be discharged/released under honorable conditions (i.e., an Honorable or General discharge)?"
    *   `ineligible_vow_discharge_type.md` is the end point if the VOW certification is not expected to be honorable.
*   **OPM Vet Guide Reference:**
    *   "Types of Preference": "To receive preference, a veteran must have been discharged or released from active duty in the Armed Forces under honorable conditions (i.e., with an honorable or general discharge)."
    *   "A word about the VOW (Veterans Opportunity to Work) Act": "A “certification” is any written document from the armed forces that certifies the service member is expected to be discharged or released from active duty service in the armed forces under honorable conditions within 120 days after the certification is submitted by the applicant."
*   **Analysis:** The advisor accurately reflects the OPM Vet Guide's requirement for discharge "under honorable conditions" and correctly specifies that this typically means an "Honorable or General discharge." The VOW Act path also correctly checks for expected honorable conditions.
*   **Conclusion:** No discrepancy found for this specific point. The advisor is consistent with the Vet Guide regarding the definition of "honorable conditions."

#### 2. Retired Military Rank Limitation (Initial Check)

*   **Advisor Files Involved:**
    *   `advisor/ownservice_discharged_checkretired.md`
    *   `advisor/ownservice_discharged_retiredmajor_isdisabled.md`
    *   `advisor/ineligible_retiredmajor_notdisabled.md`
    *   `advisor/ownservice_vow_checkretired.md`
    *   `advisor/ownservice_vow_retiredmajor_isdisabled.md`
    *   `advisor/ineligible_vow_retiredmajor_notdisabled.md`
*   **Advisor Logic:**
    *   `ownservice_discharged_checkretired.md` asks "Are you a military retiree at the rank of Major, Lieutenant Commander, or higher?"
    *   If "Yes," it leads to `ownservice_discharged_retiredmajor_isdisabled.md`, which then asks "Do you have a service-connected disability...?"
    *   If "No" to disability, it leads to `ineligible_retiredmajor_notdisabled.md`.
    *   A similar path exists for VOW Act candidates starting with `ownservice_vow_checkretired.md`.
*   **OPM Vet Guide Reference:**
    *   "Types of Preference": "Military retirees at the rank of major, lieutenant commander, or higher are not eligible for preference in appointment unless they are disabled veterans. (This does not apply to Reservists who will not begin drawing military retired pay until age 60.)"
    *   "Eligibility for Veterans' Preference in RIF": Provides more nuanced rules for RIF, distinguishing between retirees below Major and those at or above Major, and specific conditions for disability. (This report focuses on preference in appointment, as the advisor seems geared towards that, but RIF rules are noted for completeness of OPM content).
*   **Analysis:**
    *   The advisor correctly implements the general rule for preference in *appointment* that retired Majors/Lt. Commanders or higher are ineligible unless disabled.
    *   The parenthetical note about Reservists not drawing retired pay until age 60 is present in the advisor files.
    *   The advisor does not currently seem to differentiate between preference for appointment and preference for RIF, which have different rules for retirees. The current paths appear focused on initial appointment.
*   **Conclusion:** For preference in *appointment*, the advisor correctly applies the rank limitation. If the advisor is intended to cover RIF scenarios, this area would need significant expansion. For now, assuming focus on appointment, this is not a discrepancy.

#### 3. VOW Act Nuances

*   **Advisor Files Involved:**
    *   `advisor/ownservice_intro.md` (leads to VOW path)
    *   `advisor/ownservice_vow_checkretired.md`
    *   `advisor/ownservice_vow_honorableconditions.md`
    *   `advisor/ineligible_vow_discharge_type.md`
*   **Advisor Logic:**
    *   The path starting at `ownservice_intro.md` for active duty members expecting discharge within 120 days correctly directs them to `ownservice_vow_checkretired.md`.
    *   `ownservice_vow_honorableconditions.md` asks if the "VOW Act certification state you are expected to be discharged/released under honorable conditions (i.e., an Honorable or General discharge)?" and links to `ineligible_vow_discharge_type.md` if not.
    *   The advisor mentions "(and I have or can obtain a certification as described in the VOW Act)" in `ownservice_intro.md`.
*   **OPM Vet Guide Reference:**
    *   "A word about the VOW (Veterans Opportunity to Work) Act": "This new section requires Federal agencies to treat certain active duty service members as preference eligibles for purposes of an appointment in the competitive or excepted service, even though the service members have not been discharged or released from active duty."
    *   "A “certification” is any written document from the armed forces that certifies the service member is expected to be discharged or released from active duty service in the armed forces under honorable conditions within 120 days after the certification is submitted by the applicant. The certification letter should be on letterhead of the appropriate military branch of the service and contain (1) the military service dates including the expected discharge or release date; and (2) the character of service."
*   **Analysis:**
    *   The advisor correctly identifies the 120-day window and the requirement for certification of expected honorable conditions.
    *   The advisor also correctly states that the discharge must eventually be under honorable conditions.
    *   The content of the certification (letterhead, specific details like service dates, expected discharge, character of service) is mentioned in the Vet Guide but not detailed in the advisor. While the advisor states "certification as described in the VOW Act," it doesn't reiterate these specific documentary requirements. This might be a minor gap in user guidance, as the user might not know what "as described" entails without checking the Vet Guide separately.
*   **Conclusion:** The core logic is correct. Minor gap in not detailing the *contents* of the VOW Act certification, though it directs users to the Vet Guide reference.

#### 4. SSP (Sole Survivorship Preference)

*   **Advisor Files Involved:**
    *   `advisor/ownservice_discharged_checkfirst_solesurvivor.md`
    *   `advisor/ownservice_ssp_checkdd214_date.md` (leads to `ineligible_ssp_dischargedate.md` or `ownservice_ssp_discharge_reason.md`)
    *   `advisor/ownservice_ssp_checkdd214_reason.md` (leads to `ineligible_ssp_reason.md` or `ownservice_ssp_familycriteria_info.md` - note: `ownservice_ssp_eligible.md` and `ownservice_ssp_familycriteria_info.md` were not in the initial file reads, but their linked presence is assumed from other files like `ineligible_ssp_reason.md` and `ownservice_ssp_checkdd214_reason.md`. If they don't exist, this is a larger gap.)
    *   `advisor/ineligible_ssp_dischargedate.md`
    *   `advisor/ineligible_ssp_reason.md`
*   **Advisor Logic:**
    *   `ownservice_discharged_checkfirst_solesurvivor.md` asks: "Were you released or discharged from active duty after August 29, 2008, by reason of a 'sole survivorship discharge'?"
    *   This directly links to `ownservice_ssp_eligible.md` (if "Yes") or `ownservice_nodisability_nossps_checkserviceperiod.md` (if "No").
    *   However, other files like `ineligible_ssp_reason.md` and `ineligible_ssp_dischargedate.md` suggest a more detailed path might exist or was intended, for instance, `ownservice_ssp_checkdd214_date.md` which then leads to `ownservice_ssp_discharge_reason.md`. The diagram also implies a more granulated path.
    *   `ineligible_ssp_dischargedate.md` correctly states the discharge must be *after August 29, 2008*.
    *   `ineligible_ssp_reason.md` correctly states the discharge must be due to 'sole survivorship discharge'.
*   **OPM Vet Guide Reference:**
    *   "0-point Preference (SSP)": "The Hubbard Act amended the eligibility categories for veterans’ preference purposes by adding subparagraph (H) to 5 U.S.C. 2108(3). Subparagraph (H) establishes a new veterans’ preference eligibility category for veterans released or discharged from a period of active duty from the armed forces, after August 29, 2008, by reason of a “sole survivorship discharge.”"
    *   It further details what sole survivorship means (family member death/disability in service) and that it's a 0-point preference.
*   **Analysis:**
    *   The advisor correctly identifies the two main conditions: discharge after August 29, 2008, and reason being "sole survivorship discharge."
    *   The question in `ownservice_discharged_checkfirst_solesurvivor.md` combines these two. If the user says "No", they are routed away from SSP.
    *   The existence of `ineligible_ssp_reason.md` and `ineligible_ssp_dischargedate.md` suggests that there should be separate questions for the date and reason, as reflected in `ownservice_ssp_checkdd214_date.md` and `ownservice_ssp_checkdd214_reason.md`. If `ownservice_discharged_checkfirst_solesurvivor.md` is the *only* entry point to SSP, it might prematurely rule out users who meet one criterion but not the other and are unsure.
    *   The advisor does not seem to explain the family circumstances that define a "sole survivorship discharge" (e.g., "only surviving child in a family in which the father or mother or one or more siblings... served... was killed, died..."). This is a significant detail of SSP.
    *   The advisor does not explicitly state that SSP is a 0-point preference, which is a key characteristic.
*   **Conclusion:**
    *   The basic date and discharge reason are mentioned.
    *   Potential issue: The main entry point `ownservice_discharged_checkfirst_solesurvivor.md` might be too restrictive by combining two conditions. A more granular approach (asking date then reason) as suggested by other SSP-related filenames would be better.
    *   Significant Gap: The advisor does not explain the underlying family service/sacrifice conditions that lead to a "sole survivorship discharge."
    *   Gap: The advisor does not mention that SSP is a 0-point preference.
    *   Assumption: Files like `ownservice_ssp_eligible.md` and `ownservice_ssp_familycriteria_info.md` exist and cover more details. If not, the gap is larger. A check of the file list from `ls` output is needed. The `ls` output from previous steps did not show `ownservice_ssp_eligible.md` or `ownservice_ssp_familycriteria_info.md`. This indicates these files likely do **not** exist, making the gaps identified more certain.

#### 5. Derived Preference - Spouse of Disabled Veteran

*   **Advisor Files Involved:**
    *   `advisor/derived_intro.md`
    *   `advisor/derived_spouse_vetliving.md`
    *   `advisor/derived_spouse_vetqualifiedforemployment.md`
    *   `advisor/ineligible_derived_spouse_vetqualified.md`
    *   `advisor/derived_spouse_vetdisabilityreason.md`
    *   `advisor/ineligible_derived_spouse_vetnotdisabled.md`
    *   `advisor/derived_spouse_vetdisabilitydetails.md`
    *   `advisor/eligible_xp_derived_spouse.md`
    *   `advisor/derived_spouse_furtherclarification.md`
    *   `advisor/eligible_xp_derived_spouse_conditional.md`
*   **Advisor Logic:**
    *   The path correctly first checks if the veteran is living (`derived_spouse_vetliving.md`).
    *   Then, if the veteran is qualified for Federal employment (`derived_spouse_vetqualifiedforemployment.md`). If yes, leads to `ineligible_derived_spouse_vetqualified.md`. This aligns with OPM: "neither may receive preference if the veteran is living and is qualified for Federal employment."
    *   Next, it checks if the disqualification is due to a service-connected disability (`derived_spouse_vetdisabilityreason.md`). If not, leads to `ineligible_derived_spouse_vetnotdisabled.md`. This aligns with OPM.
    *   `derived_spouse_vetdisabilitydetails.md` then presents three scenarios for presumed disqualification if the veteran is unemployed:
        1.  "100 percent disabled and/or unemployable."
        2.  "retired, been separated, or resigned from a civil service position on the basis of a disability that is service-connected in origin."
        3.  "attempted to obtain a civil service position or other position along the lines of his or her usual occupation and has failed to qualify because of a service-connected disability."
        These directly lead to `eligible_xp_derived_spouse.md`.
    *   A fourth option, "none of the specific situations above fully apply, or I'm unsure," leads to `derived_spouse_furtherclarification.md`, which then guides to `eligible_xp_derived_spouse_conditional.md`, noting that OPM states preference *may* be allowed but "warrants a more careful analysis".
*   **OPM Vet Guide Reference:**
    *   "10-Point Derived Preference (XP) -> Spouse": "Ten points are added to the passing examination score or rating of the spouse of a disabled veteran who is disqualified for a Federal position along the general lines of his or her usual occupation because of a service-connected disability. Such a disqualification may be presumed when the veteran is unemployed and
        * is rated by appropriate military or Department of Veterans Affairs authorities to be 100 percent disabled and/or unemployable; or
        * has retired, been separated, or resigned from a civil service position on the basis of a disability that is service-connected in origin; or
        * has attempted to obtain a civil service position or other position along the lines of his or her usual occupation and has failed to qualify because of a service-connected disability.
    *   Preference may be allowed in other circumstances but anything less than the above warrants a more careful analysis."
*   **Analysis:**
    *   The advisor path for derived preference for a spouse of a living, disabled veteran very closely mirrors the conditions outlined in the OPM Vet Guide.
    *   It correctly identifies the initial conditions (veteran living, not qualified for federal employment due to service-connected disability).
    *   It correctly lists the three scenarios for presumed disqualification when the veteran is unemployed.
    *   It correctly handles the "other circumstances" by directing the user to a conditional eligibility page and advising more careful analysis by the hiring agency.
*   **Conclusion:** No discrepancy found. The advisor accurately reflects the OPM Vet Guide for this specific derived preference path.

#### 6. Derived Preference - Mother of Deceased Veteran

*   **Advisor Files Involved:**
    *   `advisor/derived_intro.md` (entry point)
    *   `advisor/derived_mother_vetstatus.md` (selects "Deceased")
    *   `advisor/derived_mother_deceased_vetdeathcond.md` (checks veteran's service/death conditions)
    *   `advisor/ineligible_derived_mother_deceased_vetdeathcond.md` (ineligible outcome)
    *   `advisor/derived_mother_common_fatherinfo.md` (checks marriage to veteran's father)
    *   `advisor/ineligible_derived_mother_notmarriedtofather.md` (ineligible outcome)
    *   `advisor/derived_mother_common_currentmarital.md` (checks mother's current marital/living status)
    *   `advisor/ineligible_derived_mother_currentmarital.md` (ineligible outcome)
    *   `advisor/derived_mother_clarify_currentmarital.md` (clarification for complex marital situations)
    *   `advisor/eligible_xp_derived_mother.md` (eligible outcome)
*   **Advisor Logic:**
    1.  `derived_mother_vetstatus.md`: User selects "Deceased."
    2.  `derived_mother_deceased_vetdeathcond.md`: Asks if veteran died under honorable conditions on active duty during specific periods (war, 1952-1955, or campaign medal). If "No," leads to `ineligible_derived_mother_deceased_vetdeathcond.md`. This aligns with OPM.
    3.  `derived_mother_common_fatherinfo.md`: Asks "Are you now, or were you previously, married to the father of the veteran?" If "No," leads to `ineligible_derived_mother_notmarriedtofather.md`. This aligns with OPM.
    4.  `derived_mother_common_currentmarital.md`: Asks about mother's current marital/living situation:
        *   "I live with my husband (who is either the veteran's father or my husband through remarriage), and he is totally and permanently disabled." -> `eligible_xp_derived_mother.md`. This aligns with OPM.
        *   "I am widowed (from the veteran's father or a subsequent husband), divorced, or legally separated (from the veteran's father or a subsequent husband), AND I have not remarried since that specific event..." -> `eligible_xp_derived_mother.md`. This aligns with OPM.
        *   "I am currently married, and my husband is NOT totally and permanently disabled." -> `ineligible_derived_mother_currentmarital.md`. This aligns with OPM.
        *   "None of these situations accurately describe mine." -> `derived_mother_clarify_currentmarital.md` (provides more guidance).
*   **OPM Vet Guide Reference:**
    *   "10-Point Derived Preference (XP) -> Mother of a deceased veteran": "Ten points are added... mother of a veteran who died under honorable conditions while on active duty during a war or during the period April 28, 1952, through July 1, 1955, or in a campaign or expedition for which a campaign medal has been authorized; and
        * she is or was married to the father of the veteran; and
        * she lives with her totally and permanently disabled husband (either the veteran's father or her husband through remarriage); or
        * she is widowed, divorced, or separated from the veteran's father and has not remarried; or
        * she remarried but is widowed, divorced, or legally separated from her husband when she claims preference."
    *   The guide also notes: "Preference is not given to widows or mothers of deceased veterans who qualify for preference under 5 U.S.C. 2108 (1) (B), (C) or (2). Thus, the widow or mother of a deceased disabled veteran who served after 1955, but did not serve in a war, campaign, or expedition, would not be entitled to preference." This is handled by `derived_mother_deceased_vetdeathcond.md` and its ineligible path.
*   **Analysis:**
    *   The advisor path for the mother of a deceased veteran correctly implements all the specified conditions from the OPM Vet Guide:
        *   Veteran's service/death conditions.
        *   Mother's marriage to the veteran's father.
        *   Mother's current marital/living status, including nuances of remarriage and husband's disability.
    *   The `derived_mother_clarify_currentmarital.md` provides a good fallback for complex situations.
*   **Conclusion:** No discrepancy found. The advisor accurately reflects the OPM Vet Guide for this specific derived preference path.

#### 7. Derived Preference - Mother of Living Disabled Veteran

*   **Advisor Files Involved:**
    *   `advisor/derived_intro.md` (entry point)
    *   `advisor/derived_mother_vetstatus.md` (selects "Living AND is permanently and totally disabled...")
    *   `advisor/derived_mother_living_vetseparation.md` (checks veteran's separation conditions)
    *   `advisor/ineligible_derived_mother_living_vetseparation.md` (ineligible outcome)
    *   `advisor/derived_mother_common_fatherinfo.md` (common path: checks marriage to veteran's father)
    *   `advisor/ineligible_derived_mother_notmarriedtofather.md` (common path: ineligible outcome)
    *   `advisor/derived_mother_common_currentmarital.md` (common path: checks mother's current marital/living status)
    *   `advisor/ineligible_derived_mother_currentmarital.md` (common path: ineligible outcome)
    *   `advisor/derived_mother_clarify_currentmarital.md` (common path: clarification)
    *   `advisor/eligible_xp_derived_mother.md` (common path: eligible outcome)
*   **Advisor Logic:**
    *   `advisor/derived_mother_vetstatus.md` (selects "Living AND is permanently and totally disabled...") This directly cites OPM (OPM Vet Guide, section [146]).
    2.  `derived_mother_living_vetseparation.md`: Asks if "veteran separated with an honorable or general discharge from active duty? (This active duty could have been performed at any time and includes training service in the Reserves or National Guard (OPM Vet Guide, section [146]))". If "No," leads to `ineligible_derived_mother_living_vetseparation.md`. This aligns with OPM.
    3.  The path then merges with the common logic used for "Mother of Deceased Veteran":
        *   `derived_mother_common_fatherinfo.md`: Checks marriage to veteran's father.
        *   `derived_mother_common_currentmarital.md`: Checks mother's current marital/living status.
        These subsequent steps and their logic are identical to those analyzed for the "Mother of Deceased Veteran" and were found to be accurate.
*   **OPM Vet Guide Reference:**
    *   "10-Point Derived Preference (XP) -> Mother of a disabled veteran": "Ten points are added... mother of a living disabled veteran if the veteran was separated with an honorable or general discharge from active duty, including training service in the Reserves or National Guard, performed at any time and is permanently and totally disabled from a service-connected injury or illness; and the mother:
        * is or was married to the father of the veteran; and
        * lives with her totally and permanently disabled husband (either the veteran's father or her husband through remarriage); or
        * is widowed, divorced, or separated from the veteran's father and has not remarried; or
        * remarried but is widowed, divorced, or legally separated from her husband when she claims preference."
*   **Analysis:**
    *   The advisor path for the mother of a living disabled veteran correctly implements all the specified conditions from the OPM Vet Guide:
        *   Veteran's permanent and total service-connected disability (initial condition from `derived_mother_vetstatus.md`).
        *   Veteran's separation under honorable or general discharge, including training service (from `derived_mother_living_vetseparation.md`).
        *   Mother's marriage to the veteran's father (common path).
        *   Mother's current marital/living status (common path).
*   **Conclusion:** No discrepancy found. The advisor accurately reflects the OPM Vet Guide for this specific derived preference path.

#### 8. Campaign Medal Dates vs. General Periods & Minimum Service Obligation (5-Point TP Preference)

*   **Advisor Files Involved:**
    *   `advisor/ownservice_nodisability_nossps_checkserviceperiod.md` (Central decision point for non-disabled, non-SSP veterans)
    *   `advisor/ownservice_tp_wartime_wwii.md` -> `eligible_tp_5point.md`
    *   `advisor/ownservice_tp_period_1952_1955.md` -> `eligible_tp_5point.md`
    *   `advisor/ownservice_tp_period_1955_1976.md` (Checks enlistment date for 24-month rule)
    *   `advisor/ownservice_tp_period_gulfwar1.md` -> `ownservice_tp_24month_rule_check.md`
    *   `advisor/ownservice_tp_period_post911_oif.md` -> `ownservice_tp_24month_rule_check.md`
    *   `advisor/ownservice_tp_campaignmedal.md` -> `ownservice_tp_24month_rule_check.md`
    *   `advisor/ownservice_tp_24month_rule_check.md` (Asks if enlistment was post-Sep 7, 1980 / Oct 14, 1982)
    *   `advisor/ownservice_tp_24month_duration.md` (Asks if 24 months served or full period)
    *   `advisor/ownservice_tp_24month_exceptions.md` (Checks for disability/hardship exceptions to 24-month rule)
    *   `advisor/eligible_tp_5point.md` (Eligible outcome)
    *   `advisor/ineligible_tp_minduration.md` (Ineligible due to not meeting 24-month rule)
    *   `advisor/ineligible_ownservice_noqualifyingperiod.md` (Ineligible if no qualifying period/medal selected)
*   **Advisor Logic:**
    *   `ownservice_nodisability_nossps_checkserviceperiod.md` correctly lists the various service periods and campaign medal option.
    *   For WWII and 1952-1955 period, it correctly leads to `eligible_tp_5point.md` as the 24-month rule is generally not applicable.
    *   For service 1955-1976: `ownservice_tp_period_1955_1976.md` specifically asks if original enlistment was after Sep 7, 1980, or active duty after Oct 14, 1982. If NO (i.e., enlisted *before* these dates), it correctly goes to `eligible_tp_5point.md`. If YES, it proceeds to `ownservice_tp_24month_rule_check.md`. This correctly applies the 24-month rule only to those who enlisted/started active duty after the specified 1980/1982 dates.
    *   For Gulf War, Post-9/11 OIF, and Campaign Medal service, the advisor correctly routes to `ownservice_tp_24month_rule_check.md`.
    *   `ownservice_tp_24month_rule_check.md` asks about the enlistment/active duty start date. If before Sep 7, 1980/Oct 14, 1982, it leads to `eligible_tp_5point.md`. If after, it leads to `ownservice_tp_24month_duration.md`.
    *   `ownservice_tp_24month_duration.md` asks if 24 months or the full period was served. "Yes" leads to `eligible_tp_5point.md`. "No" leads to `ownservice_tp_24month_exceptions.md`.
    *   `ownservice_tp_24month_exceptions.md` correctly checks for separation due to service-connected disability (leads to 10-point path) or hardship (leads to `eligible_tp_5point.md`). If neither, then `ineligible_tp_minduration.md`.
*   **OPM Vet Guide Reference:**
    *   "5-Point Preference (TP)": Lists the qualifying periods and campaign medal basis.
    *   Crucially: "A campaign medal holder or Gulf War veteran who originally enlisted after September 7, 1980, (or began active duty on or after October 14, 1982, and has not previously completed 24 months of continuous active duty) must have served continuously for 24 months or the full period called or ordered to active duty. The 24-month service requirement does not apply to 10-point preference eligibles separated for disability incurred or aggravated in the line of duty, or to veterans separated for hardship or other reasons under 10 U.S.C. 1171 or 1173."
    *   The guide implies the 24-month rule is primarily for "campaign medal holder or Gulf War veteran" who enlisted after the 1980/82 dates. It also applies to service "For more than 180 consecutive days, other than for training, any part of which occurred during the period beginning September 11, 2001, and ending on August 31, 2010..." if enlistment was after 1980/82.
    *   For the "more than 180 consecutive days... after January 31, 1955, and before October 15, 1976" period, the 24-month rule should only apply if their enlistment was after Sep 7, 1980. The advisor handles this correctly in `ownservice_tp_period_1955_1976.md`.
*   **Analysis:**
    *   The advisor correctly distinguishes between service periods that automatically grant 5-point preference (WWII, 1952-1955) and those that might require checking the 24-month minimum service obligation (Campaign Medal, Gulf War, Post-9/11 OIF, and the 1955-1976 period *if* enlistment was late).
    *   The logic for the 24-month rule, including the critical enlistment/active duty start date check (`ownservice_tp_24month_rule_check.md` and its specific application in `ownservice_tp_period_1955_1976.md`), and the subsequent checks for duration and exceptions, appears to be correctly implemented.
    *   The distinction between "service *during* a specific period" (e.g., Gulf War Aug 2, 1990 - Jan 2, 1992) versus "service *for more than 180 days*, any part of which occurred during X and Y dates" (e.g., Post-9/11) is handled by the initial selections in `ownservice_nodisability_nossps_checkserviceperiod.md`.
*   **Conclusion:** No discrepancy found. The advisor's logic for applying the 5-point preference criteria, including the various service periods and the 24-month minimum service obligation with its exceptions, aligns with the OPM Vet Guide.

---
The main logical paths have been reviewed. Other specific details or less common scenarios might exist within the OPM Vet Guide that are not explicitly tested here, but the core decision trees for major preference categories appear to be covered.
---

### Content Gaps

*   **Sole Survivorship Preference (SSP) Details:** As noted in Finding #4, the advisor does not detail the family circumstances required for SSP (death or disability of parent/sibling in service) nor that it's a 0-point preference. The likely non-existence of `ownservice_ssp_eligible.md` and `ownservice_ssp_familycriteria_info.md` means these details are missing.
*   **RIF (Reduction in Force) Scenarios:** The OPM Vet Guide has extensive sections on how veteran's preference applies in RIF situations, including different rules for retired military members. The current advisor seems primarily focused on preference for appointments and does not appear to address RIF scenarios. This is a major content gap if the advisor intends to be comprehensive.
*   **Specifics of "Active Duty for Training":** While some paths mention "active duty for training by National Guard or Reserve soldiers does not qualify as 'active duty' for preference" for non-disabled users, or that it *is* included for disabled veterans (e.g. `derived_mother_living_vetseparation.md`), a more centralized explanation or check related to "active duty for training" could be beneficial, especially for users who may not select a disability path initially.
*   **Details on SF-15:** Several eligibility pages mention completing the SF-15 but do not provide details on what this form entails or common documentation needed beyond what's hinted at in the eligibility criteria. While the form itself is external, a brief note on typical accompanying documents for different preference types could be helpful.

### Citation Issues

*   (Initial observations, more detailed review in Task 1.2, which is dedicated to citations)
    *   Citations are generally to page numbers in the OPM Vet Guide (e.g., `(OPM Vet Guide, section [123])`), which can be broad.
    *   Not all decision points or guidance statements derived from the Vet Guide are directly cited. For example, `ownservice_discharged_honorableconditions.md` explains honorable/general discharge requirements but doesn't have a specific citation number in that sentence.
    *   The SSP files (`ineligible_ssp_reason.md`, `ineligible_s_s_p_dischargedate.md`) have  without a preceding `[cite_start]` and actual citation number. This seems to be a formatting error. `ownservice_discharged_checkfirst_solesurvivor.md` correctly cites "(OPM Vet Guide, section [OPM Vet Guide, '0-point Preference (SSP)'])".
    *   Some citations are to "(OPM Vet Guide, section [OPM Vet Guide, 'Types of Preference'])" which is a very broad section.

## Recommendations

Based on the findings of this audit, the following recommendations are made to improve the Veteran's Preference Advisor:

1.  **SSP Enhancements:**
    *   Create the missing files: `ownservice_ssp_eligible.md` and `ownservice_ssp_familycriteria_info.md`.
    *   Modify `ownservice_discharged_checkfirst_solesurvivor.md` to link to a more granular questioning path:
        *   Start with `ownservice_ssp_checkdd214_date.md` (discharge date).
        *   Then to `ownservice_ssp_checkdd214_reason.md` (reason for discharge).
        *   Then to the new `ownservice_ssp_familycriteria_info.md` (to explain and confirm family circumstances).
        *   Finally, to `ownservice_ssp_eligible.md` if all criteria are met.
    *   The `ownservice_ssp_eligible.md` page should clearly state that SSP is a 0-point preference and briefly explain its benefits (e.g., listed ahead of non-preference eligibles).
    *   Correct citation formatting in `ineligible_ssp_reason.md` and `ineligible_ssp_dischargedate.md`.

2.  **VOW Act Clarification:**
    *   In `ownservice_intro.md` or `ownservice_vow_honorableconditions.md`, add a brief explanation of the key information a VOW Act certification should contain (e.g., service dates, expected discharge date, character of service, on letterhead), or provide a more direct link to the specific paragraph in the OPM Vet Guide that details this.

3.  **Consider RIF Scope:**
    *   Determine if RIF scenarios are within the intended scope of the advisor. If so, this will require a significant new section and logic paths, carefully distinguishing RIF preference rules from appointment preference rules, especially for retirees. If out of scope, this should be clarified to the user.

4.  **SF-15 Information:**
    *   Consider adding a general information page about the SF-15, perhaps linked from the various "eligible" pages. This page could mention that the SF-15 is "Application for 10-Point Veteran Preference" and generally requires documentation of service, disability (if applicable), and relationship (for derived preference).

5.  **Review "Active Duty for Training" Clarity:**
    *   Evaluate if a more prominent, general explanation of how "active duty for training" is treated for preference (especially for non-disabled individuals) is needed early in the "own service" path, rather than only being mentioned in specific sub-paths.

6.  **Citation Improvement (Cross-reference with Task 1.2):**
    *   Wherever possible, make citations more specific to sections or sub-sections of the OPM Vet Guide rather than just page numbers.
    *   Ensure all critical decision points based on Vet Guide rules have a corresponding citation.
    *   Review and correct formatting errors for citations (e.g.,  issues).

## Conclusion

The Veteran's Preference Advisor generally aligns well with the OPM Vet Guide for the core paths analyzed related to preference in appointments. The logic for determining 5-point and 10-point preferences (both for own service and derived) largely follows the documented rules, particularly concerning service periods, disability levels, and familial relationships.

The main areas identified for improvement include:
*   **SSP (Sole Survivorship Preference):** This path is incomplete. Key details about family circumstances and the nature of the 0-point preference are missing, and the entry flow could be more granular. Missing files need to be created.
*   **VOW Act Certification Details:** While the core logic is sound, providing users with more detail on what constitutes a valid certification would be beneficial.
*   **Scope Definition for RIF:** The advisor currently does not address RIF, which is a significant part of veteran's preference. This should either be added or explicitly noted as out of scope.
*   **Citation Specificity and Consistency:** Citations could be more granular and consistently applied.

Addressing these findings, particularly the gaps in the SSP path and clarifications for the VOW Act, will enhance the accuracy and completeness of the guidance provided to users. The structural integrity of most existing paths is good, providing a solid foundation for these improvements.
