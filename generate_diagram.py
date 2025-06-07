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
    file_data = {}
    for filename in markdown_files_in_advisor:
        filepath = os.path.join(advisor_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        file_data[filename] = content

    for filename in markdown_files_in_advisor:
        # The check 'if filename in file_data' is technically redundant now
        # as markdown_files_in_advisor is the source for file_data's keys.
        # However, keeping it doesn't harm and adds a layer of safety if logic changes.
        if filename in file_data:
            content = file_data[filename]
            # Pass the full path for context if needed, but parse_links uses os.path.basename
            full_path = os.path.join(advisor_dir, filename)
            links = parse_links(full_path, content, markdown_files_in_advisor)
            all_relationships.extend(links)
        else:
            # This path should not be reached if markdown_files_in_advisor is correct
            # and file reading was successful.
            print(f"Warning: Content for {filename} was not loaded.")

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
    output_filename = os.path.join("advisor", "advisor_diagram.md")
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(output_content)

if __name__ == "__main__":
    main()
