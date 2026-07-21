# Deployment Guide: Publishing Your SmartGen Docs Site

Once you have created and built your SmartGen Docs project, the next crucial step is to deploy it so that your audience can access your documentation. SmartGen Docs generates a static HTML website, which makes it incredibly flexible and easy to host on a wide variety of platforms.

This guide will walk you through the process of deploying your SmartGen Docs site to popular hosting services, as well as general instructions for custom web servers.

## 1. Building Your Documentation Site

Before deployment, you must build your documentation site. This process compiles your Markdown files, applies your theme, and generates all the necessary HTML, CSS, and JavaScript files into a `site/` directory (by default).

Navigate to your project\'s root directory in your terminal and run:

```bash
smartgen-docs build --clean
```

*   The `build` command generates the static site.
*   The `--clean` flag ensures that the `site/` directory is cleared before a new build, preventing any old or stale files from being included.

After a successful build, all the files ready for deployment will be located in the `site/` directory.

## 2. Deployment Options

SmartGen Docs\' static output allows for numerous deployment strategies. Here are some of the most common and recommended options:

### Option A: GitHub Pages (Recommended for Open Source Projects)

GitHub Pages is a free hosting service provided by GitHub, ideal for hosting open-source project documentation directly from your repository. SmartGen Docs integrates seamlessly with GitHub Pages.

#### Method 1: Using the `gh-pages` Branch

This is the most common method. Your built site is pushed to a dedicated `gh-pages` branch.

1.  **Install `gh-pages`**: If not already installed, you might need a tool to push your `site/` directory to a `gh-pages` branch. Many static site generators have built-in support or you can use a utility like `gh-pages` npm package or a custom script.

    If SmartGen Docs has a built-in `deploy` command for GitHub Pages (check `smartgen-docs deploy --help`), use that. Otherwise, you can use a tool like `gh-pages` (Node.js package):

    ```bash
    # Install gh-pages (if you have Node.js/npm)
npm install --save-dev gh-pages
    ```

2.  **Configure `package.json` (if using `gh-pages` npm package)**:

    Add a deploy script to your `package.json`:

    ```json
    {
      "name": "my-smartgen-docs",
      "version": "1.0.0",
      "scripts": {
        "deploy": "gh-pages -d site"
      },
      "devDependencies": {
        "gh-pages": "^x.y.z"
      }
    }
    ```

3.  **Deploy**: After building your site, run the deploy script:

    ```bash
smartgen-docs build --clean
npm run deploy
    ```

4.  **GitHub Repository Settings**: Go to your GitHub repository settings, navigate to the "Pages" section, and ensure that "Deploy from a branch" is selected, with `gh-pages` as the source branch and `/ (root)` as the folder.

#### Method 2: Deploying from `main` (or `master`) Branch `/docs` Folder

If you prefer to keep your documentation source and built output in the same branch, you can configure GitHub Pages to serve from the `/docs` folder of your `main` (or `master`) branch.

1.  **Build to `docs`**: Modify your `smartgen-docs build` command or configuration to output to a `docs/` subdirectory within your project root (not `site/`). This might require a custom build script or a `smartgen.yml` setting if available.

    *Note: SmartGen Docs typically builds to `site/`. You would need to copy the contents of `site/` to `docs/` before pushing, or configure SmartGen Docs to output directly to `docs/`.* For example:

    ```bash
smartgen-docs build --clean
mkdir -p docs # Ensure docs directory exists
cp -r site/* docs/
git add docs/
git commit -m "Update documentation"
git push origin main
    ```

2.  **GitHub Repository Settings**: In your GitHub repository settings, go to the "Pages" section, select your `main` (or `master`) branch as the source, and choose `/docs` as the folder.

### Option B: Netlify

Netlify is an excellent platform for hosting static sites, offering continuous deployment, custom domains, and HTTPS out of the box.

1.  **Connect to Git**: Sign up for Netlify and connect your GitHub (or GitLab/Bitbucket) repository.
2.  **Build Settings**: When prompted, configure your build settings:
    *   **Build command**: `smartgen-docs build --clean`
    *   **Publish directory**: `site`
3.  **Deploy**: Netlify will automatically build and deploy your site every time you push changes to your connected branch.

### Option C: Vercel

Vercel is another popular platform for static sites and serverless functions, known for its ease of use and developer experience.

1.  **Connect to Git**: Sign up for Vercel and connect your GitHub (or GitLab/Bitbucket) repository.
2.  **Configure Project**: When importing your project, Vercel will usually auto-detect SmartGen Docs. If not, configure:
    *   **Build Command**: `smartgen-docs build --clean`
    *   **Output Directory**: `site`
3.  **Deploy**: Vercel will automatically deploy your site on every push to your connected branch.

### Option D: Custom Web Server (Nginx, Apache, etc.)

For self-hosting, you can simply copy the contents of your `site/` directory to any web server.

1.  **Build**: Run `smartgen-docs build --clean` to generate your static files.
2.  **Copy Files**: Transfer the entire content of the `site/` directory to your web server\'s document root (e.g., `/var/www/html/` for Apache or Nginx).

    ```bash
    # Example using rsync for SSH deployment
    rsync -avz --delete site/ user@your-server.com:/var/www/html/your-docs-path/
    ```

3.  **Configure Web Server**: Ensure your web server is configured to serve static files from the chosen directory. For example, an Nginx configuration might look like this:

    ```nginx
    server {
        listen 80;
        server_name docs.yourdomain.com;

        root /var/www/html/your-docs-path;
        index index.html;

        location / {
            try_files $uri $uri/ =404;
        }
    }
    ```

## 3. Continuous Deployment (CI/CD)

For larger projects or teams, automating the build and deployment process with Continuous Integration/Continuous Deployment (CI/CD) is highly recommended. Platforms like GitHub Actions, GitLab CI/CD, or Jenkins can be configured to:

1.  Listen for changes in your documentation repository.
2.  Run `smartgen-docs build`.
3.  Deploy the `site/` directory to your chosen hosting platform.

This ensures that your documentation is always up-to-date with your latest changes without manual intervention.

## Troubleshooting Deployment Issues

*   **Broken Links**: Ensure your `site_url` in `smartgen.yml` is correct and matches your deployed URL. Incorrect `site_url` can lead to broken absolute links.
*   **Missing Files**: Verify that all necessary assets (images, CSS, JS) are present in your `site/` directory after building. Check your `smartgen.yml` for correct paths.
*   **Build Errors**: Review the output of `smartgen-docs build` for any warnings or errors. Use `--verbose` for more detailed debugging information.
*   **Cache Issues**: If changes aren\'t appearing, clear your browser cache or the cache of your CDN/hosting provider.

By following this guide, you can confidently deploy your SmartGen Docs site and make your valuable documentation accessible to the world.

## See Also

*   [Configuration Guide](configuration.md)
*   [CLI Reference](cli.md)
*   [SmartGen Platform](https://www.smartgentools.com) - Explore more tools from the SmartGen Platform.
