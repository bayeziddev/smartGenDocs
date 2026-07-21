# Project Folder Structure

Understanding the recommended folder structure is crucial for organizing your SmartGen Docs project effectively. A well-structured project ensures maintainability, scalability, and ease of navigation for both developers and users. This guide outlines the typical layout of a SmartGen Docs project and explains the purpose of each directory and file.

## Core Project Structure

After initializing a new project with `smartgen-docs init` and building it with `smartgen-docs build`, your project directory will generally look like this:

```
. 
├── smartgen.yml          # Main configuration file for your SmartGen Docs project
├── docs/                 # Contains all your source Markdown documentation files
│   ├── index.md          # The homepage of your documentation site
│   ├── getting-started/  # Directory for guides on getting started
│   │   ├── index.md      # Overview for the getting started section
│   │   ├── installation.md # Installation instructions
│   │   ├── quick-start.md  # Quick start guide
│   │   └── first-project.md # Guide to your first project
│   ├── api/              # API Reference documentation
│   │   └── index.md      # Overview for the API reference
│   └── ...               # Other documentation sections (e.g., guides, tutorials)
└── site/                 # Output directory for the generated static website
    ├── index.html        # The generated homepage
    ├── getting-started/  # Generated HTML files for getting started guides
    │   ├── index.html
    │   ├── installation.html
    │   └── ...
    └── ...               # Other generated HTML files and assets
```

## Explanation of Directories and Files

### `smartgen.yml`

This is the central configuration file for your SmartGen Docs project. It is written in YAML format and controls various aspects of your documentation site, including:

*   **`site_name`**: The title of your documentation site.
*   **`site_url`**: The base URL where your documentation will be hosted.
*   **`site_author`**: The author of the documentation.
*   **`site_description`**: A brief description for SEO purposes.
*   **`theme`**: Specifies the theme to be used (e.g., `default`, `premium`) and allows for palette and font customization.
*   **`nav`**: Defines the navigation structure of your documentation. This is where you link your Markdown files to create the menu hierarchy.

For more details on configuring your project, refer to the [Configuration Guide](../guides/configuration.md).

### `docs/` Directory

This directory is where all your Markdown source files (`.md`) are stored. Each Markdown file within this directory (and its subdirectories) will be processed by SmartGen Docs and converted into an HTML page in the final static site. The structure you create within the `docs/` directory often mirrors the navigation structure defined in `smartgen.yml`.

*   **`index.md`**: This file is typically the main entry point or homepage of your documentation. It provides an overview of your project.
*   **Subdirectories (e.g., `getting-started/`, `api/`, `guides/`)**: These are used to logically group related documentation pages. For instance, all guides related to getting started are placed in `docs/getting-started/`.

### `site/` Directory

This directory is automatically generated when you run the `smartgen-docs build` command. It contains the complete static website, including:

*   **HTML Files**: Each Markdown file from the `docs/` directory is converted into a corresponding HTML file (e.g., `docs/installation.md` becomes `site/installation.html`).
*   **CSS and JavaScript Assets**: The `site/` directory also includes all the necessary CSS stylesheets and JavaScript files required for your documentation site to function and display correctly.
*   **Static Assets**: Any other static assets (like images, favicons) defined in your theme or copied manually will also reside here.

**Important**: The `site/` directory should generally not be manually edited, as its contents are overwritten each time you run `smartgen-docs build`. It is intended for deployment purposes.

## Best Practices for Organization

*   **Logical Grouping**: Organize your Markdown files into logical categories using subdirectories within `docs/`. This makes it easier to find and manage content.
*   **Consistent Naming**: Use consistent and descriptive filenames for your Markdown files (e.g., `installation.md`, `api-overview.md`).
*   **Update `smartgen.yml`**: Always ensure that your `smartgen.yml` file accurately reflects the structure of your `docs/` directory and provides a clear navigation path for your users.

By adhering to this folder structure, you can maintain a clean, organized, and easily navigable documentation project with SmartGen Docs.
