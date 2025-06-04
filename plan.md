**Project Plan: Veteran's Preference Advisor Enhancement**

**Introduction:** This plan outlines the tasks required to enhance the "Veteran's Preference Advisor" tool and associated website content. Tasks are numbered for easy assignment and tracking, particularly when delegating to an AI agent like Google Jules.

**Phase 1: Foundational Accuracy and Core Advisor Enhancement**
**Goal:** Ensure the "Veteran's Preference Advisor" tool is accurate and comprehensive, based on the OPM Vet Guide.

* **1.1 Full Audit of Advisor Logic**
    * 1.1.1 **Action:** Systematically review every path and decision point within the `/advisor/` markdown files.
    * 1.1.2 **Reference:** Cross-reference all logic, conditions, and outcomes against the OPM Vet Guide.
    * 1.1.3 **Deliverable:** A report of discrepancies, gaps, or areas needing clarification.

* **1.2 Overhaul Citation System**
    * 1.2.1 **Problem:** Current citations in advisor markdown files (e.g., `[R7.2.1]`) refer to internal Repomix source tags or other unrelated files, not directly or clearly to the OPM Vet Guide content. This is evident in files like `advisor/derived_intro.md` and `advisor/derived_mother_common_currentmarital.md`.
    * 1.2.2 **Action:** Replace existing citations with a clear and consistent format that directly references the OPM Vet Guide.
    * 1.2.3 **Recommendation:** Use references like "(OPM Vet Guide, 'Section Name')" or "(OPM Vet Guide, 'Eligibility for 5-Point Preference (TP)')." For instance, information on "Mother of a disabled veteran" relating to living with a disabled husband should be cited accordingly.
    * 1.2.4 **Deliverable:** Updated advisor markdown files with accurate and meaningful citations.

* **1.3 Address Content Gaps in Advisor**
    * 1.3.1 **Action:** Based on the audit (Task 1.1) and the OPM Vet Guide, identify any veteran's preference scenarios, eligibility criteria, or specific conditions not currently covered or inadequately explained in the advisor.
    * 1.3.2 **Examples:**
        * 1.3.2.1 Nuances in "derived preference."
        * 1.3.2.2 Specific conditions for VOW Act eligibility.
        * 1.3.2.3 Details on different discharge types.
    * 1.3.3 **Deliverable:** New or updated markdown files in `/advisor/` to cover these gaps, ensuring clear, plain language.

* **1.4 Enhance "Ineligible" and "Eligibility Summary" Pages**
    * 1.4.1 **Action:** Review all `ineligible_.md` and `eligible_.md` pages.
    * 1.4.2 **For "Ineligible" pages:** Ensure they clearly state why a user might be ineligible according to the OPM Vet Guide and, where appropriate, guide the user to re-evaluate their answers or explore other potential paths (e.g., "Explore other preference types").
    * 1.4.3 **For "Eligibility Summary" pages:** Ensure they accurately summarize the specific preference type (e.g., TP 5-point, XP 10-point, CP 10-point, CPS 10-point), key entitlements, and immediate next steps, including the importance of the SF-15 for 10-point preferences.
    * 1.4.4 **Deliverable:** Revised markdown files with improved explanations and guidance.

* **1.5 Develop SF-15 Informational Content**
    * 1.5.1 **Action:** The current links like "Learn more about applying with 10-point preference (SF-15)" are placeholders. Create a dedicated page (or section on relevant eligibility pages) explaining what the SF-15 ("Application for 10-Point Veteran Preference") is, why it's needed, and link to the official OPM form/guidance. The OPM Vet Guide mentions the SF-15 extensively.
    * 1.5.2 **Deliverable:** New markdown page(s) for SF-15 information and updated links in advisor pages.

**Phase 2: User Experience (UX) and Navigation Improvement**
**Goal:** Make the website, particularly the advisor tool, more intuitive, user-friendly, and easier to navigate.

* **2.1 Refine Advisor Introduction and Instructions**
    * 2.1.1 **Action:** Review the `index.md` and `advisor/start.md` pages. Ensure the purpose of the advisor, what users can expect, and what information they might need (like DD Form 214) is exceptionally clear and encouraging.
    * 2.1.2 **Deliverable:** Updated `index.md` and `advisor/start.md`.

