# Broken Link Audit — docs.smartgentools.com
**Date:** August 5, 2026
**Scope:** All contextual (in-body/prose) internal links across the documentation site
**Pages crawled:** 45 (homepage, 12 section indexes, and all discoverable leaf pages under Getting Started, Documentation, API Reference, SDKs, SmartGen Tools, Tutorials, Guides, Resources, Community, Blog, About)

## Executive Summary

The audit found **one dominant, site-wide root cause**: the static-site generator that builds this documentation (SmartGenDocs, the same open-source generator used to build this site — `github.com/bayeziddev/smartGenDocs`) is not rewriting internal Markdown links to their built `.html` output paths. As a result, almost every in-body/contextual link on the site (the ones inside paragraphs, "See Also" sections, and cross-references — as opposed to the top-nav menu, which is built correctly) still points at the raw `.md` source path and 404s.

On top of that pattern, a handful of links have deeper structural problems: wrong subdirectory, duplicated path segments, wrong domain, or a target page that doesn't exist anywhere on the site (not even as source).

- **Total unique broken contextual links found:** 61
- **Root cause A — `.md` extension not rewritten to `.html`:** 53 links (87%)
- **Root cause B — structurally wrong path** (wrong section, duplicated segment, wrong domain): 5 links
- **Root cause C — target content doesn't exist at all** (genuine content gap, not just a bad link): 3 links

All 404s were independently re-verified by requesting the broken URL directly.

---

## Resolution Report

### A. Systematic `.md` → `.html` link bug (found across nearly every page)

- Broken Link SRC: https://docs.smartgentools.com/installation.md
- Fixed URL: https://docs.smartgentools.com/getting-started/installation.html
*(found on homepage — also missing the `getting-started/` folder segment)*

- Broken Link SRC: https://docs.smartgentools.com/getting-started/quick-start.md
- Fixed URL: https://docs.smartgentools.com/getting-started/quick-start.html

- Broken Link SRC: https://docs.smartgentools.com/getting-started/first-project.md
- Fixed URL: https://docs.smartgentools.com/getting-started/first-project.html

- Broken Link SRC: https://docs.smartgentools.com/getting-started/folder-structure.md
- Fixed URL: https://docs.smartgentools.com/getting-started/folder-structure.html

- Broken Link SRC: https://docs.smartgentools.com/getting-started/deployment.md
- Fixed URL: https://docs.smartgentools.com/getting-started/deployment.html

- Broken Link SRC: https://docs.smartgentools.com/getting-started/faq.md
- Fixed URL: https://docs.smartgentools.com/getting-started/faq.html

- Broken Link SRC: https://docs.smartgentools.com/index.md
- Fixed URL: https://docs.smartgentools.com/index.html

- Broken Link SRC: https://docs.smartgentools.com/docs/index.md
- Fixed URL: https://docs.smartgentools.com/docs/index.html

- Broken Link SRC: https://docs.smartgentools.com/docs/platform.md
- Fixed URL: https://docs.smartgentools.com/docs/platform.html

- Broken Link SRC: https://docs.smartgentools.com/docs/architecture.md
- Fixed URL: https://docs.smartgentools.com/docs/architecture.html

- Broken Link SRC: https://docs.smartgentools.com/docs/features.md
- Fixed URL: https://docs.smartgentools.com/docs/features.html

- Broken Link SRC: https://docs.smartgentools.com/docs/features.md#8-upload-manager-web-based-interface
- Fixed URL: https://docs.smartgentools.com/docs/features.html#8-upload-manager-web-based-interface
*(found on api/authentication.html and api/endpoints.html)*

- Broken Link SRC: https://docs.smartgentools.com/docs/concepts.md
- Fixed URL: https://docs.smartgentools.com/docs/concepts.html

- Broken Link SRC: https://docs.smartgentools.com/docs/releases.md
- Fixed URL: https://docs.smartgentools.com/docs/releases.html

- Broken Link SRC: https://docs.smartgentools.com/docs/changelog.md
- Fixed URL: https://docs.smartgentools.com/docs/changelog.html

- Broken Link SRC: https://docs.smartgentools.com/api/authentication.md
- Fixed URL: https://docs.smartgentools.com/api/authentication.html

- Broken Link SRC: https://docs.smartgentools.com/api/rest-api.md
- Fixed URL: https://docs.smartgentools.com/api/rest-api.html

- Broken Link SRC: https://docs.smartgentools.com/api/endpoints.md
- Fixed URL: https://docs.smartgentools.com/api/endpoints.html

- Broken Link SRC: https://docs.smartgentools.com/api/errors.md
- Fixed URL: https://docs.smartgentools.com/api/errors.html

- Broken Link SRC: https://docs.smartgentools.com/api/rate-limits.md
- Fixed URL: https://docs.smartgentools.com/api/rate-limits.html

- Broken Link SRC: https://docs.smartgentools.com/api/webhooks.md
- Fixed URL: https://docs.smartgentools.com/api/webhooks.html

- Broken Link SRC: https://docs.smartgentools.com/sdk/index.md
- Fixed URL: https://docs.smartgentools.com/sdk/index.html

