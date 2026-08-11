# Platform Release Notes & Version History

Welcome to the **Release Notes** channel of SmartGen Docs. This document records all platform updates, new features, architectural improvements, and dependency upgrades.

## Automated Release Updates via GitHub Actions

SmartGen Docs features an automated changelog and release tracking workflow (`.github/workflows/changelog.yml`) [1]. Whenever a commit or pull request is merged to the `main` branch, the automation pipeline inspects the commit metadata, computes file statistics and code changes, updates `data/changelog.json`, and renders an SEO-optimized Markdown changelog at `docs/docs/changelog.md` before committing and pushing the changes back to the repository [2].

This ensures that your release documentation is perpetually synchronized with your codebase without requiring manual intervention from maintainers.

## Release v1.1.0 (Current Stable Release)

Released on August 12, 2026, version v1.1.0 introduces the comprehensive multi-theme engine and live style switcher.

### Major Features and Improvements

- **Seven Structural Themes**: Added full production support for `default`, `book`, `education`, `techblog`, `agency`, `medicine`, and `apiplay` themes [3].
- **Live Styles Switcher**: Implemented a floating, keyboard-accessible switcher button that allows visitors to preview the documentation across all seven layout variants instantly without losing their page position [4].
- **Automated Sitemap & Robots Generation**: Updated `smartgen_docs/core.py` to generate valid `sitemap.xml` and `robots.txt` files directly into the `site/` build directory [5].
- **Playwright Verification Suite**: Added a robust automated testing tool (`tools/capture_screenshots.py`) for responsive screenshot capture and navigation validation [6].

### Bug Fixes and Optimizations

- Resolved Jekyll build conflicts by adding `.nojekyll` generation to all site builds [7].
- Fixed a pre-existing navigation bug where section overview pages failed to highlight the correct active sidebar item [8].
- Optimized build time and static asset namespacing to prevent filename collisions across distinct themes [9].

## Release v1.0.0 (Initial Public Release)

Released on July 15, 2026, version v1.0.0 established the foundational Python-native static site generator.

### Core Capabilities

- Pure Python 3.9+ runtime with zero external JavaScript framework requirements.
- Markdown-to-HTML conversion with Pygments syntax highlighting and internal link rewriting [10].
- Flexible YAML-based project configuration (`smartgen.yml`) with nested navigation support [11].
- Native GitHub Actions workflow templates for CI validation and GitHub Pages deployment [12].

## References

- [1] SmartGen Changelog Workflow. [GitHub Repository Workflow](https://github.com/bayeziddev/smartGenDocs/blob/main/.github/workflows/changelog.yml).
- [2] Automated Changelog Renderer. [SmartGen Source Code](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/changelog_renderer.py).
- [3] Structural Themes Reference. [SmartGen Theming Guide](https://docs.smartgentools.com/guides/theming.html).
- [4] Style Switcher Implementation. [SmartGen Shared Partials](https://github.com/bayeziddev/smartGenDocs/tree/main/smartgen_docs/themes/_shared/partials).
- [5] Sitemap Generation Engine. [SmartGen Builder Core](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/core.py).
- [6] Playwright Verification Suite. [SmartGen Tools](https://github.com/bayeziddev/smartGenDocs/tree/main/tools).
- [7] GitHub Pages Configuration. [SmartGen Deployment Guide](https://docs.smartgentools.com/getting-started/deployment.html).
- [8] Navigation State Resolution. [SmartGen Changelog](https://docs.smartgentools.com/docs/changelog.html).
- [9] Theme Engine Architecture. [SmartGen Theme Engine](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/theme_engine.py).
- [10] Markdown Converter. [SmartGen Core Converter](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/converter.py).
- [11] Configuration Reference. [SmartGen Configuration Guide](https://docs.smartgentools.com/guides/configuration.md).
- [12] CI/CD Pipeline Documentation. [SmartGen Documentation](https://docs.smartgentools.com/).
