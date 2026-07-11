import inspect
import importlib
import os
import sys

class AutodocGenerator:
    def __init__(self, output_dir='docs/api'):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_for_module(self, module_name):
        """Generate markdown documentation for a given module name."""
        try:
            # Add current directory to path to find local modules
            sys.path.append(os.getcwd())
            module = importlib.import_module(module_name)
        except ImportError as e:
            print(f"Error: Could not import module '{module_name}': {e}")
            return

        md_content = f"# API Reference: {module_name}\n\n"
        md_content += f"{inspect.getdoc(module) or 'No module description provided.'}\n\n"

        # Document Classes
        classes = inspect.getmembers(module, inspect.isclass)
        if classes:
            md_content += "## Classes\n\n"
            for name, cls in classes:
                if cls.__module__ == module_name:
                    md_content += self._document_class(name, cls)

        # Document Functions
        functions = inspect.getmembers(module, inspect.isfunction)
        if functions:
            md_content += "## Functions\n\n"
            for name, func in functions:
                if func.__module__ == module_name:
                    md_content += self._document_function(name, func)

        output_path = os.path.join(self.output_dir, f"{module_name}.md")
        with open(output_path, 'w') as f:
            f.write(md_content)
        
        print(f"Generated API reference for {module_name} at {output_path}")
        return f"api/{module_name}.md"

    def _document_class(self, name, cls):
        doc = f"### `class {name}`\n\n"
        doc += f"{inspect.getdoc(cls) or 'No description.'}\n\n"
        
        methods = inspect.getmembers(cls, inspect.isfunction)
        if methods:
            doc += "#### Methods\n\n"
            for m_name, m_func in methods:
                if not m_name.startswith('_') or m_name == '__init__':
                    doc += f"##### `{m_name}{inspect.signature(m_func)}`\n"
                    doc += f"{inspect.getdoc(m_func) or 'No description.'}\n\n"
        return doc

    def _document_function(self, name, func):
        doc = f"### `def {name}{inspect.signature(func)}`\n\n"
        doc += f"{inspect.getdoc(func) or 'No description.'}\n\n"
        return doc
