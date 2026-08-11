# Documentation Release Notes & Platform Updates

This document tracks all official releases, version updates, and core architectural milestones for SmartGen Docs.

## Version 1.1.0 (August 2026)

Version 1.1.0 represents a major milestone in SmartGen Docs engineering, introducing full support for seven distinct structural themes, a live client-side style switcher, automated sitemap and robots generation, and robust Playwright testing suites [1].

### Key Enhancements

- **Multi-Theme Engine**: Added production support for `default`, `book`, `education`, `techblog`, `agency`, `medicine`, and `apiplay` themes [2].
- **Live Styles Switcher**: Implemented a floating, keyboard-accessible button allowing readers to switch between all seven theme variants on the fly while preserving their exact page location [3].
- **Automated Sitemap & Robots**: The builder engine now automatically computes document modification times and generates valid `sitemap.xml` and `robots.txt` files directly into the build output [4].
- **Playwright Verification**: Added `tools/capture_screenshots.py` for automated cross-browser visual regression testing and responsive layout verification [5].

## Version 1.0.0 (July 2026)

The initial public release of SmartGen Docs established the Python-native, zero-dependency static documentation framework.

### Foundation Features

- High-performance Markdown-to-HTML conversion with Pygments syntax highlighting [6].
- Flexible YAML configuration (`smartgen.yml`) supporting nested sidebar navigation and breadcrumbs [7].
- Automated GitHub Actions workflows for continuous integration validation and GitHub Pages deployment [8].

## References

- [1] SmartGen Release History. [SmartGen GitHub Releases](https://github.com/bayeziddev/smartGenDocs/releases).
- [2] Multi-Theme Architecture. [SmartGen Theming Guide](https://docs.smartgentools.com/guides/theming.html).
- [3] Style Switcher Implementation. [SmartGen Shared Partials](https://github.com/bayeziddev/smartGenDocs/tree/main/smartgen_docs/themes/_shared/partials).
- [4] Sitemap Generation Engine. [SmartGen Builder Core](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/core.py).
- [5] Playwright Verification Suite. [SmartGen Tools](https://github.com/bayeziddev/smartGenDocs/tree/main/tools).
- [6] Markdown Converter. [SmartGen Core Converter](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/converter.py).
- [7] Configuration Guide. [SmartGen Configuration Reference](https://docs.smartgentools.com/guides/configuration.md).
- [8] CI/CD Automation. [SmartGen Deployment Documentation](https://docs.smartgentools.com/getting-started/deployment.html).
