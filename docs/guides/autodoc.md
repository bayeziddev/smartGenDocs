---
title: Autodoc Guide - Automated API Documentation with SmartGen Docs
description: Learn how to automatically generate API reference documentation from your Python code using the Autodoc feature in SmartGen Docs. This guide covers configuration, usage, and best practices for integrating code documentation.
keywords: SmartGen Docs autodoc, automated documentation, API reference, Python documentation, docstrings, Sphinx, technical writing, code documentation
---

# Autodoc Guide: Automated API Documentation

Maintaining up-to-date API reference documentation can be a time-consuming task, especially for projects with rapidly evolving codebases. SmartGen Docs simplifies this process with its powerful **Autodoc** feature, allowing you to automatically generate API documentation directly from your Python source code docstrings.

This guide will walk you through setting up and using the Autodoc plugin to seamlessly integrate your code documentation into your SmartGen Docs site, ensuring accuracy and reducing manual effort.

## 1. Enabling the Autodoc Plugin

To use the Autodoc feature, you first need to enable the `autodoc` plugin in your `smartgen.yml` configuration file. Add `autodoc` to the `plugins` section:

```yaml
plugins:
  - search
  - autodoc # Enable the autodoc plugin
  # ... other plugins
```

## 2. Configuring Autodoc

The `autodoc` plugin can be configured with specific options to control where it finds your source code and where it outputs the generated Markdown files. These options are nested under the `autodoc` entry in your `plugins` section.

```yaml
plugins:
  - autodoc:
      source_dir: smartgen_docs # Directory containing your Python source code
      output_dir: api/modules # Directory where generated Markdown files will be saved
      exclude:
        - smartgen_docs/cli.py # Files or patterns to exclude from processing
        - smartgen_docs/server.py
      # Additional options (optional)
      # include_private: false # Include private members (starting with _)
      # include_inherited: true # Include inherited members
      # docstring_style: sphinx # or google, numpy, plain
```

### Configuration Parameters

*   **`source_dir` (Required)**: Specifies the root directory where your Python source code is located. The `autodoc` plugin will recursively scan this directory for Python files (`.py`).
    *   **Example**: `smartgen_docs` (if your Python package is `smartgen_docs`)
*   **`output_dir` (Required)**: Defines the directory within your `docs/` folder where the generated Markdown files for your API reference will be placed. This directory will be created if it doesn\`t exist.
    *   **Example**: `api/modules` (resulting in `docs/api/modules/*.md`)
*   **`exclude` (Optional)**: A list of glob patterns or specific file paths to exclude from the autodoc process. This is useful for omitting internal scripts, test files, or modules that you don\`t want to expose in your public API documentation.
    *   **Example**: `smartgen_docs/cli.py` will exclude the `cli.py` file.
*   **`include_private` (Optional, default: `false`)**: Set to `true` to include private members (those starting with an underscore `_`) in the generated documentation.
*   **`include_inherited` (Optional, default: `true`)**: Set to `false` to exclude inherited members from base classes in the generated documentation.
*   **`docstring_style` (Optional, default: `sphinx`)**: Specifies the docstring format used in your Python code. Supported styles typically include `sphinx`, `google`, `numpy`, and `plain`. This helps the plugin parse your docstrings correctly.

## 3. Documenting Your Code with Docstrings

The Autodoc plugin relies on well-formatted docstrings in your Python code. While it supports various styles, using a consistent and clear docstring format is key to generating high-quality documentation.

### Example Python Module with Docstrings

Consider a simple Python module `smartgen_docs/utils.py`:

```python
"""Utility functions for SmartGen Docs.

This module provides helper functions for various operations within the SmartGen Docs ecosystem.
"""

def greet(name: str) -> str:
    """Greets a person by their name.

    :param name: The name of the person to greet.
    :type name: str
    :returns: A greeting message.
    :rtype: str

    :Example:
    >>> greet("Alice")
    \`Hello, Alice!\`
    """
    return f"Hello, {name}!"

class Calculator:
    """A simple calculator class.

    This class provides basic arithmetic operations.
    """
    def add(self, a: int, b: int) -> int:
        """Adds two numbers.

        :param a: The first number.
        :type a: int
        :param b: The second number.
        :type b
        :returns: The sum of a and b.
        :rtype: int
        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Subtracts two numbers.

        :param a: The first number.
        :type a: int
        :param b: The second number.
        :type b: int
        :returns: The difference between a and b.
        :rtype: int
        """
        return a - b
```

## 4. Generating Documentation

Once the `autodoc` plugin is enabled and configured, you can generate the API documentation by running the `smartgen-docs build` command:

```bash
smartgen-docs build
```

The `autodoc` plugin will execute during the build process, scan your `source_dir`, parse the docstrings, and create Markdown files in your specified `output_dir` (e.g., `docs/api/modules/utils.md`, `docs/api/modules/calculator.md`).

## 5. Integrating Generated Docs into Navigation

After the Markdown files are generated, you need to include them in your site\`s navigation (`nav` section in `smartgen.yml`) to make them accessible to users.

```yaml
nav:
  # ... other navigation items ...
  - API Reference:
      - Overview: api/index.md
      - Authentication: api/authentication.md
      # ... other API-related pages ...
      - Modules:
          - Utilities: api/modules/utils.md # Link to generated docs
          - Calculator: api/modules/calculator.md # Link to generated docs
```

## Best Practices for Autodoc

*   **Consistent Docstring Style**: Choose a docstring style (e.g., Sphinx, Google, NumPy) and stick to it throughout your codebase. This ensures consistent and accurate parsing by the `autodoc` plugin.
*   **Comprehensive Docstrings**: Document all public modules, classes, methods, and functions. Include a summary, detailed description, parameters, return values, and examples where appropriate.
*   **Run `build` regularly**: Integrate `smartgen-docs build` into your CI/CD pipeline or run it frequently during development to keep your documentation synchronized with your code.
*   **Review Generated Output**: Always review the generated Markdown files to ensure they accurately reflect your code and are well-formatted.
*   **Exclude Irrelevant Files**: Use the `exclude` option to prevent internal or non-public code from appearing in your API documentation.

By following this guide, you can effectively leverage SmartGen Docs\` Autodoc feature to create and maintain high-quality, automatically generated API documentation for your Python projects.

## See Also

*   [Configuration Guide](configuration.md)
*   [CLI Reference](cli.md)
*   [SmartGen Platform](https://www.smartgentools.com) - Explore more tools from the SmartGen Platform.
