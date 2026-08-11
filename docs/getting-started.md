# Getting Started with SmartGen Docs

Welcome to **SmartGen Docs**, a Python-native static documentation generator for creating fast, responsive, and SEO-ready documentation sites from Markdown and `smartgen.yml`.

## 1. Install the package

Install the published package from PyPI:

```bash
pip install smartgen-docs
```

For the complete optional feature set, including development and screenshot tooling:

```bash
pip install "smartgen-docs[full]"
python -m playwright install chromium
```

SmartGen Docs supports Python 3.9 and newer.

## 2. Initialize a project

Create a new project folder, enter it, and initialize the starter structure:

```bash
mkdir my-docs
cd my-docs
smartgen-docs init
```

The initializer creates `smartgen.yml`, a `docs/` directory, and a starter Markdown homepage.

## 3. Configure `smartgen.yml`

Open `smartgen.yml` and update the site metadata, theme, palette, and navigation:

```yaml
site_name: My SmartGen Docs
site_url: https://example.com/docs/
site_author: Your Name
site_description: A clear description of your documentation site.

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
      - Installation: getting-started/installation.md
```

The `theme.name` value controls the primary site layout. The seven supported structural theme names are `default`, `book`, `education`, `techblog`, `agency`, `medicine`, and `apiplay`.

## 4. Write Markdown content

Create Markdown files under `docs/`. The paths in `nav` are relative to that directory:

```text
docs/
├── index.md
└── getting-started/
    └── installation.md
```

Use standard Markdown headings, links, code blocks, tables, and lists. Internal links written with `.md` are contextualized to generated `.html` paths during the build.

## 5. Preview locally

Start the development server while editing content:

```bash
smartgen-docs serve --port 8000
```

Open `http://localhost:8000` in your browser. The server watches the project and refreshes the generated site as files change.

## 6. Build for production

Generate the deployable static artifact:

```bash
smartgen-docs build
```

The output is written to `site/`. It includes HTML pages, theme assets, `sitemap.xml`, `robots.txt`, and `.nojekyll` when configured for GitHub Pages.

## 7. Generate every theme variant

For the live Styles switcher, run the repository helper from a SmartGen Docs source checkout:

```bash
python3 build_all_themes.py
```

This builds the configured root theme and all seven variants under `site/styles/`.

## 8. Publish with GitHub Pages

Commit `smartgen.yml`, `docs/`, and the source project to GitHub. The repository workflow builds the static artifact and deploys it to GitHub Pages on pushes to `main`. Configure the repository Pages source as **GitHub Actions** and set the matching `site_url` in `smartgen.yml`.

## 9. Next steps

Read the [main README](../README.md) for the full CLI reference and architecture guide. For automated package releases, see [`PUBLISHING.md`](../PUBLISHING.md).
