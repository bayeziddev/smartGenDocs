# Theming Guide: Structural Themes and Color Modes

SmartGen Docs ships with a dual-layer theming architecture: readers can switch between structural layouts (`default`, `book`, `education`, `techblog`, `agency`, `medicine`, `apiplay`) and color modes (Light, Dark, Sepia, and High Contrast). Like the rest of the project, this system is hand-authored CSS and vanilla JavaScript—avoiding heavy frameworks, icon font CDNs, and client-side styling runtimes [1].

This guide explains how the system works, how to configure your primary theme in `smartgen.yml`, how color modes persist in browser local storage, and how to create custom structural themes [2].

## The Seven Built-In Structural Themes

Structural themes govern the master layout, navigation hierarchy, typography, and motion curves of your documentation:

| Theme Identifier | Family | Layout Characteristics | Recommended Use Case |
|---|---|---|---|
| **Default** (`default`) | Classic | Collapsible sidebar, search, breadcrumbs, and pagination | Standard software libraries and SDK references |
| **Book** (`book`) | Reading | Narrow measure, serif typography, drop caps, and scroll progress | Long-form specifications and technical books |
| **Education** (`education`) | Course | Curriculum modules, lesson visited trackers, and progress rails | Online workshops, tutorials, and onboarding guides |
| **Tech Blog** (`techblog`) | Editorial | Editorial magazine layout, header cards, and article metadata | Engineering blogs and release announcements |
| **Agency** (`agency`) | Portal | Gradient hero, modern card grids, and commercial service framing | Enterprise developer portals and SaaS docs |
| **Medicine** (`medicine`) | Clinical | Clinical reference framing, clean borders, and print-optimized CSS | Medical protocols and pharmaceutical APIs |
| **API Playground** (`apiplay`) | Terminal | Terminal-inspired monospace aesthetics and command-oriented layout | Developer APIs and systems architecture |

Readers can instantly preview any of these layouts using the floating **Styles** switcher button located at the bottom-left of every page [3].

## Color Modes in the Default Theme

In addition to structural themes, the default theme supports four distinct color modes:

1. **Light**: Balanced contrast for typical daytime reading [4].
2. **Dark**: Reduced brightness for low-light environments [5].
3. **Sepia**: Warm, low-glare paper tone for long reading sessions [6].
4. **High Contrast**: Pure black background, pure white text, and solid 1px borders for maximum readability [7].

## How the Theming Engine Works

The theming system operates through four core pillars:

1. **Design Tokens**: Defined as plain CSS custom properties (`--bg-primary`, `--text-primary`, `--color-primary`, etc.) in theme stylesheets [8].
2. **The `data-theme` Attribute**: Applied to the root `<html>` element to instantly toggle visual palettes [9].
3. **Pre-Paint Script**: Inlined at the very top of `<head>` to read `localStorage` or `prefers-color-scheme`, preventing any flash of unstyled content (FOUC) [10].
4. **Live Style Switcher**: Dynamically calculates the reader's current page subpath and links between isolated theme variants under `/styles/<theme>/` [11].

## References

- [1] SmartGen Theming Architecture. [SmartGen Documentation](https://docs.smartgentools.com/docs/theming.html).
- [2] Multi-Theme Guide. [SmartGen Guide: Theming](https://docs.smartgentools.com/guides/theming.html).
- [3] Style Switcher Implementation. [SmartGen Shared Partials](https://github.com/bayeziddev/smartGenDocs/tree/main/smartgen_docs/themes/_shared/partials).
- [4] Light Color Mode. [SmartGen Styles](https://docs.smartgentools.com/).
- [5] Dark Color Mode. [SmartGen Styles](https://docs.smartgentools.com/).
- [6] Sepia Color Mode. [SmartGen Styles](https://docs.smartgentools.com/).
- [7] High Contrast Mode. [SmartGen Styles](https://docs.smartgentools.com/).
- [8] CSS Design Tokens. [SmartGen Premium CSS](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/themes/default/static/css/premium.css).
- [9] Root Theme Attribute. [SmartGen Source Code](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/core.py).
- [10] Pre-Paint Script. [SmartGen Prepaint Partial](https://github.com/bayeziddev/smartGenDocs/tree/main/smartgen_docs/themes/_shared/partials).
- [11] Style Switcher Script. [SmartGen Shared Partials](https://github.com/bayeziddev/smartGenDocs/tree/main/smartgen_docs/themes/_shared/partials).
