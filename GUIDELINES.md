# SmartGen Docs Management Guidelines (Premium Edition)

This document provides comprehensive guidelines for managing and extending your **SmartGen Docs** project, a unique documentation platform created by Sayad Md Bayezid Hosan for Smartgen Platform [SmartGenDocs](https://bayeziddev.github.io/smartGenDocs/). This premium edition includes enhanced UI/UX, automated API reference generation, and a web-based content upload manager.

## 1. Installation and Setup

To get started with SmartGen Docs, you can use the provided `setup.sh` script or install it directly via pip. For the upload manager, additional dependencies are required.

### Using `setup.sh` (Recommended for initial setup)

The `setup.sh` script automates the installation of SmartGen Docs and its Python dependencies. It checks for Python 3 and `pip3`, installing `pip3` if necessary, and then installs all required Python packages, including those for the upload manager.

1.  **Navigate to the project root:**

    ```bash
    cd smartgen-docs
    ```

2.  **Make the script executable:**

    ```bash
    chmod +x setup.sh
    ```

3.  **Run the setup script:**

    ```bash
    ./setup.sh
    ```

    The script will guide you through the installation process.

### Manual Installation via Pip

If you prefer to install manually or are integrating SmartGen Docs into an existing Python environment, you can use pip:

```bash
# Ensure you are in the smartgen-docs directory
cd smartgen-docs

pip install "smartgen-docs[full]"
# Or install core and then additional dependencies
pip install smartgen-docs
pip install fastapi uvicorn
```

This command installs SmartGen Docs as a package, making the `smartgen-docs` command available globally in your environment.

## 2. Project Structure

Understanding the project structure is crucial for effective management:

```
smartgen-docs/
├── .github/                  # GitHub Actions workflows for CI/CD
│   └── workflows/
│       └── ci-cd.yml         # Automated build and deployment to GitHub Pages
├── smartgen_docs/            # Core SmartGen Docs application source code
│   ├── __init__.py
│   ├── cli.py                # Command-Line Interface definitions
│   ├── core.py               # Core logic for building the site
│   ├── converter.py          # Markdown to HTML conversion logic
│   ├── server.py             # Development server with live reload
│   ├── autodoc.py            # Automated API documentation generator
│   ├── upload_server.py      # FastAPI application for content upload manager
│   └── themes/               # Default and custom themes
│       └── default/
│           ├── base_premium.html # Premium base Jinja2 template
│           ├── page_premium.html # Premium page-specific Jinja2 template
│           ├── static/       # Static assets (CSS, JS, images)
│               └── css/
│                   └── premium.css
├── docs/                     # Your documentation Markdown files (created by `smartgen-docs init`)
├── site/                     # Generated static website output (after `smartgen-docs build`)
├── tests/                    # Unit tests for the project
├── smartgen.yml              # Project configuration file (created by `smartgen-docs init`)
├── README.md                 # Project README
├── LICENSE                   # MIT License file
└── setup.sh                  # Automated setup script
└── GUIDELINES.md             # This document
```

## 3. Basic Usage

SmartGen Docs provides a simple command-line interface:

### `smartgen-docs init`

Initializes a new SmartGen Docs project in the current directory. It creates a `smartgen.yml` configuration file and a sample `docs/index.md`.

```bash
smartgen-docs init
```

### `smartgen-docs serve [--port <port_number>]`

Starts a local development server with live reloading. Any changes to your Markdown files, configuration, or theme will automatically trigger a rebuild and refresh the browser.

```bash
smartgen-docs serve --port 8000
```

### `smartgen-docs build [--site-dir <output_directory>]`

Generates the complete static documentation site into the specified output directory (default is `site/`). This is the command you'll use to prepare your site for deployment.

```bash
smartgen-docs build
```

### `smartgen-docs autodoc <module_name> [--output <output_directory>]`

Generates API reference documentation in Markdown format from Python module docstrings. The output files will be placed in the specified output directory (default is `docs/api`).

```bash
smartgen-docs autodoc my_project.my_module --output docs/api
```

### `smartgen-docs upload-manager [--port <port_number>]`

Starts a web-based interface for uploading and managing documentation files. This allows non-technical users to easily add Markdown files to the `docs/` directory.

```bash
smartgen-docs upload-manager --port 8001
```

## 4. Configuration (`smartgen.yml`)

The `smartgen.yml` file is the heart of your documentation project. It's a YAML-formatted file that defines your site's metadata and navigation structure.

```yaml
site_name: My SmartGen Docs
site_url: https://www.smartgentools.com/docs
site_author: Sayad Md Bayezid Hosan

nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - API Reference: api/my_project.my_module.md
  - Advanced Topics: advanced/index.md
```

*   **`site_name`**: The title of your documentation site.
*   **`site_url`**: The base URL where your site will be hosted.
*   **`site_author`**: The author of the documentation.
*   **`nav`**: Defines the navigation structure. Each item is a key-value pair where the key is the display name and the value is the path to the Markdown file (relative to the `docs/` directory).

## 5. Theming and Customization (Premium UI/UX)

SmartGen Docs now features a premium, GitHub/Manus-inspired UI/UX with dark/light mode support. It uses Jinja2 for templating and a dedicated `premium.css` for styling.

*   **Templates**: The core templates are located in `smartgen_docs/themes/default/`.
    *   `base_premium.html`: The main layout, including header, footer, sidebar, search, and theme toggle.
    *   `page_premium.html`: Extends `base_premium.html` and renders the Markdown content.

*   **Styling**: The premium styles are in `smartgen_docs/themes/default/static/css/premium.css`. This file includes variables for easy color customization and responsive design.

*   **Dark/Light Mode**: A toggle button in the header allows users to switch between dark and light themes, with their preference saved locally.

*   **Search**: Client-side search functionality is integrated into the header, allowing instant filtering of navigation links.

*   **Code Blocks**: Enhanced code block styling with syntax highlighting and a convenient "Copy" button.

## 6. CI/CD with GitHub Actions

A GitHub Actions workflow (`.github/workflows/ci-cd.yml`) is set up to automate the building and deployment of your documentation to GitHub Pages.

### Workflow Overview

*   **Trigger**: The workflow runs automatically on every `push` to the `main` branch or can be manually triggered via `workflow_dispatch`.
*   **Steps**:
    1.  **Checkout repository**: Fetches your code.
    2.  **Set up Python**: Configures the Python environment.
    3.  **Install dependencies**: Installs `markdown2`, `Jinja2`, `PyYAML`, `click`, `watchdog`, `fastapi`, and `uvicorn`.
    4.  **Install SmartGen Docs**: Installs the `smartgen-docs` package in editable mode.
    5.  **Initialize and Build**: Runs `smartgen-docs init` (if `smartgen.yml` doesn't exist) and `smartgen-docs build` to generate the static site into the `site/` directory.
    6.  **Deploy to GitHub Pages**: Uses `peaceiris/actions-gh-pages@v3` to publish the contents of the `site/` directory to the `gh-pages` branch of your repository. This branch is then served by GitHub Pages.

### How to Use

1.  **Enable GitHub Pages**: Go to your GitHub repository settings, navigate to the GitHub Pages section, and select the `gh-pages` branch as the source for your deployment. Ensure the root directory is selected.
2.  **Push to `main`**: Any push to your `main` branch will automatically trigger the workflow, build your documentation, and deploy it to your GitHub Pages URL (e.g., `https://bayeziddev.github.io/smartGenDocs/`).

## 7. Live Website Feature and Management

Once deployed to GitHub Pages, your documentation becomes a live website. Here's how to manage it:

*   **Automatic Updates**: By leveraging the CI/CD pipeline, every change pushed to your `main` branch will automatically update your live website within minutes.
*   **Custom Domains**: GitHub Pages supports custom domains. You can configure this in your repository settings under the "Pages" section. You'll need to add a `CNAME` file to your `docs` directory (e.g., `echo "docs.smartgentools.com" > docs/CNAME`) and configure your DNS provider.
*   **Version Control**: All changes are tracked in your Git repository, providing a full history and the ability to revert to previous versions if needed.
*   **Accessibility**: Ensure your Markdown content is well-structured and uses semantic HTML (which `markdown2` helps with) for better accessibility.

## 8. Extending SmartGen Docs

### Adding New Features

As SmartGen Docs is open-source, you can extend its functionality:

1.  **Modify Core Logic**: Edit files in `smartgen_docs/` (e.g., `core.py`, `converter.py`, `server.py`, `autodoc.py`, `upload_server.py`) to add new features or modify existing behavior.
2.  **Create Custom Themes**: Develop new themes in `smartgen_docs/themes/` to completely change the look and feel. You would then need to update `core.py` to allow selecting different themes via `smartgen.yml`.
3.  **Enhance CLI**: Add new commands or options to `smartgen_docs/cli.py` using the `click` framework.

### Contributing Back

If you develop a useful feature or fix a bug, consider contributing back to the main SmartGen Docs project by submitting a Pull Request on GitHub. This helps improve the tool for everyone.

## 9. Troubleshooting

*   **Installation Issues**: If `pip install` fails, ensure your Python environment is correctly set up and that you have the necessary build tools (e.g., `python3-dev` on Debian/Ubuntu).
*   **Build Errors**: Check the console output of `smartgen-docs build` for specific error messages. Often, these relate to malformed Markdown or incorrect paths in `smartgen.yml`.
*   **Live Server Not Refreshing**: Ensure `watchdog` is correctly installed and that your `smartgen.yml` and Markdown files are being saved in the directories being watched.
*   **GitHub Pages Not Updating**: Check the "Actions" tab in your GitHub repository to see if the CI/CD workflow ran successfully. Look for any errors in the deployment step. Also, verify your GitHub Pages settings.

By following these guidelines, you can effectively manage, extend, and deploy your documentation using SmartGen Docs.
