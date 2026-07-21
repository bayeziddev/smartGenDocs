title: Beginner Guides - Getting Started with SmartGen Docs
description: A step-by-step beginner's guide to SmartGen Docs. Learn how to install, set up your first project, understand the folder structure, and write your first Markdown documentation page.
keywords: SmartGen Docs beginner, getting started, installation, first project, folder structure, Markdown documentation, static site generator


# Beginner Guides: Your First Steps with SmartGen Docs

Welcome to SmartGen Docs! This section is designed for newcomers, providing a gentle introduction and step-by-step instructions to get your first documentation site up and running. By the end of these guides, you'll have a foundational understanding of SmartGen Docs and be ready to create your own comprehensive project documentation.

## 1. What is SmartGen Docs?

SmartGen Docs is a lightweight, open-source static site generator specifically designed for project documentation. It transforms simple Markdown files into elegant, responsive, and easily navigable documentation websites. Key features include:

*   **Markdown-centric**: Write your content in familiar Markdown syntax.
*   **Static Site Generation**: Produces fast, secure, and deployable HTML, CSS, and JavaScript files.
*   **Customizable Themes**: Tailor the look and feel to match your brand.
*   **Command-Line Interface (CLI)**: Manage your project with simple commands.
*   **Extensible**: Support for plugins to add advanced functionalities like API autodoc and search.

## 2. Installation

SmartGen Docs is a Python-based tool and can be easily installed using `pip`.

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system. You can check your Python version by running:

```bash
python3 --version
```

### Installation Steps

1.  **Open your terminal or command prompt.**
2.  **Install SmartGen Docs using pip:**

    ```bash
    pip install smartgen-docs
    ```

    If you encounter permission errors, you might need to use `pip install --user smartgen-docs` or `sudo pip install smartgen-docs` (use `sudo` with caution).

3.  **Verify Installation**: After installation, you can verify that SmartGen Docs is correctly installed by checking its version:

    ```bash
    smartgen-docs --version
    ```

    This should output the installed version of SmartGen Docs.

## 3. Creating Your First Project

Now that SmartGen Docs is installed, let's create your first documentation project.

1.  **Choose a directory**: Navigate to the directory where you want to create your new project.

    ```bash
    cd ~/Documents/projects
    ```

2.  **Initialize a new project**: Use the `init` command followed by your desired project name.

    ```bash
    smartgen-docs init my-first-docs
    ```

    This command will create a new directory named `my-first-docs` (or whatever name you chose) and populate it with a basic project structure.

## 4. Understanding the Project Structure

After initialization, your `my-first-docs` directory will contain the following key elements:

```
my-first-docs/
├── smartgen.yml
└── docs/
    └── index.md
```

*   **`smartgen.yml`**: This is the main configuration file for your SmartGen Docs project. It defines your site's title, navigation, theme settings, and more. You'll spend a lot of time customizing this file.
*   **`docs/`**: This directory is where all your Markdown documentation files reside. Each Markdown file (`.md`) will be converted into an HTML page in your final documentation site.
*   **`docs/index.md`**: This is the default home page for your documentation. You can edit this file to add your project's introduction.

## 5. Writing Your First Documentation Page

SmartGen Docs uses Markdown for content creation, making it easy to write and maintain your documentation.

1.  **Open `docs/index.md`**: Use your favorite text editor to open the `docs/index.md` file.

2.  **Edit the content**: You'll see some default content. Let's change it to something more specific to your project.

    ```markdown
    # Welcome to My First SmartGen Docs Project!

    This is the home page for my new documentation site, built with SmartGen Docs.

    ## Getting Started

    *   Explore the navigation on the left.
    *   Check out the [Configuration Guide](../guides/configuration.md) to customize this site.
    *   Learn more about [SmartGen Docs](https://bayeziddev.github.io/smartGenDocs/).
    ```

3.  **Save the file.**

## 6. Previewing Your Documentation

To see your changes and preview your documentation site locally, use the `serve` command:

1.  **Navigate to your project directory**:

    ```bash
    cd my-first-docs
    ```

2.  **Start the development server**:

    ```bash
    smartgen-docs serve
    ```

    SmartGen Docs will start a local web server, usually accessible at `http://127.0.0.1:8000`. It will also automatically rebuild and refresh your browser whenever you save changes to your Markdown files or `smartgen.yml`.

3.  **Open in browser**: Open your web browser and navigate to the address provided by the `serve` command (e.g., `http://127.00.1:8000`). You should see your newly updated documentation site!

Congratulations! You've successfully installed SmartGen Docs, created your first project, written content, and previewed your documentation. You are now ready to explore more advanced features and build comprehensive documentation for your projects.

## See Also

*   [Configuration Guide](../guides/configuration.md)
*   [CLI Reference](../guides/cli.md)
*   [SmartGen Docs GitHub Repository](https://github.com/bayeziddev/smartGenDocs)
*   [SmartGen Platform](https://www.smartgentools.com) - Discover more tools from the SmartGen Platform.
