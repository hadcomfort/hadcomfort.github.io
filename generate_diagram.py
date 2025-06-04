import re
import os

def get_markdown_files(directory):
    markdown_files = []
    for entry in os.listdir(directory):
        if entry.endswith(".md") and os.path.isfile(os.path.join(directory, entry)):
            markdown_files.append(entry)
    return markdown_files

def parse_links(filepath, content, all_files):
    links = []
    # Regex to find markdown links: [text](link)
    # It needs to handle relative links starting with ./ or just the filename
    for match in re.finditer(r'\[[^\]]+\]\((advisor/([A-Za-z0-9_/-]+\.md)|(\.\/([A-Za-z0-9_/-]+\.md))|([A-Za-z0-9_/-]+\.md))\)', content):
        link_target_options = [
            match.group(2), # advisor/file.md
            match.group(4), # ./file.md
            match.group(5)  # file.md
        ]
        link_target = None
        for target in link_target_options:
            if target:
                if target.startswith("advisor/"):
                    link_target = target.split("advisor/")[1]
                else:
                    link_target = target
                break

        if link_target and link_target in all_files:
            source_file = os.path.basename(filepath)
            links.append((source_file, link_target))
    return links

def create_mermaid_id(filename):
    # Remove .md and replace special characters for Mermaid ID
    return filename.replace(".md", "").replace("-", "_").replace("/", "_")

def build_mermaid_string(relationships):
    mermaid_string = "graph TD;\n"
    nodes = set()
    for source, target in relationships:
        source_id = create_mermaid_id(source)
        target_id = create_mermaid_id(target)
        if source_id not in nodes:
            mermaid_string += f'  {source_id}["{source}"];\n'
            nodes.add(source_id)
        if target_id not in nodes:
            mermaid_string += f'  {target_id}["{target}"];\n'
            nodes.add(target_id)
        mermaid_string += f"  {source_id} --> {target_id};\n"
    return mermaid_string

