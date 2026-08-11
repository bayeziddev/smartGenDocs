# Publishing `smartgen-docs` to PyPI

This guide outlines the steps required to release and publish new versions of **SmartGen Docs** (`smartgen-docs`) to the Python Package Index (PyPI).

## Prerequisites

1. Ensure you have admin access to the GitHub repository `bayeziddev/smartGenDocs`.
2. Ensure you have a valid PyPI account and an API token (`PYPI_API_TOKEN`) with permissions for the `smartgen-docs` package.
3. Configure the `PYPI_API_TOKEN` secret in your GitHub repository settings under **Settings > Secrets and variables > Actions**.

---

## Release & Publish Workflow

Publishing is fully automated via GitHub Actions (`.github/workflows/publish.yml`). Follow these steps to cut a new release:

### 1. Update Version and Documentation
- Update the version string in `pyproject.toml` and `smartgen_docs/__init__.py` (if applicable).
- Update `CHANGELOG.md` or `docs/docs/changelog.md` with release notes for the new version.
- Commit all changes to the `main` branch:
  ```bash
  git add .
  git commit -m "chore: prepare release v1.1.0"
  git push origin main
  ```

### 2. Create and Push a Tag
- Tag the release using semantic versioning prefixed with `v` (matching the release trigger `v*`):
  ```bash
  git tag v1.1.0
  git push origin v1.1.0
  ```

### 3. Publish via GitHub Releases
- Navigate to your repository on GitHub: [github.com/bayeziddev/smartGenDocs](https://github.com/bayeziddev/smartGenDocs)
- Go to **Releases > Draft a new release**.
- Select the tag you just pushed (`v1.1.0`).
- Fill in the release title and detailed release notes.
- Click **Publish release**.

The GitHub Actions workflow will automatically trigger, build the source distribution and wheel, verify them with `twine`, and publish the package directly to PyPI. Once complete, users can immediately install it via:

```bash
pip install smartgen-docs
```
