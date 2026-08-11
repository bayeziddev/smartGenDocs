# SmartGen Docs Python SDK & CLI Integration

The **SmartGen Python SDK** provides programmatic access to the documentation builder engine, enabling developers to integrate static site compilation, custom theme registration, and automated autodoc generation directly into their Python applications and CI/CD pipelines [1].

## Installation & Setup

Install the SmartGen Docs package via `pip` or include it in your project's `pyproject.toml` dependencies [2]:

```bash
pip install smartgen-docs
```

## Programmatic Builder API

You can instantiate and execute the documentation builder programmatically from any Python script:

```python
from smartgen_docs.core import Builder

def build_docs():
    # Initialize builder with custom configuration and site output directory
    builder = Builder(config_path='smartgen.yml', site_dir='site')
    builder.build()
    print("Documentation build completed successfully.")

if __name__ == '__main__':
    build_docs()
```

The `Builder` class automatically loads `smartgen.yml`, parses navigation hierarchies, converts Markdown source files with Pygments syntax highlighting, and generates SEO sitemaps and robots files [3].

## References

- [1] Python SDK Reference. [SmartGen Documentation](https://docs.smartgentools.com/sdk/python.html).
- [2] Pyproject Configuration. [SmartGen Repository](https://github.com/bayeziddev/smartGenDocs/blob/main/pyproject.toml).
- [3] Builder Core Implementation. [SmartGen Source Code](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/core.py).
