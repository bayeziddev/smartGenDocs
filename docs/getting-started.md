File : getting-started.md
# Getting Started with SmartGen Docs
Welcome to the **SmartGen Docs** ecosystem. This guide will walk you through the essential steps to initialize your project, structure your documentation, and deploy your site to the web.
## 1. Installation
Before you begin, ensure you have **Python 3.8+** installed. You can install the SmartGen Docs package directly via pip:
```bash
# Standard installation
pip install smartgen-docs

# Installation with upload manager support
pip install "smartgen-docs[full]"

```
## 2. Project Initialization
Navigate to your project folder and initialize the SmartGen environment. This command creates the necessary configuration files and directory structure.
```bash
smartgen-docs init

```
This will generate:
 * **smartgen.yml**: Your master configuration file.
 * **docs/**: The directory where your content lives.
## 3. Configuring Your Site
Open the smartgen.yml file in your root directory. Configure your site metadata to match your project branding:
```yaml
site_name: My SmartGen Docs
site_url: https://bayeziddev.github.io/smartGenDocs/
site_author: Sayad Md Bayezid Hosan

# Premium Theme Settings
theme:
  name: premium
  palette:
    primary: "#0052cc"
    accent: "#ff9900"

```
## 4. Creating Content
SmartGen Docs uses Markdown for all documentation. Create your files inside the **docs/** directory.
 * **docs/index.md**: This is your site's homepage.
 * **docs/getting-started.md**: Your guide (this file).
 * **docs/api/**: Create subfolders for organized documentation.
## 5. Local Development
To preview your changes in real-time, use the built-in development server. It includes **live-reload**, meaning your browser will automatically refresh whenever you save a Markdown file.
```bash
smartgen-docs serve --port 8000

```
## 6. Building for Production
When you are ready to publish, build your site into static HTML files:
```bash
smartgen-docs build

```
This command generates your site into the **site/** folder. Your GitHub Actions workflow will automatically pick up these files and deploy them to your GitHub Pages site.
*For advanced configurations, API generation, or managing your files via the web interface, refer to the GUIDELINES.md file in your project root.*
