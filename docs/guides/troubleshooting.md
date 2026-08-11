# Troubleshooting Guide & Common Solutions

This guide provides diagnostic procedures and verified solutions for common issues encountered during local development, theme customization, and CI/CD deployments with SmartGen Docs [1].

## Common Issues and Diagnostic Table

| Symptom / Error | Probable Root Cause | Corrective Action |
|---|---|---|
| **Sitemap appears blank or invalid** | Missing root XML declarations or newline serialization issues | Verify that `site/sitemap.xml` is generated correctly and test with Python's `xml.etree.ElementTree` [2]. |
| **Styles switcher button missing** | Active theme missing `style_switcher.html` or script partials | Ensure theme templates include the shared partials and rebuild all themes using `build_all_themes.py` [3]. |
| **GitHub Pages 404 on assets** | Jekyll overriding underscore or namespaced static directories | Ensure `site/.nojekyll` is touched during build to prevent Jekyll from filtering static assets [4]. |
| **Broken internal Markdown links** | Relative links pointing to `.md` instead of `.html` | SmartGen automatically rewrites internal `.md` links, but ensure anchor paths are correctly formatted [5]. |
| **Playwright screenshot tests fail** | Chromium browser binaries missing in container | Run `python -m playwright install chromium` after installing the `screenshots` extra [6]. |

## References

- [1] SmartGen Troubleshooting Reference. [SmartGen Documentation](https://docs.smartgentools.com/docs/architecture.html).
- [2] Sitemap Generation Engine. [SmartGen Builder Core](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/core.py).
- [3] Multi-Theme Build Script. [SmartGen Repository](https://github.com/bayeziddev/smartGenDocs/blob/main/build_all_themes.py).
- [4] GitHub Pages Deployment Guide. [SmartGen Documentation](https://docs.smartgentools.com/getting-started/deployment.html).
- [5] Link Rewriting Module. [SmartGen Link Fixer](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/link_fixer.py).
- [6] Playwright Verification Suite. [SmartGen Tools](https://github.com/bayeziddev/smartGenDocs/tree/main/tools).
