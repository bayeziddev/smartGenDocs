# Theming Guide: Customizing Your SmartGen Docs Appearance

The visual appeal and user experience of your documentation site are significantly influenced by its theme. SmartGen Docs offers powerful theming capabilities, allowing you to customize nearly every aspect of your site\'s appearance, from colors and fonts to layout and interactive elements.

This guide will walk you through selecting a theme, configuring its various options, and implementing advanced customizations to create a documentation site that perfectly aligns with your brand and user needs.

## 1. Theme Selection and Configuration

The primary theme settings are defined within the `theme` section of your `smartgen.yml` file. SmartGen Docs typically provides a `default` theme and a more feature-rich `premium` theme.

### Basic Theme Configuration

```yaml
theme:
  name: premium # Choose \'default\' or \'premium\'
  palette:
    primary: "#0052cc" # Primary brand color
    accent: "#ff9900" # Accent color for highlights
  font:
    text: Roboto # Font for general text
    code: Roboto Mono # Font for code blocks
  favicon: assets/favicon.png # Path to your favicon
  logo: assets/logo.png # Path to your site logo
```

*   **`name`**: Specifies which base theme to use. The `premium` theme often includes advanced features like built-in dark mode support and more sophisticated navigation options.
*   **`palette`**: Defines the color scheme. You can set `primary` and `accent` colors using hexadecimal codes or CSS color names. These colors are used throughout the theme for elements like headers, links, and highlights.
*   **`font`**: Allows you to specify custom fonts for both general text (`text`) and code blocks (`code`). You can use web-safe fonts or link to Google Fonts (which might require additional `extra_css` or `extra_javascript` to import).
*   **`favicon`**: The path to your site\'s favicon, a small icon that appears in browser tabs and bookmarks.
*   **`logo`**: The path to your site\'s logo image, typically displayed in the header of your documentation.

### Advanced Palette Configuration (Light/Dark Mode)

The `premium` theme often supports sophisticated light and dark mode switching. You can configure distinct palettes for each mode, allowing users to toggle between them based on their system preferences or a manual switch.

```yaml
theme:
  name: premium
  palette:
    - media: "(prefers-color-scheme: light)" # Applies when system prefers light mode
      scheme: default
      primary: deep purple
      accent: amber
      toggle:
        icon: material/weather-sunny # Icon for light mode
        name: Switch to dark mode # Text for the toggle button
    - media: "(prefers-color-scheme: dark)" # Applies when system prefers dark mode
      scheme: slate
      primary: deep purple
      accent: amber
      toggle:
        icon: material/weather-night # Icon for dark mode
        name: Switch to light mode # Text for the toggle button
```

This configuration enables automatic switching based on the user\'s operating system settings and provides a toggle button for manual control.

## 2. Customizing with `extra_css` and `extra_javascript`

For more granular control over your site\'s appearance and behavior, you can inject custom CSS and JavaScript files.

### Adding Custom Styles (`extra_css`)

Create a CSS file (e.g., `docs/stylesheets/extra.css`) and reference it in your `smartgen.yml`:

```yaml
theme:
  # ... other theme settings ...
  extra_css:
    - stylesheets/extra.css
```

**`docs/stylesheets/extra.css` example:**

```css
/* Custom styles for SmartGen Docs */
:root {
  --md-primary-fg-color: #1a73e8; /* Override primary color */
  --md-accent-fg-color: #e91e63; /* Override accent color */
}

.md-header {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.md-content h1 {
  border-bottom: 2px solid var(--md-primary-fg-color);
  padding-bottom: 10px;
}
```

This allows you to override existing theme styles or add entirely new ones without modifying the core theme files.

### Adding Custom JavaScript (`extra_javascript`)

Similarly, you can include custom JavaScript files (e.g., `docs/javascripts/extra.js`) for interactive features or third-party integrations:

```yaml
theme:
  # ... other theme settings ...
  extra_javascript:
    - javascripts/extra.js
```

**`docs/javascripts/extra.js` example:**

```javascript
// Custom JavaScript for SmartGen Docs
document.addEventListener(\'DOMContentLoaded\', function() {
  console.log(\'SmartGen Docs custom script loaded!\');
  // Add custom functionality here, e.g., analytics, dynamic content loading
});
```

## 3. Overriding Theme Templates (`custom_dir`)

For the most advanced customizations, you can override individual theme templates. This requires a deeper understanding of Jinja2 templating and the theme\'s file structure.

1.  **Create a custom directory**: Specify a `custom_dir` in your `smartgen.yml` (e.g., `smartgen_docs/themes/custom`).

    ```yaml
theme:
  name: premium
  custom_dir: smartgen_docs/themes/custom
    ```

2.  **Copy and modify templates**: Copy the specific template file you wish to modify from the base theme\'s directory (e.g., `smartgen_docs/themes/premium/main.html`) into your `custom_dir` (e.g., `smartgen_docs/themes/custom/main.html`).

3.  **Make your changes**: Edit the copied template file. SmartGen Docs will prioritize templates found in your `custom_dir` over the default theme files.

This method is powerful but should be used judiciously, as it can make theme updates more challenging. Always start with `extra_css` and `extra_javascript` for simpler customizations.

## 4. Theme Features

Many themes, especially the `premium` theme, offer a variety of features that can be enabled or disabled in your `smartgen.yml`.

```yaml
theme:
  # ...
  features:
    - navigation.tabs # Top-level navigation as tabs
    - navigation.sections # Group pages into sections in the sidebar
    - search.suggest # Autocomplete suggestions in search
    - search.highlight # Highlight search terms in results
    - toc.integrate # Integrate table of contents into the sidebar
    - header.autohide # Hide header on scroll down, show on scroll up
    - content.tabs.link # Linkable tabs within content
    - content.code.copy # Copy button for code blocks
```

Experiment with these features to find the best presentation for your documentation. Each feature enhances usability and navigation in different ways.

## 5. Icons and Analytics

### Custom Icons

You can specify icons for various elements, such as your repository link, using Font Awesome icons.

```yaml
theme:
  # ...
  icon:
    repo: fontawesome/brands/github # GitHub icon for repository link
```

### Analytics Integration

Integrate web analytics services to track user engagement and site performance.

```yaml
theme:
  # ...
  analytics:
    provider: google # e.g., \'google\'
    property: G-XXXXXXXXXX # Your Google Analytics tracking ID
```

This will automatically inject the necessary tracking code into your site.

By leveraging the extensive theming options in SmartGen Docs, you can create a highly polished, branded, and user-friendly documentation experience that stands out.

## See Also

*   [Configuration Guide](configuration.md)
*   [SmartGen Docs GitHub Repository](https://github.com/bayeziddev/smartGenDocs)
*   [SmartGen Platform](https://www.smartgentools.com) - Discover more tools from the SmartGen Platform.
