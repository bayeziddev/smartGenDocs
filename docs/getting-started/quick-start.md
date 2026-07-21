# Quick Start Guide

This guide provides a rapid, step-by-step introduction to creating and serving your first documentation site with SmartGen Docs. If you have already [installed SmartGen Docs](installation.md), you can follow these instructions to get your project up and running in minutes.

## 1. Initialize a New Project

The first step is to initialize a new SmartGen Docs project. This command creates the necessary configuration file (`smartgen.yml`) and a default `index.md` file within your `docs/` directory.

Open your terminal or command prompt, navigate to the directory where you want to create your project, and run:

```bash
smartgen-docs init
```

Upon successful execution, you will see a message indicating that the project has been initialized. A new directory named `docs/` will be created, containing `index.md` and `getting-started/index.md`.

## 2. Write Your Documentation

SmartGen Docs is Markdown-centric, meaning you write your content using simple Markdown syntax. The `init` command creates a basic `docs/index.md` file, which serves as your project's homepage.

*   **Edit `docs/index.md`**: Open `docs/index.md` in your favorite text editor and start adding your content. This file will be the main landing page for your documentation.
*   **Add More Pages**: To add more documentation pages, simply create new Markdown files (`.md`) within the `docs/` directory or its subdirectories. For example, you might create `docs/features.md` or `docs/api/overview.md`.
*   **Update `smartgen.yml`**: To make your new pages visible in the navigation menu, you need to update the `nav` section in your `smartgen.yml` file. This file defines the structure of your documentation site.

    Here's an example of how to add a new page to `smartgen.yml`:

    ```yaml
    nav:
      - Home: index.md
      - Features: features.md
      - Getting Started:
          - Welcome: getting-started/index.md
    ```

## 3. Serve Your Documentation Locally

SmartGen Docs includes a built-in development server with live reloading, allowing you to preview your changes in real-time as you write. This is incredibly useful for iterative development and ensures your documentation looks as expected.

From your project's root directory (where `smartgen.yml` is located), run:

```bash
smartgen-docs serve
```

Open your web browser and navigate to `http://localhost:8000` (or the port indicated in your terminal). You will see your documentation site, and any changes you save to your Markdown files or `smartgen.yml` will automatically refresh in the browser.

## 4. Build Your Static Site

Once you are satisfied with your documentation, you can build the static HTML files that are ready for deployment. This command generates a complete static website in the `site/` directory.

From your project's root directory, run:

```bash
smartgen-docs build
```

After the command completes, a new `site/` directory will be created (or updated) in your project's root. This directory contains all the HTML, CSS, and JavaScript files that make up your documentation website, ready to be hosted on any static web server.

## Next Steps

Congratulations! You've successfully initialized, written, served, and built your first SmartGen Docs project. For a more in-depth understanding of the project structure and components, proceed to [Your First Project](first-project.md). If you're ready to deploy your site, visit the [Deployment Guide](deployment.md).
