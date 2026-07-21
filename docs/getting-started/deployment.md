# Deployment

Once you have built your SmartGen Docs project using the `smartgen-docs build` command, you will have a `site/` directory containing a complete static HTML website. Because it is purely static (HTML, CSS, JavaScript), you can deploy it to almost any web hosting service or static site hosting platform.

This guide outlines the general deployment process and provides specific instructions for popular hosting platforms.

## General Deployment Process

The general process for deploying a SmartGen Docs site involves these steps:

1.  **Build the Site**: Ensure you have the latest version of your documentation built by running `smartgen-docs build` in your project's root directory.
2.  **Locate the Output**: Verify that the `site/` directory has been created and contains your HTML files.
3.  **Upload to Host**: Transfer the contents of the `site/` directory to your chosen web hosting provider. The method for uploading depends on the provider (e.g., FTP, Git push, web interface).

## Deploying to GitHub Pages

GitHub Pages is a popular, free option for hosting static websites directly from a GitHub repository. It is an excellent choice for open-source projects and personal documentation.

### Method 1: Manual Deployment (gh-pages branch)

1.  **Initialize Git**: If your project isn't already a Git repository, initialize it:
    ```bash
    git init
    ```
2.  **Commit Source Files**: Commit your `smartgen.yml` and `docs/` directory to your main branch (e.g., `main` or `master`). Do not commit the `site/` directory.
    ```bash
    echo "site/" >> .gitignore
    git add .
    git commit -m "Initial commit of documentation source"
    ```
3.  **Build the Site**: Run `smartgen-docs build`.
4.  **Deploy using a tool like `gh-pages`**: You can use the `gh-pages` npm package to easily push the `site/` directory to a `gh-pages` branch.
    ```bash
    npx gh-pages -d site
    ```
5.  **Configure GitHub Pages**: Go to your repository settings on GitHub, navigate to the "Pages" section, and select the `gh-pages` branch as the source.

### Method 2: Automated Deployment with GitHub Actions

For a more robust workflow, you can automate the build and deployment process using GitHub Actions. This ensures your site is updated automatically whenever you push changes to your main branch.

1.  Create a file named `.github/workflows/deploy.yml` in your repository.
2.  Add the following configuration (adjust as needed for your specific setup):

    ```yaml
    name: Deploy SmartGen Docs

    on:
      push:
        branches:
          - main # Or your default branch

    jobs:
      build-and-deploy:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout repository
            uses: actions/checkout@v3

          - name: Set up Python
            uses: actions/setup-python@v4
            with:
              python-version: '3.x'

          - name: Install dependencies
            run: |
              pip install smartgen-docs

          - name: Build documentation
            run: smartgen-docs build

          - name: Deploy to GitHub Pages
            uses: peaceiris/actions-gh-pages@v3
            with:
              github_token: ${{ secrets.GITHUB_TOKEN }}
              publish_dir: ./site
    ```

## Deploying to Netlify

Netlify is another excellent platform for hosting static sites, offering continuous deployment from Git repositories.

1.  **Push to Git**: Ensure your project (excluding the `site/` directory) is pushed to a Git repository (GitHub, GitLab, or Bitbucket).
2.  **Create a Netlify Site**: Log in to Netlify and click "Add new site" -> "Import an existing project".
3.  **Connect Repository**: Connect your Git provider and select your documentation repository.
4.  **Configure Build Settings**:
    *   **Build command**: `pip install smartgen-docs && smartgen-docs build`
    *   **Publish directory**: `site`
5.  **Deploy**: Click "Deploy site". Netlify will automatically build and deploy your documentation.

## Deploying to Vercel

Vercel is a platform optimized for frontend frameworks and static sites, providing fast global deployment.

1.  **Push to Git**: Ensure your project is in a Git repository.
2.  **Import Project**: Log in to Vercel and click "Add New..." -> "Project".
3.  **Select Repository**: Import your documentation repository.
4.  **Configure Build Settings**:
    *   **Framework Preset**: Other
    *   **Build Command**: `pip install smartgen-docs && smartgen-docs build`
    *   **Output Directory**: `site`
5.  **Deploy**: Click "Deploy". Vercel will handle the build and deployment process.

By following these instructions, you can easily make your SmartGen Docs documentation accessible to the world.
