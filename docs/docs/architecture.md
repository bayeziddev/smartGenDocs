# SmartGen Docs Architecture

SmartGen Docs is designed with a modular and extensible architecture, focusing on converting Markdown content into a static, navigable documentation website. Understanding its core components and their interactions is key to customizing and extending the platform. This document outlines the main architectural elements of SmartGen Docs.

## Core Components

The SmartGen Docs system is primarily composed of the following Python modules, each responsible for a specific part of the documentation generation pipeline:

### 1. `cli.py` (Command-Line Interface)

*   **Purpose**: Provides the entry point for user interaction through the terminal. It defines commands such as `init`, `build`, `serve`, `scaffold`, `autodoc`, and `render-changelog`.
*   **Functionality**: Parses command-line arguments, dispatches tasks to the appropriate core components, and handles user feedback.
*   **Key Interaction**: Acts as the orchestrator, invoking other modules based on user commands.

### 2. `core.py` (Builder and Development Server)

*   **Purpose**: Contains the `Builder` class, responsible for the entire site generation process, and the `DevServer` for local development with live reloading.
*   **`Builder` Functionality**: 
    *   Loads `smartgen.yml` configuration.
    *   Recursively processes the navigation structure defined in `smartgen.yml`.
    *   Reads Markdown files from the `docs/` directory.
    *   Converts Markdown to HTML using `MarkdownConverter`.
    *   Renders HTML content into Jinja2 templates (`page.html`, `page_premium.html`).
    *   Resolves internal links and static asset paths using `PathResolver`.
    *   Outputs the final static HTML files to the `site/` directory.
*   **`DevServer` Functionality**: Starts a local web server, monitors changes in Markdown files and `smartgen.yml`, and triggers live reloads in the browser during development.
*   **Key Interaction**: Integrates `MarkdownConverter`, `PathResolver`, and `ThemeEngine` to produce the final website.

### 3. `converter.py` (Markdown to HTML Conversion)

*   **Purpose**: Handles the conversion of Markdown text into HTML.
*   **Functionality**: Utilizes the `markdown2` library with various extensions (e.g., fenced code blocks, tables, header IDs, TOC) to accurately parse and render Markdown syntax into HTML fragments.
*   **Key Interaction**: Used by the `Builder` to transform raw Markdown content into web-ready HTML.

### 4. `path_resolver.py` (Path and URL Resolution)

*   **Purpose**: Manages the resolution of relative and absolute paths within the generated documentation, ensuring correct linking across pages and to static assets.
*   **Functionality**: Provides methods to calculate page depth, normalize paths, and generate correct relative URLs for navigation links, breadcrumbs, and static files, regardless of the current page's location.
*   **Key Interaction**: Crucial for maintaining proper navigation and asset loading, especially in nested directory structures.

### 5. `theme_engine.py` (Templating and Theming)

*   **Purpose**: Manages the application of themes and rendering of HTML pages using Jinja2 templates.
*   **Functionality**: Loads Jinja2 templates (e.g., `base.html`, `page.html`) and injects converted Markdown content, navigation data, and configuration settings into them. Supports different themes (e.g., `default`, `premium`).
*   **Key Interaction**: Works closely with the `Builder` to wrap the generated HTML content within the chosen theme's layout.

### 6. `scaffold.py` (Project Scaffolding)

*   **Purpose**: Automates the creation of initial project structure and placeholder Markdown files based on the `smartgen.yml` navigation.
*   **Functionality**: Reads the `nav` section of `smartgen.yml` and creates corresponding directories and `.md` files if they don't already exist, populating them with basic boilerplate content.
*   **Key Interaction**: Primarily used during the `smartgen-docs init` and `smartgen-docs scaffold` commands to ensure a consistent project setup.

### 7. `autodoc.py` (API Documentation Generation)

*   **Purpose**: Generates API reference documentation directly from Python module docstrings.
*   **Functionality**: Inspects Python modules, classes, and functions to extract docstrings and signatures, then formats this information into Markdown files suitable for inclusion in the documentation.
*   **Key Interaction**: Invoked by the `smartgen-docs autodoc` command to keep API documentation synchronized with the codebase.

### 8. `changelog_renderer.py` (Changelog Generation)

*   **Purpose**: Renders a structured `changelog.json` file into a human-readable Markdown changelog.
*   **Functionality**: Reads a JSON file containing release information and formats it into a Markdown file, typically `docs/docs/changelog.md`.
*   **Key Interaction**: Used by the `smartgen-docs render-changelog` command to automate changelog updates.

## Data Flow and Processing

The typical workflow in SmartGen Docs follows this sequence:

1.  **Configuration Loading**: The `Builder` in `core.py` loads `smartgen.yml` to understand site-wide settings and navigation.
2.  **Markdown Reading**: For each page defined in the navigation, the `Builder` reads the corresponding `.md` file from the `docs/` directory.
3.  **Markdown Conversion**: The `MarkdownConverter` in `converter.py` transforms the Markdown content into HTML.
4.  **Template Rendering**: The HTML content, along with navigation data and configuration, is passed to the `ThemeEngine` (using Jinja2 templates from `theme_engine.py`) to render the full HTML page.
5.  **Path Resolution**: During template rendering, `PathResolver` ensures all internal links, image paths, and static asset URLs are correctly resolved relative to the output HTML file.
6.  **Site Output**: The final HTML pages, along with copied static assets (CSS, JS, images), are written to the `site/` directory, ready for deployment.

This architecture ensures a clear separation of concerns, making SmartGen Docs robust, maintainable, and easy to extend for future enhancements.
