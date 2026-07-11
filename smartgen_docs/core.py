import os
import yaml
import shutil
from jinja2 import Environment, FileSystemLoader
from .converter import MarkdownConverter

class Builder:
    def __init__(self, config_path, site_dir='site'):
        self.config_path = config_path
        self.site_dir = site_dir
        self.config = self.load_config()
        self.docs_dir = 'docs'
        self.theme_dir = os.path.join(os.path.dirname(__file__), 'themes', 'default')
        self.converter = MarkdownConverter()
        self.env = Environment(loader=FileSystemLoader(self.theme_dir))

    def load_config(self):
        if not os.path.exists(self.config_path):
            return {"site_name": "SmartGen Docs", "nav": []}
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)

    def build(self):
        # Clear and create site directory
        if os.path.exists(self.site_dir):
            shutil.rmtree(self.site_dir)
        os.makedirs(self.site_dir)

        # Copy static assets
        static_src = os.path.join(self.theme_dir, 'static')
        static_dst = os.path.join(self.site_dir, 'static')
        if os.path.exists(static_src):
            shutil.copytree(static_src, static_dst)

        # Build pages
        nav = self.config.get('nav', [])
        for item in nav:
            if isinstance(item, dict):
                for title, path in item.items():
                    self.build_page(title, path)
            elif isinstance(item, str):
                # Handle simple string nav items if any
                self.build_page(item, item)

    def build_page(self, title, md_path):
        src_path = os.path.join(self.docs_dir, md_path)
        if not os.path.exists(src_path):
            print(f"Warning: File {src_path} not found.")
            return

        with open(src_path, 'r') as f:
            md_content = f.read()

        html_body = self.converter.convert(md_content)
        
        # Use premium template if it exists
        template_name = 'page_premium.html' if os.path.exists(os.path.join(self.theme_dir, 'page_premium.html')) else 'page.html'
        template = self.env.get_template(template_name)
        
        # Generate breadcrumbs
        breadcrumbs = [
            {"title": "Home", "link": "index.html"},
            {"title": title, "link": md_path.replace('.md', '.html')}
        ]

        output_content = template.render(
            title=title,
            content=html_body,
            config=self.config,
            nav=self.config.get('nav', []),
            current_page=md_path,
            breadcrumbs=breadcrumbs,
            url_for=self.url_for
        )

        # Handle nested paths
        relative_path = md_path.replace('.md', '.html')
        dst_path = os.path.join(self.site_dir, relative_path)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)

        with open(dst_path, 'w') as f:
            f.write(output_content)

    def url_for(self, type, filename):
        """Helper for template to resolve static URLs."""
        if type == 'static':
            return f"static/{filename}"
        return filename
