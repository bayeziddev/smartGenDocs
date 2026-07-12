"""
Scaffold: Generate project structure and missing documentation files.

This module creates the directory structure and placeholder files based on
the smartgen.yml configuration, ensuring consistency with the navigation.
"""

import os
import yaml
import click


class Scaffolder:
    """
    Generates project structure and documentation files from smartgen.yml.
    """
    
    def __init__(self, config_path='smartgen.yml', docs_dir='docs'):
        """
        Initialize the Scaffolder.
        
        Args:
            config_path: Path to the smartgen.yml configuration file
            docs_dir: Directory where documentation files are stored
        """
        self.config_path = config_path
        self.docs_dir = docs_dir

    def load_nav(self):
        """Load navigation from smartgen.yml."""
        if not os.path.exists(self.config_path):
            click.secho(f"Error: {self.config_path} not found.", fg="red")
            return []
        with open(self.config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            return config.get('nav', [])

    def create_files(self):
        """Create missing documentation files based on navigation."""
        nav = self.load_nav()
        if not nav:
            click.secho("No navigation found or config is empty.", fg="yellow")
            return

        click.secho(f"Scanning navigation in {self.config_path}...", fg="cyan")
        self._process_nav(nav)
        click.secho("✓ Scaffolding complete! Your existing files were strictly preserved.", fg="green", bold=True)

    def _process_nav(self, nav_list):
        """
        Recursively process navigation items and create files.
        
        Args:
            nav_list: List of navigation items from smartgen.yml
        """
        for item in nav_list:
            if isinstance(item, dict):
                for title, path in item.items():
                    if isinstance(path, str) and path.endswith('.md'):
                        self._create_safe_file(title, path)
                    elif isinstance(path, list):
                        # Recursive call for nested categories (e.g., Guides, Tutorials)
                        self._process_nav(path)
            elif isinstance(item, str) and item.endswith('.md'):
                title = os.path.basename(item).replace('.md', '').capitalize()
                self._create_safe_file(title, item)

    def _create_safe_file(self, title, md_path):
        """
        Create a documentation file if it doesn't exist.
        
        Args:
            title: Title of the page
            md_path: Path to the file (relative to docs_dir)
        """
        # Ignore external HTTP/HTTPS links in navigation
        if md_path.startswith('http://') or md_path.startswith('https://'):
            return

        full_path = os.path.join(self.docs_dir, md_path)
        directory = os.path.dirname(full_path)

        # Create nested directories if they do not exist
        if directory:
            os.makedirs(directory, exist_ok=True)

        # STRICT SAFEGUARD: Check existence before writing
        if os.path.exists(full_path):
            click.secho(f"  [Skipped] {full_path} already exists.", fg="yellow")
        else:
            # Create a brand new file with a default Markdown header
            content = self._generate_placeholder(title, md_path)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            click.secho(f"  ✓ Created {full_path}", fg="green")

    def _generate_placeholder(self, title: str, file_path: str) -> str:
        """
        Generate placeholder content for a new file.
        
        Args:
            title: Title of the page
            file_path: Path to the file
        
        Returns:
            Placeholder content
        """
        # Determine if this is an index page
        is_index = file_path.endswith('index.md')
        
        if is_index:
            section = os.path.basename(os.path.dirname(file_path))
            return f"""# {title}

Welcome to the {title} section of SmartGen Docs.

## Overview

This section contains documentation for {title.lower()}.

## Getting Started

To get started with {title.lower()}, please explore the pages in this section.

## Key Topics

- Topic 1
- Topic 2
- Topic 3

## Learn More

For more information, check out the related documentation pages.
"""
        else:
            return f"""# {title}

## Introduction

This page covers {title.lower()}.

## Content

Add your content here.

## Examples

```python
# Example code here
pass
```

## See Also

- Related Topic 1
- Related Topic 2

## References

- [Reference 1](#)
- [Reference 2](#)
"""
