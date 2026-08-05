"""
SmartGen Docs -- Contextual Link Fixer Engine

Rewrites internal Markdown-style links that point at a `.md` source file
(e.g. `[Installation](installation.md)`) so they point at the built `.html`
output instead (`[Installation](installation.html)`).

This module is used two ways:

1.  Automatically, in-memory, by `core.Builder.build_page()` on every build --
    so every page ships with correct contextual links with zero manual steps.
2.  As a standalone maintenance script you can still run by hand against the
    `docs/` source tree (`python -m smartgen_docs.link_fixer --apply`) if you
    ever want the *source* Markdown files themselves rewritten too.

Guarantees zero side-effects: skips third-party external domains, strictly
modifies only text content, and never touches file names.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

# Architectural Guardrails
TARGET_DOMAIN = "docs.smartgentools.com"
DOCS_DIR = Path("docs")

# Strict Regex Pattern: Matches [text](url.md) or [text](url.md#anchor)
_MD_LINK_PATTERN = re.compile(r'(\[.*?\])\(([^)]*?\.md(?:#[^)]*)?)\)')


def rewrite_md_links(content: str, *, target_domain: str = TARGET_DOMAIN, on_fix=None) -> tuple[str, int]:
    """Rewrite internal `.md` links in a Markdown string to `.html`, in memory.

    This is the core, side-effect-free transform: it takes a string of
    Markdown source and returns `(new_content, links_fixed_count)`. It does
    NOT touch the filesystem -- callers decide what to do with the result
    (write it back to disk, or -- as `core.Builder` does -- convert it to
    HTML immediately after).

    Args:
        content: Markdown source text.
        target_domain: Absolute links to this domain are also rewritten,
            in addition to any relative/internal link.
        on_fix: Optional callback `(old_url, new_url) -> None`, invoked for
            every link that gets rewritten. Leave as `None` for silent
            operation (used during normal builds).

    Returns:
        Tuple of (possibly modified content, number of links fixed).
    """

    def replacer(match: re.Match) -> str:
        text_part = match.group(1)
        url_part = match.group(2)

        # Extract just the URL base without the anchor for domain checking
        url_base = url_part.split('#')[0]

        # Guardrail: only touch an internal relative link OR one that
        # explicitly matches our own target domain. Third-party `.md`
        # links (e.g. a link to a README on GitHub) are left untouched.
        is_internal = not url_base.startswith("http")
        is_target_domain = target_domain in url_base

        if not (is_internal or is_target_domain):
            return match.group(0)

        # Replace only the first '.md' occurrence, keeping any anchor intact
        new_url = url_part.replace(".md", ".html", 1)

        if on_fix:
            on_fix(url_part, new_url)

        return f"{text_part}({new_url})"

    return _MD_LINK_PATTERN.subn(replacer, content)


def fix_md_to_html_in_file(md_file: Path, apply: bool = False) -> int:
    """Scans a single markdown file and replaces targeted .md links with .html in its content."""
    if not md_file.exists():
        return 0

    content = md_file.read_text(encoding="utf-8")

    prefix = "✅ Fixed" if apply else "🔍 [DRY RUN] Would fix"

    def _log(old_url: str, new_url: str) -> None:
        print(f"{prefix} in {md_file.name}: '{old_url}' ➔ '{new_url}'")

    new_content, count = rewrite_md_links(content, on_fix=_log)

    if apply and count > 0:
        md_file.write_text(new_content, encoding="utf-8")

    return count


def run_fixer(apply: bool = False, **kwargs):
    """Main execution block to recursively scan the docs folder (standalone/manual use)."""
    if not DOCS_DIR.exists() or not DOCS_DIR.is_dir():
        print("❌ Fatal Error: 'docs/' directory not found. Must be executed from the project root.")
        return

    print(f"\n--- SmartGen Docs Contextual Link Fixer (Apply Mode: {apply}) ---\n")

    total_fixed = 0

    for md_file in DOCS_DIR.rglob("*.md"):
        fixed_in_file = fix_md_to_html_in_file(md_file, apply=apply)
        total_fixed += fixed_in_file

    print(f"\nSummary: {total_fixed} contextual '.md' links processed and converted to '.html'.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SmartGen Docs Auto Link Fixer")
    parser.add_argument("--apply", action="store_true", help="Apply changes directly to .md files")
    args = parser.parse_args()

    run_fixer(apply=args.apply)