def main():
    advisor_dir = "advisor"
    # List of file contents (replace with actual file reading if not pre-loaded)
    # For this script, we assume file_contents is a dictionary: {filename: content}

    # Step 1: Get all .md files in the advisor directory
    markdown_files_in_advisor = get_markdown_files(advisor_dir)

    all_relationships = []

    # This part will be manually constructed for now based on the previous read_files output
    # In a real scenario, you'd iterate and read files here.
    file_contents_raw = """[start of advisor/derived_intro.md]
---
layout: default
title: Derived Veteran's Preference - Relationship to Veteran
---

You are seeking to determine potential eligibility for veteran's preference based on the service of a qualifying veteran. This is generally a 10-point preference. What is your relationship to this veteran?

[cite_start](Note: Applicants claiming 10-point preference must typically complete Standard Form (SF) 15, Application for 10-Point Veteran Preference, and submit the requested documentation [cite: 34]).

*   `"I am the spouse of a veteran."` -> `advisor/derived_spouse_vetliving.md`
*   `"I am the widow or widower of a veteran."` -> `advisor/derived_widow_divorced.md`
*   `"I am the mother of a veteran."` -> `advisor/derived_mother_vetstatus.md`
*   `"None of the above / I made a mistake."` -> `advisor/start.md`

[Return to Advisor Start](./start.md)

[end of advisor/derived_intro.md]

[start of advisor/derived_mother_clarify_currentmarital.md]
---
layout: default
title: Mother's Preference: Clarification on Current Marital/Living Status
---

The rules for a mother's current marital and living status for derived preference can be specific and cover various situations like living with a totally and permanently disabled husband, or being widowed, divorced, or separated and not remarried.

If your situation is complex, please carefully review the OPM Vet Guide sections for "Mother of a deceased veteran" or "Mother of a disabled veteran" and your SF-15 documentation. This advisor cannot cover all nuances.

* `[Return to current marital/living status choices]` -> `derived_mother_common_currentmarital.md`
* `[Return to Advisor Start]` -> `start.md`

[end of advisor/derived_mother_clarify_currentmarital.md]

[start of advisor/derived_mother_common_currentmarital.md]
---
layout: default
title: Mother's Preference - Current Living and Marital Status
---

Which of the following best describes your current living and marital situation?

*   [cite_start]`"I live with my husband (who is either the veteran's father or my husband through remarriage), and he is totally and permanently disabled."` [cite: 143, 148] -> `eligible_xp_derived_mother.md`
*   [cite_start]`"I am widowed (from the veteran's father or a subsequent husband), divorced, or legally separated (from the veteran's father or a subsequent husband), AND I have not remarried since that specific event of widowhood, divorce, or separation."` (This covers [cite: 144, 149] [cite_start]and the essence of [cite: 145, 150]) -> `eligible_xp_derived_mother.md`
*   `"I am currently married, and my husband is NOT totally and permanently disabled."` -> `ineligible_derived_mother_currentmarital.md`
*   `"None of these situations accurately describe mine."` -> `derived_mother_clarify_currentmarital.md`

[Return to previous question](./derived_mother_common_fatherinfo.md)
[Return to Advisor Start](./start.md)

[end of advisor/derived_mother_common_currentmarital.md]

[start of advisor/derived_mother_common_fatherinfo.md]
---
layout: default
title: Mother's Preference - Relationship to Veteran's Father
---

[cite_start]Are you now, or were you previously, married to the father of the veteran? [cite: 142, 147]

* `"Yes."` -> `advisor/derived_mother_common_currentmarital.md`
* `"No."` -> `advisor/ineligible_derived_mother_notmarriedtofather.md`
* `"[Return to Veteran's Status (Deceased/Living Disabled)]"` -> `advisor/derived_mother_vetstatus.md`
* `"[Return to Advisor Start]"` -> `advisor/start.md`

[end of advisor/derived_mother_common_fatherinfo.md]

[start of advisor/derived_mother_deceased_vetdeathcond.md]
---
layout: default
title: Mother of Deceased Veteran - Conditions of Veteran's Death & Service
---

Regarding your deceased veteran child: Did they die under honorable conditions while on active duty, AND was this active duty performed during:
* a declared war (e.g., World War II), OR
* the period April 28, 1952, through July 1, 1955, OR
* [cite_start]in a campaign or expedition for which a campaign medal has been authorized? [cite: 141]

* `"Yes, all those conditions apply."` -> `advisor/derived_mother_common_fatherinfo.md`
* [cite_start]`"No, those conditions do not all apply."` (This may include situations where the veteran's service was after 1955 but not in a war/campaign, making the mother ineligible for derived preference [cite: 152]) -> `advisor/ineligible_derived_mother_deceased_vetdeathcond.md`
* `"[Return to previous question]"` -> `advisor/derived_mother_vetstatus.md`
* `"[Return to Advisor Start]"` -> `advisor/start.md`

[end of advisor/derived_mother_deceased_vetdeathcond.md]

[start of advisor/derived_mother_living_vetseparation.md]
---
layout: default
title: Mother of Living Disabled Veteran - Veteran's Separation Conditions
---

You indicated your veteran child is living and permanently and totally disabled from a service-connected injury or illness. Was this veteran separated with an honorable or general discharge from active duty? [cite_start](This active duty could have been performed at any time and includes training service in the Reserves or National Guard [cite: 146]).

* `"Yes, separated under honorable or general discharge."` -> `advisor/derived_mother_common_fatherinfo.md`
* `"No, or discharge was different."` -> `advisor/ineligible_derived_mother_living_vetseparation.md`
* `"[Return to previous question]"` -> `advisor/derived_mother_vetstatus.md`
* `"[Return to Advisor Start]"` -> `advisor/start.md`

[end of advisor/derived_mother_living_vetseparation.md]

[start of advisor/derived_mother_vetstatus.md]
---
layout: default
title: Derived Preference (Mother) - Veteran's Status (Deceased or Living Disabled)
---

Is the veteran (your son or daughter) on whose service you are basing your claim:

* `"Deceased."` -> `advisor/derived_mother_deceased_vetdeathcond.md`
* [cite_start]`"Living AND is permanently and totally disabled from a service-connected injury or illness."` [cite: 146] -> `advisor/derived_mother_living_vetseparation.md`
* `"Neither of these apply / I'm unsure."` -> `advisor/ineligible_derived_mother_vetstatus.md`
* `"[Return to Relationship Choice]"` -> `advisor/derived_intro.md`
* `"[Return to Advisor Start]"` -> `advisor/start.md`

[end of advisor/derived_mother_vetstatus.md]

[start of advisor/derived_preference_step1.md]
---
layout: default
title: Veteran's Preference Advisor - Derived Preference Step 1
---

# Derived Veteran's Preference

[cite_start]You indicated you are seeking preference based on the service of a qualifying veteran, as a spouse, widow(er), or mother[cite: 129]. [cite_start]This is known as "derived preference" because it is based on the service of a veteran who is not able to use the preference[cite: 129].

To determine potential eligibility, we first need information about the **veteran** on whose service this claim is based.

Is the veteran living?

* **[Yes, the veteran is living.](derived_preference_living_vet_step2.md)**
    * [cite_start]*In cases of derived preference for a spouse or mother of a living veteran, specific conditions apply, such as the veteran being unable to use the preference themselves due to disqualification or disability[cite: 131, 147].*

* **[No, the veteran is deceased.](derived_preference_deceased_vet_step2.md)**
    * [cite_start]*Derived preference for widows/widowers or mothers of deceased veterans also has specific qualifying conditions related to the veteran's service and the circumstances of their death[cite: 140, 142].*

---
*This advisor provides guidance based on the U.S. Office of Personnel Management (OPM) Vet Guide for HR Professionals. For official determinations, please consult directly with the hiring agency or OPM.*

[Return to Start](start.md)

[end of advisor/derived_preference_step1.md]

[start of advisor/derived_spouse_furtherclarification.md]
---
layout: default
title: Derived Preference (Spouse): Further Clarification Recommended
---

You've indicated the veteran is disqualified for their usual occupation due to a service-connected disability, but the specific conditions for a presumed disqualification were not selected. [cite_start]OPM states that preference *may* be allowed in other circumstances, but this "warrants a more careful analysis" by the hiring agency[cite: 136].

You will need to provide detailed documentation with your SF-15. This advisor cannot make a determination in such cases, but you may still be eligible.

*   `"Understood, proceed to information on conditional eligibility."` -> `eligible_xp_derived_spouse_conditional.md`
*   `"[Return to disability detail choices]"` -> `derived_spouse_vetdisabilitydetails.md`
*   `"[Return to Advisor Start]"` -> `start.md`

[end of advisor/derived_spouse_furtherclarification.md]

[start of advisor/derived_spouse_vetdisabilitydetails.md]
---
layout: default
title: Derived Preference (Spouse): Veteran's Disability Details
---

You indicated the veteran is disqualified for their usual occupation due to a service-connected disability. Such disqualification may be presumed if the veteran is unemployed AND one of the following situations applies. Which best describes the veteran's situation?

*   [cite_start]`"The veteran is unemployed AND is rated by appropriate military or Department of Veterans Affairs authorities to be 100 percent disabled and/or unemployable."` [cite: 133] -> `advisor/eligible_xp_derived_spouse.md`
*   [cite_start]`"The veteran is unemployed AND has retired, been separated, or resigned from a civil service position on the basis of a disability that is service-connected in origin."` [cite: 134] -> `advisor/eligible_xp_derived_spouse.md`
*   [cite_start]`"The veteran is unemployed AND has attempted to obtain a civil service position or other position along the lines of his or her usual occupation and has failed to qualify because of a service-connected disability."` [cite: 135] -> `advisor/eligible_xp_derived_spouse.md`
*   `"The veteran is disqualified due to a service-connected disability, but none of the specific situations above fully apply, or I'm unsure."` -> `advisor/derived_spouse_furtherclarification.md`

[Return to previous question](./derived_spouse_vetdisabilityreason.md)
[Return to Advisor Start](./start.md)

[end of advisor/derived_spouse_vetdisabilitydetails.md]

[start of advisor/derived_spouse_vetdisabilityreason.md]
---
layout: default
title: Derived Preference (Spouse): Reason for Veteran's Non-Qualification
---

[cite_start]Is the veteran disqualified for a Federal position along the general lines of his or her usual occupation *because of a service-connected disability*? [cite: 132]

*   `"Yes, due to a service-connected disability."` -> `advisor/derived_spouse_vetdisabilitydetails.md`
*   `"No, the reason is not a service-connected disability."` -> `advisor/ineligible_derived_spouse_vetnotdisabled.md`

[Return to previous question](./derived_spouse_vetqualifiedforemployment.md)
[Return to Advisor Start](./start.md)

[end of advisor/derived_spouse_vetdisabilityreason.md]

[start of advisor/derived_spouse_vetliving.md]
---
layout: default
title: Derived Preference (Spouse): Veteran's Status
---

Is the veteran on whose service you are basing your claim currently living?

*   `"Yes, the veteran is living."` -> `advisor/derived_spouse_vetqualifiedforemployment.md`
*   `"No, the veteran is deceased."` -> `advisor/derived_switch_todeceasedpath.md`

[Return to Relationship Choice](./derived_intro.md)
[Return to Advisor Start](./start.md)

[end of advisor/derived_spouse_vetliving.md]

[start of advisor/derived_spouse_vetqualifiedforemployment.md]
---
layout: default
title: Derived Preference (Spouse): Veteran's Employment Qualification
---

Is the living veteran qualified for Federal employment (i.e., able to work and apply for Federal jobs)?

[cite_start](A spouse generally cannot receive preference if the veteran is living and is qualified for Federal employment [cite: 131]).

*   `"Yes, the veteran is living and qualified for Federal employment."` -> `advisor/ineligible_derived_spouse_vetqualified.md`
*   `"No, the veteran is living but is NOT qualified for Federal employment."` -> `advisor/derived_spouse_vetdisabilityreason.md`

[Return to previous question](./derived_spouse_vetliving.md)
[Return to Advisor Start](./start.md)

[end of advisor/derived_spouse_vetqualifiedforemployment.md]

[start of advisor/derived_switch_todeceasedpath.md]
---
layout: default
title: Derived Preference: Clarification for Spouse of Deceased Veteran
---

You indicated you are the spouse of a veteran, but that the veteran is deceased.
* If you were married to the veteran at the time of their death and have not remarried (or that remarriage was annulled), you may be eligible as a **Widow/Widower**.
* If you are the mother of the deceased veteran's child and meet other criteria, you might explore eligibility as a **Mother**.

How would you like to proceed?

* `"Proceed as a Widow/Widower."` -> `derived_widow_divorced.md`
* `"Explore eligibility as a Mother."` -> `derived_mother_vetstatus.md` (User would then choose "Deceased")
* `"The veteran is actually living (I made a mistake)."` -> `derived_spouse_vetqualifiedforemployment.md`
* `[Return to Relationship Choice]` -> `derived_intro.md`
* `[Return to Advisor Start]` -> `start.md`

[end of advisor/derived_switch_todeceasedpath.md]

[start of advisor/derived_widow_clarify_vetservice.md]
---
layout: default
title: Derived Preference (Widow/Widower) - Clarification on Veteran's Service
---

To determine eligibility, please review the veteran's service records (such as the DD Form 214). Specifically, check if their service included:
* A declared war (e.g., World War II: December 7, 1941 - April 28, 1952).
* Service during the period April 28, 1952, through July 1, 1955.
* Service in a campaign or expedition for which a campaign medal was authorized (see OPM Vet Guide Appendix A).
* [cite_start]Also, verify if the veteran died while on active duty during such service, under conditions that would not have been the basis for other than an honorable or general discharge[cite: 140].

[cite_start]You can find details in the OPM Vet Guide under "10-Point Derived Preference (XP) - Widow/Widower"[cite: 139, 152].

* `"[Return to veteran's service condition choices]"` -> `advisor/derived_widow_vetservice_condition.md`
* `"[Return to Advisor Start]"` -> `advisor/start.md`

[end of advisor/derived_widow_clarify_vetservice.md]

[start of advisor/derived_widow_divorced.md]
---
layout: default
title: Derived Preference (Widow/Widower): Marital Status at Veteran's Death
---

[cite_start]Were you divorced from the veteran at the time of their death? [cite: 139]

*   `"Yes, I was divorced."` -> `ineligible_derived_widow_divorced.md`
*   `"No, I was not divorced."` -> `derived_widow_remarried.md`
*   `"[Return to Relationship Choice]"` -> `derived_intro.md`
*   `"[Return to Advisor Start]"` -> `start.md`

[end of advisor/derived_widow_divorced.md]

[start of advisor/derived_widow_remarried.md]
---
layout: default
title: Derived Preference (Widow/Widower): Remarriage Status
---
## Derived Preference (Widow/Widower): Remarriage Status

Have you remarried since the veteran's death? [cite_start](If you remarried but that subsequent marriage was annulled, select 'No, or my remarriage was annulled.') [cite: 139]

* [Yes, I have remarried (and the marriage was not annulled).](./ineligible_derived_widow_remarried.md)
* [No, I have not remarried OR my subsequent remarriage was annulled.](./derived_widow_vetservice_condition.md)
* [Return to previous question](./derived_widow_divorced.md)
* [Return to Advisor Start](./start.md)

[end of advisor/derived_widow_remarried.md]

[start of advisor/derived_widow_vetservice_condition.md]
---
layout: default
title: Derived Preference (Widow/Widower): Veteran's Service or Death Conditions
---
## Derived Preference (Widow/Widower): Veteran's Service or Death Conditions

Which of the following conditions applied to the veteran?

* [cite_start]"The veteran served during a declared war (e.g., World War II: Dec 7, 1941 - Apr 28, 1952), OR during the period April 28, 1952, through July 1, 1955, OR in a campaign or expedition for which a campaign medal has been authorized (see OPM Vet Guide Appendix A for a list of medals)." [cite: 139]](./eligible_xp_derived_widow.md)
* [cite_start]"The veteran died while on active duty (that included service as described in the option above) under conditions that would not have been the basis for other than an honorable or general discharge." [cite: 140]](./eligible_xp_derived_widow.md)
* [cite_start]"The veteran's service was after 1955 and was NOT in a war, campaign, or expedition for which a medal was authorized, AND they did not die on active duty during such specific service." (As per OPM Vet Guide, 'Note' following 5 U.S.C. 2108 (1) (B), (C) or (2) [cite: 152])](./ineligible_derived_widow_vetservicenotqualifying.md)
* [None of these, or I'm unsure.](./derived_widow_clarify_vetservice.md)
* [Return to previous question](./derived_widow_remarried.md)
* [Return to Advisor Start](./start.md)

[end of advisor/derived_widow_vetservice_condition.md]

[start of advisor/eligible_cp_10point.md]
---
layout: default
title: Veteran's Preference Advisor - Potential 10-Point Eligibility (CP)
---

[cite_start]Based on your responses, you appear to meet the criteria for 10-point veteran's preference (CP) due to a service-connected disability rating of at least 10 percent but less than 30 percent. This is an initial assessment and not a final determination of preference.

Key considerations for CP preference:
* [cite_start]You must have been discharged or released from active duty under honorable conditions (or expect to be if applying under the VOW Act).
* [cite_start]Applicants claiming 10-point preference must typically complete Standard Form (SF) 15, Application for 10-Point Veteran Preference, and submit required documentation (like your VA rating decision).
* [cite_start]For disabled veterans, "active duty" includes training service in the Reserves or National Guard.
* [cite_start]The 24-month minimum active duty service requirement that applies to some 5-point preference situations generally does not apply to those eligible for 10-point preference due to a separation for disability incurred or aggravated in the line of duty.

Remember to claim preference when applying for Federal jobs and be prepared to provide documentation.

Choices:
* "Learn more about applying with 10-point preference (SF-15)" (Link to OPM guidance on SF-15 or a future detailed info page)
* "[Return to Advisor Start](./start.md)"
```

[end of advisor/eligible_cp_10point.md]

[start of advisor/eligible_cps_10point.md]
---
layout: default
title: Veteran's Preference Advisor - Potential 10-Point Eligibility (CPS)
---

[cite_start]Based on your responses, you appear to meet the criteria for 10-point veteran's preference (CPS) due to a service-connected disability rating of 30 percent or more. This is an initial assessment and not a final determination of preference.

Key considerations for CPS preference:
* [cite_start]You must have been discharged or released from active duty under honorable conditions (or expect to be if applying under the VOW Act).
* [cite_start]Applicants claiming 10-point preference must typically complete Standard Form (SF) 15, Application for 10-Point Veteran Preference, and submit required documentation (like your VA rating decision).
* [cite_start]For disabled veterans, "active duty" includes training service in the Reserves or National Guard.
* [cite_start]The 24-month minimum active duty service requirement that applies to some 5-point preference situations generally does not apply to those eligible for 10-point preference due to a separation for disability incurred or aggravated in the line of duty.

Remember to claim preference when applying for Federal jobs and be prepared to provide documentation.

Choices:
* "Learn more about applying with 10-point preference (SF-15)" (Link to OPM guidance on SF-15 or a future detailed info page)
* "[Return to Advisor Start](./start.md)"
```

[end of advisor/eligible_cps_10point.md]

[start of advisor/eligible_tp_5point.md]
---
title: "Veteran's Preference Advisor - Potential 5-Point Eligibility (TP)"
layout: default
---

Based on your responses, you appear to meet the criteria for 5-point veteran's preference (TP), provided your discharge was (or will be, if VOW Act applies) under honorable conditions and all other general eligibility requirements are met. This is an initial assessment and not a final determination of preference. Remember to claim preference when applying for Federal jobs and be prepared to provide necessary documentation (like your DD Form 214 or VOW Act certification).

Choices:
*   [Learn more about what to do next](./#) <!-- Placeholder link -->
*   [Return to Advisor Start](./start.md)
```

[end of advisor/eligible_tp_5point.md]

[start of advisor/eligible_xp_10point.md]
---
layout: default
title: Veteran's Preference Advisor - Potential 10-Point Eligibility (XP)
---

[cite_start]Based on your responses, you appear to meet the criteria for 10-point veteran's preference (XP). This is an initial assessment and not a final determination of preference.

Key considerations for XP preference:
* [cite_start]It can be based on receiving a Purple Heart OR having a service-connected disability (or receiving compensation/pension for it) that doesn't fall into the specific CP (10-20%) or CPS (30%+) categories.
* [cite_start]You must have been discharged or released from active duty under honorable conditions (or expect to be if applying under the VOW Act).
* [cite_start]Applicants claiming 10-point preference must typically complete Standard Form (SF) 15, Application for 10-Point Veteran Preference, and submit required documentation.
* [cite_start]For disabled veterans, "active duty" includes training service in the Reserves or National Guard.
* [cite_start]The 24-month minimum active duty service requirement that applies to some 5-point preference situations generally does not apply to those eligible for 10-point preference due to a separation for disability incurred or aggravated in the line of duty.

Remember to claim preference when applying for Federal jobs and be prepared to provide documentation.

Choices:
* "Learn more about applying with 10-point preference (SF-15)" (Link to OPM guidance on SF-15 or a future detailed info page)
* "[Return to Advisor Start](./start.md)"
```

[end of advisor/eligible_xp_10point.md]

[start of advisor/eligible_xp_derived_mother.md]
---
layout: default
title: Veteran's Preference Advisor - Potential 10-Point Derived Preference (XP) - Mother
---

Based on your responses, you appear to meet the criteria for 10-point derived veteran's preference (XP) as the mother of a qualifying veteran (either deceased under specific conditions or living and permanently and totally disabled from a service-connected cause).

This is an initial assessment and not a final determination of preference. Remember to:
* Claim preference when applying for Federal jobs.
* Complete the Standard Form (SF) 15, Application for 10-Point Veteran Preference.
* Be prepared to provide necessary documentation (e.g., veteran's birth certificate listing you as mother, proof of your marriage to veteran's father, veteran's proof of service/disability/death as applicable, documentation for your current marital/living status).

* `"Learn more about applying with 10-point preference (SF-15)"` (Link to OPM guidance on SF-15 or a future detailed info page)
* `[Return to Advisor Start]` -> `start.md`

[end of advisor/eligible_xp_derived_mother.md]

[start of advisor/eligible_xp_derived_spouse.md]
---
layout: default
title: Veteran's Preference Advisor - Potential 10-Point Derived Preference (XP) - Spouse
---

[cite_start]Based on your responses, you appear to meet the criteria for 10-point derived veteran's preference (XP) as the spouse of a veteran who is disqualified for a Federal position along the general lines of his or her usual occupation because of a service-connected disability[cite: 132, 133, 134, 135].

This is an initial assessment and not a final determination of preference. Remember to:
* Claim preference when applying for Federal jobs.
* Complete the Standard Form (SF) 15, Application for 10-Point Veteran Preference.
* Be prepared to provide necessary documentation (e.g., marriage certificate, veteran's proof of service-connected disability and unemployability/disqualification for usual occupation).

* `"Learn more about applying with 10-point preference (SF-15)"` (Link to OPM guidance on SF-15 or a future detailed info page)
* `[Return to Advisor Start]` -> `start.md`

[end of advisor/eligible_xp_derived_spouse.md]

[start of advisor/eligible_xp_derived_spouse_conditional.md]
---
layout: default
title: Veteran's Preference Advisor - Potential Conditional 10-Point Derived Preference (XP) - Spouse
---

Based on your responses, you *may* meet the criteria for 10-point derived veteran's preference (XP) as the spouse of a veteran disqualified for their usual occupation due to a service-connected disability.

[cite_start]However, because your situation does not fall under the standard presumptions for disqualification, your claim will require a more careful analysis by the hiring agency, and possibly OPM[cite: 136].

Key reminders:
*   Complete the SF-15, Application for 10-Point Veteran Preference.
*   Be prepared to provide comprehensive documentation supporting the veteran's service-connected disability and their disqualification from employment in their usual occupation.

This is an initial assessment and not a final determination of preference.

*   `"Learn more about applying with 10-point preference (SF-15)"` #(Link to OPM guidance on SF-15 or a future detailed info page)
*   `"[Return to Advisor Start]"` -> `start.md`

[end of advisor/eligible_xp_derived_spouse_conditional.md]

[start of advisor/eligible_xp_derived_widow.md]
---
layout: default
title: Veteran's Preference Advisor - Potential 10-Point Derived Preference (XP) - Widow/Widower
---

[cite_start]Based on your responses, you appear to meet the criteria for 10-point derived veteran's preference (XP) as the widow/widower of a qualifying veteran[cite: 139, 140].

This is an initial assessment and not a final determination of preference. Remember to:
* Claim preference when applying for Federal jobs.
* Complete the Standard Form (SF) 15, Application for 10-Point Veteran Preference.
* Be prepared to provide necessary documentation (e.g., marriage certificate, veteran's death certificate, veteran's proof of qualifying service).

* `"Learn more about applying with 10-point preference (SF-15)"` (Link to OPM guidance on SF-15 or a future detailed info page)
* `[Return to Advisor Start]` -> `start.md`

[end of advisor/eligible_xp_derived_widow.md]

[start of advisor/ineligible_derived_mother_currentmarital.md]
---
layout: default
title: Mother's Preference: Potentially Ineligible - Current Marital/Living Status
---

To be eligible for derived preference as a mother, your current marital and living situation must meet specific criteria. These include:
* [cite_start]Living with your husband (veteran's father or remarried husband) who is totally and permanently disabled[cite: 143, 148], OR
* [cite_start]Being widowed, divorced, or legally separated (from veteran's father or subsequent husband) and not having remarried since that event[cite: 144, 145, 149, 150].

Based on your response (currently married and husband is not P&T disabled), you may not meet these conditions.

* `[Return to check current marital/living status]` -> `derived_mother_common_currentmarital.md`
* `[Return to Relationship Choice]` -> `derived_intro.md`
* `[Return to Advisor Start]` -> `start.md`

[end of advisor/ineligible_derived_mother_currentmarital.md]

[start of advisor/ineligible_derived_mother_deceased_vetdeathcond.md]
---
layout: default
title: Mother's Preference - Potentially Ineligible - Deceased Veteran's Service/Death Conditions
---

[cite_start]For a mother to claim preference for a deceased veteran, the veteran generally must have died under honorable conditions while on active duty during a declared war, specific post-war periods (April 28, 1952 - July 1, 1955), or in a campaign or expedition for which a campaign medal was authorized[cite: 141]. [cite_start]Preference is also generally not granted if the deceased veteran's own preference eligibility was based *only* on other criteria (e.g., service after 1955 not in a war/campaign)[cite: 152]. Based on your responses, these conditions may not be met.

*   `"[Return to check veteran's death/service conditions]"` -> `derived_mother_deceased_vetdeathcond.md`
*   `"[Return to Relationship Choice]"` -> `derived_intro.md`
*   `"[Return to Advisor Start]"` -> `start.md`

[end of advisor/ineligible_derived_mother_deceased_vetdeathcond.md]

[start of advisor/ineligible_derived_mother_living_vetseparation.md]
---
layout: default
title: Mother's Preference - Potentially Ineligible - Living Veteran's Separation
---

[cite_start]For a mother to claim preference for a living, permanently and totally disabled veteran, the veteran must have been separated from active duty (including training service) with an honorable or general discharge[cite: 146]. Based on your response, this condition may not be met.

*   `"[Return to check veteran's separation]"` -> `derived_mother_living_vetseparation.md`
*   `"[Return to Relationship Choice]"` -> `derived_intro.md`
*   `"[Return to Advisor Start]"` -> `start.md`

[end of advisor/ineligible_derived_mother_living_vetseparation.md]

[start of advisor/ineligible_derived_mother_notmarriedtofather.md]
---
layout: default
title: Mother's Preference - Potentially Ineligible - Marriage to Veteran's Father
---

[cite_start]To be eligible for derived preference as a mother, you must be (or have been) married to the father of the veteran[cite: 142, 147]. Based on your response, this condition may not be met.

*   `"[Return to check marriage to veteran's father]"` -> `derived_mother_common_fatherinfo.md`
*   `"[Return to Relationship Choice]"` -> `derived_intro.md`
*   `"[Return to Advisor Start]"` -> `start.md`

[end of advisor/ineligible_derived_mother_notmarriedtofather.md]

[start of advisor/ineligible_derived_mother_vetstatus.md]
---
layout: default
title: Mother's Preference - Potentially Ineligible - Veteran's Status
---

To be eligible for derived preference as a mother, the veteran (your son or daughter) must generally be either:
1. [cite_start]Deceased under specific conditions related to their active duty service (during a war, specific period, or campaign)[cite: 141], OR
2. [cite_start]Living and permanently and totally disabled from a service-connected injury or illness, and honorably separated[cite: 146].

Based on your response, the veteran's status may not meet these requirements.

*   `"[Return to check veteran's status]"` -> `derived_mother_vetstatus.md`
*   `"[Return to Relationship Choice]"` -> `derived_intro.md`
*   `"[Return to Advisor Start]"` -> `start.md`

[end of advisor/ineligible_derived_mother_vetstatus.md]

[start of advisor/ineligible_derived_spouse_vetnotdisabled.md]
---
layout: default
title: Derived Preference (Spouse): Potentially Ineligible - Disqualification Not Due to Service-Connected Disability
---

[cite_start]For a spouse to claim derived preference for a living veteran, the veteran must be disqualified for a Federal position along the general lines of his or her usual occupation *because of a service-connected disability*[cite: 132]. Based on your response that the disqualification is not due to a service-connected disability, you may not be eligible for derived preference.

*   `[Return to check reason for non-qualification]` -> `derived_spouse_vetdisabilityreason.md`
*   `[Return to Relationship Choice]` -> `derived_intro.md`
*   `[Return to Advisor Start]` -> `start.md`

[end of advisor/ineligible_derived_spouse_vetnotdisabled.md]

[start of advisor/ineligible_derived_spouse_vetqualified.md]
---
layout: default
title: Derived Preference (Spouse): Potentially Ineligible - Veteran Qualified
---

[cite_start]Generally, a spouse cannot receive derived preference if the veteran is living and qualified for Federal employment[cite: 131]. Based on your response, you may not be eligible for derived preference as a spouse under this condition.

*   `[Return to check veteran's employment qualification]` -> `derived_spouse_vetqualifiedforemployment.md`
*   `[Return to Relationship Choice]` -> `derived_intro.md`
*   `[Return to Advisor Start]` -> `start.md`

[end of advisor/ineligible_derived_spouse_vetqualified.md]

[start of advisor/ineligible_derived_widow_divorced.md]
---
layout: default
title: Derived Preference (Widow/Widower): Potentially Ineligible - Divorced
---
## Derived Preference (Widow/Widower): Potentially Ineligible - Divorced

[cite_start]To be eligible for derived preference as a widow or widower, you must not have been divorced from the veteran at the time of their death[cite: 139]. Based on your response, you may not be eligible.

* [Return to check marital status at death](./derived_widow_divorced.md)
* [Return to Relationship Choice](./derived_intro.md)
* [Return to Advisor Start](./start.md)

[end of advisor/ineligible_derived_widow_divorced.md]

[start of advisor/ineligible_derived_widow_remarried.md]
---
layout: default
title: Derived Preference (Widow/Widower): Potentially Ineligible - Remarried
---
## Derived Preference (Widow/Widower): Potentially Ineligible - Remarried

[cite_start]To be eligible for derived preference as a widow or widower, you must not have remarried since the veteran's death, or if you remarried, that subsequent marriage must have been annulled[cite: 139]. Based on your response, you may not be eligible.

* [Return to check remarriage status](./derived_widow_remarried.md)
* [Return to Relationship Choice](./derived_intro.md)
* [Return to Advisor Start](./start.md)

[end of advisor/ineligible_derived_widow_remarried.md]

[start of advisor/ineligible_derived_widow_vetservicenotqualifying.md]
---
layout: default
title: Derived Preference (Widow/Widower): Potentially Ineligible - Veteran's Service
---
## Derived Preference (Widow/Widower): Potentially Ineligible - Veteran's Service

For derived preference as a widow/widower, the veteran's service generally must have been during a declared war, specific post-war periods (April 28, 1952 - July 1, 1955), or in a campaign or expedition for which a medal was authorized; [cite_start]OR the veteran must have died on active duty during such qualifying service[cite: 139, 140].

[cite_start]Preference is generally not granted to widows or mothers if the deceased veteran's own preference eligibility was based *only* on other criteria (e.g., service after 1955 that was not in a war or campaign, such as >180 days of active duty or Gulf War service without a specific campaign medal)[cite: 152]. Based on your response, the veteran's service may not qualify for this type of derived preference.

* [Return to check veteran's service conditions](./derived_widow_vetservice_condition.md)
* [Return to Relationship Choice](./derived_intro.md)
* [Return to Advisor Start](./start.md)

[end of advisor/ineligible_derived_widow_vetservicenotqualifying.md]

[start of advisor/ineligible_discharge_type.md]
---
layout: default
title: "Own Service: Ineligible - Discharge Not Under Honorable Conditions"
---

Veteran's preference requires a discharge or release under honorable conditions (i.e., an Honorable or General discharge). (OPM Vet Guide, 'Types of Preference'). If your discharge was of a different character, you may not be eligible.

*   [Return to Advisor Start](./start.md)

[end of advisor/ineligible_discharge_type.md]

[start of advisor/ineligible_general.md]
---
layout: default
title: Veteran's Preference Advisor - Initial Ineligibility
---

Based on your initial selection, it appears you may not be directly pursuing veteran's preference based on your own service or as a qualifying relative (spouse, widow(er), mother) of a veteran. This advisor focuses on those categories. Veteran's preference is a specific entitlement for those who served in the Armed Forces during certain periods or campaigns, or have service-connected disabilities, and for certain family members (see OPM Vet Guide, 'Why Preference is Given').

*   [Return to Advisor Start](./start.md)

[end of advisor/ineligible_general.md]

[start of advisor/ineligible_ownservice_noqualifyingperiod.md]
---
title: "Veteran's Preference Advisor - Potentially Ineligible for 5-Point Preference (No Qualifying Period Indicated)"
layout: default
---

Based on your responses, it appears your service does not fall into the specified periods or involve a qualifying campaign medal for 5-point preference (TP) as a veteran who, in this path, has not indicated a service-connected disability or sole survivorship discharge. (See OPM Vet Guide, '5-Point Preference (TP)'). If you made an error or wish to explore other preference types (like based on disability), please return to the relevant section.

Choices:
*   [I want to re-check for disability preference (10-point) or sole survivorship.](./ownservice_checkdisability_intro.md)
*   [Review service period choices again.](./ownservice_nodisability_nossps_checkserviceperiod.md)
*   [Return to Advisor Start](./start.md)
```

[end of advisor/ineligible_ownservice_noqualifyingperiod.md]

[start of advisor/ineligible_ownservice_status.md]
---
layout: default
title: Ineligible Based on Current Service Status
---

Based on your responses, you do not currently meet the preliminary requirements for veteran's preference. Generally, you must be discharged or released from active duty under honorable conditions to be eligible. If you are still on active duty, you may be eligible under the VOW Act if you are within 120 days of discharge and can provide a certification. <!-- TODO: Add link to VOW Act info or back to VOW questions if applicable --> For more information, please review the OPM Vet Guide [Appendix A - Definitions of Terms and Categories, Page 31].

*   [I made a mistake in my previous answers, take me back.](./ownservice_intro.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ineligible_ownservice_status.md]

[start of advisor/ineligible_retiredmajor_notdisabled.md]
---
layout: default
title: "Own Service: Ineligible - Retired Officer Not Disabled"
---

Military retirees at the rank of Major, Lieutenant Commander, or higher are not eligible for preference in appointment unless they are disabled veterans. (OPM Vet Guide, 'Types of Preference'). Based on your responses, you may not be eligible for veteran's preference under this condition.

*   [Return to Advisor Start](./start.md)

[end of advisor/ineligible_retiredmajor_notdisabled.md]

[start of advisor/ineligible_ssp_dischargedate.md]
---
layout: default
title: Sole Survivor Preference: Potentially Ineligible - Discharge Date Not Met
---

[cite_start]To be eligible for 0-point Sole Survivor Preference (SSP) under the Hubbard Act, your release or discharge from active duty must have occurred *after August 29, 2008*. [cite_end]

Based on your response, your discharge date does not meet this requirement for SSP. You may still be eligible for other types of veteran's preference based on your service.

Choices:
* "[Re-check discharge date information]" -> advisor/ownservice_ssp_dischargedate.md
* "[Explore other preference types (e.g., 5-point, disability)]" -> advisor/ownservice_checkdisability_intro.md
* "[Return to Advisor Start]" -> advisor/start.md

[end of advisor/ineligible_ssp_dischargedate.md]

[start of advisor/ineligible_ssp_reason.md]
---
layout: default
title: Sole Survivor Preference: Potentially Ineligible - Reason for Discharge Not Met
---

[cite_start]Eligibility for 0-point Sole Survivor Preference (SSP) requires that the specific reason for your discharge (after August 29, 2008) was a 'sole survivorship discharge'.[cite_end]

If your discharge was for other reasons, you would not qualify for SSP. However, you might be eligible for other types of veteran's preference (e.g., 5-point preference based on service period or campaign medal, or 10-point preference if disabled).

Choices:
* "[Re-check reason for discharge information]" -> advisor/ownservice_ssp_discharge_reason.md
* "[Explore other preference types (e.g., 5-point, disability)]" -> advisor/ownservice_checkdisability_intro.md
* "[Return to Advisor Start]" -> advisor/start.md
---

[end of advisor/ineligible_ssp_reason.md]

[start of advisor/ineligible_tp_minduration.md]
---
title: "Veteran's Preference Advisor - Ineligible for 5-Point Preference (Minimum Service Not Met)"
layout: default
---

To qualify for 5-point preference based on your service period and original enlistment/active duty start date (after Sep 7, 1980/Oct 14, 1982), you generally must have served continuously for 24 months OR the full period for which you were called or ordered to active duty, unless specific exceptions apply (like a separation for service-connected disability qualifying for 10-point preference, or a hardship separation). (OPM Vet Guide, '5-Point Preference (TP)'). Based on your responses, it appears you may not meet this minimum service requirement for 5-point preference under this specific service path.

Choices:
*   [Review service duration or exception choices.](./ownservice_tp_24month_duration.md)
*   [Review service period choices again.](./ownservice_nodisability_nossps_checkserviceperiod.md)
*   [Return to Advisor Start](./start.md)
```

[end of advisor/ineligible_tp_minduration.md]

[start of advisor/ineligible_vow_discharge_type.md]
---
layout: default
title: "Own Service (VOW Act): Ineligible - Discharge Not Expected to be Honorable"
---

Veteran's preference requires eventual discharge or release under honorable conditions. If your VOW Act certification does not indicate an expected honorable discharge, you may not proceed with a claim for preference at this time under the VOW Act. (See OPM Vet Guide, 'A word about the VOW Act').

*   [Return to Advisor Start](./start.md)

[end of advisor/ineligible_vow_discharge_type.md]

[start of advisor/ineligible_vow_retiredmajor_notdisabled.md]
---
layout: default
title: "Own Service (VOW Act): Ineligible - Retired Officer Not Disabled"
---

Military retirees at the rank of Major, Lieutenant Commander, or higher are not eligible for preference unless they are disabled veterans. (OPM Vet Guide, 'Types of Preference'). Based on your responses, you may not be eligible for veteran's preference if you retire at this rank without a disability.

*   [Return to Advisor Start](./start.md)

[end of advisor/ineligible_vow_retiredmajor_notdisabled.md]

[start of advisor/ownservice_checkdisability_intro.md]
---
layout: default
title: Veteran's Preference Advisor - Check for Service-Connected Disability or Purple Heart
---

Next, we'll check if you might be eligible for 10-point preference. Do you have a service-connected disability recognized by the Department of Veterans Affairs (VA) or your branch of service, OR have you received a Purple Heart? (See OPM Vet Guide, '10-Point Disability Preference (XP)' for Purple Heart).

* [Yes, I have a service-connected disability OR I received a Purple Heart.](./ownservice_disability_details.md)
* [No.](./ownservice_discharged_checkfirst_solesurvivor.md)
* [Return to Advisor Start](./start.md)

[end of advisor/ownservice_checkdisability_intro.md]

[start of advisor/ownservice_cp_details.md]
---
layout: default
title: Own Service: 10-Point Preference (CP) - 10-20% Disability
---

You indicated a service-connected disability rating of 10% or 20%. [cite_start]This generally qualifies you for 10-point Veteran's Preference (CP), provided your discharge was (or will be, if VOW Act applies) under honorable conditions and all other general eligibility requirements are met. [cite_start]For disabled veterans, active duty includes training service in the Reserves or National Guard. [cite_start]Remember to complete the SF-15 form.

*   [Confirm, proceed to eligibility summary.](./eligible_cp_10point.md)
*   [I made a mistake, review disability/Purple Heart options.](./ownservice_disability_details.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_cp_details.md]

[start of advisor/ownservice_cps_details.md]
---
layout: default
title: Own Service: 10-Point Preference (CPS) - 30%+ Disability
---

You indicated a service-connected disability rating of 30% or more. [cite_start]This generally qualifies you for 10-point Veteran's Preference (CPS), provided your discharge was (or will be, if VOW Act applies) under honorable conditions and all other general eligibility requirements are met. [cite_start]For disabled veterans, active duty includes training service in the Reserves or National Guard. [cite_start]Remember to complete the SF-15 form.

*   [Confirm, proceed to eligibility summary.](./eligible_cps_10point.md)
*   [I made a mistake, review disability/Purple Heart options.](./ownservice_disability_details.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_cps_details.md]

[start of advisor/ownservice_disability_clarify_sf15.md]
---
layout: default
title: Own Service: Disability Preference - Clarification Needed
---

Understanding your specific disability rating and type is important for determining 10-point preference. Please review your documentation from the Department of Veterans Affairs (VA) or your branch of service. [cite_start]The Standard Form 15 (SF-15), 'Application for 10-Point Veteran Preference,' also provides details on required documentation. Once you have more information, you can select the appropriate option from the previous page.

*   [Return to disability/Purple Heart options.](./ownservice_disability_details.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_disability_clarify_sf15.md]

[start of advisor/ownservice_disability_details.md]
---
layout: default
title: Own Service: Disability or Purple Heart Details
---

You indicated you have a service-connected disability or received a Purple Heart. To determine the type of 10-point preference, please select the option that best describes your situation. [cite_start](Remember, if you are claiming 10-point preference, you will typically need to complete an SF-15 form and provide supporting documentation. )

*   ["I received a Purple Heart."](./ownservice_xp_purpleheart.md)
*   ["I have a service-connected disability rating of 30% or more from the VA or my branch of service."](./ownservice_cps_details.md)
*   ["I have a service-connected disability rating of 10% or 20% from the VA or my branch of service."](./ownservice_cp_details.md)
*   ["I have a service-connected disability (rated less than 10% or not yet rated but recognized) OR I am receiving compensation, disability retirement benefits, or pension from the military or VA due to a service-connected disability, but I don't fit the 10-30%+ categories above."](./ownservice_xp_generaldisability_details.md)
*   ["I'm not sure about the percentage or type."](./ownservice_disability_clarify_sf15.md)
*   "[Return to Advisor Start](./start.md)"

[end of advisor/ownservice_disability_details.md]

[start of advisor/ownservice_discharged_checkdd214_discharge.md]
---
layout: default
title: "Own Service: Discharged - Check DD Form 214 for Discharge"
---

Your DD Form 214 (Certificate of Release or Discharge from Active Duty) will state the character of your service. Please review this document. Once you have this information, you can restart or continue.

*   [I have checked, and it was Honorable or General.](./ownservice_checkdisability_intro.md)
*   [I have checked, and it was other than Honorable/General.](./ineligible_discharge_type.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_discharged_checkdd214_discharge.md]

[start of advisor/ownservice_discharged_checkfirst_solesurvivor.md]
---
layout: default
title: "Own Service: Check for Sole Survivorship Preference"
---

You've indicated no current claim to disability/Purple Heart preference. Now we need to determine other types of preference you might be eligible for. Were you released or discharged from active duty after August 29, 2008, by reason of a 'sole survivorship discharge'? (See OPM Vet Guide, '0-point Preference (SSP)').

* [Yes, I believe I had a sole survivorship discharge.](./ownservice_ssp_eligible.md)
* [No, or I'm not sure.](./ownservice_nodisability_nossps_checkserviceperiod.md)
* [Return to Advisor Start](./start.md)

[end of advisor/ownservice_discharged_checkfirst_solesurvivor.md]

[start of advisor/ownservice_discharged_checkretired.md]
---
layout: default
title: "Own Service: Discharged - Check Retiree Status"
---

Are you a military retiree at the rank of Major, Lieutenant Commander, or higher? (This generally does not apply to Reservists who will not begin drawing military retired pay until age 60. See OPM Vet Guide, 'Types of Preference' and Appendix C for rank equivalents).

*   [Yes, I am a retiree at Major/Lt. Commander or higher.](./ownservice_discharged_retiredmajor_isdisabled.md)
*   [No, I am not a retiree at that rank, OR I am a Reservist not yet drawing retired pay until age 60.](./ownservice_discharged_honorableconditions.md)

[Return to Advisor Start](./start.md)

[end of advisor/ownservice_discharged_checkretired.md]

[start of advisor/ownservice_discharged_honorableconditions.md]
---
layout: default
title: "Own Service: Discharged - Character of Service"
---

To receive preference, a veteran must have been discharged or released from active duty in the Armed Forces under honorable conditions. This typically means an Honorable or General discharge. (OPM Vet Guide, 'Types of Preference'). What was the character of your discharge?

*   [Honorable or General Discharge.](./ownservice_checkdisability_intro.md)
*   [Other than Honorable/General (e.g., Undesirable, Bad Conduct, Dishonorable).](./ineligible_discharge_type.md)
*   [I'm not sure / Need to check my DD Form 214.](./ownservice_discharged_checkdd214_discharge.md)

[Return to Advisor Start](./start.md)

[end of advisor/ownservice_discharged_honorableconditions.md]

[start of advisor/ownservice_discharged_retiredmajor_isdisabled.md]
---
layout: default
title: "Own Service: Retired Major/Lt. Cmdr+ - Check Disability"
---

Military retirees at the rank of Major, Lieutenant Commander, or higher are generally not eligible for preference in appointment unless they are disabled veterans. (OPM Vet Guide, 'Types of Preference'). Do you have a service-connected disability recognized by the Department of Veterans Affairs (VA) or your branch of service?

*   [Yes, I am a disabled veteran.](./ownservice_discharged_honorableconditions.md)
*   [No, I am not a disabled veteran.](./ineligible_retiredmajor_notdisabled.md)

[Return to Advisor Start](./start.md)

[end of advisor/ownservice_discharged_retiredmajor_isdisabled.md]

[start of advisor/ownservice_intro.md]
---
layout: default
title: Veteran's Preference Advisor - Based on Your Own Service
---

You indicated you are seeking preference based on your own service in the U.S. Armed Forces. To proceed, please select your current status:

*   [I have been discharged or released from active duty in the Armed Forces.](./ownservice_discharged_checkretired.md)
*   [I am currently an active duty service member and expect to be discharged or released from active duty service under honorable conditions within 120 days (and I have or can obtain a certification as described in the VOW Act).](./ownservice_vow_checkretired.md)
*   [None of the above apply to me.](./ineligible_ownservice_status.md)

[Return to Advisor Start](./start.md)

[end of advisor/ownservice_intro.md]

[start of advisor/ownservice_nodisability_nossps_checkserviceperiod.md]
---
layout: default
title: "Own Service: Check Service Periods for 5-Point Preference (TP)"
---

Since you haven't indicated eligibility for disability or sole survivorship preference at this stage, let's check if your service meets criteria for 5-point preference (TP). Did your active service (not solely for training, if you are non-disabled) include any of the following periods or events? (Select all that apply, or the one that best fits. We will address the 24-month service requirement later if applicable. See OPM Vet Guide, '5-Point Preference (TP)' for details on qualifying periods.)

*   [Service during a declared war (specifically World War II: December 7, 1941 - April 28, 1952).](./ownservice_tp_wartime_wwii.md)
*   [Service during the period April 28, 1952, through July 1, 1955.](./ownservice_tp_period_1952_1955.md)
*   [Service for more than 180 consecutive days (other than for training), any part of which occurred after January 31, 1955, and before October 15, 1976.](./ownservice_tp_period_1955_1976.md)
*   [Service during the Gulf War from August 2, 1990, through January 2, 1992.](./ownservice_tp_period_gulfwar1.md)
*   [Service for more than 180 consecutive days (other than for training), any part of which occurred during the period beginning September 11, 2001, and ending on August 31, 2010 (the last day of Operation Iraqi Freedom).](./ownservice_tp_period_post911_oif.md)
*   [Service in a campaign or expedition for which a campaign medal has been authorized (e.g., Armed Forces Expeditionary Medal).](./ownservice_tp_campaignmedal.md) (Refer to OPM Vet Guide Appendix A for a list)
*   [None of the above service periods or medals apply to me.](./ineligible_ownservice_noqualifyingperiod.md)

[Return to Advisor Start](./start.md)

[end of advisor/ownservice_nodisability_nossps_checkserviceperiod.md]

[start of advisor/ownservice_ssp_checkdd214_date.md]
---
layout: default
title: Sole Survivor Preference: Check DD Form 214 for Discharge Date
---

Your DD Form 214 (Certificate of Release or Discharge from Active Duty) will state your date of discharge for the relevant period of service. Please review this document to confirm if your discharge occurred *after August 29, 2008*.

Once you have this information, please select an option:

Choices:
* "My discharge was after August 29, 2008." -> advisor/ownservice_ssp_discharge_reason.md
* "My discharge was on or before August 29, 2008." -> advisor/ineligible_ssp_dischargedate.md
* "[Return to Advisor Start]" -> advisor/start.md
---

[end of advisor/ownservice_ssp_checkdd214_date.md]

[start of advisor/ownservice_ssp_checkdd214_reason.md]
---
layout: default
title: Sole Survivor Preference: Check DD Form 214 for Discharge Reason
---

Your DD Form 214 (Certificate of Release or Discharge from Active Duty) or other official separation documents should state the specific reason or authority for your discharge. Please review these documents to confirm if the reason was explicitly a 'sole survivorship discharge'.

Once you have this information, please select an option:

Choices:
* "Yes, the reason documented was 'sole survivorship discharge'." -> advisor/ownservice_ssp_familycriteria_info.md
* "No, the reason documented was different or unclear regarding sole survivorship." -> advisor/ineligible_ssp_reason.md
* "[Return to Advisor Start]" -> advisor/start.md
---

[end of advisor/ownservice_ssp_checkdd214_reason.md]

[start of advisor/ownservice_tp_24month_duration.md]
---
layout: default
title: "Own Service: 5-Point Preference - Minimum Service Duration Fulfilled"
---

You indicated your relevant original enlistment or start of active duty was after September 7, 1980, or on/after October 14, 1982, respectively. Did you complete at least 24 months of continuous active duty, OR the full period for which you were called or ordered to active duty (if less than 24 months)? (OPM Vet Guide, '5-Point Preference (TP)')

*   [Yes, I served 24 months continuously OR the full period for which I was called/ordered.](./eligible_tp_5point.md)
*   [No, I did not complete 24 months OR the full period.](./ownservice_tp_24month_exceptions.md)
*   [I made a mistake with my enlistment date.](./ownservice_tp_24month_rule_check.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_tp_24month_duration.md]

[start of advisor/ownservice_tp_24month_exceptions.md]
---
layout: default
title: "Own Service: 5-Point Preference - Minimum Service Duration Exceptions"
---

The 24-month minimum service rule (or full period if shorter) generally applies if you originally enlisted after September 7, 1980, or began active duty on or after October 14, 1982. However, this rule does not apply if you were separated for a service-connected disability (which would typically make you eligible for 10-point preference) or for hardship (under 10 U.S.C. 1171 or 1173). (OPM Vet Guide, '5-Point Preference (TP)'). Do either of these exceptions apply to your situation for the period of service in question?

*   [Yes, I was separated due to a service-connected disability.](./ownservice_disability_details.md)
*   [Yes, I was separated for hardship under 10 U.S.C. 1171 or 1173.](./eligible_tp_5point.md)
*   [No, neither of these exceptions apply.](./ineligible_tp_minduration.md)
*   [I made a mistake with my service duration.](./ownservice_tp_24month_duration.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_tp_24month_exceptions.md]

[start of advisor/ownservice_tp_24month_rule_check.md]
---
layout: default
title: "Own Service: 5-Point Preference - Minimum Service Enlistment Date Check"
---

> For some service periods (like Gulf War, Post-9/11 OIF, or Campaign Medal service), a minimum service duration applies if you originally enlisted after September 7, 1980, OR began active duty on or after October 14, 1982. This rule generally requires 24 months of continuous active duty OR serving the full period for which you were called/ordered to active duty, unless certain exceptions apply (e.g., disability separation for 10-point preference, hardship separation; see OPM Vet Guide, '5-Point Preference (TP)').
>
> Did you originally enlist after September 7, 1980, OR first begin any period of active duty on or after October 14, 1982?

*   [Yes, my original enlistment/active duty started on or after those dates.](./ownservice_tp_24month_duration.md)
*   [No, my original enlistment/active duty for the qualifying service period started before those dates.](./eligible_tp_5point.md)
*   [I made a mistake, check other service periods.](./ownservice_nodisability_nossps_checkserviceperiod.md)
*   [Return to Advisor Start](./start.md]

[end of advisor/ownservice_tp_24month_rule_check.md]

[start of advisor/ownservice_tp_campaignmedal.md]
---
layout: default
title: "Own Service: Campaign Medal for 5-Point Preference"
---

You indicated service in a campaign or expedition for which a campaign medal has been authorized (e.g., Armed Forces Expeditionary Medal). This service can qualify for 5-point preference (TP) if other conditions, including a minimum service duration for some, are met. (Refer to OPM Vet Guide Appendix A for a list of qualifying medals/campaigns).

*   [Continue to check service duration requirements.](./ownservice_tp_24month_rule_check.md)
*   [I made a mistake, check other service periods.](./ownservice_nodisability_nossps_checkserviceperiod.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_tp_campaignmedal.md]

[start of advisor/ownservice_tp_period_1952_1955.md]
---
layout: default
title: "Own Service: Service April 1952 - July 1955 for 5-Point Preference"
---

You indicated service during the period April 28, 1952, through July 1, 1955. This service qualifies for 5-point preference (TP), provided your discharge was honorable and other general conditions are met. The 24-month minimum service rule generally does not apply to this period for establishing preference eligibility (OPM Vet Guide, '5-Point Preference (TP)').

*   [Confirm, proceed to eligibility summary.](./eligible_tp_5point.md)
*   [I made a mistake, check other service periods.](./ownservice_nodisability_nossps_checkserviceperiod.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_tp_period_1952_1955.md]

[start of advisor/ownservice_tp_period_1955_1976.md]
---
layout: default
title: "Own Service: Service 1955-1976 (>180 days) for 5-Point Preference"
---

You indicated service for more than 180 consecutive days (other than for training), with some part after January 31, 1955, and before October 15, 1976. This service generally qualifies for 5-point preference (TP). The 24-month minimum active duty service requirement typically applies only to veterans who originally enlisted after September 7, 1980, or first began active duty on or after October 14, 1982 (see 38 U.S.C. 5303A(d) and OPM Vet Guide, '5-Point Preference (TP)'). For your service in the 1955-1976 period, did your original enlistment in the Armed Forces occur after September 7, 1980, OR did you first begin any period of active duty on or after October 14, 1982?

*   [No, my original enlistment/active duty for the qualifying service started before those dates.](./eligible_tp_5point.md)
*   [Yes, my original enlistment/active duty started on or after those dates.](./ownservice_tp_24month_rule_check.md)
*   [I made a mistake, check other service periods.](./ownservice_nodisability_nossps_checkserviceperiod.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_tp_period_1955_1976.md]

[start of advisor/ownservice_tp_period_gulfwar1.md]
---
layout: default
title: "Own Service: Gulf War Service (1990-1992) for 5-Point Preference"
---

You indicated service during the Gulf War (August 2, 1990, through January 2, 1992). This service can qualify for 5-point preference (TP) if other conditions, including a minimum service duration for some, are met. (OPM Vet Guide, '5-Point Preference (TP)' and 'A word about Gulf War Preference').

*   [Continue to check service duration requirements.](./ownservice_tp_24month_rule_check.md)
*   [I made a mistake, check other service periods.](./ownservice_nodisability_nossps_checkserviceperiod.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_tp_period_gulfwar1.md]

[start of advisor/ownservice_tp_period_post911_oif.md]
---
layout: default
title: "Own Service: Post-9/11 Service / OIF (>180 days) for 5-Point Preference"
---

You indicated service for more than 180 consecutive days (other than for training), with some part occurring from September 11, 2001, through August 31, 2010 (Operation Iraqi Freedom). This service can qualify for 5-point preference (TP) if other conditions, including a minimum service duration for some, are met. (OPM Vet Guide, '5-Point Preference (TP)').

*   [Continue to check service duration requirements.](./ownservice_tp_24month_rule_check.md)
*   [I made a mistake, check other service periods.](./ownservice_nodisability_nossps_checkserviceperiod.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_tp_period_post911_oif.md]

[start of advisor/ownservice_tp_wartime_wwii.md]
---
layout: default
title: "Own Service: WWII Service for 5-Point Preference"
---

You indicated service during World War II (December 7, 1941 - April 28, 1952). This service qualifies for 5-point preference (TP), provided your discharge was honorable and other general conditions are met. The 24-month minimum service rule generally does not apply to this period for establishing preference eligibility (OPM Vet Guide, '5-Point Preference (TP)').

*   [Confirm, proceed to eligibility summary.](./eligible_tp_5point.md)
*   [I made a mistake, check other service periods.](./ownservice_nodisability_nossps_checkserviceperiod.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_tp_wartime_wwii.md]

[start of advisor/ownservice_vow_checkretired.md]
---
layout: default
title: "Own Service (VOW Act): Check Retiree Status"
---

Regarding your upcoming discharge/release: Are you a military retiree (or will you be upon discharge/release) at the rank of Major, Lieutenant Commander, or higher? (This generally does not apply to Reservists who will not begin drawing military retired pay until age 60. See OPM Vet Guide, 'Types of Preference' and Appendix C for rank equivalents.)

*   [Yes, I expect to be a retiree at Major/Lt. Commander or higher.](./ownservice_vow_retiredmajor_isdisabled.md)
*   [No, I do not expect to be a retiree at that rank, OR I am a Reservist not anticipating drawing retired pay until age 60.](./ownservice_vow_honorableconditions.md)

[Return to Advisor Start](./start.md)

[end of advisor/ownservice_vow_checkretired.md]

[start of advisor/ownservice_vow_honorableconditions.md]
---
layout: default
title: "Own Service (VOW Act): Expected Character of Service"
---

To receive preference, discharge must be under honorable conditions. Does your VOW Act certification state you are expected to be discharged/released under honorable conditions (i.e., an Honorable or General discharge)? (See OPM Vet Guide, 'A word about the VOW Act' regarding certification requirements).

*   [Yes, my certification indicates an expected Honorable or General discharge.](./ownservice_checkdisability_intro.md)
*   [No, my certification indicates otherwise, or I cannot obtain such certification.](./ineligible_vow_discharge_type.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_vow_honorableconditions.md]

[start of advisor/ownservice_vow_retiredmajor_isdisabled.md]
---
layout: default
title: "Own Service (VOW Act): Retired Major/Lt. Cmdr+ - Check Disability"
---

Military retirees at the rank of Major, Lieutenant Commander, or higher are generally not eligible for preference unless they are disabled veterans. (OPM Vet Guide, 'Types of Preference'). Do you currently have a service-connected disability, or do you anticipate being recognized as a disabled veteran upon discharge?

*   [Yes, I am (or expect to be) a disabled veteran.](./ownservice_vow_honorableconditions.md)
*   [No, I am not (and do not expect to be) a disabled veteran.](./ineligible_vow_retiredmajor_notdisabled.md)

[Return to Advisor Start](./start.md)

[end of advisor/ownservice_vow_retiredmajor_isdisabled.md]

[start of advisor/ownservice_xp_generaldisability_details.md]
---
layout: default
title: Own Service: 10-Point Preference (XP) - General Disability
---

You indicated you have a present service-connected disability OR are receiving compensation, disability retirement benefits, or pension from the military or the Department of Veterans Affairs, not specifically categorized as 10-20% (CP) or 30%+ (CPS). [cite_start]This may qualify you for 10-point Veteran's Preference (XP), provided your discharge was (or will be, if VOW Act applies) under honorable conditions and all other general eligibility requirements are met. [cite_start]For disabled veterans, active duty includes training service in the Reserves or National Guard. [cite_start]Remember to complete the SF-15 form.

*   [Confirm, proceed to eligibility summary.](./eligible_xp_10point.md)
*   [I made a mistake, review disability/Purple Heart options.](./ownservice_disability_details.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_xp_generaldisability_details.md]

[start of advisor/ownservice_xp_purpleheart.md]
---
layout: default
title: Own Service: 10-Point Preference (XP) - Purple Heart
---

You indicated you received a Purple Heart. [cite_start]Receipt of a Purple Heart qualifies you for 10-point Veteran's Preference (XP), provided your discharge was (or will be, if VOW Act applies) under honorable conditions and all other general eligibility requirements are met. [cite_start]For disabled veterans, active duty includes training service in the Reserves or National Guard.

*   [Confirm, proceed to eligibility summary.](./eligible_xp_10point.md)
*   [I made a mistake, review disability/Purple Heart options.](./ownservice_disability_details.md)
*   [Return to Advisor Start](./start.md)

[end of advisor/ownservice_xp_purpleheart.md]

[start of advisor/start.md]
---
layout: default
title: Veteran's Preference Advisor - Start
---

This tool is designed to help you understand potential eligibility for U.S. Federal employment veterans' preference. Please select the primary basis on which you are seeking to determine potential eligibility: (Note: 'Armed Forces' generally means Army, Navy, Air Force, Marine Corps, and Coast Guard as defined in 5 U.S.C. 2101(2). Specific conditions apply for other uniformed services like NOAA and Public Health Service; see OPM Vet Guide Appendix B for details.)

*   [My own service in the U.S. Armed Forces](./ownservice_intro.md)
*   [The service of a qualifying veteran, if I am a spouse, widow(er), or mother](./derived_intro.md)
*   [Neither of the above](./ineligible_general.md)

[Return to Advisor Start](./start.md)

[end of advisor/start.md]
"""
    # Split the raw string into individual file contents
    # Each file starts with "[start of advisor/filename.md]" and ends with "[end of advisor/filename.md]"
    file_blocks = re.split(r'\[end of advisor/[^\]]+\]', file_contents_raw)

    file_data = {}
    for block in file_blocks:
        if not block.strip():
            continue
        match = re.search(r'\[start of (advisor/[^\]]+)\]\n(.*)', block, re.DOTALL)
        if match:
            filepath = match.group(1)
            content = match.group(2)
            # remove "advisor/" prefix from filepath for consistency with markdown_files_in_advisor
            filename = filepath.split("advisor/")[1]
            file_data[filename] = content

    for filename in markdown_files_in_advisor:
        if filename in file_data:
            content = file_data[filename]
            # Pass the full path for context if needed, but parse_links uses os.path.basename
            full_path = os.path.join(advisor_dir, filename)
            links = parse_links(full_path, content, markdown_files_in_advisor)
            all_relationships.extend(links)
        else:
            # This case should ideally not happen if file_contents_raw is complete
            print(f"Warning: Content for {filename} not found in the provided raw string.")


    mermaid_definition = build_mermaid_string(all_relationships)

    output_content = f"""---
layout: default
title: Advisor Logic Diagram
---

# Advisor Logic Diagram

This diagram shows the flow of the Veteran's Preference Advisor.

```mermaid
{mermaid_definition}
```
"""
    print(output_content)

if __name__ == "__main__":
    main()
