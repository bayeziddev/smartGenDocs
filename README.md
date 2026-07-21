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

## What is SmartGen Docs?

**SmartGen Docs** is an open-source **Python static site generator** built specifically for **project documentation**. It's a `pip install`-able alternative in the same space as MkDocs and Sphinx, with three deliberate differences:

- **Zero third-party front-end dependency.** No icon fonts, no UI framework, no CDN calls. Every pixel in the default theme is hand-authored CSS and inline SVG. Code syntax highlighting runs server-side through **Pygments** at build time — highlighted code even with JavaScript disabled.
- **One toolchain, one config file.** `smartgen-docs init / serve / build` covers scaffolding, a live-reload dev server, and static output. Navigation, theme palette, and site metadata all live in a single `smartgen.yml`.
- **Markdown-first, no lock-in.** Every page is a plain `.md` file with YAML front matter. Your content isn't trapped in a proprietary format.

If you're searching for a **documentation generator**, a **markdown to HTML converter**, an **MkDocs alternative**, or a lightweight **docs-as-code** tool that deploys straight to **GitHub Pages**, this repo is built for exactly that.

---

## Table of Contents — Your A-to-Z Guide

| # | Section | What's there |
|---|---|---|
| A | [What is SmartGen Docs?](#what-is-smartgen-docs) | Project summary and philosophy |
| B | [Features](#features) | Full feature list |
| C | [Live Demo](#live-demo) | See it running |
| D | [Installation](#installation) | `pip install` and requirements |
| E | [Quick Start](#quick-start) | Your first project in 3 commands |
| F | [Project and Folder Structure](#project-and-folder-structure) | Where everything lives |
| G | [Configuration (`smartgen.yml`)](#configuration-smartgenyml) | Site metadata, nav, theme palette |
| H | [Writing Content](#writing-content) | Markdown conventions, front matter |
| I | [Theming and Customization](#theming-and-customization) | CSS tokens, light/dark mode |
| J | [CLI Reference](#cli-reference) | `init`, `serve`, `build` |
| K | [Deployment (GitHub Pages)](#deployment-github-pages) | Correct Pages setup, `.nojekyll`, `CNAME` |
| L | [SEO and Metadata](#seo-and-metadata) | Canonical URLs, Open Graph, sitemap |
| M | [Full Documentation](#full-documentation) | Every guide, tutorial, and reference page |
| N | [Roadmap](#roadmap) | Where the project is headed |
| O | [Contributing](#contributing) | How to open a PR |
| P | [Community](#community) | Discussions, issues, feature requests |
| Q | [Sponsor](#sponsor) | Support the project |
| R | [License](#license) | MIT |
| S | [Contact](#contact) | Direct contact details |

---

## Features

- 📝 **Markdown-centric** authoring with YAML front matter
- ⚙️ **Single YAML config** (`smartgen.yml`) for navigation, metadata, and theme palette
- 🔁 **Live-reload dev server** — edits appear instantly while you write
- 🎨 **Original, configurable theme** — no Material Design, no icon-font dependency
- 🌓 **Light/dark mode**, tuned for contrast in both
- 🖍️ **Server-side syntax highlighting** via Pygments — zero client-side highlighting JS
- 🔍 **Built-in client-side search**
- 🧭 **Collapsible sidebar navigation**, breadcrumbs, and previous/next page links
- 📱 **Fully responsive**, mobile-first layout
- 🚀 **GitHub Actions deploy workflow** included, ready for GitHub Pages
- 🔎 **SEO-ready out of the box** — per-page canonical URLs, Open Graph, Twitter Card meta

## Live Demo

The docs you're reading about are themselves built with SmartGen Docs:

**→ [docs.smartgentools.com](https://docs.smartgentools.com)**

## Installation

```bash
pip install -r requirements.txt
pip install -e .
```

Requires Python 3.9+. Core dependencies: `Jinja2`, `markdown2`, `PyYAML`, `Pygments`, `click`, `watchdog` — see [`requirements.txt`](requirements.txt) for the full list.

## Quick Start

```bash
# 1. Scaffold a new documentation project
smartgen-docs init my-docs
cd my-docs

# 2. Start the live-reload dev server
smartgen-docs serve

# 3. Build the static site for deployment
smartgen-docs build --config smartgen.yml --site-dir site
```

Your static site is now in `site/` — upload it anywhere, or see [Deployment](#deployment-github-pages) below for GitHub Pages.

## Project and Folder Structure

```
smartGenDocs/
├── smartgen.yml                    # Site config: nav, metadata, theme palette
├── docs/                           # All Markdown content lives here
│   ├── index.md                    # Homepage
│   ├── getting-started/            # Onboarding guides
│   ├── docs/                       # Core concepts & architecture
│   ├── guides/                     # Configuration, SEO, performance, security
│   ├── api/                        # API reference
│   ├── sdk/                        # Language SDKs
│   ├── tools/                      # SmartGen Tools documentation
│   ├── tutorials/                  # Step-by-step tutorials
│   ├── resources/                  # Roadmap, examples, glossary
│   ├── community/                  # Contributing, sponsor, issues
│   ├── blog/                       # Release notes & articles
│   └── about/                      # Project & license info
├── smartgen_docs/                  # The generator itself (Python package)
│   ├── core.py                     # Build pipeline
│   ├── cli.py                      # `smartgen-docs` command entry point
│   ├── converter.py                # Markdown → HTML (Pygments-highlighted)
│   ├── theme_engine.py             # Template loader
│   └── themes/default/             # The default theme
│       ├── base_premium.html       # Page shell: header, sidebar, footer
│       ├── page_premium.html       # Content wrapper
│       └── static/css/premium.css  # The entire visual design system
├── .github/workflows/main.yml      # CI: validate → build → deploy to Pages
└── site/                           # Build output (generated, not committed)
```

## Configuration (`smartgen.yml`)

Everything about a SmartGen Docs site is declared in one file:

```yaml
site_name: SmartGen Docs
site_url: https://docs.smartgentools.com/
site_author: Sayad Md Bayezid Hosan

theme:
  palette:
    primary: "#4A3AE3"
    accent: "#C2660D"

nav:
  - Home: index.md
  - Getting Started:
      - Welcome: getting-started/index.md
      - Quick Start: getting-started/quick-start.md
  # ...full tree in smartgen.yml
```

Change `theme.palette` to reskin the entire site without touching CSS. Change `nav` to restructure the whole sidebar.

## Writing Content

Every page is Markdown with YAML front matter:

```markdown
---
title: Page Title
---

# Page Title

Regular Markdown. Fenced code blocks are highlighted automatically:

\`\`\`python
def hello():
    print("SmartGen Docs")
\`\`\`
```

Add the page's path to `nav:` in `smartgen.yml` to make it appear in the sidebar — pages not listed in `nav` are not built.

## Theming and Customization

The entire look lives in [`smartgen_docs/themes/default/static/css/premium.css`](smartgen_docs/themes/default/static/css/premium.css) as CSS custom properties:

```css
:root {
  --color-primary: #4A3AE3;
  --color-accent: #C2660D;
  --font-sans: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

Override any token, or override `theme.palette` in `smartgen.yml` for primary/accent without touching CSS at all.

## CLI Reference

| Command | Description |
|---|---|
| `smartgen-docs init <name>` | Scaffold a new documentation project |
| `smartgen-docs serve` | Start the live-reload development server |
| `smartgen-docs build --config smartgen.yml --site-dir site` | Build the static site |

## Deployment (GitHub Pages)

This repo ships a complete CI/CD workflow at [`.github/workflows/main.yml`](.github/workflows/main.yml) that validates, builds, and deploys on every push to `main`.

**For this to work, your repo's Pages source must be set correctly:**

1. Go to **Settings → Pages**
2. Under **Build and deployment → Source**, select **"GitHub Actions"** — *not* "Deploy from a branch"

If Pages is left on "Deploy from a branch," GitHub will run its own Jekyll build over your repository in parallel with the Actions workflow, and whichever one "wins" can vary — this is what causes a raw `README.md`/Jekyll page to appear instead of your real site. The build now also writes `.nojekyll` and `CNAME` (from `site_url`) into every build automatically, so once the Source setting above is corrected, this shouldn't resurface.

## SEO and Metadata

Every built page includes:
- A unique, self-referencing `<link rel="canonical">`
- Open Graph (`og:title`, `og:description`, `og:url`) and Twitter Card meta, both page-specific
- A single `<h1>` per page and a clean heading hierarchy

## Full Documentation

The complete guide lives at **[docs.smartgentools.com](https://docs.smartgentools.com)**:

- [Getting Started](https://docs.smartgentools.com/getting-started/index.html) — installation, first project, deployment, FAQ
- [Documentation](https://docs.smartgentools.com/docs/index.html) — concepts, architecture, platform, release notes
- [Guides](https://docs.smartgentools.com/guides/configuration.html) — configuration, customization, SEO, performance, accessibility, security
- [API Reference](https://docs.smartgentools.com/api/index.html) — REST API, authentication, endpoints, webhooks
- [SDKs](https://docs.smartgentools.com/sdk/index.html) — Python, JavaScript, PHP, Go, Java
- [Tools](https://docs.smartgentools.com/tools/index.html) — the SmartGen Tools suite
- [Tutorials](https://docs.smartgentools.com/tutorials/index.html) — beginner to advanced walkthroughs

## Roadmap

Where the project stands today and what's next, kept honest and updated as things ship: **[docs/resources/roadmap.md](docs/resources/roadmap.md)**.

## Contributing

Contributions are welcome — see **[docs/community/contributing.md](docs/community/contributing.md)**.

- 🐛 [Report an issue](https://github.com/bayeziddev/smartGenDocs/issues)
- 💡 [Request a feature](docs/community/features.md)
- 💬 [Join discussions](docs/community/discussions.md)

## Community

- [Community Home](docs/community/index.md)
- [Discussions](docs/community/discussions.md)
- [Report an Issue](https://github.com/bayeziddev/smartGenDocs/issues)

## Sponsor

If SmartGen Docs saves you time, consider supporting development: **[docs/community/sponsor.md](docs/community/sponsor.md)**

PayPal, crypto (USDT/BEP20), bKash, Nagad, and international bank transfer are all listed there.

## License

MIT — see [LICENSE](LICENSE). Free to use, modify, and distribute, with attribution.

## Contact

Built and maintained by **Sayad Md Bayezid Hosan**.

- Business: [info@sayadbayezid.com](mailto:info@sayadbayezid.com)
- Support: [support@sayadbayezid.com](mailto:support@sayadbayezid.com)
- WhatsApp: [+880 1519-601517](https://wa.me/8801519601517)
- All verified profiles: [sayadbayezid.com/verified-profiles](https://sayadbayezid.com/verified-profiles/)

---

<div align="center">

**[⬆ back to top](#smartgen-docs)**

</div>
