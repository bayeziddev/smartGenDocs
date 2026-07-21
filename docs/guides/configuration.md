# Configuration Guide

The `smartgen.yml` file is the central configuration hub for your SmartGen Docs project. It defines everything from your site's metadata and navigation structure to its visual theme and various build settings. A well-structured `smartgen.yml` is crucial for creating a functional and user-friendly documentation site.

This guide will walk you through the essential sections and parameters of the `smartgen.yml` file, explaining how to customize your documentation site to meet your specific needs.

## `smartgen.yml` Structure Overview

The `smartgen.yml` file uses YAML (YAML Ain't Markup Language) syntax, which is human-readable and ideal for configuration files. It typically contains the following top-level sections:

*   **`site_name`**: The title of your documentation site.
*   **`site_url`**: The base URL where your documentation will be hosted.
*   **`site_author`**: The author of the documentation.
*   **`site_description`**: A brief description of your documentation site for SEO and general information.
*   **`repo_url`**: The URL of your project's source code repository (e.g., GitHub).
*   **`repo_name`**: The name of your repository (e.g., `GitHub`).
*   **`edit_uri`**: The base URI for editing pages, often pointing to your repository's `edit` functionality.
*   **`theme`**: Configuration for the visual theme of your site.
*   **`nav`**: Defines the navigation structure and order of your documentation pages.
*   **`plugins`**: Enables and configures various plugins for extended functionality.
*   **`extra`**: A section for any additional custom variables or settings you might need.

## Essential Configuration Parameters

### 1. Site Metadata

These parameters define the basic information about your documentation site.

```yaml
site_name: My Awesome Project Docs
site_url: https://docs.myawesomeproject.com
site_author: John Doe
site_description: Comprehensive documentation for My Awesome Project.
repo_url: https://github.com/myuser/myawesomeproject
repo_name: GitHub
edit_uri: edit/main/docs/
```

*   **`site_name`**: This will appear in the browser tab title and often in the site header.
*   **`site_url`**: Important for generating correct absolute links and for SEO.
*   **`site_author`**: The primary author or organization responsible for the documentation.
*   **`site_description`**: A short, descriptive summary of your project. This is often used in search engine results.
*   **`repo_url`**: A link to your project's source code repository. SmartGen Docs themes often use this to display a link to the repository.
*   **`repo_name`**: The display name for the repository link (e.g., 
`GitHub`).
*   **`edit_uri`**: This is used to construct 
links to allow users to edit documentation pages directly in your repository. The value should be the path to your `docs/` directory within your repository, relative to the repository root (e.g., `edit/main/docs/` for a `main` branch).

### 2. Theme Configuration

The `theme` section allows you to control the visual appearance of your documentation site. SmartGen Docs supports multiple themes, and you can customize various aspects of the selected theme.

```yaml
theme:
  name: premium # or 'default'
  custom_dir: smartgen_docs/themes/default # Path to your custom theme directory
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: deep purple
      accent: amber
      toggle:
        icon: material/weather-sunny
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: deep purple
      accent: amber
      toggle:
        icon: material/weather-night
        name: Switch to light mode
  font:
    text: Roboto
    code: Roboto Mono
  favicon: assets/favicon.png
  logo: assets/logo.png
  features:
    - navigation.tabs
    - navigation.sections
    - search.suggest
    - search.highlight
    - toc.integrate
    - header.autohide
    - content.tabs.link
    - content.code.copy
  icon:
    repo: fontawesome/brands/github
  analytics:
    provider: google
    property: G-XXXXXXXXXX
  extra_css:
    - stylesheets/extra.css
  extra_javascript:
    - javascripts/extra.js
```

*   **`name`**: Specifies the theme to use. SmartGen Docs typically provides `default` and `premium` themes. The `premium` theme offers more advanced features like dark mode.
*   **`custom_dir`**: If you have created a custom theme or modified an existing one, specify the path to its directory here. This allows SmartGen Docs to find your custom templates and assets.
*   **`palette`**: Configures the color scheme for your site, including support for light and dark modes based on user preferences. You can define `primary` and `accent` colors, as well as icons and names for the theme toggle.
*   **`font`**: Sets the primary text and code fonts for your documentation. You can use Google Fonts or local fonts.
*   **`favicon`**: Path to your site's favicon.
*   **`logo`**: Path to your site's logo, which typically appears in the header.
*   **`features`**: A list of theme-specific features to enable. These can include navigation styles (tabs, sections), search enhancements, table of contents integration, and code block functionalities.
*   **`icon.repo`**: Sets the icon for your repository link, often using Font Awesome icons.
*   **`analytics`**: Integrates analytics services like Google Analytics. Provide the `provider` and `property` (e.g., `G-XXXXXXXXXX`).
*   **`extra_css`**: A list of additional CSS files to include, allowing for further styling customization.
*   **`extra_javascript`**: A list of additional JavaScript files to include, enabling custom interactive features.

For more details on customizing themes, refer to the [Theming Guide](theming.md).

### 3. Navigation (`nav`)

The `nav` section is arguably the most important part of your `smartgen.yml` as it defines the entire structure and order of your documentation's navigation menu. It uses a hierarchical list to represent sections and individual pages.

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Introduction: getting-started/index.md
    - Installation: getting-started/installation.md
    - Quick Start: getting-started/quick-start.md
    - Your First Project: getting-started/first-project.md
    - Folder Structure: getting-started/folder-structure.md
    - Deployment: getting-started/deployment.md
    - FAQ: getting-started/faq.md
  - Documentation:
    - Overview: docs/index.md
    - Platform: docs/platform.md
    - Architecture: docs/architecture.md
    - Features: docs/features.md
    - Concepts: docs/concepts.md
    - Release Notes: docs/releases.md
    - Changelog: docs/changelog.md
  - Guides:
    - Overview: guides/index.md
    - Configuration: guides/configuration.md
    - Theming: guides/theming.md
    - CLI Reference: guides/cli.md
    - Autodoc: guides/autodoc.md
    - Deployment: guides/deployment.md
  - API Reference:
    - Overview: api/index.md
    - Authentication: api/authentication.md
    - REST API: api/rest-api.md
    - Endpoints: api/endpoints.md
    - Error Codes: api/errors.md
    - Rate Limits: api/rate-limits.md
    - Webhooks: api/webhooks.md
  - Contributing: contributing.md
  - License: license.md
```

*   **Top-level items**: These represent main sections in your navigation (e.g., `Home`, `Getting Started`).
*   **Sub-items**: Indented items under a top-level section create sub-menus. The value associated with each item is the path to the Markdown file (relative to the `docs/` directory).
*   **`index.md`**: Using `index.md` within a subdirectory (e.g., `getting-started/index.md`) allows you to have an overview page for that section, which is typically linked when the parent section is clicked.

**Best Practices for `nav`:**

*   **Logical Grouping**: Organize your content into logical sections to improve discoverability.
*   **Clear Naming**: Use descriptive and concise names for your navigation items.
*   **Consistency**: Maintain a consistent hierarchy and naming convention throughout your navigation.

### 4. Plugins

The `plugins` section allows you to extend the functionality of SmartGen Docs by enabling various plugins. Plugins can add new features, modify content processing, or integrate with external tools.

```yaml
plugins:
  - search
  - autodoc
  - changelog_renderer
  - scaffold
  - upload_manager
```

*   **`search`**: Enables the built-in search functionality for your documentation site.
*   **`autodoc`**: Activates the API auto-generation feature, allowing you to generate documentation from Python docstrings. Refer to the [Autodoc Guide](autodoc.md) for configuration details.
*   **`changelog_renderer`**: Enables the plugin that renders a JSON changelog file into a Markdown page. This is what generated the [Changelog](docs/changelog.md) page.
*   **`scaffold`**: Activates the scaffolding plugin, which can automatically create missing Markdown files and directories based on your `nav` configuration.
*   **`upload_manager`**: Enables the web-based Upload Manager for easier content management.

Each plugin might have its own specific configuration options, which would be nested under the plugin's name. For example:

```yaml
plugins:
  - autodoc:
      source_dir: smartgen_docs
      output_dir: api/modules
      exclude:
        - smartgen_docs/cli.py
```

### 5. Extra Variables (`extra`)

The `extra` section is a flexible area where you can define any custom variables or settings that you want to make available in your theme templates. This is useful for adding custom links, social media profiles, or other dynamic content.

```yaml
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/bayeziddev/smartGenDocs
    - icon: fontawesome/brands/twitter
      link: https://twitter.com/bayeziddev
  custom_message: Welcome to the official SmartGen Docs documentation!
```

These variables can then be accessed within your Jinja2 templates (e.g., `{{ config.extra.custom_message }}`).

## Validating Your Configuration

After making changes to `smartgen.yml`, it's always a good idea to validate your configuration to catch any syntax errors or logical inconsistencies. You can do this by running the `smartgen-docs build` command locally. Any errors will be reported in the console.

By mastering the `smartgen.yml` configuration, you gain full control over the structure, appearance, and functionality of your SmartGen Docs site, ensuring it perfectly meets your project's documentation requirements.
