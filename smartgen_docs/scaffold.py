import os
import yaml
import click

class Scaffolder:
    def __init__(self, config_path='smartgen.yml', docs_dir='docs'):
        self.config_path = config_path
        self.docs_dir = docs_dir

    def load_nav(self):
        if not os.path.exists(self.config_path):
            click.secho(f"Error: {self.config_path} not found.", fg="red")
            return []
        with open(self.config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            return config.get('nav', [])

    def create_files(self):
        nav = self.load_nav()
        if not nav:
            click.secho("No navigation found or config is empty.", fg="yellow")
            return

        click.secho(f"Scanning navigation in {self.config_path}...", fg="cyan")
        self._process_nav(nav)
        click.secho("Scaffolding complete! Your existing files were strictly preserved.", fg="green", bold=True)

    def _process_nav(self, nav_list):
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
            click.secho(f"[Skipped] {full_path} already exists.", fg="yellow")
        else:
            # Create a brand new file with a default Markdown header
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\nStart writing documentation for **{title}** here.\n")
            click.secho(f"[Created] {full_path}", fg="green")