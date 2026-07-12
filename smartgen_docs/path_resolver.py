"""
PathResolver: A utility for normalizing and resolving paths in SmartGen Docs.

This module ensures that all paths are resolved consistently, treating smartgen.yml
as the 'Single Source of Truth'. It handles:
- Converting relative Markdown paths to HTML paths
- Generating absolute URLs for nested pages
- Resolving static assets
- Managing breadcrumb paths
"""

import os
from pathlib import Path
from typing import Optional, Tuple


class PathResolver:
    """
    Resolves and normalizes paths for the SmartGen Docs framework.
    
    All paths are normalized relative to the site root, ensuring consistency
    across nested directories and preventing 404 errors.
    """
    
    def __init__(self, site_url: str = "", base_path: str = ""):
        """
        Initialize the PathResolver.
        
        Args:
            site_url: The base URL of the site (e.g., https://example.com/docs/)
            base_path: The base path for relative URLs (e.g., /docs/)
        """
        self.site_url = site_url.rstrip('/')
        self.base_path = base_path.rstrip('/') if base_path else ""
    
    def md_to_html(self, md_path: str) -> str:
        """
        Convert a Markdown file path to an HTML path.
        
        Args:
            md_path: Path to the Markdown file (e.g., 'getting-started/index.md')
        
        Returns:
            Path to the HTML file (e.g., 'getting-started/index.html')
        """
        if md_path.startswith('http://') or md_path.startswith('https://'):
            return md_path
        return md_path.replace('.md', '.html')
    
    def get_relative_path(self, current_page: str, target_page: str) -> str:
        """
        Get a relative path from the current page to the target page.
        
        Args:
            current_page: Path to the current page (e.g., 'getting-started/index.html')
            target_page: Path to the target page (e.g., 'docs/architecture.html')
        
        Returns:
            Relative path (e.g., '../docs/architecture.html')
        """
        if target_page.startswith('http://') or target_page.startswith('https://'):
            return target_page
        
        current_dir = os.path.dirname(current_page)
        if current_dir:
            # Calculate relative path
            common = os.path.commonpath([current_dir, os.path.dirname(target_page)])
            up_count = len(Path(current_dir).relative_to(common).parts)
            relative = os.path.join(*(['..'] * up_count), target_page)
            return relative.replace('\\', '/')
        return target_page
    
    def get_absolute_path(self, page_path: str, current_depth: int = 0) -> str:
        """
        Get an absolute path from the site root.
        
        Args:
            page_path: Path to the page (e.g., 'getting-started/index.html')
            current_depth: Depth of the current page in the directory structure
        
        Returns:
            Absolute path from site root (e.g., '/getting-started/index.html')
        """
        if page_path.startswith('http://') or page_path.startswith('https://'):
            return page_path
        
        if page_path.startswith('/'):
            return page_path
        
        # Build absolute path
        path = f"/{page_path}".replace('\\', '/')
        return path
    
    def resolve_static(self, asset_path: str, current_depth: int = 0) -> str:
        """
        Resolve a static asset path.
        
        Args:
            asset_path: Path to the asset (e.g., 'css/style.css')
            current_depth: Depth of the current page in the directory structure
        
        Returns:
            Correct path to the asset
        """
        if asset_path.startswith('http://') or asset_path.startswith('https://'):
            return asset_path
        
        if current_depth == 0:
            return f"static/{asset_path}" if not asset_path.startswith('static/') else asset_path
        
        # For nested pages, go up the directory tree
        up_path = '/'.join(['..'] * current_depth)
        return f"{up_path}/static/{asset_path}" if not asset_path.startswith('static/') else f"{up_path}/{asset_path}"
    
    def get_breadcrumb_link(self, breadcrumb_path: str, current_depth: int = 0) -> str:
        """
        Get a breadcrumb link that works from any depth.
        
        Args:
            breadcrumb_path: Path to the breadcrumb target
            current_depth: Depth of the current page
        
        Returns:
            Correct relative path for the breadcrumb
        """
        if breadcrumb_path.startswith('http://') or breadcrumb_path.startswith('https://'):
            return breadcrumb_path
        
        if current_depth == 0:
            return breadcrumb_path
        
        # For nested pages, go up the directory tree
        up_path = '/'.join(['..'] * current_depth)
        return f"{up_path}/{breadcrumb_path}"
    
    def get_current_depth(self, page_path: str) -> int:
        """
        Calculate the depth of a page in the directory structure.
        
        This counts the number of directory levels the page is nested under.
        For example:
          - 'index.html'          → depth 0 (root)
          - 'getting-started/index.html' → depth 1 (one folder deep)
          - 'docs/sub/index.html' → depth 2 (two folders deep)
        
        Args:
            page_path: Path to the page (e.g., 'getting-started/index.html')
        
        Returns:
            Depth (0 for root, 1 for one level deep, etc.)
        """
        if not page_path:
            return 0
        
        # Normalize path
        clean_path = page_path.strip('/')
        
        # Split into parts by '/'
        parts = clean_path.split('/')
        
        # If the last part is an HTML file, count directories only
        if clean_path.endswith('.html'):
            # Directory depth = total parts minus 1 (the filename)
            return len(parts) - 1 if len(parts) > 0 else 0
        
        # For non-html paths, count all parts
        return len(parts)
    
    def normalize_path(self, path: str) -> str:
        """
        Normalize a path by removing redundant separators and dots.
        
        Args:
            path: Path to normalize
        
        Returns:
            Normalized path
        """
        if path.startswith('http://') or path.startswith('https://'):
            return path
        
        # Use pathlib for normalization
        normalized = str(Path(path).as_posix())
        return normalized.lstrip('./')
