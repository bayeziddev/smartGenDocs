# Developer Tutorials & Step-by-Step Guides

Welcome to the **Tutorials** channel of SmartGen Docs. This section provides comprehensive, actionable walkthroughs designed to help you master every aspect of the SmartGen platform, from initial project scaffolding to advanced theme creation and automated CI/CD deployments.

## Tutorial 1: Initializing Your First Documentation Project

Getting started with SmartGen Docs takes less than a minute. By combining Python's robust packaging ecosystem with a clean command-line interface, you can spin up a fully searchable, SEO-ready documentation site without writing boilerplate HTML or configuring complex bundlers.

To initialize your project, install the package and run the initialization command in your target directory:

```bash
pip install smartgen-docs
smartgen-docs init
```

The initialization command generates a default `smartgen.yml` configuration file along with a starting set of Markdown documentation files under `docs/`. You can immediately preview your site locally by running the built-in development server with live reload enabled [1]:

```bash
smartgen-docs serve --port 8000
```

When you edit any Markdown file under `docs/`, the development server updates the output in real-time, allowing you to iterate rapidly on your content.

## Tutorial 2: Creating a Custom Structural Theme

SmartGen Docs allows developers to craft bespoke layouts by implementing custom structural themes. Unlike color mode toggles that merely adjust CSS variables, structural themes redefine the underlying HTML markup, navigation structure, and typography of your site [2].

To create a new theme named `enterprise`, set up the following directory structure inside your project or package installation under `smartgen_docs/themes/enterprise/`:

```text
smartgen_docs/themes/enterprise/
├── base.html                 # Master HTML layout skeleton
├── page.html                 # Content rendering wrapper
└── static/
    └── css/
        └── enterprise.css    # Isolated theme design tokens and styles
```

Your `base.html` can include shared partials from `_shared/` such as the pre-paint script, active navigation script, and the live style switcher. Once created, simply reference `name: enterprise` in your `smartgen.yml` configuration, and the theme engine will automatically compile it [3].

## Tutorial 3: Automating CI/CD and Multi-Theme Builds

Deploying a multi-theme documentation site requires building both the primary site root and all alternate style variants into isolated subdirectories. SmartGen Docs accomplishes this through a custom build script (`build_all_themes.py`) and a native GitHub Actions workflow (`.github/workflows/main.yml`) [4].

When you push updates to your repository, the GitHub Actions runner installs dependencies, executes the multi-theme build script, generates sitemap and robots files, touches the `.nojekyll` flag to prevent Jekyll interference, and deploys the resulting artifact directly to GitHub Pages [5].

## References

- [1] Local Development Server. [SmartGen CLI Guide](https://docs.smartgentools.com/guides/cli.html).
- [2] Theme System Architecture. [SmartGen Theming Guide](https://docs.smartgentools.com/guides/theming.html).
- [3] Configuration Reference. [SmartGen Configuration Guide](https://docs.smartgentools.com/guides/configuration.md).
- [4] Multi-Theme Build Script. [SmartGen GitHub Repository](https://github.com/bayeziddev/smartGenDocs).
- [5] GitHub Pages Deployment. [SmartGen Deployment Guide](https://docs.smartgentools.com/getting-started/deployment.html).
