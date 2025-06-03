Phase 3

Okay, here is a multi-step asynchronous plan for **Phase 3: Derived Preference Path**. This phase focuses on users who are seeking veteran's preference based on the service of a qualifying veteran, specifically as a spouse, widow(er), or mother.

This plan assumes users arrive from `advisor/start.md` by selecting "The service of a qualifying veteran, if I am a spouse, widow(er), or mother," which links to the first file in this phase: `advisor/derived_intro.md`.

---

## Veteran's Preference Advisor: Site Development Plan - Phase 3: Derived Preference Path

**Overall Goal for Phase 3:** To create the decision tree paths for individuals claiming 10-point "derived preference" (XP) based on the service of a qualifying veteran (spouse, widow(er), or mother).

**General Instructions for AI Agent:**
* For each task below, create the specified Markdown file in the `/advisor/` directory.
* Ensure each file uses `layout: default` (or the custom advisor layout).
* Include a link back to the start: `[Return to Advisor Start](./start.md)` on nearly every page.
* Incorporate citations from `hrdocs.txt` as indicated, using the format ``.
* [cite_start]Content should guide the user to determine potential eligibility for 10-point derived preference (XP) and highlight the need for SF-15 and supporting documentation. [cite: 34]

---

### Phase 3 Development Tasks (Asynchronous)

Each task involves creating one Markdown file with the specified attributes.

**Task 3.1: Create `advisor/derived_intro.md`**
* **File**: `advisor/derived_intro.md` (New - this was a placeholder in the original overall plan)
* **Title**: `Derived Veteran's Preference - Relationship to Veteran`
* **Purpose**: To determine the claimant's relationship to the veteran on whose service the claim is based.
* **Content/Question**:
    ```markdown
    You are seeking to determine potential eligibility for veteran's preference based on the service of a qualifying veteran. This is generally a 10-point preference. What is your relationship to this veteran?

    [cite_start](Note: Applicants claiming 10-point preference must typically complete Standard Form (SF) 15, Application for 10-Point Veteran Preference, and submit the requested documentation [cite: 34]).
    ```
* **Choices**:
    * `"I am the spouse of a veteran."` -> `advisor/derived_spouse_vetliving.md`
    * `"I am the widow or widower of a veteran."` -> `advisor/derived_widow_divorced.md`
    * `"I am the mother of a veteran."` -> `advisor/derived_mother_vetstatus.md`
    * `"None of the above / I made a mistake."` -> `advisor/start.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

---
#### Spouse Path Files (Tasks 3.2 - 3.9)
---

**Task 3.2: Create `advisor/derived_spouse_vetliving.md`**
* **File**: `advisor/derived_spouse_vetliving.md` (New)
* **Title**: `Derived Preference (Spouse): Veteran's Status`
* **Purpose**: To determine if the veteran is living, which is a primary condition for spouse preference.
* **Content/Question**:
    ```markdown
    Is the veteran on whose service you are basing your claim currently living?
    ```
* **Choices**:
    * `"Yes, the veteran is living."` -> `advisor/derived_spouse_vetqualifiedforemployment.md`
    * `"No, the veteran is deceased."` -> `advisor/derived_switch_todeceasedpath.md` (Utility node to guide to widow/mother if applicable)
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.3: Create `advisor/derived_spouse_vetqualifiedforemployment.md`**
* **File**: `advisor/derived_spouse_vetqualifiedforemployment.md` (New)
* **Title**: `Derived Preference (Spouse): Veteran's Employment Qualification`
* **Purpose**: To determine if the living veteran is qualified for Federal employment, as this impacts spouse's eligibility.
* **Content/Question**:
    ```markdown
    Is the living veteran qualified for Federal employment (i.e., able to work and apply for Federal jobs)?

    [cite_start](A spouse generally cannot receive preference if the veteran is living and is qualified for Federal employment [cite: 131]).
    ```
