<div align="center">

# SmartGen Docs

**A zero-dependency, Python-native static site generator for documentation — Markdown in, a fast, SEO-ready static site out.**

[![Live Docs](https://img.shields.io/badge/docs-live-4A3AE3?style=flat-square)](https://docs.smartgentools.com)
[![PyPI ready](https://img.shields.io/badge/install-pip-C2660D?style=flat-square)](#installation)
[![License: MIT](https://img.shields.io/badge/license-MIT-0B8F6B?style=flat-square)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-4A3AE3?style=flat-square)](requirements.txt)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-C2660D?style=flat-square)](docs/community/contributing.md)

[**Live Documentation**](https://docs.smartgentools.com) · [Quick Start](#quick-start) · [Roadmap](docs/resources/roadmap.md) · [Sponsor](docs/community/sponsor.md) · [Report an Issue](https://github.com/bayeziddev/smartGenDocs/issues)

</div>

---
<<report-linkready>>
🚨 **Alert:** The `report html` has been updated with the latest broken link scan results!
<<<<report-linkready >>

---
## What is SmartGen Docs?
# Multi-theme system for SmartGen Docs
New update 4 theme [README_START_HERE.md](README_START_HERE.md)
**Repo:** `bayeziddev/smartGenDocs`
**Files touched:** `smartgen_docs/themes/default/static/css/premium.css`, `smartgen_docs/themes/default/base_premium.html`, `smartgen.yml`, `docs/guides/theming.md` (new), plus 11 pre-existing broken-link fixes across `docs/*.md`.

Everything below was built with zero third-party CSS/JS — no theming library, no icon font, no CDN script. Same approach the project already uses.

## What you get

**Four themes** — Light (existing), Dark (existing, unchanged visually), and two new ones:
- **Sepia** — warm, low-glare paper tone for long reading sessions.
- **High Contrast** — pure black/white dark theme with flat 1px outlines instead of soft shadows, aimed at readers who need stronger contrast rather than a decorative dark mode.

**A real switcher**, not just a toggle — the moon/sun icon (top right) now opens a small keyboard-accessible menu (arrow keys, Enter, Escape) with all four themes, a preview swatch, and a checkmark on the active one.

**No flash of the wrong theme.** A tiny inline script at the very top of `<head>` reads the reader's saved choice (or their OS's `prefers-color-scheme` on a first visit) and sets it before anything else loads.

**Everything is CSS custom properties.** Each theme is one block in `premium.css` (`:root[data-theme="sepia"] { --bg-primary: ...; }` etc.) redefining the same ~25 tokens the whole site is already built on — adding a 5th theme is copy a block, add one line to a JS array, done. Full walkthrough with a worked example in `docs/guides/theming.md`.

**A brand-color override still works.** If `smartgen.yml` sets `theme.palette.primary`/`accent`, that now applies across all 4 themes consistently (previously it only worked because there was only one light + one dark palette to override).

## A bug I fixed along the way

While wiring up the switcher I found — and fixed — a real, pre-existing bug in the same file: the Previous/Next page navigation at the bottom of every page picks the "active" sidebar link by matching the URL's filename only. Since every section has its own `index.html` (`api/index.html`, `about/index.html`, ...), on any section-overview page ALL of them matched at once, and Previous/Next silently showed the wrong neighbors. I verified this with a real headless-browser render before and after — see the API audit report for the before/after on `api/index.html` specifically. The fix (`updateActiveNav()` in `base_premium.html`) now compares fully-resolved page paths instead of filenames.

## A pre-existing documentation problem I found and fixed

`docs/guides/theming.md` already existed in your repo (tracked in `origin/main`), but it was never in `smartgen.yml`'s `nav`, so it was never built — which is why `https://docs.smartgentools.com/guides/theming.html` 404s on the live site today. More importantly, its *content* described a theming system that doesn't exist in this codebase at all: `extra_css`/`extra_javascript` config, a `custom_dir` template-override mechanism, Font Awesome icon config, an `analytics.provider` block, and an MkDocs-Material-style `palette` array with `toggle: { icon: material/weather-sunny }`. None of that is implemented anywhere in `smartgen_docs/core.py` — it looks like leftover placeholder content from an earlier pass that documented a different tool's config format rather than this one, and it directly contradicts the project's own "zero third-party" positioning by describing a Font-Awesome/Google-Fonts-style setup. I replaced it with documentation of the theme system that's actually in this codebase, and added it to `smartgen.yml`'s nav so it actually gets built and is reachable.

## Also included: the still-outstanding link fixes from the last round

11 of the content-level link fixes from the previous broken-link audit hadn't been applied yet (only the generator-level `.md`→`.html` code fix was merged) — I reapplied them here so this patch is a complete, one-shot fix: `Sponsor Us`, both SDK reference links, the marketing-page "Guides" link, both `Deployment Guide` cross-references, the `Changelog` link, the homepage `Installation` link, and the doubled-path `Quick Start` link. I also fixed a handful of new ones I found while writing the theming guide: two dead-end references to a nonexistent `extra_javascript` feature, and four references to the still-missing CLI Reference / Autodoc Guide pages — those two guides genuinely don't exist yet (real content gap, not a link bug), so I pointed them at the closest real content instead (`docs/features.html`'s CLI and Autodoc sections) rather than leaving them 404.

## How to apply

```bash
cd smartGenDocs
git checkout -b feature/multi-theme-system
git apply theme-system-and-fixes.patch
```

Or copy the 4 standalone files in this delivery directly over their counterparts in your repo:
- `base_premium.html` → `smartgen_docs/themes/default/base_premium.html`
- `premium.css` → `smartgen_docs/themes/default/static/css/premium.css`
- `theming.md` → `docs/guides/theming.md`
- `smartgen.yml` → repo root (only adds one `Theming:` nav line — diff it against yours first if you've made other nav changes since)

Then rebuild (`smartgen-docs build`) and check the palette icon in the header.

## Verified

I built the site locally with all of this applied and confirmed, via a real headless-browser render (not just static HTML inspection):
- All 4 themes apply correctly, persist across reloads via `localStorage`, and respect OS preference on first visit.
- All 25 code blocks across the site stay properly Pygments-highlighted and readable in every theme, including computed-color contrast checks on the High Contrast theme specifically.
- The Previous/Next nav bug is fixed on `api/index.html` and confirmed unaffected on every other page.
- Zero `.md` hrefs remain anywhere in the built output.

