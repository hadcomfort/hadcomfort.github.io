The AI agent will need access to:
1.  Your **"Updated Veteran's Preference Advisor: Site Development Plan (Phase 1 Focus)"** (the document you just provided).
2.  The actual Markdown files in the `/advisor/` directory as they are developed.
3.  The `hrdocs.txt` (OPM Vet Guide) for citation verification.

Here's the QA plan:

---

## Veteran's Preference Advisor: Phase 1 Development - Quality Assurance Plan

**Overall Goal:** To verify that all components outlined in the "Updated Veteran's Preference Advisor: Site Development Plan (Phase 1 Focus)" have been implemented accurately and completely.

**General Instructions for AI Agent:**
* For each QA phase and task, review the specified Markdown files against the requirements detailed in the "Updated Veteran's Preference Advisor: Site Development Plan (Phase 1 Focus)" (referred to as "the Plan Document" below).
* Note any discrepancies, errors, or omissions for correction.
* Pull requests should be specific to the items verified in that task.

---

### QA Phase 1: Core File Existence and Naming Conventions Verification

* **Objective:** Ensure all specified files for Phase 1 exist with the correct names and in the correct directory. Verify correct handling of new vs. replaced files.
* **Files to View (from the Plan Document):** All files listed in Phase 1, Sections 1 through 6.
* **Verification Tasks (can be parallelized per file):**

    1.  **Directory Check:**
        * For each file specified in the Plan Document:
            * Confirm the file resides in the `/advisor/` directory.
    2.  **Filename Accuracy:**
        * For each file specified in the Plan Document:
            * Confirm the filename exactly matches the name given in the Plan Document (e.g., `advisor/start.md`, `advisor/ineligible_general.md`).
    3.  **New File Creation:**
        * Identify all files marked as "(New)" or "(File to be created...)" in the Plan Document.
        * Confirm each of these files has been created.
            * `advisor/ownservice_vow_checkretired.md`
            * `advisor/ownservice_vow_retiredmajor_isdisabled.md`
            * `advisor/ineligible_vow_retiredmajor_notdisabled.md`
            * `advisor/ownservice_vow_honorableconditions.md`
            * `advisor/ineligible_vow_discharge_type.md`
            * `advisor/ownservice_checkdisability_intro.md`
            * `advisor/ownservice_tp_24month_duration.md`
            * `advisor/ownservice_tp_24month_exceptions.md`
            * `advisor/eligible_tp_5point.md`
            * `advisor/ineligible_tp_minduration.md`
            * `advisor/ineligible_ownservice_noqualifyingperiod.md`
            * *(Note: `advisor/derived_intro.md`, `advisor/ownservice_disability_details.md`, `advisor/ownservice_ssp_eligible.md` are future phase files but their placeholders might be checked for link validity later if linked from Phase 1 files).*
    4.  **File Replacement:**
        * Identify all files specified as replacing others in the Plan Document:
            * `advisor/ineligible_general.md` (replaces `ineligible_start.md`)
            * `advisor/ownservice_intro.md` (replaces `own_service_step1.md`)
            * `advisor/ownservice_nodisability_nossps_checkserviceperiod.md` (replaces `ownservice_nodisability_checkserviceperiod.md`)
        * Confirm the new file exists and the old file (if it existed) is no longer present or is clearly marked for deprecation if still needed for other branches.

---

### QA Phase 2: Page Titles and Layout Verification

* **Objective:** Verify that each Phase 1 Markdown file has the correct title and specified layout.
* **Files to View (from the Plan Document and corresponding developed .md files):** All files listed in Phase 1, Sections 1 through 6.
* **Verification Tasks (can be parallelized per file):**

    1.  **Title Verification:**
        * For each file listed in the Plan Document:
            * Open the corresponding Markdown file.
            * Check that the `Title:` frontmatter matches the exact title specified in the Plan Document.
    2.  **Layout Verification:**
        * For each file listed in the Plan Document:
            * Open the corresponding Markdown file.
            * Confirm the frontmatter includes `layout: default` (or the specified custom advisor layout, if one was decided upon).

---

### QA Phase 3: Content, Purpose, and Citation Accuracy Verification

* **Objective:** Ensure the content (Purpose, Content/Question) of each page aligns with the Plan Document and that citations are correctly indicated.
* **Files to View (from the Plan Document, corresponding developed .md files, and hrdocs.txt):** All files listed in Phase 1, Sections 1 through 6.
* **Verification Tasks (can be parallelized per file):**

    1.  **Purpose Alignment:**
        * For each file in the Plan Document:
            * Read the stated `Purpose:`.
            * Review the actual `Content/Question:` in the Markdown file.
            * Confirm the content fulfills the stated purpose.
    2.  **Content/Question Accuracy:**
        * For each file in the Plan Document:
            * Compare the `Content/Question:` in the Markdown file with the text specified in the Plan Document.
            * Verify accuracy and completeness. Minor wording changes for clarity are acceptable if they don't alter the meaning or logic, but should be noted.
    3.  **Citation Marker Presence:**
        * For each file, check the `Content/Question:` and `Notes:` in the Plan Document for mentions of "OPM Vet Guide" or specific sections/appendices.
        * In the corresponding Markdown file, ensure that:
            * The relevant information from the OPM Vet Guide is incorporated or accurately summarized.
            * Where the Plan Document says "(See OPM Vet Guide...)" or similar, ensure the Markdown file includes such a reference or that the information is directly integrated. (The Plan notes "Citations from hrdocs.txt are incorporated into the content/questions as appropriate"). Verify this incorporation.

