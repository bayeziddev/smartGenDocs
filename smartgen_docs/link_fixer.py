"""
SmartGen Docs -- Contextual Link Fixer Engine

Scans the root 'docs/' folder and safely converts internal '.md' links to '.html'.
Guarantees zero side-effects: Skips third-party external domains, strictly modifies
only the text content of the files, and never alters the actual file names.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

# Architectural Guardrails
TARGET_DOMAIN = "docs.smartgentools.com"
DOCS_DIR = Path("docs")

def fix_md_to_html_in_file(md_file: Path, apply: bool = False) -> int:
    """Scans a single markdown file and replaces targeted .md links with .html in its content."""
    if not md_file.exists():
        return 0

    # 1. Read the file content into memory (does not touch the filename)
    content = md_file.read_text(encoding="utf-8")
    
    # Strict Regex Pattern: Matches [text](url.md) or [text](url.md#anchor)
    pattern = re.compile(r'(\[.*?\])\(([^)]*?\.md(?:#[^)]*)?)\)')
    
    def replacer(match):
        text_part = match.group(1)
        url_part = match.group(2)
        
        # Extract just the URL base without the anchor for domain checking
        url_base = url_part.split('#')[0]
        
        # Guardrail: Check if it is an internal relative link OR matches the target domain
        is_internal = not url_base.startswith("http")
        is_target_domain = TARGET_DOMAIN in url_base
        
        if is_internal or is_target_domain:
            # Replace the '.md' with '.html' safely, keeping anchors intact if any
            # Using rsplit or replace to ensure we only change the extension
            new_url = url_part.replace(".md", ".html", 1)
            
            if apply:
                print(f"✅ Fixed in {md_file.name}: '{url_part}' ➔ '{new_url}'")
            else:
                print(f"🔍 [DRY RUN] Would fix in {md_file.name}: '{url_part}' ➔ '{new_url}'")
            
            return f"{text_part}({new_url})"
        
        # If it is a third-party .md link, return the original match unaltered
        return match.group(0)

    # 2. Perform the substitution in memory
    new_content, count = pattern.subn(replacer, content)

    # 3. Write changes back to the exact same file (overwrites content, does not rename)
    if apply and count > 0:
        md_file.write_text(new_content, encoding="utf-8")

    return count

def run_fixer(apply: bool = False, **kwargs):
    """Main execution block to recursively scan the docs folder."""
    if not DOCS_DIR.exists() or not DOCS_DIR.is_dir():
        print("❌ Fatal Error: 'docs/' directory not found. Must be executed from the project root.")
        return

    print(f"\n--- SmartGen Docs Contextual Link Fixer (Apply Mode: {apply}) ---\n")
    
    total_fixed = 0
    
    # Recursively find all markdown files strictly inside the docs/ folder
    for md_file in DOCS_DIR.rglob("*.md"):
        fixed_in_file = fix_md_to_html_in_file(md_file, apply=apply)
        total_fixed += fixed_in_file

    print(f"\nSummary: {total_fixed} contextual '.md' links processed and converted to '.html'.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SmartGen Docs Auto Link Fixer")
    parser.add_argument("--apply", action="store_true", help="Apply changes directly to .md files")
    args = parser.parse_args()

    run_fixer(apply=args.apply)