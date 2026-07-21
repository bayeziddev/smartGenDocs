# Frequently Asked Questions (FAQ)

This section addresses common questions and provides solutions to frequently encountered issues when working with SmartGen Docs. If you don't find the answer to your question here, please refer to the [Troubleshooting Guide](../guides/troubleshooting.md) or open an issue on our [GitHub Repository](https://github.com/bayeziddev/smartGenDocs/issues).

## General Questions

### What is SmartGen Docs?

SmartGen Docs is a lightweight, open-source static site generator designed to help you create professional and responsive documentation websites from Markdown files. It focuses on simplicity, speed, and ease of deployment.

### Is SmartGen Docs free to use?

Yes, SmartGen Docs is open-source and completely free to use under the [MIT License](../about/license.md).

### What are the main benefits of using SmartGen Docs?

Key benefits include:

*   **Simplicity**: Easy to learn and use, especially for those familiar with Markdown.
*   **Speed**: Generates static HTML, resulting in fast-loading websites.
*   **Flexibility**: Customizable themes and a clear project structure.
*   **Open Source**: Community-driven development and transparent codebase.
*   **Deployment**: Easy deployment to various static site hosting platforms like GitHub Pages, Netlify, and Vercel.

### What are the system requirements for SmartGen Docs?

SmartGen Docs requires Python 3.8 or newer and `pip` for installation. No other specific system requirements are typically needed beyond a standard development environment.

## Installation and Setup

### How do I install SmartGen Docs?

You can install SmartGen Docs using `pip`:

```bash
pip install smartgen-docs
```

For detailed instructions, refer to the [Installation Guide](installation.md).

### How do I upgrade SmartGen Docs to the latest version?

To upgrade, use the following `pip` command:

```bash
pip install --upgrade smartgen-docs
```

### What should I do if `smartgen-docs` command is not found after installation?

This usually indicates that the Python scripts directory is not in your system's PATH. Ensure that `pip`'s installation directory is included in your system's PATH environment variable. You might need to restart your terminal after installation.

### Can I use a custom theme with SmartGen Docs?

Yes, SmartGen Docs supports customizable themes using Jinja2 templates. You can modify existing themes or create your own. Refer to the [Customization Guide](../guides/customization.md) for more information.

## Project Structure and Content

### Where should I put my Markdown files?

All your Markdown source files (`.md`) should be placed within the `docs/` directory of your project. You can create subdirectories within `docs/` to organize your content logically.

### How do I add a new page to my documentation?

1.  Create a new Markdown file (e.g., `docs/my-new-page.md`).
2.  Add the new page to the `nav` section of your `smartgen.yml` file to make it appear in the navigation menu. For example:

    ```yaml
    nav:
      - Home: index.md
      - My New Page: my-new-page.md
    ```

### How do I create nested navigation menus?

You can create nested menus in your `smartgen.yml` by defining a dictionary where the key is the parent menu item and the value is a list of its child pages. For example:

```yaml
nav:
  - Home: index.md
  - Parent Section:
      - Child Page 1: parent-section/child-page-1.md
      - Child Page 2: parent-section/child-page-2.md
```

Refer to the [Folder Structure Guide](folder-structure.md) and [Configuration Guide](../guides/configuration.md) for more details.

## Building and Serving

### How do I preview my documentation locally?

Run the following command from your project's root directory:

```bash
smartgen-docs serve
```

This starts a development server with live reloading, accessible at `http://localhost:8000` by default.

### How do I build the static site for deployment?

Execute the `build` command from your project's root directory:

```bash
smartgen-docs build
```

This will generate all static HTML, CSS, and JavaScript files into the `site/` directory.

### Can I deploy my SmartGen Docs site to GitHub Pages?

Yes, SmartGen Docs sites are perfectly suited for GitHub Pages. You can deploy manually or automate the process using GitHub Actions. See the [Deployment Guide](deployment.md) for detailed instructions.
