"""
Core: Main documentation builder for SmartGen Docs.

This module handles the conversion of Markdown files to HTML pages,
using the PathResolver to ensure all links are correct across nested directories.
"""

import os
import yaml
import shutil
from datetime import datetime, timezone
from xml.sax.saxutils import escape
from .converter import MarkdownConverter
from .path_resolver import PathResolver
from .link_fixer import rewrite_md_links
from .theme_engine import ThemeEngine


class Builder:
    """
    Builds the documentation site from Markdown files.
    """

    def __init__(self, config_path='smartgen.yml', site_dir='site'):
        """
        Initialize the Builder.

        Args:
            config_path: Path to the smartgen.yml configuration file
            site_dir: Directory where the built site will be output
        """
        self.config_path = config_path
        self.site_dir = site_dir
        self.config = self.load_config()
        self.docs_dir = 'docs'
        self.themes_root = os.path.join(os.path.dirname(__file__), 'themes')
        theme_name = (self.config.get('theme') or {}).get('name')
        self.theme_engine = ThemeEngine(theme_name, self.themes_root)
        self.theme_dir = self.theme_engine.theme_dir  # kept for back-compat
        self.env = self.theme_engine.env               # kept for back-compat
        self.converter = MarkdownConverter()

        # Initialize PathResolver
        site_url = self.config.get('site_url', '')
        self.path_resolver = PathResolver(site_url=site_url)

    def load_config(self):
        """Load the smartgen.yml configuration."""
        if not os.path.exists(self.config_path):
            return {"site_name": "SmartGen Docs", "nav": []}
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)

    def build(self):
        """Build the entire documentation site."""
        # Clear and create site directory
        if os.path.exists(self.site_dir):
            shutil.rmtree(self.site_dir)
        os.makedirs(self.site_dir)

        # Tell GitHub Pages not to run its own Jekyll build over this output.
        # Without this, GitHub Pages can silently fall back to auto-generating
        # a Jekyll site from README.md whenever the Pages source is set to
        # "Deploy from a branch" instead of "GitHub Actions".
        with open(os.path.join(self.site_dir, '.nojekyll'), 'w') as f:
            pass

        # Persist the custom domain across every deploy. Without this file in
        # the build artifact, an Actions-based Pages deployment can silently
        # drop a custom domain that was only ever set through the repo's
        # Settings UI.
        site_url = self.config.get('site_url', '')
        if site_url:
            domain = site_url.replace('https://', '').replace('http://', '').split('/')[0]
            if domain and '.' in domain and 'github.io' not in domain:
                with open(os.path.join(self.site_dir, 'CNAME'), 'w') as f:
                    f.write(domain)

        # Copy static assets. Delegated to ThemeEngine so each theme's
        # assets land in the right place: the default theme keeps its
        # historical un-namespaced static/ path, every other theme is
        # namespaced under static/<theme-name>/ so themes can't clobber
        # each other's filenames (see theme_engine.py).
        static_dst = os.path.join(self.site_dir, 'static')
        os.makedirs(static_dst, exist_ok=True)
        self.theme_engine.copy_static(static_dst)

        # Build pages with support for nested navigation
        nav = self.config.get('nav', [])

        # Flatten nav into an ordered sequence of real (title, md_path) pages,
        # in the same order they appear in the sidebar. This lets us compute
        # real, server-rendered Previous/Next links per page instead of
        # relying on client-side JS to fill them in after the fact.
        self.page_sequence = []

        def flatten_nav(nav_list):
            for item in nav_list:
                if isinstance(item, dict):
                    for title, path in item.items():
                        if isinstance(path, str):
                            if not path.startswith('http'):
                                self.page_sequence.append((title, path))
                        elif isinstance(path, list):
                            flatten_nav(path)
                elif isinstance(item, str):
                    self.page_sequence.append((item, item))

        flatten_nav(nav)

        def process_nav(nav_list):
            """Recursively process navigation items."""
            for item in nav_list:
                if isinstance(item, dict):
                    for title, path in item.items():
                        if isinstance(path, str):
                            self.build_page(title, path)
                        elif isinstance(path, list):
                            # Recursive call for nested categories
                            process_nav(path)
                elif isinstance(item, str):
                    self.build_page(item, item)
                    
        process_nav(nav)
        self._write_seo_files()

    def _write_seo_files(self):
        """Write valid sitemap.xml and robots.txt into the generated site."""
        site_url = (self.config.get('site_url') or '').strip().rstrip('/')
        if not site_url:
            site_url = 'http://localhost'

        urls = []
        for root, _dirs, files in os.walk(self.site_dir):
            for filename in files:
                if not filename.endswith('.html'):
                    continue
                full_path = os.path.join(root, filename)
                relative = os.path.relpath(full_path, self.site_dir).replace(os.sep, '/')
                if relative == 'index.html':
                    url_path = '/'
                else:
                    url_path = '/' + relative
                urls.append((url_path, os.path.getmtime(full_path)))

        urls.sort(key=lambda item: item[0])
        lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        ]
        for url_path, mtime in urls:
            lastmod = datetime.fromtimestamp(mtime, tz=timezone.utc).date().isoformat()
            priority = '1.0' if url_path == '/' else '0.8'
            changefreq = 'weekly' if url_path in {'/', '/docs/changelog.html', '/docs/releases.html'} else 'monthly'
            lines.extend([
                '  <url>',
                f'    <loc>{escape(site_url + url_path)}</loc>',
                f'    <lastmod>{lastmod}</lastmod>',
                f'    <changefreq>{changefreq}</changefreq>',
                f'    <priority>{priority}</priority>',
                '  </url>',
            ])
        lines.append('</urlset>')
        with open(os.path.join(self.site_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')

        with open(os.path.join(self.site_dir, 'robots.txt'), 'w', encoding='utf-8') as f:
            f.write('User-agent: *\nAllow: /\n\n')
            f.write(f'Sitemap: {site_url}/sitemap.xml\n')

    def build_page(self, title, md_path):
        """
        Build a single page from Markdown to HTML.
        
        Args:
            title: Title of the page
            md_path: Path to the Markdown file (relative to docs_dir)
        """
        # Skip external URLs
        if md_path.startswith('http://') or md_path.startswith('https://'):
            return
        
        src_path = os.path.join(self.docs_dir, md_path)
        if not os.path.exists(src_path):
            print(f"Warning: File {src_path} not found.")
            return

        with open(src_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Rewrite contextual internal links that still point at the '.md'
        # source (e.g. '[Installation](installation.md)') so they point at
        # the built '.html' page instead. Without this, every in-body link
        # 404s on the live site even though the generated nav menu is fine,
        # because the nav is built from smartgen.yml paths directly while
        # body content is authored in Markdown and passed through untouched.
        md_content, _links_fixed = rewrite_md_links(md_content)

        html_body = self.converter.convert(md_content)

        template = self.theme_engine.get_template()

        # Calculate page depth for relative path resolution
        relative_path = md_path.replace('.md', '.html')
        current_depth = self.path_resolver.get_current_depth(relative_path)
        
        # Generate breadcrumbs with proper paths
        breadcrumbs = [
            {"title": "Home", "link": self.path_resolver.get_breadcrumb_link("index.html", current_depth)},
            {"title": title, "link": relative_path}
        ]

        # Real, server-rendered previous/next links (same order as the sidebar)
        prev_page, next_page = None, None
        sequence = getattr(self, 'page_sequence', [])
        current_index = None
        for i, (seq_title, seq_path) in enumerate(sequence):
            if seq_path == md_path:
                current_index = i
                if i > 0:
                    p_title, p_path = sequence[i - 1]
                    prev_page = {"title": p_title, "link": self.path_resolver.get_breadcrumb_link(p_path.replace('.md', '.html'), current_depth)}
                if i < len(sequence) - 1:
                    n_title, n_path = sequence[i + 1]
                    next_page = {"title": n_title, "link": self.path_resolver.get_breadcrumb_link(n_path.replace('.md', '.html'), current_depth)}
                break

        # Generic, theme-agnostic "how far through the docs is this page"
        # data. Any theme can use it (e.g. a curriculum-style progress
        # bar); themes that don't care simply ignore these context vars.
        total_pages = len(sequence)
        progress_percent = (
            round(((current_index + 1) / total_pages) * 100)
            if current_index is not None and total_pages
            else None
        )

        output_content = template.render(
            title=title,
            content=html_body,
            config=self.config,
            nav=self.config.get('nav', []),
            current_page=md_path,
            raw_markdown=md_content,
            breadcrumbs=breadcrumbs,
            prev_page=prev_page,
            next_page=next_page,
            current_depth=current_depth,
            path_resolver=self.path_resolver,
            url_for=lambda type, filename: self._url_for(type, filename, current_depth),
            theme_name=self.theme_engine.name,
            current_index=current_index,
            total_pages=total_pages,
            progress_percent=progress_percent,
        )

        # Handle nested paths
        dst_path = os.path.join(self.site_dir, relative_path)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)

        with open(dst_path, 'w', encoding='utf-8') as f:
            f.write(output_content)

    def _url_for(self, type, filename, current_depth=0):
        """
        Helper for template to resolve URLs.
        
        Args:
            type: Type of URL ('static', 'page', etc.)
            filename: Name of the file
            current_depth: Depth of the current page
        
        Returns:
            Resolved URL
        """
        if type == 'static':
            # Themes other than the default are namespaced under
            # static/<theme-name>/ (see theme_engine.py) so their assets
            # can't collide with another theme's filenames. Every theme's
            # own templates can still just write url_for('static',
            # 'css/whatever.css') -- the namespace is applied here,
            # transparently, based on whichever theme is actually active.
            namespace = self.theme_engine.static_namespace
            resolved_filename = f"{namespace}/{filename}" if namespace else filename
            return self.path_resolver.resolve_static(resolved_filename, current_depth)
        elif type == 'page':
            return self.path_resolver.get_breadcrumb_link(filename, current_depth)
        return filename