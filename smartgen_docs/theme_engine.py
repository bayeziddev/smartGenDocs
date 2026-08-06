"""
ThemeEngine: resolves a theme name to a Jinja2 environment, a content
template, and a set of static asset directories -- with safe fallback to
the default theme so a typo'd or half-installed `theme.name` in
smartgen.yml never hard-fails a build.

Directory convention, under smartgen_docs/themes/:

    themes/
      _shared/                     # NOT a selectable theme -- include-only
        partials/
          theme_prepaint.html      # pre-paint FOUC-prevention <script>
          theme_switcher.html      # the palette icon + popover markup
          theme_switcher_script.html
      default/                     # the existing "premium" theme
        base_premium.html
        page_premium.html
        static/css/premium.css
      education/                   # a structural theme
        base.html
        page.html
        static/css/education.css
      book/
        base.html
        page.html
        static/css/book.css
      ...

Adding a theme is just adding a new directory here with its own
templates and static/ folder -- nothing in core.py has to change, and
nothing about one theme's markup, CSS, or asset filenames can collide
with another's (see the static-namespacing rule below).

Every theme directory needs at least one of `page.html` or
`page_premium.html` (checked in that order) -- that file is rendered as
the page content template.  `page_premium.html` only exists so the
original theme doesn't need to be renamed; every new theme should use
`page.html`.  A theme's `base.html`/`base_premium.html` (extended by its
page template) is a theme-internal detail ThemeEngine doesn't need to
know about.

Shared partials: every theme's templates can `{% include %}` anything
under `_shared/`, and can also fall back to the *default* theme's own
templates for anything they don't override (the ChoiceLoader below
checks the requested theme's own directory first, then `_shared/`, then
`default/`) -- so, for example, a new theme that wants the exact same
theme-switcher script as the default theme just includes it by name and
never has to copy-paste it.

---

This replaces an earlier version of this module that shipped in the repo
but was never actually wired into `core.py` (nothing imported it). It
also worked differently in a way that wouldn't have fit how this
generator already renders pages: it returned raw file *paths* instead of
compiled Jinja2 templates, had no shared-loader / template-inheritance
story across themes, and copied every theme's `static/` into the same
un-namespaced `site/static/` folder -- which two themes shipping, say,
their own `static/css/main.css` would silently clobber. The design below
fixes all three: it hands back a ready-to-use `jinja2.Environment`, lets
themes `{% include %}` or `{% extends %}` shared/default templates, and
namespaces every non-default theme's assets so they can't collide.
"""

from __future__ import annotations

import os
import shutil
from jinja2 import ChoiceLoader, Environment, FileSystemLoader

DEFAULT_THEME = "default"

# Back-compat: smartgen.yml files written before this module existed say
# `theme.name: premium` (the display name of the built-in theme, not its
# directory name). Keep that spelling working forever.
THEME_ALIASES = {
    "premium": DEFAULT_THEME,
}

# Checked in order; first one that exists in the theme's directory wins.
# page_premium.html is checked first for backward compatibility: the
# default theme's directory also still contains an older, unmaintained
# page.html/base.html pair (superseded by page_premium.html/
# base_premium.html years ago, but never deleted) -- so for *new* themes,
# which only ship page.html, that's still the one that gets picked;
# for the default theme specifically, this ordering makes sure the real,
# maintained template keeps winning.
CONTENT_TEMPLATE_CANDIDATES = ("page_premium.html", "page.html")


