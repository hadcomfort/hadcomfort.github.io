Phase 1: Foundational Accuracy and Core Advisor Enhancement
Goal: Ensure the "Veteran's Preference Advisor" tool is accurate and comprehensive, based on the OPM Vet Guide.
Tasks:
 * Full Audit of Advisor Logic:
   * Action: Systematically review every path and decision point within the /advisor/ markdown files.
   * Reference: Cross-reference all logic, conditions, and outcomes against the OPM Vet Guide.
   * Deliverable: A report of discrepancies, gaps, or areas needing clarification.
 * Overhaul Citation System:
   * Problem: Current citations in advisor markdown files (e.g., [R7.2.1]) refer to internal Repomix source tags or other unrelated files, not directly or clearly to the OPM Vet Guide content. This is evident in files like advisor/derived_intro.md and advisor/derived_mother_common_currentmarital.md.
   * Action: Replace existing citations with a clear and consistent format that directly references the OPM Vet Guide.
   * Recommendation: Use references like "(OPM Vet Guide, 'Section Name')" or "(OPM Vet Guide, 'Eligibility for 5-Point Preference (TP)')." For instance, information on "Mother of a disabled veteran" relating to living with a disabled husband should be cited accordingly.
   * Deliverable: Updated advisor markdown files with accurate and meaningful citations.
 * Address Content Gaps in Advisor:
   * Action: Based on the audit (Task 1.1) and the OPM Vet Guide, identify any veteran's preference scenarios, eligibility criteria, or specific conditions not currently covered or inadequately explained in the advisor.
   * Examples: Nuances in "derived preference," specific conditions for VOW Act eligibility, or details on different discharge types.
   * Deliverable: New or updated markdown files in /advisor/ to cover these gaps, ensuring clear, plain language.
 * Enhance "Ineligible" and "Eligibility Summary" Pages:
   * Action: Review all "ineligible_.md" and "eligible_.md" pages.
   * For "Ineligible" pages: Ensure they clearly state why a user might be ineligible according to the OPM Vet Guide and, where appropriate, guide the user to re-evaluate their answers or explore other potential paths (e.g., "Explore other preference types").
   * For "Eligibility Summary" pages: Ensure they accurately summarize the specific preference type (e.g., TP 5-point, XP 10-point, CP 10-point, CPS 10-point), key entitlements, and immediate next steps, including the importance of the SF-15 for 10-point preferences.
   * Deliverable: Revised markdown files with improved explanations and guidance.
 * Develop SF-15 Informational Content:
   * Action: The current links like "Learn more about applying with 10-point preference (SF-15)" are placeholders. Create a dedicated page (or section on relevant eligibility pages) explaining what the SF-15 ("Application for 10-Point Veteran Preference") is, why it's needed, and link to the official OPM form/guidance. The OPM Vet Guide mentions the SF-15 extensively.
   * Deliverable: New markdown page(s) for SF-15 information and updated links in advisor pages.
