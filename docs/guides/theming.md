# Theming Guide

SmartGen Docs ships with a built-in, multi-theme system: readers can switch between **Light**, **Dark**, **Sepia**, and **High Contrast**, and their choice is remembered on their next visit. Like the rest of the default theme, it's hand-authored CSS and vanilla JavaScript — no theming framework, no icon library, no third-party stylesheet. Every color a theme uses lives in one place and is easy to read, copy, and change.

This guide explains how the system works, how to pick a theme as a reader, how to set a site-wide brand color as a site owner, and how to add your own theme as a contributor.

## The four built-in themes

| Theme | Family | Purpose |
|---|---|---|
| **Light** | Light | The default. Balanced contrast for typical daytime reading. |
| **Dark** | Dark | Reduced brightness for low-light environments. |
| **Sepia** | Light | Warm, low-glare paper tone, aimed at long reading sessions. |
| **High Contrast** | Dark | Pure black background, pure white text, solid 1px borders instead of soft shadows — aimed at readers who need stronger contrast (WCAG AAA-level target) rather than a decorative dark mode. |

Readers switch themes from the palette icon at the top right of every page. It opens a small menu (keyboard-accessible: arrow keys to move, <kbd>Enter</kbd> to pick, <kbd>Esc</kbd> to close) listing all four, each with a small preview swatch and a checkmark on the active one.

## How it works

The whole system is four pieces, all in `smartgen_docs/themes/default/`:

1. **Design tokens**, in `static/css/premium.css`. `:root` defines the Light theme's values as plain CSS custom properties (`--bg-primary`, `--text-primary`, `--color-primary`, and so on). Each other theme is a block like:

    ```css
    :root[data-theme="sepia"] {
        --bg-primary: #F7F1E3;
        --text-primary: #2E2515;
        /* ...every other token... */
    }
    ```

   Nothing else in the stylesheet references a specific color by hex value — every rule in the site (backgrounds, text, borders, buttons, code blocks) is written against these tokens, so a new theme only has to redefine the tokens once and the entire site repaints correctly.