* **Choices**:
    * `"Yes, the veteran is living and qualified for Federal employment."` -> `advisor/ineligible_derived_spouse_vetqualified.md`
    * `"No, the veteran is living but is NOT qualified for Federal employment."` -> `advisor/derived_spouse_vetdisabilityreason.md`
    * `"[Return to previous question]"` -> `advisor/derived_spouse_vetliving.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.4: Create `advisor/derived_spouse_vetdisabilityreason.md`**
* **File**: `advisor/derived_spouse_vetdisabilityreason.md` (New)
* **Title**: `Derived Preference (Spouse): Reason for Veteran's Non-Qualification`
* **Purpose**: To ascertain if the veteran's non-qualification for employment is due to a service-connected disability.
* **Content/Question**:
    ```markdown
    [cite_start]Is the veteran disqualified for a Federal position along the general lines of his or her usual occupation *because of a service-connected disability*? [cite: 132]
    ```
* **Choices**:
    * `"Yes, due to a service-connected disability."` -> `advisor/derived_spouse_vetdisabilitydetails.md`
    * `"No, the reason is not a service-connected disability."` -> `advisor/ineligible_derived_spouse_vetnotdisabled.md`
    * `"[Return to previous question]"` -> `advisor/derived_spouse_vetqualifiedforemployment.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.5: Create `advisor/derived_spouse_vetdisabilitydetails.md`**
* **File**: `advisor/derived_spouse_vetdisabilitydetails.md` (New)
* **Title**: `Derived Preference (Spouse): Veteran's Disability Details`
* **Purpose**: To check for conditions where a veteran's disqualification for their usual occupation due to service-connected disability is presumed.
* **Content/Question**:
    ```markdown
    You indicated the veteran is disqualified for their usual occupation due to a service-connected disability. Such disqualification may be presumed if the veteran is unemployed AND one of the following situations applies. Which best describes the veteran's situation?
    ```
* **Choices**:
    * [cite_start]`"The veteran is unemployed AND is rated by appropriate military or Department of Veterans Affairs authorities to be 100 percent disabled and/or unemployable."` [cite: 133] -> `advisor/eligible_xp_derived_spouse.md`
    * [cite_start]`"The veteran is unemployed AND has retired, been separated, or resigned from a civil service position on the basis of a disability that is service-connected in origin."` [cite: 134] -> `advisor/eligible_xp_derived_spouse.md`
    * [cite_start]`"The veteran is unemployed AND has attempted to obtain a civil service position or other position along the lines of his or her usual occupation and has failed to qualify because of a service-connected disability."` [cite: 135] -> `advisor/eligible_xp_derived_spouse.md`
    * `"The veteran is disqualified due to a service-connected disability, but none of the specific situations above fully apply, or I'm unsure."` -> `advisor/derived_spouse_furtherclarification.md`
    * `"[Return to previous question]"` -> `advisor/derived_spouse_vetdisabilityreason.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.6: Create `advisor/ineligible_derived_spouse_vetqualified.md`**
* **File**: `advisor/ineligible_derived_spouse_vetqualified.md` (New)
* **Title**: `Derived Preference (Spouse): Potentially Ineligible - Veteran Qualified`
* **Purpose**: Explains potential ineligibility if the veteran is living and qualified for employment.
* **Content/Question**:
    ```markdown
    [cite_start]Generally, a spouse cannot receive derived preference if the veteran is living and qualified for Federal employment[cite: 131]. Based on your response, you may not be eligible for derived preference as a spouse under this condition.
    ```
* **Choices**:
    * `"[Return to check veteran's employment qualification]"` -> `advisor/derived_spouse_vetqualifiedforemployment.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.7: Create `advisor/ineligible_derived_spouse_vetnotdisabled.md`**
* **File**: `advisor/ineligible_derived_spouse_vetnotdisabled.md` (New)
* **Title**: `Derived Preference (Spouse): Potentially Ineligible - Disqualification Not Due to Service-Connected Disability`
* **Purpose**: Explains potential ineligibility if veteran's non-qualification isn't due to service-connected disability.
* **Content/Question**:
    ```markdown
    [cite_start]For a spouse to claim derived preference for a living veteran, the veteran must be disqualified for a Federal position along the general lines of his or her usual occupation *because of a service-connected disability*[cite: 132]. Based on your response that the disqualification is not due to a service-connected disability, you may not be eligible for derived preference.
    ```