Phase 2: User Experience (UX) and Navigation Improvement
Goal: Make the website, particularly the advisor tool, more intuitive, user-friendly, and easier to navigate.
Tasks:
 * Refine Advisor Introduction and Instructions:
   * Action: Review the index.md and advisor/start.md pages. Ensure the purpose of the advisor, what users can expect, and what information they might need (like DD Form 214) is exceptionally clear and encouraging.
   * Deliverable: Updated index.md and advisor/start.md.
 * Consistency in Navigation Links:
   * Action: Ensure all advisor pages consistently feature:
     * Correct and clearly labeled links for choices.
     * A "Return to previous question" link where logical.
     * A persistent "Return to Advisor Start" link.
   * Deliverable: Standardized navigation across all /advisor/ pages.
 * Mobile Responsiveness and Readability Review:
   * Action: The jekyll-theme-minimal is generally responsive. Thoroughly test the advisor flow and all content pages on various screen sizes (desktop, tablet, mobile). Pay attention to font sizes, line spacing, and link tap targets. The current SCSS defines responsive behavior.
   * Deliverable: CSS adjustments in _sass/jekyll-theme-minimal.scss or assets/css/style.scss if needed.
 * Accessibility Audit (Basic):
   * Action: Review for basic accessibility:
     * Sufficient color contrast (e.g., body text color:#727272; on white is WCAG AA for normal text, but check other elements).
     * Logical heading structure (H1, H2, H3) in markdown files for screen readers.
     * Ensure links are descriptive.
   * Deliverable: Report of accessibility issues and implemented fixes.
Phase 3: Content Expansion and Value Addition
Goal: Broaden the scope of information available on the site by leveraging the rich content within the OPM Vet Guide.
Tasks:
 * Create a Glossary of Terms:
   * Action: Develop a glossary page defining key terms used in veteran's preference and federal hiring (e.g., "Active Duty," "Honorable Conditions," "Compensable Service-Connected Disability," "VRA," "VEOA," "RIF").
   * Reference: The OPM Vet Guide (e.g., definitions in Appendix A, types of preference).
   * Deliverable: A new glossary.md page, with terms linked from advisor and other content pages.
 * Develop an FAQ Section:
   * Action: Create an FAQ page addressing common questions veterans might have.
   * Potential Topics (derived from the OPM Vet Guide):
     * How is "war" defined for preference purposes?
     * What's the difference between 5-point and 10-point preference?
     * How does preference apply in Reductions in Force (RIF)?
     * What if I don't have my DD Form 214?
     * What is "derived preference"?
     * Does preference apply to all federal jobs?
   * Deliverable: A new faq.md page.
 * Summaries of Key OPM Vet Guide Sections:
   * Action: Create reader-friendly summary pages for complex but important topics from the OPM Vet Guide.
   * Examples:
     * "Crediting Experience of Preference Eligibles."
     * "Physical Qualifications and Waivers."
     * "Restoration After Uniformed Service" (USERRA rights).
     * "Special Appointing Authorities for Veterans" (VRA, 30% Disabled, etc.).
   * Deliverable: New markdown pages for each summary.
 * Detailed Guides on Veteran Hiring Authorities:
   * Action: Expand on specific hiring authorities like:
     * Veterans Recruitment Appointment (VRA).
     * Veterans Employment Opportunities Act (VEOA).
     * Appointment of 30 Percent or More Disabled Veterans.
     * Hubbard Act (Sole Survivor Preference).
   * Deliverable: Dedicated pages for each authority, explaining eligibility, how to apply, and benefits.
Phase 4: Technical Refinements and Maintainability
Goal: Improve the Jekyll site's structure, performance, and ease of future updates.
Tasks:
 * Implement Jekyll Data Files:
   * Action: For repetitive data, such as lists of qualifying campaigns/medals or definitions for the glossary, use Jekyll data files (in _data directory).
   * Benefit: Centralizes data, making updates easier and content more consistent.
   * Deliverable: Relevant .yml or .json data files and updated markdown to use them.
 * Utilize Jekyll Includes for Repetitive Content:
   * Action: Identify blocks of text or HTML repeated across multiple pages (e.g., the disclaimer on index.md, "Return to Advisor Start" link structure). Convert these into Jekyll includes (_includes directory).
   * Benefit: Reduces redundancy and simplifies updates to common elements.
   * Deliverable: Include files and updated markdown.
 * Content Organization with Jekyll Collections (Optional but Recommended):
   * Action: Consider structuring related content like FAQ items, Glossary terms, or Advisor path segments as Jekyll Collections.
   * Benefit: Better organization of source files and more flexible presentation options.
   * Deliverable: Configuration in _config.yml and reorganized files if implemented.
 * Improve OPM Vet Guide Management & Citation (Advanced):
   * Challenge: The OPM Vet Guide is a very large, single text file. Citing it meaningfully (as per Phase 1.2) is key. For long-term maintainability:
   * Option 1 (Simpler): Create an internal "anchor" system within the OPM Vet Guide if you decide to display it directly, or use clear section headings from the original OPM Vet Guide for citations.
   * Option 2 (More Complex): Break down the OPM Vet Guide into multiple smaller markdown files (e.g., _opm_guide_sections/introduction.md, _opm_guide_sections/5_point_preference.md). Then, citations in advisor pages can link directly to these more granular, human-readable files. This would also allow these sections to be displayed as standalone pages if desired.
   * Deliverable: A chosen strategy implemented for better OPM Vet Guide integration.
 * Enhance README.md:
   * Action: The current README.md is minimal. Expand it to include:
     * A detailed description of the project's purpose.
     * How to run the Jekyll site locally for development or contributions.
     * Brief overview of the content structure.
   * Deliverable: Updated README.md.
 * Review _config.yml:
   * Action: Check for unused plugins (e.g., mathjax is listed but likely unused). Ensure settings are optimal.
   * Deliverable: Cleaned up and optimized _config.yml.
Phase 5: Review, Testing, and Launch Preparations
Goal: Ensure all changes are implemented correctly, the site functions as expected, and content is polished before wider announcement.
Tasks:
 * Comprehensive Advisor Path Testing:
   * Action: Manually go through every possible path in the Veteran's Preference Advisor. Verify:
     * Correct logic and outcomes.
     * All links work.
     * Citations are accurate and helpful.
     * Content is clear and free of typos/grammar errors.
   * Deliverable: Testing checklist and bug/issue report.
 * Cross-Browser and Cross-Device Testing:
   * Action: Test the entire website on major browsers (Chrome, Firefox, Safari, Edge) and different devices (desktop, tablet, mobile).
   * Deliverable: Browser/device compatibility report.
 * Proofreading and Editing:
   * Action: Have a fresh pair of eyes review all new and significantly modified content for clarity, grammar, spelling, and tone.
   * Deliverable: Edited and polished content.
 * Final Link Check:
   * Action: Use a link checker tool (or manually verify) all internal and external links. Ensure links to official resources like OPM and VA are current.
   * Deliverable: Report of broken links and fixes.
By following this multi-phase plan, you can significantly enhance the quality, accuracy, and user-friendliness of your Veterans Information Resource website, making it an even more valuable tool for veterans and their families.
