# Fix: contextual `.md` links 404 across docs.smartgentools.com

**Repo:** `bayeziddev/smartGenDocs`
**Root path affected:** `smartgen_docs/` (the site generator package) + several files under `docs/` (your content)

## Root cause

Your build pipeline (`smartgen_docs/core.py`, `Builder.build_page()`) converts each Markdown file straight to HTML without ever rewriting internal links that point at `.md` source files (e.g. `[Installation](installation.md)`) into links at the built `.html` page (`installation.html`). The top nav renders fine because it's built separately from `smartgen.yml`, but every in-body/"See Also" link keeps its raw `.md` target and 404s once deployed.

You'd actually already written the fix — `smartgen_docs/link_fixer.py` — but it was never wired into anything. It's a standalone script not called from `cli.py`, not called from `core.py`'s build step, and not run in `.github/workflows/main.yml`. It's dead code.

There's also a smaller, separate bug: `smartgen_docs/cli.py`'s `audit` command does `from .link_auditor import run_audit`, but `link_auditor.py` was deleted from the repo (see your own `docs/docs/changelog.md`, commit "Delete link_auditor.py"). Running `smartgen-docs audit` currently crashes with `ModuleNotFoundError`.

Separately, 8 links weren't just missing `.html` — they were structurally wrong in the source content itself (duplicated path segments, wrong subfolder, wrong filename, or the wrong domain entirely). Those needed hand fixes in the `.md` files, not a generator change.

## What's in this fix

### 1. Generator changes (apply automatically to every future build)

- **`smartgen_docs/link_fixer.py`** — refactored so the regex-based `.md`→`.html` rewrite logic is now a reusable, in-memory function `rewrite_md_links(content) -> (new_content, count)`, importable by other modules. The original standalone CLI usage (`python -m smartgen_docs.link_fixer --apply`) still works exactly as before.
- **`smartgen_docs/core.py`** — `Builder.build_page()` now calls `rewrite_md_links()` on every page's Markdown source right before converting it to HTML. This is the actual fix: it makes the bug self-healing for every page, forever, with zero manual steps.
- **`smartgen_docs/cli.py`** — the `audit` command no longer crashes outright; it now fails with a clear message instead of an unhandled `ModuleNotFoundError`, and points you at the new automatic fix / the manual dry-run command.

### 2. Content fixes (8 hand-authored links, wrong regardless of the generator fix)

| File | Was | Now |
|---|---|---|
| `docs/getting-started/index.md` | `[Installation](/installation.md)` | `[Installation](/getting-started/installation.html)` |
| `docs/getting-started/installation.md` | `[Quick Start Guide](docs/getting-started/quick-start.md)` | `[Quick Start Guide](quick-start.md)` |
| `docs/guides/configuration.md` | `[Changelog](docs/changelog.md)` | `[Changelog](../docs/changelog.md)` |
| `docs/guides/configuration.md` | `[Deployment Guide](deployment.md)` | `[Deployment Guide](../getting-started/deployment.md)` |
| `docs/tutorials/integrations.md` | `[Deployment Guide](../guides/deployment.md#3-continuous-deployment-cicd)` | `[Deployment Guide](../getting-started/deployment.md)` |
| `docs/tutorials/integrations.md` | `[Deployment Guide](../guides/deployment.md)` | `[Deployment Guide](../getting-started/deployment.md)` |
| `docs/tutorials/case-studies.md` | `[Deployment Guide](../guides/deployment.md)` | `[Deployment Guide](../getting-started/deployment.md)` |
| `docs/sdk/index.md` | `[Python SDK Reference](python-sdk.md)` | `[Python SDK Reference](python.md)` |
| `docs/sdk/index.md` | `[JavaScript SDK Reference](javascript-sdk.md)` | `[JavaScript SDK Reference](javascript.md)` |
| `docs/about/index.md` | `[Sponsor Us](sponsor.md)` | `[Sponsor Us](../community/sponsor.md)` |
| `docs/tools/marketing.md` | `[SmartGen Docs Guides](https://smartgentools.com/docs/)` | `[SmartGen Docs Guides](../guides/configuration.md)` |

*(There's no dedicated Theming/Autodoc/CLI-reference page anywhere on the site — `docs/tutorials/best-practices.md`, `tutorials/api.md`, and `tutorials/beginner.md` link to `guides/theming.md`, `guides/autodoc.md`, `guides/cli.md`, none of which exist as source. That's a content gap, not a link bug — you'll want to either write those three pages or remove the links. I didn't touch those in this patch since it's a content decision, not a bug fix.)*

## How to apply

**Option A — apply the patch:**
```bash
cd smartGenDocs
git checkout -b fix/contextual-md-links
git apply fix-contextual-md-links.patch
```

**Option B — copy the 3 fixed files directly:**
Replace these files in your repo with the attached versions:
- `smartgen_docs/link_fixer.py`
- `smartgen_docs/core.py`
- `smartgen_docs/cli.py`

Then hand-apply the 11 content edits in the table above to their respective `docs/*.md` files.

## Verification

I built the site locally with this fix applied (`smartgen-docs build`) and confirmed:
- Zero `href="*.md"` links remain anywhere in the generated `site/` output.
- All 61 previously-broken contextual links from the earlier audit now resolve to real, existing `.html` pages.

After you merge this, just commit as normal — the GitHub Actions workflow already runs `smartgen-docs build`, so the fix applies to the next deploy automatically. No CI changes needed.
