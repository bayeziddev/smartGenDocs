# Autodoc Guide

The `autodoc` feature in SmartGen Docs provides a powerful way to automatically generate API reference documentation directly from your Python project's docstrings. This ensures that your code documentation remains synchronized with your codebase, reducing manual effort and potential inconsistencies. This guide will walk you through how to configure and use the `autodoc` command.

## What is Autodoc?

`autodoc` is a plugin that scans your Python source files, extracts information from classes, functions, and methods (including their docstrings, signatures, and module paths), and then formats this information into Markdown files. These generated Markdown files can then be seamlessly integrated into your SmartGen Docs site.

## 1. Enabling the Autodoc Plugin

To use the `autodoc` feature, you must first enable the `autodoc` plugin in your `smartgen.yml` configuration file. You can also configure its behavior in this section.

```yaml
plugins:
  - autodoc:
      source_dir: smartgen_docs # Directory containing your Python source code
      output_dir: api/modules    # Directory where generated Markdown files will be saved
      exclude:
        - smartgen_docs/cli.py # Files or patterns to exclude
```

*   **`source_dir`**: (Optional) Specifies the root directory where your Python source code resides. SmartGen Docs will recursively scan this directory for Python modules. Defaults to `smartgen_docs`.
*   **`output_dir`**: (Optional) Specifies the directory within your `docs/` folder where the generated API Markdown files will be placed. Defaults to `api/modules`.
*   **`exclude`**: (Optional) A list of glob patterns to exclude specific files or directories from the `autodoc` process. This is useful for omitting internal scripts, test files, or CLI entry points that don't need API documentation.

## 2. Documenting Your Python Code

`autodoc` relies heavily on well-written **docstrings** in your Python code. Follow standard Python documentation conventions (e.g., reStructuredText, NumPy, or Google style docstrings) to ensure `autodoc` can extract meaningful information.

### Example Python Module (`my_module.py`)

```python
"""A simple example module for demonstration."""

class MyClass:
    """A sample class to illustrate autodoc.

    :param name: The name of the instance.
    :type name: str
    """
    def __init__(self, name):
        self.name = name

    def greet(self, greeting="Hello"):
        """Greets the user with a personalized message.

        :param greeting: The greeting message. Defaults to "Hello".
        :type greeting: str
        :return: A personalized greeting string.
        :rtype: str
        """
        return f"{greeting}, {self.name}!"

def utility_function(a, b):
    """Performs a simple addition of two numbers.

    :param a: The first number.
    :type a: int
    :param b: The second number.
    :type b: int
    :return: The sum of a and b.
    :rtype: int
    :raises TypeError: if a or b are not integers.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    return a + b
```

## 3. Running the `autodoc` Command

Once your plugin is configured and your code is documented, you can run the `autodoc` command from your project's root directory:

```bash
smartgen-docs autodoc
```

This command will:

1.  Scan the `source_dir` (e.g., `smartgen_docs`).
2.  Parse Python modules and extract docstrings and signatures.
3.  Generate Markdown files for each module, class, and function/method.
4.  Save these Markdown files into the `output_dir` (e.g., `docs/api/modules`).

### Example Output Structure

After running `autodoc`, you might find a structure like this:

```
docs/
├── api/
│   ├── modules/
│   │   ├── smartgen_docs.my_module.md
│   │   └── smartgen_docs.another_module.md
│   └── index.md # Your manually created API overview
└── ...
```

## 4. Integrating Generated Docs into Navigation

To make your generated API documentation accessible on your site, you need to include the `output_dir` in your `smartgen.yml` navigation (`nav` section).

```yaml
nav:
  - API Reference:
    - Overview: api/index.md
    - Modules:
      - My Module: api/modules/smartgen_docs.my_module.md
      - Another Module: api/modules/smartgen_docs.another_module.md
    - Authentication: api/authentication.md
    # ... other API pages
```

It's recommended to create an `index.md` file within your `output_dir` (e.g., `docs/api/modules/index.md`) to provide an overview of your API modules.

## 5. Customizing Autodoc Output

While `autodoc` generates standard Markdown, you might want to customize the output format or content. This typically involves:

*   **Custom Jinja2 Templates**: If the `autodoc` plugin supports it, you might be able to provide custom Jinja2 templates to control how the Markdown is generated. Check the plugin's specific documentation for this advanced feature.
*   **Post-processing Scripts**: You can write small scripts to modify the generated Markdown files after `autodoc` has run, for example, to add custom headers, footers, or reformat specific sections.

## Best Practices for Autodoc

*   **Consistent Docstrings**: Maintain a consistent docstring style across your entire codebase.
*   **Clear Descriptions**: Write clear, concise, and comprehensive docstrings for all public APIs.
*   **Type Hinting**: Use Python type hints in your function and method signatures; `autodoc` can often leverage these for better documentation.
*   **Run Regularly**: Integrate `autodoc` into your CI/CD pipeline to ensure your API documentation is always up-to-date with your latest code changes.
*   **Review Generated Output**: Always review the generated Markdown files to ensure they accurately reflect your code and are easy to understand.

By following this guide, you can effectively leverage SmartGen Docs' `autodoc` feature to maintain high-quality, automatically generated API reference documentation for your Python projects.