class ThemeEngine:
    """Resolves `theme_name` against `themes_root` and exposes everything
    core.Builder needs to render pages in that theme: a Jinja2
    Environment, the content template to render per page, and the
    static-asset directories to copy into the build output."""

    def __init__(self, theme_name: str | None, themes_root: str):
        self.themes_root = themes_root
        self.shared_dir = os.path.join(themes_root, "_shared")

        requested = theme_name or DEFAULT_THEME
        requested = THEME_ALIASES.get(requested, requested)
        self.requested_name = theme_name or DEFAULT_THEME

        self.name, self.theme_dir, self.template_name = self._resolve(requested)

        # Namespacing rule for static assets: the default theme keeps its
        # historical, un-namespaced output path (static/css/premium.css)
        # so nothing that already links to it breaks. Every other theme's
        # assets are copied under static/<theme-name>/ instead, so two
        # themes can both ship e.g. static/css/main.css without clobbering
        # each other in the build output.
        self.static_namespace = "" if self.name == DEFAULT_THEME else self.name

        self.env = Environment(
            loader=ChoiceLoader(
                [
                    FileSystemLoader(self.theme_dir),
                    FileSystemLoader(self.shared_dir),
                    FileSystemLoader(os.path.join(themes_root, DEFAULT_THEME)),
                ]
            )
        )

    def _resolve(self, requested_slug: str) -> tuple[str, str, str]:
        """Find a real theme directory + content template for
        `requested_slug`. Falls back to the default theme (printing a
        warning) if the requested one doesn't exist or has no usable
        content template, so a bad theme.name in smartgen.yml degrades
        gracefully instead of crashing the build."""
        candidate_dir = os.path.join(self.themes_root, requested_slug)
        template = self._find_content_template(candidate_dir)
        if template:
            return requested_slug, candidate_dir, template

        if requested_slug != DEFAULT_THEME:
            available = ", ".join(self.available_themes(self.themes_root)) or "(none found)"
            print(
                f"⚠️  Theme '{requested_slug}' not found under "
                f"{self.themes_root} (or missing page.html/page_premium.html). "
                f"Falling back to '{DEFAULT_THEME}'. Available themes: {available}"
            )

        default_dir = os.path.join(self.themes_root, DEFAULT_THEME)
        default_template = self._find_content_template(default_dir)
        if not default_template:
            raise RuntimeError(
                f"The default theme itself is missing or broken (looked in "
                f"{default_dir} for {' / '.join(CONTENT_TEMPLATE_CANDIDATES)}). "
                "This SmartGen Docs installation looks corrupted."
            )
        return DEFAULT_THEME, default_dir, default_template

    @staticmethod
    def _find_content_template(theme_dir: str) -> str | None:
        if not os.path.isdir(theme_dir):
            return None
        for candidate in CONTENT_TEMPLATE_CANDIDATES:
            if os.path.exists(os.path.join(theme_dir, candidate)):
                return candidate
        return None

    @staticmethod
    def available_themes(themes_root: str) -> list[str]:
        """List every directory under `themes_root` that's a real,
        selectable theme (has a content template). Excludes `_shared/`
        and anything else that isn't a theme."""
        if not os.path.isdir(themes_root):
            return []
        found = []
        for entry in sorted(os.listdir(themes_root)):
            if entry.startswith("_") or entry.startswith("."):
                continue
            theme_dir = os.path.join(themes_root, entry)
            if ThemeEngine._find_content_template(theme_dir):
                found.append(entry)
        return found

    def get_template(self):
        """The Jinja2 Template to render for every page in this theme."""
        return self.env.get_template(self.template_name)

    def iter_static_dirs(self):
        """Yield (source_dir, dest_subdir) pairs to copy into the build's
        static/ output directory. dest_subdir is '' for the default theme
        (historical, un-namespaced path) and the theme's own slug for
        everything else -- see the namespacing note in the module
        docstring."""
        theme_static = os.path.join(self.theme_dir, "static")
        if os.path.isdir(theme_static):
            yield theme_static, self.static_namespace

        # Shared, theme-agnostic static assets (if any exist) always land
        # at static/_shared/ so they can never collide with a theme's own
        # filenames either.
        shared_static = os.path.join(self.shared_dir, "static")
        if os.path.isdir(shared_static):
            yield shared_static, "_shared"

    def copy_static(self, site_static_dir: str) -> None:
        """Copy every static directory this theme contributes into the
        build output, honoring the namespacing rule above."""
        for source_dir, dest_subdir in self.iter_static_dirs():
            dest_dir = os.path.join(site_static_dir, dest_subdir) if dest_subdir else site_static_dir
            shutil.copytree(source_dir, dest_dir, dirs_exist_ok=True)