* **Choices**:
    * `"[Return to check reason for non-qualification]"` -> `advisor/derived_spouse_vetdisabilityreason.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.8: Create `advisor/derived_spouse_furtherclarification.md`**
* **File**: `advisor/derived_spouse_furtherclarification.md` (New)
* **Title**: `Derived Preference (Spouse): Further Clarification Recommended`
* **Purpose**: To guide users whose veteran's disability situation is not clear-cut for presumed disqualification.
* **Content/Question**:
    ```markdown
    You've indicated the veteran is disqualified for their usual occupation due to a service-connected disability, but the specific conditions for a presumed disqualification were not selected. [cite_start]OPM states that preference *may* be allowed in other circumstances, but this "warrants a more careful analysis" by the hiring agency[cite: 136].

    You will need to provide detailed documentation with your SF-15. This advisor cannot make a determination in such cases, but you may still be eligible.
    ```
* **Choices**:
    * `"Understood, proceed to information on conditional eligibility."` -> `advisor/eligible_xp_derived_spouse_conditional.md`
    * `"[Return to disability detail choices]"` -> `advisor/derived_spouse_vetdisabilitydetails.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.9: Create `advisor/eligible_xp_derived_spouse_conditional.md`**
* **File**: `advisor/eligible_xp_derived_spouse_conditional.md` (New)
* **Title**: `Veteran's Preference Advisor - Potential Conditional 10-Point Derived Preference (XP) - Spouse`
* **Purpose**: Informs user of potential eligibility as a spouse, emphasizing their situation requires careful agency review.
* **Content/Question**:
    ```markdown
    Based on your responses, you *may* meet the criteria for 10-point derived veteran's preference (XP) as the spouse of a veteran disqualified for their usual occupation due to a service-connected disability.

    [cite_start]However, because your situation does not fall under the standard presumptions for disqualification, your claim will require a more careful analysis by the hiring agency, and possibly OPM[cite: 136].

    Key reminders:
    * Complete the SF-15, Application for 10-Point Veteran Preference.
    * Be prepared to provide comprehensive documentation supporting the veteran's service-connected disability and their disqualification from employment in their usual occupation.

    This is an initial assessment and not a final determination of preference.
    ```
* **Choices**:
    * `"Learn more about applying with 10-point preference (SF-15)"` (Link to OPM guidance on SF-15 or a future detailed info page)
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

---
#### Widow/Widower Path Files (Tasks 3.10 - 3.16)
---

**Task 3.10: Create `advisor/derived_widow_divorced.md`**
* **File**: `advisor/derived_widow_divorced.md` (New)
* **Title**: `Derived Preference (Widow/Widower): Marital Status at Veteran's Death`
* **Purpose**: To check if the claimant was divorced from the veteran.
* **Content/Question**:
    ```markdown
    [cite_start]Were you divorced from the veteran at the time of their death? [cite: 139]
    ```
* **Choices**:
    * `"Yes, I was divorced."` -> `advisor/ineligible_derived_widow_divorced.md`
    * `"No, I was not divorced."` -> `advisor/derived_widow_remarried.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.11: Create `advisor/derived_widow_remarried.md`**
* **File**: `advisor/derived_widow_remarried.md` (New)
* **Title**: `Derived Preference (Widow/Widower): Remarriage Status`
* **Purpose**: To check if the claimant has remarried.
* **Content/Question**:
    ```markdown
    Have you remarried since the veteran's death? [cite_start](If you remarried but that subsequent marriage was annulled, select 'No, or my remarriage was annulled.') [cite: 139]
    ```
* **Choices**:
    * `"Yes, I have remarried (and the marriage was not annulled)."` -> `advisor/ineligible_derived_widow_remarried.md`
    * `"No, I have not remarried OR my subsequent remarriage was annulled."` -> `advisor/derived_widow_vetservice_condition.md`
    * `"[Return to previous question]"` -> `advisor/derived_widow_divorced.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.12: Create `advisor/derived_widow_vetservice_condition.md`**
