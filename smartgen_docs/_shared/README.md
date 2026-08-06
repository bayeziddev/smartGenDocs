# `_shared/` — include-only partials for every theme

This directory is **not** a selectable theme (`ThemeEngine.available_themes()`
skips anything starting with `_`). It exists so multiple, structurally
unrelated themes can reuse the same small set of well-tested behaviors
without copy-pasting markup or JS.

Any theme's templates can pull these in with a plain Jinja `{% include %}`,
because `ThemeEngine` wires every theme's `Environment` with a `ChoiceLoader`
that checks the theme's own directory first, then `_shared/`, then
`default/` (see `theme_engine.py`).

## What's here

- **`partials/theme_prepaint.html`** — the pre-paint, FOUC-preventing
  `<script>`. Include first thing in `<head>`. Requires `theme_modes`: a
  list of mode value strings your theme's CSS implements, e.g.
  `{% set theme_modes = ['light', 'dark'] %}`.

- **`partials/theme_switcher.html`** — the trigger button + empty popover
  markup for the color-mode switcher. Drop it in your header/toolbar. No
  context required.

- **`partials/theme_switcher_script.html`** — the behavior for the markup
  above (open/close, keyboard nav, persistence). Include once near the end
  of `<body>`. Requires `theme_switcher_modes`: a list of
  `{value, label, swatch_bg, swatch_fg}` dicts describing the same modes
  passed to `theme_prepaint.html`, e.g.:

  ```jinja
  {% set theme_switcher_modes = [
      {"value": "light", "label": "Day",   "swatch_bg": "#FBF9F4", "swatch_fg": "#2E7D5B"},
      {"value": "dark",  "label": "Night", "swatch_bg": "#10241A", "swatch_fg": "#7FD4AE"}
  ] %}
  {% include "partials/theme_switcher_script.html" with context %}
  ```

  All three partials share one `localStorage` key (`smartgen-theme`), so a
  reader who picks "Dark" on one theme gets it on every other theme too.

- **`partials/active_nav_script.html`** — marks the nav link matching the
  current URL as active (and expands its parent section, if any). Works
  across completely different sidebar markup: any link opts in with a
  `data-nav-link` attribute next to `href`, and a collapsible section opts
  in with `data-nav-section` / `data-nav-submenu`. No context required.

## Writing a new theme

A new theme only needs, under `smartgen_docs/themes/<name>/`:

```
<name>/
  base.html          # your own layout; include whichever _shared partials you want
  page.html          # {% extends "base.html" %} + {% block content %}{{ content|safe }}{% endblock %}
  static/css/*.css   # your own design tokens + structural CSS
```

`ThemeEngine` picks it up automatically — nothing in `core.py` or
`theme_engine.py` needs to change, and its static assets are namespaced
under `static/<name>/` so they can never collide with another theme's
filenames. See `education/` and `book/` for two complete, working examples
with very different layouts built from the same shared partials.