* **2.2 Consistency in Navigation Links**
    * 2.2.1 **Action:** Ensure all advisor pages consistently feature:
        * 2.2.1.1 Correct and clearly labeled links for choices.
        * 2.2.1.2 A "Return to previous question" link where logical.
        * 2.2.1.3 A persistent "Return to Advisor Start" link.
    * 2.2.2 **Deliverable:** Standardized navigation across all `/advisor/` pages.

* **2.3 Mobile Responsiveness and Readability Review**
    * 2.3.1 **Action:** The `jekyll-theme-minimal` is generally responsive. Thoroughly test the advisor flow and all content pages on various screen sizes (desktop, tablet, mobile). Pay attention to font sizes, line spacing, and link tap targets. The current SCSS defines responsive behavior.
    * 2.3.2 **Deliverable:** CSS adjustments in `_sass/jekyll-theme-minimal.scss` or `assets/css/style.scss` if needed.

* **2.4 Accessibility Audit (Basic)**
    * 2.4.1 **Action:** Review for basic accessibility:
        * 2.4.1.1 Sufficient color contrast (e.g., body text color: `#727272`; on white is WCAG AA for normal text, but check other elements).
        * 2.4.1.2 Logical heading structure (H1, H2, H3) in markdown files for screen readers.
        * 2.4.1.3 Ensure links are descriptive.
    * 2.4.2 **Deliverable:** Report of accessibility issues and implemented fixes.

**Phase 3: Content Expansion and Value Addition**
**Goal:** Broaden the scope of information available on the site by leveraging the rich content within the OPM Vet Guide.

* **3.1 Create a Glossary of Terms**
    * 3.1.1 **Action:** Develop a glossary page defining key terms used in veteran's preference and federal hiring (e.g., "Active Duty," "Honorable Conditions," "Compensable Service-Connected Disability," "VRA," "VEOA," "RIF").
    * 3.1.2 **Reference:** The OPM Vet Guide (e.g., definitions in Appendix A, types of preference).
    * 3.1.3 **Deliverable:** A new `glossary.md` page, with terms linked from advisor and other content pages.

* **3.2 Develop an FAQ Section**
    * 3.2.1 **Action:** Create an FAQ page addressing common questions veterans might have.
    * 3.2.2 **Potential Topics (derived from the OPM Vet Guide):**
        * 3.2.2.1 How is "war" defined for preference purposes?
        * 3.2.2.2 What's the difference between 5-point and 10-point preference?
        * 3.2.2.3 How does preference apply in Reductions in Force (RIF)?
        * 3.2.2.4 What if I don't have my DD Form 214?
        * 3.2.2.5 What is "derived preference"?
        * 3.2.2.6 Does preference apply to all federal jobs?
    * 3.2.3 **Deliverable:** A new `faq.md` page.

* **3.3 Summaries of Key OPM Vet Guide Sections**
    * 3.3.1 **Action:** Create reader-friendly summary pages for complex but important topics from the OPM Vet Guide.
    * 3.3.2 **Examples:**
        * 3.3.2.1 "Crediting Experience of Preference Eligibles."
        * 3.3.2.2 "Physical Qualifications and Waivers."
        * 3.3.2.3 "Restoration After Uniformed Service" (USERRA rights).
        * 3.3.2.4 "Special Appointing Authorities for Veterans" (VRA, 30% Disabled, etc.).
    * 3.3.3 **Deliverable:** New markdown pages for each summary.

* **3.4 Detailed Guides on Veteran Hiring Authorities**
    * 3.4.1 **Action:** Expand on specific hiring authorities like:
        * 3.4.1.1 Veterans Recruitment Appointment (VRA).
        * 3.4.1.2 Veterans Employment Opportunities Act (VEOA).
        * 3.4.1.3 Appointment of 30 Percent or More Disabled Veterans.
        * 3.4.1.4 Hubbard Act (Sole Survivor Preference).
    * 3.4.2 **Deliverable:** Dedicated pages for each authority, explaining eligibility, how to apply, and benefits.

**Phase 4: Technical Refinements and Maintainability**
**Goal:** Improve the Jekyll site's structure, performance, and ease of future updates.

