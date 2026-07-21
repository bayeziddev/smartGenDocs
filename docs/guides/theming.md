# Theming Guide

The visual presentation of your documentation is crucial for user experience. SmartGen Docs provides flexible theming capabilities, allowing you to customize the look and feel of your site to match your brand or project aesthetics. This guide will walk you through how to select, configure, and extend themes using Jinja2 templates and CSS.

## 1. Theme Selection

SmartGen Docs comes with built-in themes, typically `default` and `premium`. You select your theme in the `smartgen.yml` configuration file under the `theme` section:

```yaml
theme:
  name: premium # Choose 'default' or 'premium'
```

*   **`default`**: A clean, basic theme that provides essential functionality.
*   **`premium`**: An enhanced theme offering more advanced features like dark mode, improved navigation, and a modern design.

## 2. Customizing with `palette`

The `premium` theme (and potentially others) allows for extensive color customization through the `palette` setting in `smartgen.yml`. This enables you to define color schemes for both light and dark modes.

```yaml
theme:
  name: premium
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: deep purple # Primary color for light mode
      accent: amber        # Accent color for light mode
      toggle:
        icon: material/weather-sunny
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: deep purple # Primary color for dark mode
      accent: amber        # Accent color for dark mode
      toggle:
        icon: material/weather-night
        name: Switch to light mode
```

*   **`media`**: Specifies the media query for when this palette should be active (e.g., `(prefers-color-scheme: light)` for light mode).
*   **`scheme`**: A descriptive name for the color scheme.
*   **`primary`**: The main color used for headers, primary buttons, and other prominent elements.
*   **`accent`**: A secondary color used for highlights, links, and interactive elements.
*   **`toggle`**: Configures the icon and text for the theme switcher button.

## 3. Custom Fonts

You can specify custom fonts for your documentation site using the `font` setting:

```yaml
theme:
  name: premium
  font:
    text: Roboto      # Font for general text
    code: Roboto Mono # Font for code blocks
```

SmartGen Docs will attempt to load these fonts. For web fonts (like Google Fonts), ensure they are correctly linked or imported in your custom CSS.

## 4. Adding Custom CSS and JavaScript

For more advanced styling and interactive features, you can include your own CSS and JavaScript files. These are specified in the `extra_css` and `extra_javascript` sections:

```yaml
theme:
  name: premium
  extra_css:
    - stylesheets/extra.css
  extra_javascript:
    - javascripts/extra.js
```

*   **`extra_css`**: A list of paths to your custom CSS files. These files will be loaded after the theme's default CSS, allowing you to override styles.
*   **`extra_javascript`**: A list of paths to your custom JavaScript files. These scripts will be loaded at the end of the `<body>`, making them suitable for adding interactive elements or custom behaviors.

**Example `stylesheets/extra.css`:**

```css
/* Custom styles to override theme defaults */
:root {
  --md-primary-fg-color: #673ab7; /* Deep Purple */
  --md-accent-fg-color: #ffc107; /* Amber */
}

.md-header {
  box-shadow: 0 2px 4px rgba(0,0,0,.1);
}
```

## 5. Overriding Theme Templates with `custom_dir`

For complete control over the theme's layout and structure, you can override individual Jinja2 templates. This is done by specifying a `custom_dir` in your `smartgen.yml`:

```yaml
theme:
  name: default
  custom_dir: smartgen_docs/themes/my_custom_theme
```

1.  **Create a Custom Directory**: Create a directory (e.g., `smartgen_docs/themes/my_custom_theme`) in your project.
2.  **Copy Templates**: Copy the specific template files you wish to modify from the original theme's directory (e.g., `smartgen_docs/themes/default/base.html`) into your `custom_dir`.
3.  **Make Changes**: Edit the copied template files. SmartGen Docs will prioritize templates found in `custom_dir` over the default theme's templates.

This approach allows you to modify any part of the HTML structure, add new blocks, or change the rendering logic using Jinja2 syntax.

## 6. Favicon and Logo

You can easily set your site's favicon and logo:

```yaml
theme:
  name: premium
  favicon: assets/favicon.png
  logo: assets/logo.png
```

*   **`favicon`**: Path to a `.png`, `.ico`, or `.svg` file that will be used as the site's favicon.
*   **`logo`**: Path to an image file (e.g., `.png`, `.svg`) that will be displayed as the site logo in the header.

Ensure these assets are placed in a publicly accessible directory, typically `docs/assets/` or similar, and the paths are correct relative to your project root.

## 7. Theme Features

The `features` setting allows you to enable or disable specific functionalities provided by the theme. These can greatly enhance the user experience.

```yaml
theme:
  name: premium
  features:
    - navigation.tabs       # Top-level navigation as tabs
    - navigation.sections   # Collapsible sections in sidebar
    - search.suggest        # Search suggestions as you type
    - search.highlight      # Highlight search results on page
    - toc.integrate         # Integrate table of contents into sidebar
    - header.autohide       # Header hides on scroll down, reappears on scroll up
    - content.tabs.link     # Allow linking directly to content tabs
    - content.code.copy     # Add a copy button to code blocks
```

Refer to the theme's documentation (or experiment) to understand the full range of available features and their impact on your site.

By leveraging these theming options, you can create a highly customized and visually appealing documentation site with SmartGen Docs that perfectly aligns with your project's identity.
