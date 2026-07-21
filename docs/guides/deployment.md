# Deployment Guide

Once you have created and configured your documentation site with SmartGen Docs, the next crucial step is to deploy it so that it is accessible to your users. Since SmartGen Docs generates a static website, deployment is generally straightforward and can be done on various hosting platforms. This guide will walk you through the common methods and best practices for deploying your SmartGen Docs site.

## 1. Understanding the `site/` Directory

When you run the `smartgen-docs build` command, SmartGen Docs processes your Markdown files, `smartgen.yml` configuration, and theme templates to generate a complete static website. All the output files (HTML, CSS, JavaScript, images, etc.) are placed in the `site/` directory at the root of your project.

This `site/` directory is what you need to upload to your web server or hosting provider. It is self-contained and does not require any server-side processing (like PHP, Node.js, or Python applications) to run.

## 2. Deployment Methods

There are several popular and efficient ways to deploy static websites. Choose the method that best suits your needs and existing infrastructure.

### A. GitHub Pages

**GitHub Pages** is a free and popular hosting service that publishes websites directly from a GitHub repository. It's an excellent choice for open-source projects and personal documentation.

#### Steps:

1.  **Create a GitHub Repository**: If you haven't already, create a public GitHub repository for your SmartGen Docs project.
2.  **Configure `smartgen.yml`**: Ensure your `site_url` in `smartgen.yml` is set correctly to your GitHub Pages URL (e.g., `https://username.github.io/repository-name/`).
3.  **Build Your Site**: Run `smartgen-docs build` to generate the `site/` directory.
4.  **Push to `gh-pages` Branch**: GitHub Pages typically serves from a `gh-pages` branch or the `docs/` folder on your `main` branch. The recommended approach for static site generators is to push the contents of your `site/` directory to a dedicated `gh-pages` branch.
    ```bash
    # Navigate into the built site directory
    cd site
    # Initialize a new Git repository (if not already done)
    git init
    # Add all files
    git add .
    # Commit changes
    git commit -m "Deploy SmartGen Docs to GitHub Pages"
    # Force push to the gh-pages branch (create if it doesn't exist)
    git push -f https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git main:gh-pages
    # Go back to your project root
    cd ..
    ```
5.  **Enable GitHub Pages**: In your GitHub repository settings, go to 
"Pages" and select the `gh-pages` branch as your publishing source. Your site should be live shortly.

### B. Netlify

**Netlify** is a popular platform for hosting static sites, offering continuous deployment, global CDN, and custom domain support. It integrates directly with your Git repository.

#### Steps:

1.  **Connect to Git**: Sign up for Netlify and connect your GitHub (or GitLab/Bitbucket) repository.
2.  **Configure Build Settings**: When prompted, configure your build settings:
    *   **Build Command**: `smartgen-docs build`
    *   **Publish Directory**: `site/`
3.  **Deploy**: Netlify will automatically build and deploy your site every time you push changes to your repository. You can also configure custom domains and other features through the Netlify dashboard.

### C. Vercel

**Vercel** is another excellent platform for static sites and serverless functions, known for its developer experience and performance. It also offers continuous deployment from Git.

#### Steps:

1.  **Connect to Git**: Sign up for Vercel and import your Git repository.
2.  **Configure Project**: Vercel will usually auto-detect your project. If not, configure:
    *   **Build Command**: `smartgen-docs build`
    *   **Output Directory**: `site/`
3.  **Deploy**: Vercel will deploy your site on every push to your connected branch. You can manage domains, analytics, and more from the Vercel dashboard.

### D. Amazon S3 / Google Cloud Storage

For more control or integration with existing cloud infrastructure, you can host your static site on object storage services like Amazon S3 or Google Cloud Storage.

#### Steps:

1.  **Build Your Site**: Run `smartgen-docs build` to generate the `site/` directory.
2.  **Upload Files**: Use the respective cloud provider's CLI (e.g., `aws s3 sync` or `gsutil rsync`) or web console to upload the entire contents of your `site/` directory to a configured bucket.
3.  **Configure Bucket for Static Hosting**: Enable static website hosting on your bucket and configure a custom domain if desired.
4.  **CDN (Optional but Recommended)**: For better performance and security, integrate a Content Delivery Network (CDN) like Amazon CloudFront or Google Cloud CDN in front of your storage bucket.

### E. Traditional Web Server (Nginx/Apache)

You can also host your SmartGen Docs site on a traditional web server like Nginx or Apache.

#### Steps:

1.  **Build Your Site**: Run `smartgen-docs build` to generate the `site/` directory.
2.  **Transfer Files**: Copy the entire `site/` directory to your web server's document root (e.g., `/var/www/html/your-docs/`).
3.  **Configure Web Server**: Configure your web server to serve the files from this directory. Ensure proper MIME types are set and that `index.html` is recognized as the default file for directories.

#### Example Nginx Configuration (Conceptual)

```nginx
server {
    listen 80;
    server_name docs.yourdomain.com;

    root /var/www/html/your-docs/site;
    index index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

## 3. Continuous Deployment (CI/CD)

For automated deployments, especially in team environments, integrating SmartGen Docs into a Continuous Integration/Continuous Deployment (CI/CD) pipeline is highly recommended. Tools like GitHub Actions, GitLab CI/CD, or Jenkins can automate the build and deployment process whenever changes are pushed to your repository.

#### Example GitHub Actions Workflow (Conceptual `main.yml`)

```yaml
name: Deploy SmartGen Docs to GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Build SmartGen Docs
        run: smartgen-docs build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
          publish_branch: gh-pages
```

This workflow will:

1.  Checkout your repository.
2.  Set up a Python environment.
3.  Install the necessary Python dependencies.
4.  Run `smartgen-docs build` to generate the static site.
5.  Deploy the contents of the `site/` directory to the `gh-pages` branch of your repository.

## Post-Deployment Considerations

*   **Custom Domains**: Most hosting providers allow you to configure custom domains for your static site.
*   **HTTPS**: Always ensure your deployed site uses HTTPS for security.
*   **SEO**: Optimize your `smartgen.yml` metadata (`site_description`, `site_name`) and ensure your Markdown content is well-structured for search engines.
*   **Monitoring**: Monitor your deployed site for uptime and performance.

By following this guide, you can successfully deploy your SmartGen Docs site and make your documentation accessible to your audience.
