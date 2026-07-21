# Command-Line Interface (CLI) Reference

The SmartGen Docs Command-Line Interface (CLI) is your primary tool for interacting with the documentation generator. It allows you to initialize new projects, build your documentation site, serve it locally for development, and perform various utility tasks. This guide provides a comprehensive overview of all available CLI commands and their usage.

## Basic Usage

All SmartGen Docs commands start with `smartgen-docs` followed by the specific command and its arguments or options.

```bash
smartgen-docs <command> [options]
```

To get help for any command, you can use the `--help` flag:

```bash
smartgen-docs --help
smartgen-docs <command> --help
```

## Available Commands

### 1. `smartgen-docs init`

Initializes a new SmartGen Docs project in the current directory. This command sets up the basic directory structure and creates a default `smartgen.yml` configuration file.

*   **Usage**: `smartgen-docs init`
*   **Options**:
    *   `--force`: Overwrite existing files if they conflict with the new project structure.

#### Example

```bash
# Initialize a new project
smartgen-docs init

# Initialize and overwrite existing files if any conflicts
smartgen-docs init --force
```

### 2. `smartgen-docs build`

Builds the static HTML documentation site from your Markdown source files and `smartgen.yml` configuration. The generated site will be placed in the `site/` directory.

*   **Usage**: `smartgen-docs build`
*   **Options**:
    *   `--clean`: Remove the `site/` directory before building.
    *   `--strict`: Treat warnings as errors.
    *   `--verbose`: Enable verbose output.

#### Example

```bash
# Build the documentation site
smartgen-docs build

# Clean the site directory and then build
smartgen-docs build --clean
```

### 3. `smartgen-docs serve`

Starts a local development server with live reloading. This allows you to preview your documentation in real-time as you make changes to your Markdown files or `smartgen.yml`.

*   **Usage**: `smartgen-docs serve`
*   **Options**:
    *   `--host <address>`: Specify the host address for the server (default: `127.0.0.1`).
    *   `--port <port>`: Specify the port for the server (default: `8000`).
    *   `--livereload-port <port>`: Specify the port for the live reload server (default: `8001`).
    *   `--dev-addr <address:port>`: Shorthand for `--host` and `--port`.

#### Example

```bash
# Start the development server on default host and port
smartgen-docs serve

# Start the server on a specific port
smartgen-docs serve --port 8080

# Start the server on a specific address and port
smartgen-docs serve --dev-addr 0.0.0.0:8000
```

### 4. `smartgen-docs scaffold`

Automatically generates missing Markdown files and directories based on the navigation structure defined in your `smartgen.yml` file. This helps ensure that all pages listed in your navigation have corresponding content files.

*   **Usage**: `smartgen-docs scaffold`

#### Example

```bash
# Scaffold missing documentation files
smartgen-docs scaffold
```

### 5. `smartgen-docs autodoc`

Generates API reference documentation from Python docstrings. This command scans your specified Python source directories and creates Markdown files with API documentation, which can then be included in your site.

*   **Usage**: `smartgen-docs autodoc [options]`
*   **Options**:
    *   `--source-dir <path>`: The directory containing your Python source code (default: `smartgen_docs`).
    *   `--output-dir <path>`: The directory where generated Markdown files will be saved (default: `docs/api/modules`).
    *   `--exclude <pattern>`: A glob pattern to exclude files or directories from processing (can be used multiple times).

#### Example

```bash
# Generate API documentation from smartgen_docs directory
smartgen-docs autodoc

# Generate API documentation from a specific source and output directory
smartgen-docs autodoc --source-dir my_project/src --output-dir docs/reference

# Generate API documentation excluding a specific file
smartgen-docs autodoc --exclude "smartgen_docs/cli.py"
```

### 6. `smartgen-docs render-changelog`

Renders a JSON changelog file into a Markdown formatted changelog page. This command is useful for maintaining an up-to-date and easily readable changelog within your documentation.

*   **Usage**: `smartgen-docs render-changelog [options]`
*   **Options**:
    *   `--json-path <path>`: The path to your JSON changelog file (default: `data/changelog.json`).
    *   `--output <path>`: The path where the Markdown changelog will be saved (default: `docs/docs/changelog.md`).

#### Example

```bash
# Render the default changelog.json to Markdown
smartgen-docs render-changelog

# Render a custom changelog file to a specific output path
smartgen-docs render-changelog --json-path my_project/changelog.json --output docs/updates/project_changelog.md
```

## Next Steps

For more detailed information on specific plugins and their configurations, refer to the [Autodoc Guide](autodoc.md) and the [Configuration Guide](configuration.md).
