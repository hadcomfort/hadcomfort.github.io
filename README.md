# Veteran's Preference Advisor Website (hadcomfort.github.io)

This README provides an overview of the Veteran's Preference Advisor website project, how to run it locally, and its content structure.

## Overview

### Project Description

Welcome to our Veteran's Preference Advisor! This website is designed to help you understand how U.S. Veteran's Preference works in federal hiring.

Our core feature is the "Veteran's Preference Advisor" tool. This interactive tool will guide you through a series of questions to help you determine your potential eligibility for different types of veteran's preference.

The information provided by this tool is based on the Office of Personnel Management (OPM) Vet Guide. Our goal is to make this information more accessible and easier to understand.

We hope this tool empowers you with the knowledge to navigate the federal hiring process with greater confidence.

## Development

This section covers how to set up and run the website locally, and provides an overview of the project's content structure.

### Running the Site Locally

To run this website on your local machine, you'll need to have a few prerequisites installed and then follow the steps below.

#### Prerequisites

- **Ruby**: It's recommended to use the latest stable version (e.g., 3.x). You can check if Ruby is installed by running `ruby -v`. If not, consider using a version manager like rbenv or RVM, or download it from [ruby-lang.org](https://www.ruby-lang.org/en/downloads/).
- **Bundler**: Bundler is a Ruby gem that manages project dependencies. Install it by running `gem install bundler`. Once Bundler is installed, other gems should generally be installed via `bundle install`.
- **Jekyll**: Jekyll is a static site generator. While `gem install jekyll` works, running `bundle install` in the project directory (see step 3 below) is the preferred way to install Jekyll and other project-specific gems if a `Gemfile` is present (which is good practice, though not currently in this project).

#### Step-by-Step Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/hadcomfort/hadcomfort.github.io.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd hadcomfort.github.io
    ```

3.  **Install dependencies:** This command installs all necessary Ruby gems, including Jekyll and its dependencies, as defined by the project (typically in a `Gemfile` and `Gemfile.lock`, or default Jekyll gems if these files are not present).
    ```bash
    bundle install
    ```

4.  **Serve the site:** This command builds the site and starts a local web server.
    ```bash
    bundle exec jekyll serve
    ```

### Accessing the Local Site

Once the server is running (you'll see output in your terminal indicating this), you can access the site by opening your web browser and navigating to:

`http://localhost:4000`

You should see the website running just as it would online. Jekyll will automatically rebuild the site when you save changes to most files (you might need to refresh your browser to see the updates).

### Content Structure

This website is built using Jekyll, a static site generator. Jekyll processes the markdown files, layouts, and other assets in this repository to create the final HTML website. Here's a brief overview of the key directories and files:

-   **`/advisor/`**: This directory is central to our site. It contains a series of Markdown files (`.md`) that make up the interactive Veteran's Preference Advisor. Each file typically represents a specific question, decision point, or outcome in the advisor's flow, guiding the user through the eligibility determination process.

-   **`hrdocs.txt`**: This text file contains the full content of the Office of Personnel Management (OPM) Vet Guide. It serves as the primary source document and reference for the logic, definitions, and information presented in the Veteran's Preference Advisor.

-   **`plan.md`**: This file outlines the project plan, including past achievements and future enhancements envisioned for the advisor tool and the overall website. It provides context on the project's development roadmap.

-   **`_layouts/`**: This directory holds the HTML template files that define the structure for different types of pages on the site. For example, `default.html` might define the main site template, and other layouts might exist for specific page types like blog posts or advisor pages.

-   **`assets/`**: This folder is used for static assets. Currently, it primarily contains CSS files (under `assets/css/`) which define the visual styling of the website. In the future, it might also include images or other static resources.

-   **`_data/`** (potential future use): While not currently implemented, this directory could be used to store structured data in YAML, JSON, or CSV format. This is useful for content like lists of qualifying military campaigns, glossary definitions, or other data sets that can be easily managed and reused across the site (as envisioned in task 4.1 of `plan.md`).

-   **`_includes/`** (potential future use): This directory, also a potential future enhancement (see task 4.2 in `plan.md`), would be used for reusable snippets of HTML or Markdown. These snippets could be included in multiple pages or layouts to avoid repetition and make site maintenance easier.

Understanding this structure can be helpful if you plan to contribute to the project or explore its technical details.
