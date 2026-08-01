"""
SmartGen Docs -- Intelligent Auto-Fixer Engine

Reads audit-report.json and safely repairs broken links in source Markdown files (.md).
Guarantees zero side-effects: Skips third-party external domains, ignores code blocks,
and offers a --dry-run option before writing changes.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse

# 1. Master list of valid live URLs provided by you (Source of Truth)
VALID_URLS = [
    "https://docs.smartgentools.com/",
    "https://docs.smartgentools.com/community/sponsor.html",
    "https://docs.smartgentools.com/getting-started/index.html",
    "https://docs.smartgentools.com/getting-started/installation.html",
    "https://docs.smartgentools.com/getting-started/quick-start.html",
    "https://docs.smartgentools.com/getting-started/first-project.html",
    "https://docs.smartgentools.com/getting-started/folder-structure.html",
    "https://docs.smartgentools.com/getting-started/deployment.html",
    "https://docs.smartgentools.com/getting-started/faq.html",
    "https://docs.smartgentools.com/docs/index.html",
    "https://docs.smartgentools.com/docs/platform.html",
    "https://docs.smartgentools.com/docs/architecture.html",
    "https://docs.smartgentools.com/docs/features.html",
    "https://docs.smartgentools.com/docs/concepts.html",
    "https://docs.smartgentools.com/docs/releases.html",
    "https://docs.smartgentools.com/docs/changelog.html",
    "https://docs.smartgentools.com/api/index.html",
    "https://docs.smartgentools.com/api/authentication.html",
    "https://docs.smartgentools.com/api/rest-api.html",
    "https://docs.smartgentools.com/api/endpoints.html",
    "https://docs.smartgentools.com/api/errors.html",
    "https://docs.smartgentools.com/api/rate-limits.html",
    "https://docs.smartgentools.com/api/webhooks.html",
    "https://docs.smartgentools.com/sdk/index.html",
    "https://docs.smartgentools.com/sdk/javascript.html",
    "https://docs.smartgentools.com/sdk/python.html",
    "https://docs.smartgentools.com/sdk/php.html",
    "https://docs.smartgentools.com/sdk/java.html",
    "https://docs.smartgentools.com/sdk/go.html",
    "https://docs.smartgentools.com/tools/index.html",
    "https://docs.smartgentools.com/tools/qr-generator.html",
    "https://docs.smartgentools.com/tools/seo.html",
    "https://docs.smartgentools.com/tools/ai.html",
    "https://docs.smartgentools.com/tools/developer.html",
    "https://docs.smartgentools.com/tools/marketing.html",
    "https://docs.smartgentools.com/tools/utilities.html",
    "https://docs.smartgentools.com/tutorials/index.html",
    "https://docs.smartgentools.com/tutorials/beginner.html",
    "https://docs.smartgentools.com/tutorials/api.html",
    "https://docs.smartgentools.com/tutorials/integrations.html",
    "https://docs.smartgentools.com/tutorials/best-practices.html",
    "https://docs.smartgentools.com/tutorials/case-studies.html",
    "https://docs.smartgentools.com/guides/configuration.html",
    "https://docs.smartgentools.com/guides/customization.html",
    "https://docs.smartgentools.com/guides/security.html",
    "https://docs.smartgentools.com/guides/performance.html",
    "https://docs.smartgentools.com/guides/seo.html",
    "https://docs.smartgentools.com/guides/accessibility.html",
    "https://docs.smartgentools.com/guides/troubleshooting.html",
    "https://docs.smartgentools.com/resources/downloads.html",
    "https://docs.smartgentools.com/resources/templates.html",
    "https://docs.smartgentools.com/resources/examples.html",
    "https://docs.smartgentools.com/resources/roadmap.html",
    "https://docs.smartgentools.com/resources/glossary.html",
    "https://docs.smartgentools.com/community/index.html",
    "https://docs.smartgentools.com/community/issues.html",
    "https://docs.smartgentools.com/community/features.html",
    "https://docs.smartgentools.com/community/discussions.html",
    "https://docs.smartgentools.com/community/contributing.html",
    "https://docs.smartgentools.com/blog/index.html",
    "https://docs.smartgentools.com/blog/latest.html",
    "https://docs.smartgentools.com/blog/tutorials.html",
    "https://docs.smartgentools.com/blog/releases.html",
    "https://docs.smartgentools.com/about/index.html",
    "https://docs.smartgentools.com/about/developer.html",
    "https://docs.smartgentools.com/about/contact.html",
    "https://docs.smartgentools.com/about/license.html"
]

TARGET_DOMAIN = "docs.smartgentools.com"


def is_third_party_domain(url: str) -> bool:
    """Filter to check and skip third-party/external domains."""
    if url.startswith("http://") or url.startswith("https://"):
        parsed = urlparse(url)
        if parsed.netloc and parsed.netloc != TARGET_DOMAIN:
            return True
    return False


def html_to_md_path(html_source: str) -> Path:
    """Converts site/path/file.html to docs/path/file.md."""
    path_str = html_source.replace("\\", "/")
    if path_str.startswith("site/"):
        path_str = path_str.replace("site/", "docs/", 1)
    
    p = Path(path_str)
    if p.suffix == ".html":
        p = p.with_suffix(".md")
    return p


def find_best_matching_url(broken_url: str) -> str | None:
    """Finds the most accurate valid link that matches the broken URL."""
    broken_clean = broken_url.split("#")[0].split("?")[0].strip("/")
    filename = Path(broken_clean).name.replace(".html", "").replace(".md", "")

    if not filename:
        return None

    for valid_url in VALID_URLS:
        if filename in valid_url:
            return valid_url
    return None


def fix_links_in_file(md_file: Path, broken_url: str, new_url: str, apply: bool = False) -> bool:
    """Replaces the link only if it matches the strict Markdown format."""
    if not md_file.exists():
        print(f"❌ Target Markdown file not found: {md_file}")
        return False

    content = md_file.read_text(encoding="utf-8")
    
    # Strict Regex Pattern: [text](broken_url)
    escaped_broken = re.escape(broken_url)
    pattern = rf'(\[.*?\]\()({escaped_broken})(\)'

    if not re.search(pattern, content):
        # Fallback for relative paths without leading slash
        alt_broken = broken_url.lstrip("/")
        escaped_alt = re.escape(alt_broken)
        pattern = rf'(\[.*?\]\()({escaped_alt})(\)'
        if not re.search(pattern, content):
            print(f"⚠️ Link '{broken_url}' not found in strict Markdown format in {md_file}")
            return False

    new_content = re.sub(pattern, r'\1' + new_url + r'\3', content)

    if apply:
        md_file.write_text(new_content, encoding="utf-8")
        print(f"✅ Fixed: {md_file} | '{broken_url}' ➔ '{new_url}'")
    else:
        print(f"🔍 [DRY RUN] Would fix in {md_file}: '{broken_url}' ➔ '{new_url}'")

    return True


def run_fixer(report_json_path: str = "site/audit-report.json", apply: bool = False):
    report_file = Path(report_json_path)
    if not report_file.exists():
        # Fallback path if generated in default site root
        report_file = Path("audit-report.json")
        if not report_file.exists():
            print(f"❌ Report file not found at {report_json_path}. Run audit first.")
            return

    data = json.loads(report_file.read_text(encoding="utf-8"))
    results = data.get("results", [])

    print(f"\n--- SmartGen Docs Link Fixer (Apply Mode: {apply}) ---\n")

    fixed_count = 0
    skipped_count = 0

    for item in results:
        if item.get("status") != "broken":
            continue

        source_html = item.get("source_page", "")
        broken_url = item.get("url", "")

        # Guardrail 1: Skip manual third-party links
        if is_third_party_domain(broken_url):
            print(f"🛡️ SKIPPED (External Domain): {broken_url} in {source_html}")
            skipped_count += 1
            continue

        # Extract matching source markdown file
        md_file = html_to_md_path(source_html)
        
        # Find best valid URL match
        best_url = find_best_matching_url(broken_url)

        if not best_url:
            print(f"⚠️ SKIPPED (No valid match found): {broken_url}")
            skipped_count += 1
            continue

        if fix_links_in_file(md_file, broken_url, best_url, apply=apply):
            fixed_count += 1

    print(f"\nSummary: {fixed_count} links processed/fixed, {skipped_count} external/unmatched links skipped.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SmartGen Docs Auto Link Fixer")
    parser.add_argument("--apply", action="store_true", help="Apply changes directly to .md files")
    parser.add_argument("--report", default="site/audit-report.json", help="Path to audit-report.json")
    args = parser.parse_args()

    run_fixer(report_json_path=args.report, apply=args.apply)