2. **The `data-theme` attribute**, set on `<html>`. Switching themes is just setting or removing this one attribute — `<html data-theme="dark">`, `<html data-theme="sepia">`, and so on. Light has no attribute at all (it's the `:root` default), which keeps the common case cheap.

3. **A tiny pre-paint script**, inlined at the very top of `<head>` in `base_premium.html`. Before any CSS or content loads, it reads the reader's saved choice from `localStorage` (key `smartgen-theme`) and, if they've never chosen, falls back to their OS's `prefers-color-scheme`. It sets `data-theme` synchronously, so the page never flashes the wrong theme on load.

4. **The theme switcher script**, near the end of `base_premium.html`. A `THEMES` array is the single source of truth for the switcher menu (value, label, and the two preview-swatch colors); the menu's HTML is generated from it. Picking an option calls `applyTheme(value)`, which sets `data-theme`, saves the choice to `localStorage`, and re-renders the menu's checkmark.

## Site owners: setting a brand color

If your `smartgen.yml` sets a custom palette:

```yaml
theme:
  name: premium
  palette:
    primary: "#0052CC"
    accent: "#FF9900"
```

that primary/accent pair applies on top of **every** theme, light or dark — so your brand color stays consistent no matter which theme a reader picks. Everything else about the theme (backgrounds, text, borders) still adapts normally.

This `theme.palette.primary` / `theme.palette.accent` pair is the only theme-related setting `smartgen.yml` currently reads. There is no `extra_css`, `extra_javascript`, `custom_dir`, `features` list, icon-font config, or analytics block — an earlier draft of this page described those (borrowed from a different static-site generator's config format) but none of it is implemented in `smartgen_docs/core.py`, so it never did anything. If you need one of those capabilities, it's a real feature request, not a documentation gap — see [Contributing](../community/contributing.md).

## Contributors: adding a new theme

Adding a theme is two small edits and a rebuild — no build tooling changes needed.

**1. Add a token block to `smartgen_docs/themes/default/static/css/premium.css`**, next to the existing ones:

```css
:root[data-theme="forest"] {
    --color-primary: #2E7D5B;
    --color-primary-light: #E1F2E9;
    --color-primary-hover: #256B4C;
    --color-accent: #B5651D;
    --color-accent-light: #F6E6D8;
    --color-mint: #2E7D5B;
    --color-success: #2E7D5B;
    --color-warning: #B5651D;
    --color-danger: #C4314B;
    --color-info: #2E7D5B;

    --bg-primary: #F4F8F5;
    --bg-secondary: #E9F1EB;
    --bg-tertiary: #DCE9DF;
    --bg-hover: #E1F2E9;
    --bg-active: #E1F2E9;
    --bg-code: #EAF2EC;

    --text-primary: #16241C;
    --text-secondary: #3E5548;
    --text-tertiary: #5C7466;
    --text-active: #2E7D5B;

    --border-color: #CBDECF;
    --border-light: #DCE9DF;
    --border-active: #2E7D5B;

    --shadow-sm: 0 1px 2px rgba(22, 36, 28, 0.06);
    --shadow-md: 0 6px 16px rgba(22, 36, 28, 0.10);
    --shadow-lg: 0 18px 46px rgba(22, 36, 28, 0.16);
}
```

Every token from the reference table below must be present, or elements using it will silently fall back to the Light theme's value.

**2. Register it in the `THEMES` array** in `smartgen_docs/themes/default/base_premium.html` (search for `THEME SWITCHER`):

```js
const THEMES = [
    { value: 'light',    label: 'Light',        swatchBg: '#ffffff', swatchFg: '#4A3AE3' },
    { value: 'dark',     label: 'Dark',          swatchBg: '#0B0E16', swatchFg: '#8C9EFF' },
    { value: 'sepia',    label: 'Sepia',         swatchBg: '#F7F1E3', swatchFg: '#A8540B' },
    { value: 'contrast', label: 'High Contrast', swatchBg: '#000000', swatchFg: '#A6B4FF' },
    { value: 'forest',   label: 'Forest',        swatchBg: '#F4F8F5', swatchFg: '#2E7D5B' },
];
```

**3. Also update the `VALID` list** in the pre-paint script at the top of `<head>` (same file) so the new theme survives a hard refresh:

```js
var VALID = ['light', 'dark', 'sepia', 'contrast', 'forest'];
```

Rebuild (`smartgen-docs build`), refresh, and the new theme appears in the switcher immediately — no other file needs to change.

### Token reference

| Token | Governs |
|---|---|
| `--color-primary` / `--color-primary-light` / `--color-primary-hover` | Links, active nav item, primary buttons, focus accents. |
| `--color-accent` / `--color-accent-light` | Secondary highlights (e.g. the Sponsor button). |
| `--color-mint` / `--color-success` | Success states. |
| `--color-warning` | Warning states. |
| `--color-danger` | Error states. |
| `--color-info` | Informational callouts. |
| `--bg-primary` | Page background. |
| `--bg-secondary` / `--bg-tertiary` | Sidebar, cards, table stripes. |
| `--bg-hover` / `--bg-active` | Hover and active/selected surface states. |
| `--bg-code` | Code block background (outside of syntax-highlighted tokens). |
| `--text-primary` | Body text and headings. |
| `--text-secondary` / `--text-tertiary` | Supporting and muted text. |
| `--text-active` | Text color for the active nav item / active states. |
| `--border-color` / `--border-light` / `--border-active` | Dividers, card borders, focus/active borders. |
| `--shadow-sm` / `--shadow-md` / `--shadow-lg` | Elevation for menus, cards, and popovers. Use flat outlines instead of blur for a high-contrast theme (see how `contrast` does this). |

Syntax-highlighted code (the `.codehilite` blocks Pygments generates at build time) is colored separately, under `.codehilite .k`, `.codehilite .s`, and so on in `premium.css`. The default token colors are tuned for light backgrounds and are shared by Light/Sepia; if your new theme is dark-family, add a `[data-theme="yourtheme"] .codehilite ...` override block the same way `[data-theme="dark"] .codehilite ...` does, so keywords and strings stay legible against a dark background.

## Accessibility notes

- The switcher menu is a proper `role="menu"` with `role="menuitemradio"` items, arrow-key navigation, and an `aria-checked` state — it's fully usable without a mouse.
- `prefers-reduced-motion` is respected site-wide; theme changes don't add any motion beyond the existing color/background transition, which is itself disabled for readers who've asked for reduced motion.
- High Contrast exists specifically for readers who need it — treat it as a first-class theme, not an afterthought, when you touch shared components.

## See Also

- [Configuration Guide](configuration.md) — the rest of `smartgen.yml`, including the `theme.palette` brand-color override.
- [Customization Guide](customization.md) — customizing templates and layout beyond color.
