---
title: CLI Reference - SmartGen Docs Command-Line Interface
description: A comprehensive reference for the SmartGen Docs Command-Line Interface (CLI). Learn how to use CLI commands for project initialization, building, serving, and managing your documentation site.
keywords: SmartGen Docs CLI, command-line interface, smartgen-docs, build, serve, init, deploy, documentation tools
---

# CLI Reference: SmartGen Docs Command-Line Interface

The SmartGen Docs Command-Line Interface (CLI) is your primary tool for interacting with and managing your documentation projects. It provides a set of powerful commands to initialize new projects, build your documentation, serve it locally for development, and perform other essential tasks.

This guide provides a comprehensive reference for all available CLI commands, their options, and practical usage examples.

## Installation

Before using the CLI, ensure SmartGen Docs is installed. If you haven't already, you can install it via pip:

```bash
pip install smartgen-docs
```

Once installed, the `smartgen-docs` command will be available in your terminal.

## General Command Structure

All SmartGen Docs CLI commands follow a similar structure:

```bash
smartgen-docs <command> [options] [arguments]
```

*   **`<command>`**: The specific action you want to perform (e.g., `init`, `build`, `serve`).
*   **`[options]`**: Optional flags that modify the behavior of the command (e.g., `--clean`, `--verbose`).
*   **`[arguments]`**: Additional parameters required by the command (e.g., a project name).

## Available Commands

### 1. `smartgen-docs init <project_name>`

Initializes a new SmartGen Docs project with a basic directory structure and a default `smartgen.yml` configuration file.

```bash
smartgen-docs init my-new-docs
```

This command creates a new directory named `my-new-docs` (or whatever `project_name` you provide) and populates it with essential files, including:

*   `smartgen.yml`: The main configuration file.
*   `docs/`: Directory for your Markdown documentation files.
*   `docs/index.md`: A sample home page.

**Options:**

*   `--template <template_name>`: Specify a custom template for initialization (e.g., `smartgen-docs init --template advanced my-advanced-docs`).
*   `--force`: Overwrite existing files if the project directory is not empty.

### 2. `smartgen-docs build`

Builds your documentation project into a static HTML website. The generated files are placed in the `site/` directory by default.

```bash
smartgen-docs build
```

This command processes all your Markdown files, applies the chosen theme, generates navigation, and creates a complete static site ready for deployment.

**Options:**

*   `--clean`: Remove the `site/` directory before building to ensure a fresh build.
*   `--strict`: Treat warnings as errors, causing the build to fail if any issues are detected.
*   `--verbose`: Output more detailed information during the build process.
*   `--config <path_to_config>`: Specify an alternative `smartgen.yml` file.
*   `--theme <theme_name>`: Override the theme specified in `smartgen.yml`.

### 3. `smartgen-docs serve`

Starts a local development server to preview your documentation site in real-time. This command automatically rebuilds and reloads your browser whenever you make changes to your Markdown files or `smartgen.yml`.

```bash
smartgen-docs serve
```

By default, the server runs on `http://127.0.0.1:8000`. Open this URL in your web browser to view your documentation.

**Options:**

*   `--host <address>`: Specify the host address (e.g., `0.0.0.0` to make it accessible from other devices on your network).
*   `--port <port_number>`: Specify a different port (e.g., `smartgen-docs serve --port 8080`).
*   `--dev-addr <address:port>`: Equivalent to `--host` and `--port` combined.
*   `--livereload-ignore <pattern>`: Ignore specific files or directories from live reloading.

### 4. `smartgen-docs deploy`

Deploys your built documentation site to a hosting service. The exact behavior of this command depends on configured plugins or deployment scripts.

```bash
smartgen-docs deploy
```

Typically, this command is used in conjunction with a `gh-pages` plugin for GitHub Pages deployment or custom scripts for other platforms.

**Options:**

*   `--message <commit_message>`: Specify a custom commit message for deployment (e.g., for Git-based deployments).

### 5. `smartgen-docs new <path/to/page.md>`

Creates a new Markdown page with a predefined template and adds it to your navigation (if configured to do so by a scaffolding plugin).

```bash
smartgen-docs new docs/guides/my-new-guide.md
```

This command helps maintain consistency in your documentation structure and can pre-fill front matter.

### 6. `smartgen-docs upload`

Launches the web-based Upload Manager, allowing you to easily upload assets (images, files) to your documentation project.

```bash
smartgen-docs upload
```

This command is useful for managing media files without directly interacting with the file system.

## Getting Help

For a quick overview of any command and its options, use the `--help` flag:

```bash
smartgen-docs --help
smartgen-docs build --help
```

This will display detailed usage information directly in your terminal.

## Best Practices for CLI Usage

*   **Work in your project root**: Always run `smartgen-docs` commands from the root directory of your documentation project (where `smartgen.yml` is located).
*   **Use `serve` for development**: Leverage the `smartgen-docs serve` command for real-time feedback during content creation.
*   **Clean builds**: Use `smartgen-docs build --clean` before deploying to ensure no stale files are included.
*   **Version Control**: Keep your entire documentation project, including `smartgen.yml` and all Markdown files, under version control (e.g., Git).

By mastering the SmartGen Docs CLI, you can efficiently manage your documentation workflow, from initial setup to deployment and ongoing maintenance.

## See Also

*   [Configuration Guide](configuration.md)
*   [Deployment Guide](deployment.md)
*   [SmartGen Platform](https://www.smartgentools.com) - Explore other tools from the SmartGen Platform.
