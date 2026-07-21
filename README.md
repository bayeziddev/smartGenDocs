# SmartGen Docs
[Live Demu Smartgen Docs](https://bayeziddev.github.io/smartGenDocs/)

---
[SmartGen Changelog](https://bayeziddev.github.io/smartGenDocs/docs/docs/changelog)

**SmartGen Docs** is a lightweight, open-source static site generator designed specifically for project documentation. Built from the ground up by **Sayad Md Bayezid Hosan** for the **Smartgen Platform (www.smartgentools.com)**, it offers a simple yet powerful way to transform Markdown files into elegant, responsive documentation websites.

## Features

*   **Markdown-centric**: Write your documentation in clean, easy-to-read Markdown.
*   **Static Site Generation**: Generates a complete static HTML website, ready for deployment on any web server.
*   **YAML Configuration**: Simple `smartgen.yml` file for easy project configuration and navigation definition.
*   **Live Reload Development Server**: Develop your documentation with a built-in server that automatically reloads changes as you save.
*   **Customizable Themes**: Easily extend and customize the look and feel using Jinja2 templates and standard CSS.
*   **Command-Line Interface (CLI)**: Intuitive CLI for building, serving, and initializing new documentation projects.

## Installation

SmartGen Docs can be easily installed via pip:

```bash
pip install smartgen-docs
```

## Quick Start

1.  **Initialize a new project:**

    ```bash
smartgen-docs init
    ```

    This will create a `smartgen.yml` configuration file and a `docs/index.md` file.

2.  **Write your documentation:**

    Edit `docs/index.md` and add more Markdown files to the `docs/` directory. Update `smartgen.yml` to include new pages in your navigation.

3.  **Serve your documentation locally:**

    ```bash
smartgen-docs serve
    ```

    Open your browser to `http://localhost:8000` to see your documentation with live reloading.

4.  **Build your static site:**

    ```bash
smartgen-docs build
    ```

    This will generate your static site in the `site/` directory, ready for deployment.

## Project Structure

A typical SmartGen Docs project looks like this:

```
. 
├── smartgen.yml          # Project configuration
├── docs/                 # Your Markdown documentation files
│   ├── index.md
│   └── chapter1.md
└── site/                 # Generated static website (after running `smartgen-docs build`)
    ├── index.html
    └── chapter1.html
```

## Contributing

SmartGen Docs is open source and welcomes [contributions](CONTRIBUTING.md). Feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## [License](LICENSE)|[smartGen](https://smartgentools.com)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## About the Author

**Sayad Md Bayezid Hosan** is the creator of SmartGen Docs and the founder of [Smartgen Verified](https://sayadbayezid.com/verified-profiles/), a hub for innovative tools and solutions.
