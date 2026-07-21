# Your First SmartGen Docs Project

This guide provides a detailed walkthrough of initializing a new SmartGen Docs project and understanding its core components. If you have followed the [Installation Guide](installation.md) and the [Quick Start Guide](quick-start.md), you are ready to delve deeper into the structure of your documentation site.

## 1. Initializing the Project

As covered in the Quick Start, you initialize a new project using the `init` command:

```bash
smartgen-docs init
```

This command performs several key actions:

*   **Creates `smartgen.yml`**: This is the central configuration file for your SmartGen Docs project. It defines your site's name, navigation structure, theme, and other global settings. You will frequently interact with this file to customize your documentation.
*   **Creates `docs/` directory**: This directory is the heart of your documentation content. All your Markdown files (`.md`) that will be converted into HTML pages reside here.
*   **Creates `docs/index.md`**: This file serves as the homepage for your documentation site. It's the first page users will see when they visit your documentation.
*   **Creates `docs/getting-started/index.md`**: This is a placeholder for the Getting Started section's overview page.

## 2. Understanding the Project Structure

After initialization, your project directory will have a structure similar to this:

```
. 
├── smartgen.yml          # Project configuration
├── docs/                 # Your Markdown documentation files
│   ├── index.md          # Homepage of your documentation
│   └── getting-started/  # Directory for getting started guides
│       └── index.md      # Overview for the getting started section
└── site/                 # Generated static website (after running `smartgen-docs build`)
    ├── index.html
    └── ...
```

*   **`smartgen.yml`**: This YAML file is where you configure your site. It controls the site's title, author, description, theme, and most importantly, the navigation structure. The `nav` section dictates the order and hierarchy of your documentation pages.
*   **`docs/`**: This directory contains all your source Markdown files. Each Markdown file (`.md`) will be transformed into an HTML page in your final documentation site. You can create subdirectories within `docs/` to organize your content logically, mirroring your navigation structure.
*   **`site/`**: This directory is generated when you run `smartgen-docs build`. It contains the complete static HTML, CSS, and JavaScript files that make up your documentation website. This is the content you will deploy to a web server.

## 3. Customizing `smartgen.yml`

The `smartgen.yml` file is crucial for defining your documentation's structure and appearance. Here are some key sections you'll work with:

```yaml
site_name: My Awesome Docs
site_url: https://example.com/docs
site_author: John Doe
site_description: Comprehensive documentation for my awesome project.

theme:
  name: premium # Or 'default'
  palette:
    primary: "#007bff"
    accent: "#ffc107"

nav:
  - Home: index.md
  - Introduction: introduction.md
  - Features:
      - Feature A: features/feature-a.md
      - Feature B: features/feature-b.md
  - API Reference: api/index.md
```

*   **`site_name`, `site_url`, `site_author`, `site_description`**: These fields define basic metadata for your site, used in headers, footers, and SEO.
*   **`theme`**: This section allows you to select a theme (`default` or `premium`) and customize its colors and fonts.
*   **`nav`**: This is the most important section for content organization. It defines the main navigation menu of your documentation. You can create nested menus by listing sub-pages under a main category. The paths specified here are relative to your `docs/` directory.

## 4. Adding Content

To add new content, simply create a new Markdown file in the `docs/` directory or a relevant subdirectory. For example, to add a page about new features, you might create `docs/features.md` and then add it to your `smartgen.yml` navigation.

## Next Steps

Now that you understand the project structure, you can proceed to organize your content effectively. Learn more about the recommended [Folder Structure](folder-structure.md) for best practices.