* **4.1 Implement Jekyll Data Files**
    * 4.1.1 **Action:** For repetitive data, such as lists of qualifying campaigns/medals or definitions for the glossary, use Jekyll data files (in `_data` directory).
    * 4.1.2 **Benefit:** Centralizes data, making updates easier and content more consistent.
    * 4.1.3 **Deliverable:** Relevant `.yml` or `.json` data files and updated markdown to use them.

* **4.2 Utilize Jekyll Includes for Repetitive Content**
    * 4.2.1 **Action:** Identify blocks of text or HTML repeated across multiple pages (e.g., the disclaimer on `index.md`, "Return to Advisor Start" link structure). Convert these into Jekyll includes (`_includes` directory).
    * 4.2.2 **Benefit:** Reduces redundancy and simplifies updates to common elements.
    * 4.2.3 **Deliverable:** Include files and updated markdown.

* **4.3 Content Organization with Jekyll Collections (Optional but Recommended)**
    * 4.3.1 **Action:** Consider structuring related content like FAQ items, Glossary terms, or Advisor path segments as Jekyll Collections.
    * 4.3.2 **Benefit:** Better organization of source files and more flexible presentation options.
    * 4.3.3 **Deliverable:** Configuration in `_config.yml` and reorganized files if implemented.

* **4.4 Improve OPM Vet Guide Management & Citation (Advanced)**
    * 4.4.1 **Challenge:** The OPM Vet Guide is a very large, single text file. Citing it meaningfully (as per Task 1.2) is key. For long-term maintainability:
    * 4.4.2 **Option 1 (Simpler):** Create an internal "anchor" system within the OPM Vet Guide if you decide to display it directly, or use clear section headings from the original OPM Vet Guide for citations.
    * 4.4.3 **Option 2 (More Complex):** Break down the OPM Vet Guide into multiple smaller markdown files (e.g., `_opm_guide_sections/introduction.md`, `_opm_guide_sections/5_point_preference.md`). Then, citations in advisor pages can link directly to these more granular, human-readable files. This would also allow these sections to be displayed as standalone pages if desired.
    * 4.4.4 **Deliverable:** A chosen strategy implemented for better OPM Vet Guide integration.

* **4.5 Enhance README.md**
    * 4.5.1 **Action:** The current `README.md` is minimal. Expand it to include:
        * 4.5.1.1 A detailed description of the project's purpose.
        * 4.5.1.2 How to run the Jekyll site locally for development or contributions.
        * 4.5.1.3 Brief overview of the content structure.
    * 4.5.2 **Deliverable:** Updated `README.md`.

* **4.6 Review _config.yml**
    * 4.6.1 **Action:** Check for unused plugins (e.g., `mathjax` is listed but likely unused). Ensure settings are optimal.
    * 4.6.2 **Deliverable:** Cleaned up and optimized `_config.yml`.

**Phase 5: Review, Testing, and Launch Preparations**
**Goal:** Ensure all changes are implemented correctly, the site functions as expected, and content is polished before wider announcement.

* **5.1 Comprehensive Advisor Path Testing**
    * 5.1.1 **Action:** Manually go through every possible path in the Veteran's Preference Advisor. Verify:
        * 5.1.1.1 Correct logic and outcomes.
        * 5.1.1.2 All links work.
        * 5.1.1.3 Citations are accurate and helpful.
        * 5.1.1.4 Content is clear and free of typos/grammar errors.
    * 5.1.2 **Deliverable:** Testing checklist and bug/issue report.

* **5.2 Cross-Browser and Cross-Device Testing**
    * 5.2.1 **Action:** Test the entire website on major browsers (Chrome, Firefox, Safari, Edge) and different devices (desktop, tablet, mobile).
    * 5.2.2 **Deliverable:** Browser/device compatibility report.

* **5.3 Proofreading and Editing**
    * 5.3.1 **Action:** Have a fresh pair of eyes review all new and significantly modified content for clarity, grammar, spelling, and tone.
    * 5.3.2 **Deliverable:** Edited and polished content.

* **5.4 Final Link Check**
    * 5.4.1 **Action:** Use a link checker tool (or manually verify) all internal and external links. Ensure links to official resources like OPM and VA are current.
    * 5.4.2 **Deliverable:** Report of broken links and fixes.
