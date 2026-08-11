# Theming Architecture in SmartGen Docs

SmartGen Docs is built upon a dual-layer theming architecture that separates structural layouts from color modes. This design enables developers to switch between entirely distinct documentation layouts while maintaining consistent color schemes, responsive navigation, and accessibility standards [1].

## Dual-Layer Theming Paradigm

The theming system distinguishes between two independent abstraction layers:

1. **Structural Themes (`theme.name` in `smartgen.yml`)**: These define the master HTML skeleton, sidebar navigation patterns, typography rules, and motion curves. Selecting a structural theme completely transforms the presentation of your documentation (e.g., conventional docs vs. curriculum modules vs. book-like reading layouts) [2].
2. **Color Modes (`data-theme` attribute)**: These manage visual palettes (such as Light, Dark, Sepia, and High Contrast) through CSS custom properties. Color modes apply uniformly across structural themes, allowing readers to toggle their preferred visual contrast on the fly [3].

The following table details the primary structural themes and their architectural characteristics:

| Theme Identifier | Configuration Key | Layout Paradigm | Primary Use Case |
|---|---|---|---|
| **Default** | `default` (or `premium`) | Conventional collapsible sidebar, search, breadcrumbs, and footer pagination | Standard software libraries and SDK references |
| **Book** | `book` | Focused reading layout, narrow serif measure, drop caps, and scroll progress | Long-form technical books and specifications |
| **Education** | `education` | Curriculum modules, lesson visited trackers, and progress rails | Interactive tutorials, workshops, and courses |
| **Tech Blog** | `techblog` | Editorial magazine layout, header cards, and article metadata | Engineering blogs and release announcements |
| **Agency** | `agency` | Gradient hero, modern card grids, and commercial service framing | Enterprise portals and SaaS landing documentation |
| **Medicine** | `medicine` | Clinical reference framing, clean borders, and print-optimized typography | Medical protocols and pharmaceutical guides |
| **API Playground** | `apiplay` | Terminal-inspired monospace aesthetics and command-oriented design | Developer APIs and systems architecture |

## Implementing a Custom Structural Theme

Adding a new structural theme requires no modifications to the core builder engine (`core.py`) or theme resolution logic (`theme_engine.py`). The `ThemeEngine` automatically discovers any directory placed under `smartgen_docs/themes/<name>/` that contains a valid `page.html` or `page_premium.html` template [4].

A standard theme directory requires the following file layout:

```text
smartgen_docs/themes/custom/
├── base.html                  # Master HTML layout and container structure
├── page.html                  # Content wrapper extending base.html
└── static/
    └── css/
        └── custom.css         # Theme design tokens and structural CSS
```

Within your theme's `base.html`, you can include shared partials from `_shared/` using Jinja's `{% include %}` directive. This avoids code duplication for standard components like the pre-paint FOUC-prevention script, active navigation script, and the live style switcher [5].

## References

- [1] SmartGen Theming Overview. [SmartGen Documentation](https://docs.smartgentools.com/docs/theming.html).
- [2] Structural Themes Reference. [SmartGen Guide: Theming](https://docs.smartgentools.com/guides/theming.html).
- [3] Color Mode Architecture. [SmartGen Repository](https://github.com/bayeziddev/smartGenDocs).
- [4] Theme Engine Resolution. [SmartGen Source Code](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/theme_engine.py).
- [5] Shared Partials Reference. [SmartGen Shared Partials](https://github.com/bayeziddev/smartGenDocs/tree/main/smartgen_docs/themes/_shared/partials).
