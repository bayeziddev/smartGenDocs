# Roadmap

SmartGen Docs is a documentation site generator built in Python: Markdown in, a fast static site out. This page tracks where the project actually stands and where it's headed — updated as things ship, not written as a wishlist.

## Where things stand today

- **Markdown-first authoring.** Every page is a plain `.md` file with YAML front matter — no proprietary format, no lock-in.
- **Zero third-party front-end dependency.** The theme ships its own CSS and hand-drawn SVG icon set. No icon fonts, no UI framework, no CDN calls for anything visual. Code syntax highlighting runs server-side through Pygments at build time, so pages stay correct even with JavaScript disabled.
- **One toolchain.** `smartgen-docs init`, `serve`, and `build` cover the full lifecycle — scaffolding, a live-reload dev server, and static output — without stitching together separate tools.
- **Configuration-driven theming.** Sidebar structure, color palette, and site metadata all live in a single `smartgen.yml`, so a new site can be reskinned without touching CSS.

## What's next

Real, prioritized directions — not commitments to a date:

- **Build caching.** Every `build` currently re-renders every page from scratch. A content-hash cache that skips unchanged pages is the next concrete step toward faster rebuilds on large documentation sets.
- **Build-time search index.** Search currently matches against the rendered navigation in the browser; a proper index generated at build time is planned, so results cover full page content, not just titles.
- **Documented plugin hooks.** A clear extension point for custom Markdown extensions and build steps, so the core stays small and the rest is opt-in.
- **Versioned documentation.** Support for maintaining more than one version of a doc set side by side.

## Longer-term direction

The longer-term goal is a build pipeline that only redoes the work a change actually requires — tracking which source files feed which output pages, so editing one page doesn't force a full rebuild of the whole site. That's a substantial undertaking on its own, and it'll be scoped and written up here as real work begins on it, not promised ahead of that.

## Get involved

SmartGen Docs is open source and still early. If a direction here matters to you, open an issue or a discussion on [GitHub](https://github.com/bayeziddev/smartGenDocs) — priorities on this page are shaped by the people actually using the tool.