* **File**: `advisor/derived_widow_vetservice_condition.md` (New)
* **Title**: `Derived Preference (Widow/Widower): Veteran's Service or Death Conditions`
* **Purpose**: To determine if the veteran's service or circumstances of death meet criteria for derived preference.
* **Content/Question**:
    ```markdown
    Which of the following conditions applied to the veteran?
    ```
* **Choices**:
    * [cite_start]`"The veteran served during a declared war (e.g., World War II: Dec 7, 1941 - Apr 28, 1952), OR during the period April 28, 1952, through July 1, 1955, OR in a campaign or expedition for which a campaign medal has been authorized (see OPM Vet Guide Appendix A for a list of medals)."` [cite: 139] -> `advisor/eligible_xp_derived_widow.md`
    * [cite_start]`"The veteran died while on active duty (that included service as described in the option above) under conditions that would not have been the basis for other than an honorable or general discharge."` [cite: 140] -> `advisor/eligible_xp_derived_widow.md`
    * [cite_start]`"The veteran's service was after 1955 and was NOT in a war, campaign, or expedition for which a medal was authorized, AND they did not die on active duty during such specific service."` (As per OPM Vet Guide, 'Note' following 5 U.S.C. 2108 (1) (B), (C) or (2) [cite: 152]) -> `advisor/ineligible_derived_widow_vetservicenotqualifying.md`
    * `"None of these, or I'm unsure."` -> `advisor/derived_widow_clarify_vetservice.md`
    * `"[Return to previous question]"` -> `advisor/derived_widow_remarried.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.13: Create `advisor/ineligible_derived_widow_divorced.md`**
* **File**: `advisor/ineligible_derived_widow_divorced.md` (New)
* **Title**: `Derived Preference (Widow/Widower): Potentially Ineligible - Divorced`
* **Purpose**: Explains potential ineligibility if divorced from the veteran.
* **Content/Question**:
    ```markdown
    [cite_start]To be eligible for derived preference as a widow or widower, you must not have been divorced from the veteran at the time of their death[cite: 139]. Based on your response, you may not be eligible.
    ```
* **Choices**:
    * `"[Return to check marital status at death]"` -> `advisor/derived_widow_divorced.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.14: Create `advisor/ineligible_derived_widow_remarried.md`**
* **File**: `advisor/ineligible_derived_widow_remarried.md` (New)
* **Title**: `Derived Preference (Widow/Widower): Potentially Ineligible - Remarried`
* **Purpose**: Explains potential ineligibility if remarried (and not annulled).
* **Content/Question**:
    ```markdown
    [cite_start]To be eligible for derived preference as a widow or widower, you must not have remarried since the veteran's death, or if you remarried, that subsequent marriage must have been annulled[cite: 139]. Based on your response, you may not be eligible.
    ```
* **Choices**:
    * `"[Return to check remarriage status]"` -> `advisor/derived_widow_remarried.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.15: Create `advisor/ineligible_derived_widow_vetservicenotqualifying.md`**
* **File**: `advisor/ineligible_derived_widow_vetservicenotqualifying.md` (New)
* **Title**: `Derived Preference (Widow/Widower): Potentially Ineligible - Veteran's Service`
* **Purpose**: Explains potential ineligibility based on veteran's service type if not war/campaign related.
* **Content/Question**:
    ```markdown
    For derived preference as a widow/widower, the veteran's service generally must have been during a declared war, specific post-war periods (April 28, 1952 - July 1, 1955), or in a campaign or expedition for which a medal was authorized; [cite_start]OR the veteran must have died on active duty during such qualifying service[cite: 139, 140].

    [cite_start]Preference is generally not granted to widows or mothers if the deceased veteran's own preference eligibility was based *only* on other criteria (e.g., service after 1955 that was not in a war or campaign, such as >180 days of active duty or Gulf War service without a specific campaign medal)[cite: 152]. Based on your response, the veteran's service may not qualify for this type of derived preference.
    ```