---

### QA Phase 4: Navigational Choices and Links Verification

* **Objective:** Verify that all navigational choices (links) within each Phase 1 file are correctly implemented as per the Plan Document, including "Return to Advisor Start" links.
* **Files to View (from the Plan Document and corresponding developed .md files):** All files listed in Phase 1, Sections 1 through 6.
* **Verification Tasks (can be parallelized per file):**

    1.  **Choice Text and Destination Verification:**
        * For each file detailed in the Plan Document:
            * Locate the `Choices:` section.
            * For each choice listed:
                * Verify the link text in the Markdown file accurately matches the specified choice text (e.g., "My own service in the U.S. Armed Forces").
                * Verify the link destination (e.g., `-> advisor/ownservice_intro.md`) correctly points to the specified target Markdown file. Ensure relative paths are correct (e.g., `./filename.md`).
    2.  **"Return to Advisor Start" Link:**
        * For almost every page (as per "Overall Site Structure Considerations"):
            * Confirm the presence of the link: `[Return to Advisor Start](./start.md)`.
            * Verify it correctly links to `advisor/start.md`.
            * Note any files where this link is missing (unless intentionally omitted and documented).
    3.  **External/Informational Links (if any):**
        * For `advisor/eligible_tp_5point.md`:
            * Check the choice: `"Learn more about what to do next" (Link to a general info page, or OPM guidance)`.
            * Verify this link exists and, if the target is defined, that it's correct. If the target is not yet defined, note it as pending.

---

### QA Phase 5: Logic Flow and Notes Implementation Verification

* **Objective:** Check that any specific logic flows or conditions mentioned in the "Notes" or content of the Plan Document are correctly implemented.
* **Files to View (from the Plan Document and corresponding developed .md files):** Primarily files with "Notes:" or complex branching logic.
* **Verification Tasks (can be parallelized per file where notes exist):**

    1.  **`advisor/start.md` Notes:**
        * Plan Note: "Links updated to new standardized filenames."
        * Confirm all links in `start.md` use the standardized filenames as per the Plan Document.
    2.  **`advisor/ownservice_intro.md` Notes:**
        * Plan Note: "Review and potentially update `ineligible_ownservice_status.md`."
        * While the AI can't "review" in a subjective sense, it can confirm that `ineligible_ownservice_status.md` reflects the content described for it in the Plan Document.
    3.  **`advisor/ownservice_discharged_retiredmajor_isdisabled.md` Content Logic:**
        * Plan Content: "Yes, I am a disabled veteran." -> `advisor/ownservice_discharged_honorableconditions.md` (Disability preference will be key, but other conditions like honorable discharge are still checked first).
        * Confirm this specific routing logic is implemented.
    4.  **`advisor/ownservice_vow_honorableconditions.md` Content Logic:**
        * Plan Choice: "Yes, my certification indicates an expected Honorable or General discharge." -> `advisor/ownservice_checkdisability_intro.md` (Routing to check disability first... wording on subsequent pages may need to remind user this is based on certification until DD214 issued).
        * Confirm this routing. Note if subsequent pages (`ownservice_checkdisability_intro.md` path) have reminders about VOW Act certification basis (though this might be a Phase 2 check depending on how content is structured).
    5.  **`advisor/ownservice_checkdisability_intro.md` Link to Future Phase:**
        * Plan Choice: "Yes, I have a service-connected disability OR I received a Purple Heart." -> `advisor/ownservice_disability_details.md` (File to be created in Phase 2 - Disability Path).
        * Verify the link exists. The target file might not be fully developed, but the link should be present.
    6.  **`advisor/ownservice_discharged_checkfirst_solesurvivor.md` Link to Future Phase & Content:**
        * Plan Choice: "Yes, I believe I had a sole survivorship discharge." -> `advisor/ownservice_ssp_eligible.md` (File to be created in Phase 4 - Sole Survivor Path).
        * Verify the link exists.
        * Plan Note: "content adjusted for flow" & "Renamed from `ownservice_nodisability_checkserviceperiod.md` for clarity of this path".
        * Confirm the content aligns with what's in the Plan Doc for `advisor/ownservice_discharged_checkfirst_solesurvivor.md`.
    7.  **`advisor/ownservice_tp_24month_exceptions.md` Link to Future Phase:**
        * Plan Choice: "Yes, I was separated due to a service-connected disability." -> `advisor/ownservice_disability_details.md` (Link to Phase 2 - Disability Path...).
        * Verify the link exists.
    8.  **Disclaimer Accessibility:**
        * Per "Overall Site Structure Considerations," verify that the disclaimer is "visible or easily accessible from all advisor pages." Determine how this was implemented (e.g., footer, standard include) and check its presence/accessibility on a sample of pages, then extrapolate or list all pages for verification.