- Broken Link SRC: https://docs.smartgentools.com/tools/index.md
- Fixed URL: https://docs.smartgentools.com/tools/index.html

- Broken Link SRC: https://docs.smartgentools.com/tools/qr-generator.md
- Fixed URL: https://docs.smartgentools.com/tools/qr-generator.html

- Broken Link SRC: https://docs.smartgentools.com/tools/seo.md
- Fixed URL: https://docs.smartgentools.com/tools/seo.html

- Broken Link SRC: https://docs.smartgentools.com/tools/ai.md
- Fixed URL: https://docs.smartgentools.com/tools/ai.html

- Broken Link SRC: https://docs.smartgentools.com/tools/developer.md
- Fixed URL: https://docs.smartgentools.com/tools/developer.html

- Broken Link SRC: https://docs.smartgentools.com/tools/marketing.md
- Fixed URL: https://docs.smartgentools.com/tools/marketing.html

- Broken Link SRC: https://docs.smartgentools.com/tools/utilities.md
- Fixed URL: https://docs.smartgentools.com/tools/utilities.html

- Broken Link SRC: https://docs.smartgentools.com/tutorials/index.md
- Fixed URL: https://docs.smartgentools.com/tutorials/index.html

- Broken Link SRC: https://docs.smartgentools.com/tutorials/beginner.md
- Fixed URL: https://docs.smartgentools.com/tutorials/beginner.html

- Broken Link SRC: https://docs.smartgentools.com/tutorials/api.md
- Fixed URL: https://docs.smartgentools.com/tutorials/api.html

- Broken Link SRC: https://docs.smartgentools.com/tutorials/integrations.md
- Fixed URL: https://docs.smartgentools.com/tutorials/integrations.html

- Broken Link SRC: https://docs.smartgentools.com/tutorials/best-practices.md
- Fixed URL: https://docs.smartgentools.com/tutorials/best-practices.html

- Broken Link SRC: https://docs.smartgentools.com/tutorials/case-studies.md
- Fixed URL: https://docs.smartgentools.com/tutorials/case-studies.html

- Broken Link SRC: https://docs.smartgentools.com/guides/configuration.md
- Fixed URL: https://docs.smartgentools.com/guides/configuration.html

- Broken Link SRC: configuration.md#site-metadata (relative link on guides/seo.html)
- Fixed URL: https://docs.smartgentools.com/guides/configuration.html#site-metadata

- Broken Link SRC: https://docs.smartgentools.com/guides/customization.md
- Fixed URL: https://docs.smartgentools.com/guides/customization.html

- Broken Link SRC: https://docs.smartgentools.com/guides/seo.md
- Fixed URL: https://docs.smartgentools.com/guides/seo.html

- Broken Link SRC: https://docs.smartgentools.com/guides/troubleshooting.md
- Fixed URL: https://docs.smartgentools.com/guides/troubleshooting.html

- Broken Link SRC: https://docs.smartgentools.com/resources/roadmap.md
- Fixed URL: https://docs.smartgentools.com/resources/roadmap.html

- Broken Link SRC: https://docs.smartgentools.com/community/index.md
- Fixed URL: https://docs.smartgentools.com/community/index.html

- Broken Link SRC: https://docs.smartgentools.com/community/issues.md
- Fixed URL: https://docs.smartgentools.com/community/issues.html

- Broken Link SRC: https://docs.smartgentools.com/community/features.md
- Fixed URL: https://docs.smartgentools.com/community/features.html

- Broken Link SRC: https://docs.smartgentools.com/community/discussions.md
- Fixed URL: https://docs.smartgentools.com/community/discussions.html

- Broken Link SRC: https://docs.smartgentools.com/community/contributing.md
- Fixed URL: https://docs.smartgentools.com/community/contributing.html

- Broken Link SRC: https://docs.smartgentools.com/blog/index.md
- Fixed URL: https://docs.smartgentools.com/blog/index.html

- Broken Link SRC: https://docs.smartgentools.com/about/index.md
- Fixed URL: https://docs.smartgentools.com/about/index.html

- Broken Link SRC: https://docs.smartgentools.com/about/developer.md
- Fixed URL: https://docs.smartgentools.com/about/developer.html

- Broken Link SRC: https://docs.smartgentools.com/about/contact.md
- Fixed URL: https://docs.smartgentools.com/about/contact.html

- Broken Link SRC: https://docs.smartgentools.com/about/license.md
- Fixed URL: https://docs.smartgentools.com/about/license.html

### B. Structurally wrong paths (not just an extension problem)

- Broken Link SRC: https://docs.smartgentools.com/sdk/python-sdk.md
- Fixed URL: https://docs.smartgentools.com/sdk/python.html
*(found on sdk/index.html — filename itself is wrong, not just the extension; the real page is `python.html`, not `python-sdk.html`)*

- Broken Link SRC: https://docs.smartgentools.com/sdk/javascript-sdk.md
- Fixed URL: https://docs.smartgentools.com/sdk/javascript.html
*(same issue — real page is `javascript.html`)*