* **Choices**:
    * `"[Return to check veteran's service conditions]"` -> `advisor/derived_widow_vetservice_condition.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.16: Create `advisor/derived_widow_clarify_vetservice.md`**
* **File**: `advisor/derived_widow_clarify_vetservice.md` (New)
* **Title**: `Derived Preference (Widow/Widower): Clarification on Veteran's Service`
* **Purpose**: Advises user to check documentation for veteran's service details.
* **Content/Question**:
    ```markdown
    To determine eligibility, please review the veteran's service records (such as the DD Form 214). Specifically, check if their service included:
    * A declared war (e.g., World War II: December 7, 1941 - April 28, 1952).
    * Service during the period April 28, 1952, through July 1, 1955.
    * Service in a campaign or expedition for which a campaign medal was authorized (see OPM Vet Guide Appendix A).
    * [cite_start]Also, verify if the veteran died while on active duty during such service, under conditions that would not have been the basis for other than an honorable or general discharge[cite: 140].

    [cite_start]You can find details in the OPM Vet Guide under "10-Point Derived Preference (XP) - Widow/Widower"[cite: 139, 152].
    ```
* **Choices**:
    * `"[Return to veteran's service condition choices]"` -> `advisor/derived_widow_vetservice_condition.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

---
#### Mother Path Files (Tasks 3.17 - 3.26)
---

**Task 3.17: Create `advisor/derived_mother_vetstatus.md`**
* **File**: `advisor/derived_mother_vetstatus.md` (New)
* **Title**: `Derived Preference (Mother): Veteran's Status (Deceased or Living Disabled)`
* **Purpose**: To determine if the veteran (son/daughter) is deceased or living and permanently/totally disabled.
* **Content/Question**:
    ```markdown
    Is the veteran (your son or daughter) on whose service you are basing your claim:
    ```
* **Choices**:
    * `"Deceased."` -> `advisor/derived_mother_deceased_vetdeathcond.md`
    * [cite_start]`"Living AND is permanently and totally disabled from a service-connected injury or illness."` [cite: 146] -> `advisor/derived_mother_living_vetseparation.md`
    * `"Neither of these apply / I'm unsure."` -> `advisor/ineligible_derived_mother_vetstatus.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.18: Create `advisor/derived_mother_deceased_vetdeathcond.md`**
* **File**: `advisor/derived_mother_deceased_vetdeathcond.md` (New)
* **Title**: `Mother of Deceased Veteran: Conditions of Veteran's Death & Service`
* **Purpose**: To check if the deceased veteran's service and death conditions qualify.
* **Content/Question**:
    ```markdown
    Regarding your deceased veteran child: Did they die under honorable conditions while on active duty, AND was this active duty performed during:
    * a declared war (e.g., World War II), OR
    * the period April 28, 1952, through July 1, 1955, OR
    * [cite_start]in a campaign or expedition for which a campaign medal has been authorized? [cite: 141]
    ```
