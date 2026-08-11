# SmartGen Docs

[![PyPI version](https://img.shields.io/pypi/v/smartgen-docs.svg)](https://pypi.org/project/smartgen-docs/)
[![CI Status](https://github.com/bayeziddev/smartGenDocs/actions/workflows/main.yml/badge.svg)](https://github.com/bayeziddev/smartGenDocs/actions/workflows/main.yml)
[![Publish Status](https://github.com/bayeziddev/smartGenDocs/actions/workflows/publish.yml/badge.svg)](https://github.com/bayeziddev/smartGenDocs/actions/workflows/publish.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**SmartGen Docs** is a Python-native static documentation generator. It converts Markdown content and a YAML configuration into a fast, SEO-ready, responsive documentation website with multiple layouts, color modes, navigation, syntax highlighting, sitemap generation, and GitHub Pages deployment support.

[![Live Documentation](https://img.shields.io/badge/docs-live-4A3AE3?style=flat-square)](https://docs.smartgentools.com/)
[![Python](https://img.shields.io/badge/python-3.9%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-0B8F6B?style=flat-square)](LICENSE)
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/bayeziddev/smartGenDocs/main.yml?branch=main&style=flat-square&label=build)](https://github.com/bayeziddev/smartGenDocs/actions/workflows/main.yml)

**Project links:** [Live Documentation](https://docs.smartgentools.com/) · [GitHub Repository](https://github.com/bayeziddev/smartGenDocs) · [Issue Tracker](https://github.com/bayeziddev/smartGenDocs/issues) · [SmartGen Tools](https://www.smartgentools.com)

> **Important:** SmartGen Docs generates a static site. The generated `site/` directory is the deployable artifact; it does not require a database, server-side runtime, or JavaScript framework in production.

## Features

| Area | Included capability |
|---|---|
| Content | Markdown-to-HTML conversion, nested documentation folders, front matter-compatible content, code blocks, tables, lists, links, and headings |
| Navigation | YAML-defined navigation, nested sections, breadcrumbs, active navigation state, previous/next page links, and page progress data |
| Themes | Seven structural themes: Premium/Default, Book, Education, Tech Blog, Agency, Medicine, and API Playground |
| Live style switching | A floating **Styles** button that switches between the seven complete site designs while preserving the current page |
| Color modes | Theme-specific light/dark or day/night palettes, with pre-paint handling to reduce flashes of the wrong color mode |
| Styling | Theme-scoped CSS assets, shared Jinja partials, configurable primary and accent colors, responsive layouts, and reduced-motion support where provided by a theme |
| SEO | Canonical URLs, site metadata, custom-domain support, generated `sitemap.xml`, generated `robots.txt`, and `.nojekyll` output |
| Links | Contextual rewriting of internal Markdown `.md` links to generated `.html` links |
| Code quality | Pygments syntax highlighting and a local build process suitable for CI validation |
| Development | Local server with live reload, project scaffolding, API documentation generation, changelog rendering, and an upload manager |
| Deployment | GitHub Actions build and GitHub Pages deployment with all theme variants emitted under `site/styles/<theme>` |
| Verification | Playwright-based responsive screenshots and automated checks for the Styles menu and same-page theme navigation |
| Extensibility | Shared theme loaders, optional search, image, minification, and development dependency groups, plus plugin entry points in project metadata |

## Requirements

SmartGen Docs supports **Python 3.9 or newer**. Git is recommended for version control. Playwright and a browser are only required when running the screenshot verification guide.

## Installation

You can install SmartGen Docs directly from PyPI using pip:

```bash
pip install smartgen-docs
```

Or install with optional feature extras (such as search, image support, minification, and development tools):

```bash
pip install "smartgen-docs[search,images,minify,dev]"
```

If you are contributing to the source code or running from a local clone:

```bash
git clone https://github.com/bayeziddev/smartGenDocs.git
cd smartGenDocs
python -m pip install -e .
```

The available extras are:

| Extra | Purpose |
|---|---|
| `search` | Search-related dependencies such as Whoosh |
| `images` | Image processing support through Pillow |
| `minify` | HTML, CSS, and JavaScript minification dependencies |
| `dev` | Testing, formatting, linting, packaging, and publishing tools |
| `screenshots` | Playwright for browser screenshots and UI verification |
| `full` | The complete optional feature set, including screenshots |

## Quick start

If you are starting a new documentation project, initialize a configuration and content skeleton:

```bash
smartgen-docs init
```

Build the static site into `site/`:

```bash
smartgen-docs build
```

Start the local development server with live reload:

```bash
smartgen-docs serve
```

The default development server runs at `http://localhost:8000`. To use a different port:

```bash
smartgen-docs serve --port 8080
```

The generated output can also be served by any static web server:

```bash
python -m http.server 8000 --directory site
```

## Configuration

The primary configuration file is `smartgen.yml`. The current project uses the Book theme as its root layout and builds every listed style variant for the live switcher.

```yaml
site_name: SmartGen Docs
site_url: https://docs.smartgentools.com/
site_author: Sayad Md Bayezid Hosan
site_description: SmartGen Platform Documentation

repo_name: bayeziddev/smartGenDocs
repo_url: https://github.com/bayeziddev/smartGenDocs

theme:
  name: book
  palette:
    primary: "#4A3AE3"
    accent: "#C2660D"

style_switcher:
  enabled: true
  variants:
    - default
    - book
    - education
    - techblog
    - agency
    - medicine
    - apiplay

nav:
  - Home: index.md
  - Getting Started:
      - Welcome: getting-started/index.md
      - Installation: getting-started/installation.md
```

The `site_url` value must be the exact public base URL, including the trailing slash if that is how the project convention is written. It is used for canonical links, the sitemap, `robots.txt`, and custom-domain handling. The `theme.name` value determines the theme rendered at the site root. The `style_switcher.variants` list determines which complete theme trees are generated under `site/styles/` during the multi-theme build.

## Documentation content and navigation

Markdown files live under `docs/`. Navigation paths are relative to that directory. A nested navigation section becomes a nested directory in the generated site:

```yaml
nav:
  - Home: index.md
  - API Reference:
      - Overview: api/index.md
      - Authentication: api/authentication.md
      - Endpoints: api/endpoints.md
```

This produces paths such as `site/index.html`, `site/api/index.html`, `site/api/authentication.html`, and `site/api/endpoints.html`. Internal Markdown links are rewritten from `.md` to the corresponding generated `.html` path during the build.

## Theme system

SmartGen Docs has two separate theming layers.

**Structural themes** change the entire site layout and visual language. The available structural themes are shown below:

| Theme name | Description |
|---|---|
| `default` | Premium/Original SmartGen Docs layout |
| `book` | Reading-first documentation with a focused, book-like layout |
| `education` | Course and lesson-oriented documentation layout |
| `techblog` | Editorial and magazine-inspired documentation layout |
| `agency` | Service portal with client-facing presentation patterns |
| `medicine` | Clinical reference and print-oriented documentation layout |
| `apiplay` | Utility/API playground with terminal-style presentation |

**Color modes** are handled inside individual themes through shared pre-paint and theme-switcher partials. A structural theme can expose modes such as Light/Dark or Day/Night without changing the selected structural theme.

A theme directory normally contains a content template, a base layout, and its static assets:

```text
smartgen_docs/themes/<theme-name>/
├── base.html
├── page.html
└── static/
    └── css/
        └── <theme-name>.css
```

Shared partials are stored under `smartgen_docs/themes/_shared/partials/`. They include navigation behavior, color-mode behavior, and the live structural style switcher.

## The live Styles switcher

The live switcher is different from the light/dark color-mode control. It exposes the complete structural themes in a floating **Styles** button. When a visitor selects a theme, the browser navigates to the same page inside the selected theme tree.

The workflow builds the primary theme at the root and builds every configured variant under the following pattern:

```text
site/
├── index.html                         # configured primary theme
├── getting-started/index.html         # configured primary theme
└── styles/
    ├── default/index.html
    ├── book/index.html
    ├── education/index.html
    ├── techblog/index.html
    ├── agency/index.html
    ├── medicine/index.html
    └── apiplay/index.html
```

The shared switcher partial calculates the current page path and preserves that path when changing styles. For example, a visitor on `getting-started/index.html` can switch to Medicine and arrive at `styles/medicine/getting-started/index.html` rather than being sent to the Medicine homepage.

## SEO files and sitemap

Every build now writes the SEO support files directly into the generated artifact:

```text
site/sitemap.xml
site/robots.txt
site/.nojekyll
site/CNAME                 # generated for a non-github.io site_url
```

The generated sitemap is a valid XML document containing the HTML pages discovered in the built site, with absolute URLs based on `site_url`, modification dates, change frequencies, and priorities. The generated `robots.txt` permits indexing and points crawlers to the public sitemap URL.

A sitemap should be opened as XML or downloaded by a browser. If a browser displays a blank document, validate the file rather than treating the browser rendering as the source of truth:

```bash
python -c "import xml.etree.ElementTree as ET; ET.parse('site/sitemap.xml'); print('sitemap is valid XML')"
```

For the public project, the expected sitemap URL is [https://docs.smartgentools.com/sitemap.xml](https://docs.smartgentools.com/sitemap.xml).

## Playwright screenshots and responsive verification

The repository includes `tools/capture_screenshots.py`. It verifies that the Styles button exists, checks that all seven theme options render on desktop and mobile, captures screenshots, and confirms that switching to Medicine preserves the current documentation page.

Install Playwright through the project extra:

```bash
python -m pip install -e ".[screenshots]"
python -m playwright install chromium
```

Build the complete multi-theme site and start a local server:

```bash
python3 build_all_themes.py
python -m http.server 8000 --directory site
```

In another terminal, run the screenshot verification script:

```bash
python tools/capture_screenshots.py \
  --base-url http://127.0.0.1:8000 \
  --output screenshots
```

The script captures three desktop pages and one mobile page. It writes images such as:

```text
screenshots/
├── desktop-index.html.png
├── desktop-index.html-menu.png
├── desktop-getting-started-index.html.png
├── desktop-getting-started-index.html-menu.png
├── desktop-docs-index.html.png
├── desktop-docs-index.html-menu.png
├── mobile-getting-started.png
└── mobile-getting-started-menu.png
```

The exact filenames are based on the page path passed by the script. The test fails if the switcher is absent, if the menu does not contain all seven themes, or if the same-page navigation target is incorrect.

To test a deployed site instead of the local build, pass the public URL:

```bash
python tools/capture_screenshots.py \
  --base-url https://docs.smartgentools.com \
  --output screenshots-live
```

## Command-line reference

| Command | Purpose |
|---|---|
| `smartgen-docs init` | Create a starter `smartgen.yml` and initial documentation structure |
| `smartgen-docs build` | Build the configured theme into `site/` |
| `smartgen-docs build --config custom.yml --site-dir public` | Build with a custom configuration and output directory |
| `smartgen-docs serve` | Run the development server with live reload |
| `smartgen-docs serve --port 8080` | Run the development server on a custom port |
| `smartgen-docs scaffold` | Generate missing content files and folders from navigation configuration |
| `smartgen-docs autodoc MODULE` | Generate API reference documentation for a Python module |
| `smartgen-docs autodoc MODULE --output docs/api` | Write API documentation to a custom directory |
| `smartgen-docs render-changelog` | Convert `data/changelog.json` into Markdown documentation |
| `smartgen-docs upload-manager` | Start the optional browser-based upload and management interface |

The command aliases `smartgen` and `smartgen-docs` are both installed by the package.

## GitHub Actions deployment

The repository workflow is `.github/workflows/main.yml`. On pushes to `main`, it performs the following sequence:

1. Checks out the repository and installs Python dependencies.
2. Validates the configuration, documentation directory, and Markdown file count.
3. Runs `build_all_themes.py` to build the configured root theme and all style variants.
4. Verifies the `site/` artifact and `.nojekyll` marker.
5. Uploads the artifact with `actions/upload-pages-artifact`.
6. Deploys it with `actions/deploy-pages`.
7. Writes a workflow summary to the Actions run page.

For GitHub Pages deployment, enable **GitHub Actions** as the Pages source in repository settings. The workflow requires `pages: write` and `id-token: write` permissions. If a custom domain is configured through `site_url`, the builder writes a matching `CNAME` file into the artifact.

## Project structure

```text
smartGenDocs/
├── .github/workflows/main.yml       # CI, multi-theme build, and Pages deployment
├── build_all_themes.py              # Builds root and alternate theme trees
├── data/changelog.json              # Changelog source data
├── docs/                            # Markdown documentation content
├── robots.txt                       # Source crawler policy reference
├── sitemap.xml                      # Source sitemap reference; generated output is site/sitemap.xml
├── smartgen.yml                     # Project configuration and navigation
├── smartgen_docs/
│   ├── cli.py                       # Command-line interface
│   ├── core.py                      # Markdown build engine and SEO files
│   ├── converter.py                 # Markdown conversion and highlighting
│   ├── link_fixer.py                # Internal Markdown-link rewriting
│   ├── path_resolver.py             # Nested-page and asset URL resolution
│   ├── theme_engine.py              # Theme discovery and template loading
│   └── themes/                      # Structural themes and shared partials
├── tools/capture_screenshots.py     # Playwright screenshot and UI verification
└── site/                            # Generated static output; not hand-edited
```

## Troubleshooting

| Symptom | Check |
|---|---|
| `sitemap.xml` appears blank or invalid | Confirm that the deployed file is `site/sitemap.xml`, rebuild the site, and validate it with `xml.etree.ElementTree` or an XML validator |
| Styles button is missing | Confirm that the active theme includes both `style_switcher.html` and `style_switcher_script.html`, then rebuild all themes with `python3 build_all_themes.py` |
| A style option opens the wrong page | Confirm that the target page exists under `site/styles/<theme>/` and that the site is served from the configured root URL |
| GitHub Actions fails during validation | Inspect the failed step first; YAML shell blocks must use ordinary `${{ ... }}` expressions and valid Bash syntax |
| Custom-domain links are wrong | Set `site_url` to the exact public URL and ensure Pages is configured for the same domain |
| Playwright cannot launch Chromium | Run `python -m playwright install chromium` after installing the `screenshots` extra |
| Local pages show stale content | Delete `site/`, rebuild, and hard-refresh the browser; generated output should not be manually edited |
| A page is missing | Confirm the Markdown file exists under `docs/` and that it is included in `smartgen.yml` navigation |

## Contributing

Create a feature branch, make a focused change, build the documentation locally, and run the screenshot verification when modifying themes or the style switcher:

```bash
git checkout -b feature/my-change
python -m pip install -e ".[dev,screenshots]"
python3 build_all_themes.py
python tools/capture_screenshots.py
```

Open a pull request with a concise description of the change and include screenshots when the visual output changes. Documentation content should use clear headings, descriptive links, accessible text, and valid code examples.

## License

SmartGen Docs is released under the [MIT License](LICENSE). Copyright © 2026 Sayad Md Bayezid Hosan.

## Support

For bugs and feature requests, use the [GitHub issue tracker](https://github.com/bayeziddev/smartGenDocs/issues). For project and platform information, visit [SmartGen Tools](https://www.smartgentools.com).


## Hosting & Deployment

SmartGen Docs provides flexible hosting options:
1. **Manus Cloud Builder Preview**: Instantly available at [Cloud Builder Demo](https://smartgen-doc-ljotzzbw.manus.space) with live theme switching and configuration tools.
2. **GitHub Pages (Free Custom Domains)**: For production docs requiring custom domains without paid upgrades, build your site with `smartgen-docs build` and deploy the generated `site/` folder to GitHub Pages.