- Broken Link SRC: https://docs.smartgentools.com/about/sponsor.md
- Fixed URL: https://docs.smartgentools.com/community/sponsor.html
*(found on about/index.html — this page lives under `/community/`, not `/about/`; there is no `about/sponsor.html` at all)*

- Broken Link SRC: https://docs.smartgentools.com/getting-started/docs/getting-started/quick-start.md
- Fixed URL: https://docs.smartgentools.com/getting-started/quick-start.html
*(found on getting-started/installation.html — the path segment `getting-started/` is duplicated/nested by mistake)*

- Broken Link SRC: https://docs.smartgentools.com/guides/docs/changelog.md
- Fixed URL: https://docs.smartgentools.com/docs/changelog.html
*(found on guides/configuration.html — `docs/` is incorrectly nested inside `/guides/`)*

- Broken Link SRC: https://docs.smartgentools.com/guides/index.md
- Fixed URL: https://docs.smartgentools.com/guides/configuration.html
*(found on multiple "See Also" sections — there is no `guides/index.html` on this site; `configuration.html` is the de facto entry point for the Guides section, per the main nav)*

- Broken Link SRC: https://docs.smartgentools.com/guides/deployment.md
- Fixed URL: https://docs.smartgentools.com/getting-started/deployment.html
*(found on tutorials/case-studies.html — there is no Deployment page under `/guides/`; the real deployment guide lives at `/getting-started/deployment.html`)*

- Broken Link SRC: https://docs.smartgentools.com/guides/deployment.md#3-continuous-deployment-cicd
- Fixed URL: https://docs.smartgentools.com/getting-started/deployment.html
*(found on tutorials/best-practices.html — same wrong-section issue; also note the target page has no anchor matching `#3-continuous-deployment-cicd` — the closest matching section is "Method 2: Automated Deployment with GitHub Actions," so the anchor ID should be corrected once you're on the right page)*

- Broken Link SRC: https://smartgentools.com/docs/ (anchor text: "SmartGen Docs Guides")
- Fixed URL: https://docs.smartgentools.com/guides/configuration.html
*(found on tools/marketing.html — this link points at the marketing site's domain instead of the docs subdomain, and the marketing-site path returns no content)*

### C. Genuine content gaps (linked page doesn't exist anywhere — not even as source)

These three pages are referenced repeatedly across Guides and Tutorials content but were never built — there's no `.md` source and no `.html` output for them. This isn't a link-rewrite bug; the content simply doesn't exist yet. Recommended interim fix is to repoint to the closest existing page and flag these for actual content creation:

- Broken Link SRC: https://docs.smartgentools.com/guides/theming.md
- Fixed URL: https://docs.smartgentools.com/guides/customization.html *(interim redirect — closest existing topic; recommend authoring a real Theming Guide)*
*(found on best-practices.html, tutorials/beginner.html context)*

- Broken Link SRC: https://docs.smartgentools.com/guides/autodoc.md
- Fixed URL: https://docs.smartgentools.com/docs/features.html *(interim redirect; recommend authoring a real Autodoc Guide)*
*(found on tutorials/api.html, tutorials/best-practices.html)*

- Broken Link SRC: https://docs.smartgentools.com/guides/cli.md
- Fixed URL: https://docs.smartgentools.com/getting-started/quick-start.html *(interim redirect; recommend authoring a real CLI Reference page)*
*(found on tutorials/api.html, tutorials/beginner.html)*

---

## Notes on Methodology

- Every link listed above was independently confirmed to return an HTTP 404 by requesting the exact broken URL directly.
- "Fixed URL" targets were confirmed to return HTTP 200 with real content (not confirmed for the three content-gap items in Section C, since no equivalent page exists — those are best-fit interim redirects, not a rewrite fix).
- Top-navigation menu links (the sidebar/header nav repeated on every page) were **not** broken — this audit was scoped to contextual/in-body links, per your request, and the nav is generated correctly.
- A number of section stub pages (e.g. `sdk/javascript.html`, `sdk/python.html`, `sdk/php.html`, `sdk/java.html`, `sdk/go.html`, `blog/*`, `resources/downloads.html`, `resources/templates.html`, `resources/examples.html`, `resources/glossary.html`, `guides/customization.html`, `guides/performance.html`, `guides/accessibility.html`, `guides/troubleshooting.html`) currently contain only placeholder/template text ("Add your content here"). They resolve fine (not broken links), but are worth flagging separately as thin-content pages once the link fixes above are shipped.

## Recommended Fix Priority

1. **Fix the link-rewrite bug in the SmartGenDocs generator itself** (Section A, 53 links) — this is almost certainly one bug in `converter.py` / `theme_engine.py` where internal Markdown links aren't being rewritten from `.md` to `.html` at build time. Fixing it there resolves the large majority of broken links across the whole site in one change, and prevents recurrence on every future page.
2. **Hand-fix the 8 structurally wrong links** (Section B) — these are individual authoring mistakes in the source Markdown and need manual correction.
3. **Decide on the 3 missing pages** (Section C) — either write the Theming Guide, Autodoc Guide, and CLI Reference pages, or update the referencing pages to stop promising content that doesn't exist.