* **Choices**:
    * `"Yes, all those conditions apply."` -> `advisor/derived_mother_common_fatherinfo.md`
    * [cite_start]`"No, those conditions do not all apply."` (This may include situations where the veteran's service was after 1955 but not in a war/campaign, making the mother ineligible for derived preference [cite: 152]) -> `advisor/ineligible_derived_mother_deceased_vetdeathcond.md`
    * `"[Return to previous question]"` -> `advisor/derived_mother_vetstatus.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.19: Create `advisor/derived_mother_living_vetseparation.md`**
* **File**: `advisor/derived_mother_living_vetseparation.md` (New)
* **Title**: `Mother of Living Disabled Veteran: Veteran's Separation Conditions`
* **Purpose**: To check the separation conditions of the living, permanently and totally disabled veteran.
* **Content/Question**:
    ```markdown
    You indicated your veteran child is living and permanently and totally disabled from a service-connected injury or illness. Was this veteran separated with an honorable or general discharge from active duty? [cite_start](This active duty could have been performed at any time and includes training service in the Reserves or National Guard [cite: 146]).
    ```
* **Choices**:
    * `"Yes, separated under honorable or general discharge."` -> `advisor/derived_mother_common_fatherinfo.md`
    * `"No, or discharge was different."` -> `advisor/ineligible_derived_mother_living_vetseparation.md`
    * `"[Return to previous question]"` -> `advisor/derived_mother_vetstatus.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.20: Create `advisor/derived_mother_common_fatherinfo.md`**
* **File**: `advisor/derived_mother_common_fatherinfo.md` (New)
* **Title**: `Mother's Preference: Relationship to Veteran's Father`
* **Purpose**: To check the mother's marital history with the veteran's father, a common requirement.
* **Content/Question**:
    ```markdown
    [cite_start]Are you now, or were you previously, married to the father of the veteran? [cite: 142, 147]
    ```
* **Choices**:
    * `"Yes."` -> `advisor/derived_mother_common_currentmarital.md`
    * `"No."` -> `advisor/ineligible_derived_mother_notmarriedtofather.md`
    * `"[Return to Veteran's Status (Deceased/Living Disabled)]"` -> `advisor/derived_mother_vetstatus.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.21: Create `advisor/derived_mother_common_currentmarital.md`**
* **File**: `advisor/derived_mother_common_currentmarital.md` (New)
* **Title**: `Mother's Preference: Current Living and Marital Status`
* **Purpose**: To determine if the mother's current living and marital status meets eligibility criteria.
* **Content/Question**:
    ```markdown
    Which of the following best describes your current living and marital situation?
    ```
* **Choices**:
    * [cite_start]`"I live with my husband (who is either the veteran's father or my husband through remarriage), and he is totally and permanently disabled."` [cite: 143, 148] -> `advisor/eligible_xp_derived_mother.md`
    * [cite_start]`"I am widowed (from the veteran's father or a subsequent husband), divorced, or legally separated (from the veteran's father or a subsequent husband), AND I have not remarried since that specific event of widowhood, divorce, or separation."` (This covers [cite: 144, 149] [cite_start]and the essence of [cite: 145, 150]) -> `advisor/eligible_xp_derived_mother.md`
    * `"I am currently married, and my husband is NOT totally and permanently disabled."` -> `advisor/ineligible_derived_mother_currentmarital.md`
    * `"None of these situations accurately describe mine."` -> `advisor/derived_mother_clarify_currentmarital.md`
    * `"[Return to previous question]"` -> `advisor/derived_mother_common_fatherinfo.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.22: Create `advisor/ineligible_derived_mother_vetstatus.md`**
* **File**: `advisor/ineligible_derived_mother_vetstatus.md` (New)
* **Title**: `Mother's Preference: Potentially Ineligible - Veteran's Status`
* **Purpose**: Explains ineligibility if veteran is not deceased under qualifying conditions or living P&T disabled.
* **Content/Question**:
    ```markdown
    To be eligible for derived preference as a mother, the veteran (your son or daughter) must generally be either:
    1. [cite_start]Deceased under specific conditions related to their active duty service (during a war, specific period, or campaign)[cite: 141], OR
    2. [cite_start]Living and permanently and totally disabled from a service-connected injury or illness, and honorably separated[cite: 146].

    Based on your response, the veteran's status may not meet these requirements.
    ```
* **Choices**:
    * `"[Return to check veteran's status]"` -> `advisor/derived_mother_vetstatus.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.23: Create `advisor/ineligible_derived_mother_deceased_vetdeathcond.md`**
* **File**: `advisor/ineligible_derived_mother_deceased_vetdeathcond.md` (New)
* **Title**: `Mother's Preference: Potentially Ineligible - Deceased Veteran's Service/Death Conditions`
* **Purpose**: Explains ineligibility if deceased veteran's service/death doesn't meet criteria.
* **Content/Question**:
    ```markdown
    [cite_start]For a mother to claim preference for a deceased veteran, the veteran generally must have died under honorable conditions while on active duty during a declared war, specific post-war periods (April 28, 1952 - July 1, 1955), or in a campaign or expedition for which a campaign medal was authorized[cite: 141]. [cite_start]Preference is also generally not granted if the deceased veteran's own preference eligibility was based *only* on other criteria (e.g., service after 1955 not in a war/campaign)[cite: 152]. Based on your responses, these conditions may not be met.
    ```
* **Choices**:
    * `"[Return to check veteran's death/service conditions]"` -> `advisor/derived_mother_deceased_vetdeathcond.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.24: Create `advisor/ineligible_derived_mother_living_vetseparation.md`**
* **File**: `advisor/ineligible_derived_mother_living_vetseparation.md` (New)
* **Title**: `Mother's Preference: Potentially Ineligible - Living Veteran's Separation`
* **Purpose**: Explains ineligibility if living P&T disabled veteran was not honorably separated.
* **Content/Question**:
    ```markdown
    [cite_start]For a mother to claim preference for a living, permanently and totally disabled veteran, the veteran must have been separated from active duty (including training service) with an honorable or general discharge[cite: 146]. Based on your response, this condition may not be met.
    ```
* **Choices**:
    * `"[Return to check veteran's separation]"` -> `advisor/derived_mother_living_vetseparation.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.25: Create `advisor/ineligible_derived_mother_notmarriedtofather.md`**
* **File**: `advisor/ineligible_derived_mother_notmarriedtofather.md` (New)
* **Title**: `Mother's Preference: Potentially Ineligible - Marriage to Veteran's Father`
* **Purpose**: Explains ineligibility if mother was not married to veteran's father.
* **Content/Question**:
    ```markdown
    [cite_start]To be eligible for derived preference as a mother, you must be (or have been) married to the father of the veteran[cite: 142, 147]. Based on your response, this condition may not be met.
    ```
* **Choices**:
    * `"[Return to check marriage to veteran's father]"` -> `advisor/derived_mother_common_fatherinfo.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.26: Create `advisor/ineligible_derived_mother_currentmarital.md`**
* **File**: `advisor/ineligible_derived_mother_currentmarital.md` (New)
* **Title**: `Mother's Preference: Potentially Ineligible - Current Marital/Living Status`
* **Purpose**: Explains ineligibility if mother's current marital/living status doesn't meet criteria.
* **Content/Question**:
    ```markdown
    To be eligible for derived preference as a mother, your current marital and living situation must meet specific criteria. These include:
    * [cite_start]Living with your husband (veteran's father or remarried husband) who is totally and permanently disabled[cite: 143, 148], OR
    * [cite_start]Being widowed, divorced, or legally separated (from veteran's father or subsequent husband) and not having remarried since that event[cite: 144, 145, 149, 150].

    Based on your response (currently married and husband is not P&T disabled), you may not meet these conditions.
    ```
* **Choices**:
    * `"[Return to check current marital/living status]"` -> `advisor/derived_mother_common_currentmarital.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.27: Create `advisor/derived_mother_clarify_currentmarital.md`**
* **File**: `advisor/derived_mother_clarify_currentmarital.md` (New)
* **Title**: `Mother's Preference: Clarification on Current Marital/Living Status`
* **Purpose**: Advises user to check documentation for complex marital/living situations.
* **Content/Question**:
    ```markdown
    The rules for a mother's current marital and living status for derived preference can be specific and cover various situations like living with a totally and permanently disabled husband, or being widowed, divorced, or separated and not remarried.

    If your situation is complex, please carefully review the OPM Vet Guide sections for "Mother of a deceased veteran" or "Mother of a disabled veteran" and your SF-15 documentation. This advisor cannot cover all nuances.
    ```
* **Choices**:
    * `"[Return to current marital/living status choices]"` -> `advisor/derived_mother_common_currentmarital.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

---
#### General Derived Preference Outcome & Utility Files (Tasks 3.28 - 3.31)
---

**Task 3.28: Create `advisor/eligible_xp_derived_spouse.md`**
* **File**: `advisor/eligible_xp_derived_spouse.md` (New)
* **Title**: `Veteran's Preference Advisor - Potential 10-Point Derived Preference (XP) - Spouse`
* **Purpose**: Informs user of potential eligibility for 10-point derived preference as a spouse.
* **Content/Question**:
    ```markdown
    [cite_start]Based on your responses, you appear to meet the criteria for 10-point derived veteran's preference (XP) as the spouse of a veteran who is disqualified for a Federal position along the general lines of his or her usual occupation because of a service-connected disability[cite: 132, 133, 134, 135].

    This is an initial assessment and not a final determination of preference. Remember to:
    * Claim preference when applying for Federal jobs.
    * Complete the Standard Form (SF) 15, Application for 10-Point Veteran Preference.
    * Be prepared to provide necessary documentation (e.g., marriage certificate, veteran's proof of service-connected disability and unemployability/disqualification for usual occupation).
    ```
* **Choices**:
    * `"Learn more about applying with 10-point preference (SF-15)"` (Link to OPM guidance on SF-15 or a future detailed info page)
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.29: Create `advisor/eligible_xp_derived_widow.md`**
* **File**: `advisor/eligible_xp_derived_widow.md` (New)
* **Title**: `Veteran's Preference Advisor - Potential 10-Point Derived Preference (XP) - Widow/Widower`
* **Purpose**: Informs user of potential eligibility for 10-point derived preference as a widow/widower.
* **Content/Question**:
    ```markdown
    [cite_start]Based on your responses, you appear to meet the criteria for 10-point derived veteran's preference (XP) as the widow/widower of a qualifying veteran[cite: 139, 140].

    This is an initial assessment and not a final determination of preference. Remember to:
    * Claim preference when applying for Federal jobs.
    * Complete the Standard Form (SF) 15, Application for 10-Point Veteran Preference.
    * Be prepared to provide necessary documentation (e.g., marriage certificate, veteran's death certificate, veteran's proof of qualifying service).
    ```
* **Choices**:
    * `"Learn more about applying with 10-point preference (SF-15)"` (Link to OPM guidance on SF-15 or a future detailed info page)
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.30: Create `advisor/eligible_xp_derived_mother.md`**
* **File**: `advisor/eligible_xp_derived_mother.md` (New)
* **Title**: `Veteran's Preference Advisor - Potential 10-Point Derived Preference (XP) - Mother`
* **Purpose**: Informs user of potential eligibility for 10-point derived preference as a mother.
* **Content/Question**:
    ```markdown
    Based on your responses, you appear to meet the criteria for 10-point derived veteran's preference (XP) as the mother of a qualifying veteran (either deceased under specific conditions or living and permanently and totally disabled from a service-connected cause).

    This is an initial assessment and not a final determination of preference. Remember to:
    * Claim preference when applying for Federal jobs.
    * Complete the Standard Form (SF) 15, Application for 10-Point Veteran Preference.
    * Be prepared to provide necessary documentation (e.g., veteran's birth certificate listing you as mother, proof of your marriage to veteran's father, veteran's proof of service/disability/death as applicable, documentation for your current marital/living status).
    ```
* **Choices**:
    * `"Learn more about applying with 10-point preference (SF-15)"` (Link to OPM guidance on SF-15 or a future detailed info page)
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

**Task 3.31: Create `advisor/derived_switch_todeceasedpath.md`** (Utility File)
* **File**: `advisor/derived_switch_todeceasedpath.md` (New)
* **Title**: `Derived Preference: Clarification for Spouse of Deceased Veteran`
* **Purpose**: To correctly route a user who selected "Spouse" but whose veteran is deceased.
* **Content/Question**:
    ```markdown
    You indicated you are the spouse of a veteran, but that the veteran is deceased.
    * If you were married to the veteran at the time of their death and have not remarried (or that remarriage was annulled), you may be eligible as a **Widow/Widower**.
    * If you are the mother of the deceased veteran's child and meet other criteria, you might explore eligibility as a **Mother**.

    How would you like to proceed?
    ```
* **Choices**:
    * `"Proceed as a Widow/Widower."` -> `advisor/derived_widow_divorced.md`
    * `"Explore eligibility as a Mother."` -> `advisor/derived_mother_vetstatus.md` (User would then choose "Deceased")
    * `"The veteran is actually living (I made a mistake)."` -> `advisor/derived_spouse_vetqualifiedforemployment.md`
    * `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
    * `"[Return to Advisor Start]"` -> `advisor/start.md`

---

This plan provides a comprehensive set of tasks for developing Phase 3. Each task is self-contained, allowing for asynchronous execution.
