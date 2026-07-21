# Release Notes

This section provides a summary of major releases for SmartGen Docs, highlighting new features, improvements, and important bug fixes. For a detailed historical record of all changes, please refer to the [Changelog](changelog.md).

## Version 1.0.0 (Initial Release)

**Release Date**: [Insert Date of 1.0.0 Release Here]

### New Features

*   **Core Static Site Generation**: Initial implementation of converting Markdown files to static HTML.
*   **YAML Configuration**: Introduction of `smartgen.yml` for basic site configuration and navigation.
*   **Markdown Support**: Basic Markdown parsing with support for headings, lists, and paragraphs.
*   **CLI Tools**: `init`, `build`, and `serve` commands for project management and local development.
*   **Default Theme**: A basic, functional theme for documentation display.

### Improvements

*   Initial project scaffolding for quick setup.
*   Basic error handling for file operations.

### Bug Fixes

*   Resolved minor parsing issues with complex Markdown structures.

## Version 1.1.0 (Enhanced Theming and Content Features)

**Release Date**: [Insert Date of 1.1.0 Release Here]

### New Features

*   **Premium Theme**: Introduction of an advanced `premium` theme with dark/light mode and improved aesthetics.
*   **Extended Markdown**: Added support for fenced code blocks, tables, header IDs, and task lists.
*   **Path Resolver**: Implemented intelligent path resolution for internal links and static assets.
*   **Jinja2 Templating**: Enhanced theming capabilities using Jinja2 for more flexible layout customization.

### Improvements

*   Improved build performance for larger documentation sites.
*   More robust handling of nested navigation structures.
*   Better error messages for configuration issues.

### Bug Fixes

*   Fixed issues with relative paths in deeply nested documentation pages.
*   Addressed styling inconsistencies in the default theme.

## Version 1.2.0 (Developer Tools and Automation)

**Release Date**: [Insert Date of 1.2.0 Release Here]

### New Features

*   **API Auto-Generation (`autodoc`)**: Command to automatically generate API reference documentation from Python docstrings.
*   **Changelog Renderer**: Tool to convert `changelog.json` into a Markdown changelog page.
*   **Scaffolding Command**: `scaffold` command to auto-generate missing Markdown files based on `smartgen.yml`.
*   **Upload Manager**: Web-based interface for easier content management (requires FastAPI and Uvicorn).

### Improvements

*   Enhanced CLI for better user experience and more informative output.
*   Improved documentation for core components and usage.

### Bug Fixes

*   Resolved issues with `autodoc` not correctly parsing certain Python constructs.
*   Fixed minor bugs in the `serve` command's live reloading functionality.

## Future Releases

We are continuously working to improve SmartGen Docs. Future releases will focus on:

*   Further theme enhancements and customization options.
*   Expanded integrations with other SmartGen Platform tools.
*   Performance optimizations for very large documentation projects.
*   Community-driven features and improvements.

Stay tuned for updates, and feel free to contribute your ideas and code on our [GitHub Repository](https://github.com/bayeziddev/smartGenDocs).
