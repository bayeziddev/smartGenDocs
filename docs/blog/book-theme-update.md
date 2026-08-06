diff --git a/smartgen_docs/themes/book/base.html b/smartgen_docs/themes/book/base.html
new file mode 100644
index 0000000..96f9414
--- /dev/null
+++ b/smartgen_docs/themes/book/base.html
@@ -0,0 +1,395 @@
+<!DOCTYPE html>
+<html lang="en">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    {% set theme_modes = ['light', 'dark'] %}
+    {% include "partials/theme_prepaint.html" with context %}
+    <meta name="description" content="{{ config.site_description | default('Documentation') }}">
+    {% set page_url = config.site_url.rstrip('/') + '/' + current_page.replace('.md', '.html') if current_page and current_page != 'index.md' else config.site_url %}
+    <link rel="canonical" href="{{ page_url }}">
+    <meta property="og:title" content="{{ title }} - {{ config.site_name }}">
+    <meta property="og:description" content="{{ config.site_description | default('Documentation') }}">
+    <meta property="og:url" content="{{ page_url }}">
+    <meta property="og:type" content="website">
+    <meta name="twitter:card" content="summary">
+    <title>{{ title }} - {{ config.site_name }}</title>
+    <link rel="stylesheet" href="{{ url_for('static', 'css/book.css') }}">
+    <noscript><style>.book-content > * { opacity: 1 !important; transform: none !important; }</style></noscript>
+    {% if config.theme and config.theme.palette %}
+    <style>
+        :root, :root[data-theme] {
+            --book-primary: {{ config.theme.palette.primary | default('#1F3A5F') }};
+            --book-accent: {{ config.theme.palette.accent | default('#7A6A53') }};
+        }
+    </style>
+    {% endif %}
+</head>
+<body class="book-body">
+    <!-- AMBIENT BACKGROUND MOTION
+         Fixed, decorative, pointer-events:none layer sitting behind
+         everything: two slow-drifting light washes plus a handful of
+         open-book glyphs that rise and turn like pages settling. Pure
+         CSS transform/opacity keyframes -- no images, no third-party
+         particle library. Disabled entirely under prefers-reduced-motion
+         (see book.css). -->
+    <div class="book-ambient" aria-hidden="true">
+        <span class="book-ambient-glow book-ambient-glow-a"></span>
+        <span class="book-ambient-glow book-ambient-glow-b"></span>
+        <span class="book-ambient-page book-ambient-page-1">
+            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 5.5c2-1 5-1 8 .5 3-1.5 6-1.5 8-.5v13c-2-1-5-1-8 .5-3-1.5-6-1.5-8-.5V5.5Z"/></svg>
+        </span>
+        <span class="book-ambient-page book-ambient-page-2">
+            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 5.5c2-1 5-1 8 .5 3-1.5 6-1.5 8-.5v13c-2-1-5-1-8 .5-3-1.5-6-1.5-8-.5V5.5Z"/></svg>
+        </span>
+        <span class="book-ambient-page book-ambient-page-3">
+            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 5.5c2-1 5-1 8 .5 3-1.5 6-1.5 8-.5v13c-2-1-5-1-8 .5-3-1.5-6-1.5-8-.5V5.5Z"/></svg>
+        </span>
+        <span class="book-ambient-mote book-ambient-mote-1"></span>
+        <span class="book-ambient-mote book-ambient-mote-2"></span>
+        <span class="book-ambient-mote book-ambient-mote-3"></span>
+        <span class="book-ambient-mote book-ambient-mote-4"></span>
+    </div>
+
+    <!-- SCROLL READING PROGRESS -->
+    <div class="book-progress-rail"><div class="book-progress-fill" id="book-progress-fill"></div></div>
+
+    <!-- RUNNING HEAD -->
+    <header class="book-header" id="book-header">
+        <div class="book-container">
+            <button class="book-menu-toggle" id="menu-toggle" type="button" aria-label="Toggle contents">
+                <svg class="icon" viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
+            </button>
+            <a class="book-brand" href="{{ url_for('page', 'index.html') }}">
+                <span class="book-brand-mark" aria-hidden="true">
+                    <svg viewBox="0 0 24 24"><path d="M4 5.5c2-1 5-1 8 .5 3-1.5 6-1.5 8-.5v13c-2-1-5-1-8 .5-3-1.5-6-1.5-8-.5V5.5Z"/><path d="M12 6v13"/></svg>
+                </span>
+                <span class="book-brand-name">{{ config.site_name }}</span>
+            </a>
+            <span class="book-running-title">{{ title }}</span>
+
+            <div class="book-search">
+                <svg class="icon" viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.3-4.3"/></svg>
+                <input type="text" id="search-input" placeholder="Searchâ¦">
+                <div class="book-search-results" id="search-results"></div>
+            </div>
+
+            <div class="book-header-right">
+                <button class="book-icon-btn" id="focus-toggle" type="button" aria-pressed="false" aria-label="Toggle focused reading mode" title="Focused reading mode">
+                    <svg class="icon" viewBox="0 0 24 24"><path d="M4 9V5a1 1 0 0 1 1-1h4M20 9V5a1 1 0 0 0-1-1h-4M4 15v4a1 1 0 0 0 1 1h4M20 15v4a1 1 0 0 1-1 1h-4"/></svg>
+                </button>
+                <a href="https://github.com/bayeziddev/smartGenDocs" target="_blank" rel="noopener" class="book-icon-btn" aria-label="View source on GitHub">
+                    <svg class="icon filled" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
+                </a>
+                {% include "partials/theme_switcher.html" %}
+
+                <!-- READER AVATAR
+                     A dynamic, data-driven avatar for the person reading --
+                     not a fake login. It reflects real local state (pages
+                     visited, overall progress, last page) tracked in
+                     localStorage, same convention as the Education theme's
+                     lesson-visited tracking. Hover shows a quick-glance
+                     tooltip + glow ring; click opens the full popover. -->
+                <div class="book-avatar" id="book-avatar">
+                    <button class="book-avatar-btn" id="avatar-toggle" type="button"
+                            aria-haspopup="true" aria-expanded="false" aria-controls="avatar-popover"
+                            aria-label="Your reading session">
+                        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
+                            <circle cx="12" cy="8.5" r="3.4"/>
+                            <path d="M5 20c1.2-3.6 4-5.4 7-5.4s5.8 1.8 7 5.4"/>
+                        </svg>
+                        <span class="book-avatar-ring" aria-hidden="true"></span>
+                    </button>
+                    <span class="book-avatar-tooltip" role="tooltip">Your reading session</span>
+
+                    <div class="book-avatar-popover" id="avatar-popover" role="dialog" aria-label="Your reading session" hidden>
+                        <div class="book-avatar-popover-header">
+                            <span class="book-avatar-popover-icon" aria-hidden="true">
+                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
+                                    <circle cx="12" cy="8.5" r="3.4"/>
+                                    <path d="M5 20c1.2-3.6 4-5.4 7-5.4s5.8 1.8 7 5.4"/>
+                                </svg>
+                            </span>
+                            <div>
+                                <p class="book-avatar-name">Reading session</p>
+                                <p class="book-avatar-sub">Tracked in this browser only</p>
+                            </div>
+                        </div>
+                        <div class="book-avatar-stats">
+                            <div class="book-avatar-stat">
+                                <span id="avatar-pages-read">0</span>
+                                <label>Pages visited</label>
+                            </div>
+                            <div class="book-avatar-stat">
+                                <span id="avatar-progress">0%</span>
+                                <label>Book progress</label>
+                            </div>
+                        </div>
+                        <button class="book-avatar-action" id="avatar-resume" type="button">Resume last page</button>
+                    </div>
+                </div>
+            </div>
+        </div>
+    </header>
+
+    <div class="book-sidebar-overlay" id="sidebar-overlay"></div>
+
+    <div class="book-shell">
+        <!-- CONTENTS RAIL -->
+        <aside class="book-sidebar" id="sidebar">
+            <div class="book-sidebar-header">
+                <span>Contents</span>
+                <button class="book-sidebar-close" id="sidebar-close" type="button" aria-label="Close contents">
+                    <svg class="icon" viewBox="0 0 24 24"><path d="M5 5l14 14M19 5 5 19"/></svg>
+                </button>
+            </div>
+            <nav class="book-nav">
+                <ul>
+                {% for item in nav %}
+                    {% for label, link in item.items() %}
+                        {% if link is string %}
+                            {% if not link.startswith('http') %}
+                                {% set html_link = link.replace('.md', '.html') %}
+                                {% set is_active = (link == current_page) %}
+                                <li class="book-nav-item{% if is_active %} active{% endif %}" style="--stagger:{{ loop.index0 }}">
+                                    <a href="{{ url_for('page', html_link) }}" data-nav-link data-book-page="{{ html_link }}" class="book-nav-link{% if is_active %} active{% endif %}">{{ label }}</a>
+                                </li>
+                            {% else %}
+                                <li class="book-nav-item" style="--stagger:{{ loop.index0 }}">
+                                    <a href="{{ link }}" target="_blank" rel="noopener" class="book-nav-link book-nav-link-external">{{ label }}</a>
+                                </li>
+                            {% endif %}
+                        {% else %}
+                            {% set section_label = label %}
+                            {%- set ns = namespace(has_active_child=false) -%}
+                            {% for subitem in link %}
+                                {% for sublabel, sublink in subitem.items() %}
+                                    {% if not sublink.startswith('http') and sublink == current_page %}
+                                        {% set ns.has_active_child = true %}
+                                    {% endif %}
+                                {% endfor %}
+                            {% endfor %}
+                            <li class="book-chapter{% if ns.has_active_child %} expanded{% endif %}" data-nav-section style="--stagger:{{ loop.index0 }}">
+                                <button class="book-chapter-toggle" type="button" data-section="{{ section_label | lower | replace(' ', '-') }}">
+                                    <span class="book-chapter-label">{{ section_label }}</span>
+                                    <svg class="icon book-chapter-arrow" viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg>
+                                </button>
+                                <ul class="book-chapter-pages" data-nav-submenu>
+                                    {% for subitem in link %}
+                                        {% for sublabel, sublink in subitem.items() %}
+                                            {% if not sublink.startswith('http') %}
+                                                {% set html_link = sublink.replace('.md', '.html') %}
+                                                {% set is_active = (sublink == current_page) %}
+                                                <li class="book-nav-item book-nav-item-sub">
+                                                    <a href="{{ url_for('page', html_link) }}" data-nav-link data-book-page="{{ html_link }}" class="book-nav-link{% if is_active %} active{% endif %}">{{ sublabel }}</a>
+                                                </li>
+                                            {% else %}
+                                                <li class="book-nav-item book-nav-item-sub">
+                                                    <a href="{{ sublink }}" target="_blank" rel="noopener" class="book-nav-link book-nav-link-external">{{ sublabel }}</a>
+                                                </li>
+                                            {% endif %}
+                                        {% endfor %}
+                                    {% endfor %}
+                                </ul>
+                            </li>
+                        {% endif %}
+                    {% endfor %}
+                {% endfor %}
+                </ul>
+            </nav>
+        </aside>
+
+        <!-- PAGE -->
+        <main class="book-main">
+            <div class="book-page">
+                {% if current_index is not none %}
+                <p class="book-chapter-eyebrow">Page {{ current_index + 1 }} of {{ total_pages }}</p>
+                {% endif %}
+                <h1 class="book-title">{{ title }}</h1>
+                <div class="book-rule" aria-hidden="true">&#10022;</div>
+
+                <article class="book-content" data-current-path="{{ current_page.replace('.md', '.html') if current_page else '' }}" data-progress="{{ progress_percent if progress_percent is not none else 0 }}">
+                    {% block content %}{% endblock %}
+                </article>
+
+                <div class="book-page-turn">
+                    {% if prev_page %}
+                    <a class="book-page-btn book-page-prev" href="{{ prev_page.link }}">
+                        <span class="book-page-corner">&#10094;</span>
+                        <span>
+                            <span class="book-page-label">Previous</span>
+                            <span class="book-page-title">{{ prev_page.title }}</span>
+                        </span>
+                    </a>
+                    {% else %}<span></span>{% endif %}
+                    {% if next_page %}
+                    <a class="book-page-btn book-page-next" href="{{ next_page.link }}">
+                        <span>
+                            <span class="book-page-label">Next</span>
+                            <span class="book-page-title">{{ next_page.title }}</span>
+                        </span>
+                        <span class="book-page-corner">&#10095;</span>
+                    </a>
+                    {% endif %}
+                </div>
+            </div>
+        </main>
+    </div>
+
+    <footer class="book-footer">
+        <div class="book-container">
+            <p class="book-footer-copy">&copy; 2026 <a href="{{ config.site_url }}">{{ config.site_author }}</a> &middot; Built with SmartGen Docs &middot; <a href="https://github.com/bayeziddev/smartGenDocs" target="_blank" rel="noopener">GitHub</a></p>
+        </div>
+    </footer>
+
+    <script>
+        // ========== SIDEBAR TOGGLE (Mobile) ==========
+        const menuToggle = document.getElementById('menu-toggle');
+        const sidebar = document.getElementById('sidebar');
+        const sidebarClose = document.getElementById('sidebar-close');
+        const sidebarOverlay = document.getElementById('sidebar-overlay');
+        function openSidebar() { sidebar.classList.add('open'); sidebarOverlay.classList.add('visible'); }
+        function closeSidebar() { sidebar.classList.remove('open'); sidebarOverlay.classList.remove('visible'); }
+        menuToggle.addEventListener('click', openSidebar);
+        sidebarClose.addEventListener('click', closeSidebar);
+        sidebarOverlay.addEventListener('click', closeSidebar);
+
+        // ========== CHAPTER EXPAND/COLLAPSE ==========
+        document.querySelectorAll('.book-chapter-toggle').forEach(toggle => {
+            toggle.addEventListener('click', () => toggle.closest('.book-chapter').classList.toggle('expanded'));
+        });
+
+        // ========== FOCUSED READING MODE ==========
+        (function () {
+            const KEY = 'smartgen-book-focus';
+            const toggle = document.getElementById('focus-toggle');
+            function setFocus(on) {
+                document.body.classList.toggle('book-focus', on);
+                toggle.setAttribute('aria-pressed', String(on));
+            }
+            let saved = false;
+            try { saved = localStorage.getItem(KEY) === '1'; } catch (e) { /* ignore */ }
+            setFocus(saved);
+            toggle.addEventListener('click', () => {
+                const on = !document.body.classList.contains('book-focus');
+                setFocus(on);
+                try { localStorage.setItem(KEY, on ? '1' : '0'); } catch (e) { /* ignore */ }
+            });
+        })();
+
+        // ========== SCROLL READING PROGRESS + HEADER MOTION ==========
+        (function () {
+            const fill = document.getElementById('book-progress-fill');
+            const article = document.querySelector('.book-content');
+            const header = document.getElementById('book-header');
+            if (!fill || !article) return;
+            function update() {
+                const rect = article.getBoundingClientRect();
+                const total = rect.height - window.innerHeight + rect.top + window.scrollY;
+                const scrolled = window.scrollY - (rect.top + window.scrollY) + window.innerHeight * 0.5;
+                const pct = total > 0 ? Math.min(100, Math.max(0, (scrolled / total) * 100)) : 0;
+                fill.style.width = pct + '%';
+                if (header) header.classList.toggle('is-scrolled', window.scrollY > 8);
+            }
+            document.addEventListener('scroll', update, { passive: true });
+            window.addEventListener('resize', update);
+            update();
+        })();
+
+        // ========== SCROLL-IN REVEAL FOR CONTENT ==========
+        (function () {
+            const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
+            const items = document.querySelectorAll('.book-content > *');
+            if (reduceMotion || !('IntersectionObserver' in window)) {
+                items.forEach(el => el.classList.add('is-visible'));
+                return;
+            }
+            const io = new IntersectionObserver((entries) => {
+                entries.forEach(entry => {
+                    if (entry.isIntersecting) {
+                        entry.target.classList.add('is-visible');
+                        io.unobserve(entry.target);
+                    }
+                });
+            }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
+            items.forEach(el => io.observe(el));
+        })();
+
+        // ========== COPY CODE BUTTON ==========
+        document.querySelectorAll('.book-content pre').forEach(block => {
+            const button = document.createElement('button');
+            button.className = 'copy-code-btn';
+            button.innerHTML = '<span>Copy</span>';
+            button.addEventListener('click', () => {
+                const codeEl = block.querySelector('code');
+                const code = codeEl ? codeEl.textContent : block.textContent;
+                navigator.clipboard.writeText(code).then(() => {
+                    button.querySelector('span').textContent = 'Copied';
+                    setTimeout(() => { button.querySelector('span').textContent = 'Copy'; }, 2000);
+                });
+            });
+            block.style.position = 'relative';
+            block.appendChild(button);
+        });
+
+        // ========== READER AVATAR: session tracking + popover ==========
+        (function () {
+            const PAGES_KEY = 'smartgen-book-pages-read';
+            const LAST_KEY = 'smartgen-book-last-page';
+            const article = document.querySelector('.book-content');
+            const here = article ? article.dataset.currentPath : '';
+            const progress = article ? parseInt(article.dataset.progress, 10) || 0 : 0;
+
+            let visited = [];
+            try { visited = JSON.parse(localStorage.getItem(PAGES_KEY) || '[]'); } catch (e) { visited = []; }
+            if (here && !visited.includes(here)) visited.push(here);
+            try {
+                localStorage.setItem(PAGES_KEY, JSON.stringify(visited));
+                if (here) localStorage.setItem(LAST_KEY, here);
+            } catch (e) { /* ignore */ }
+
+            const pagesEl = document.getElementById('avatar-pages-read');
+            const progressEl = document.getElementById('avatar-progress');
+            if (pagesEl) pagesEl.textContent = String(visited.length);
+            if (progressEl) progressEl.textContent = progress + '%';
+
+            const avatar = document.getElementById('book-avatar');
+            const avatarToggle = document.getElementById('avatar-toggle');
+            const avatarPopover = document.getElementById('avatar-popover');
+            const avatarResume = document.getElementById('avatar-resume');
+            if (!avatar || !avatarToggle || !avatarPopover) return;
+
+            function openPopover() {
+                avatarPopover.hidden = false;
+                avatarToggle.setAttribute('aria-expanded', 'true');
+            }
+            function closePopover() {
+                avatarPopover.hidden = true;
+                avatarToggle.setAttribute('aria-expanded', 'false');
+            }
+            avatarToggle.addEventListener('click', () => {
+                avatarPopover.hidden ? openPopover() : closePopover();
+            });
+            document.addEventListener('click', (e) => {
+                if (!avatarPopover.hidden && !avatar.contains(e.target)) closePopover();
+            });
+            document.addEventListener('keydown', (e) => {
+                if (e.key === 'Escape' && !avatarPopover.hidden) { closePopover(); avatarToggle.focus(); }
+            });
+            if (avatarResume) {
+                avatarResume.addEventListener('click', () => {
+                    let last = null;
+                    try { last = localStorage.getItem(LAST_KEY); } catch (e) { /* ignore */ }
+                    if (last) window.location.href = last;
+                });
+            }
+        })();
+    </script>
+    {% include "partials/active_nav_script.html" %}
+    {% set theme_switcher_modes = [
+        {"value": "light", "label": "Day", "swatch_bg": "#F5F6F3", "swatch_fg": "#1F3A5F"},
+        {"value": "dark", "label": "Night", "swatch_bg": "#14171C", "swatch_fg": "#7C9CC4"}
+    ] %}
+    {% include "partials/theme_switcher_script.html" with context %}
+</body>
+</html>
diff --git a/smartgen_docs/themes/book/page.html b/smartgen_docs/themes/book/page.html
new file mode 100644
index 0000000..e3d3199
--- /dev/null
+++ b/smartgen_docs/themes/book/page.html
@@ -0,0 +1,4 @@
+{% extends "base.html" %}
+{% block content %}
+{{ content | safe }}
+{% endblock %}
diff --git a/smartgen_docs/themes/book/static/css/book.css b/smartgen_docs/themes/book/static/css/book.css
new file mode 100644
index 0000000..f41db46
--- /dev/null
+++ b/smartgen_docs/themes/book/static/css/book.css
@@ -0,0 +1,417 @@
+/* ==========================================================================
+   Book / Writer Docs theme
+   Focused reading mode: serif typography, chapter-style navigation,
+   paginated feel, drop caps, scroll-based reading progress, ambient
+   background motion, a reader avatar, and fluid page/element/scroll
+   motion throughout. Zero third-party fonts/icons/CSS/animation
+   libraries -- system serif stack, inline SVG, and native CSS/JS only.
+   ========================================================================== */
+
+/* ---------- Design tokens ---------- */
+:root {
+    /* Palette -- cool paper white + ink blue + muted brass accent.
+       Deliberately NOT warm-cream-plus-terracotta, to read as distinct
+       from the Education theme's warm parchment palette. */
+    --book-bg: #F5F6F3;
+    --book-bg-soft: #ECEEE8;
+    --book-surface: #FFFFFF;
+    --book-ink: #1B2430;
+    --book-ink-soft: #4B5768;
+    --book-ink-faint: #8993A1;
+    --book-border: #DDE1DC;
+    --book-primary: #1F3A5F;
+    --book-primary-soft: #E7ECF3;
+    --book-accent: #7A6A53;
+    --book-accent-soft: #EFEAE0;
+    --book-danger: #A83232;
+    --book-shadow: 0 1px 2px rgba(27, 36, 48, .05), 0 8px 24px -10px rgba(27, 36, 48, .2);
+
+    /* Ambient background motion -- low-alpha versions of the same
+       palette, kept faint enough that reading contrast never suffers. */
+    --book-glow-a: rgba(31, 58, 95, .08);
+    --book-glow-b: rgba(122, 106, 83, .09);
+    --book-page-tint: rgba(122, 106, 83, .14);
+    --book-mote-tint: rgba(31, 58, 95, .18);
+
+    /* Typography -- system serif reading stack */
+    --book-font-serif: Georgia, "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Palatino, "Noto Serif", serif;
+    --book-font-sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
+    --book-font-mono: ui-monospace, "SF Mono", "Cascadia Code", "Roboto Mono", Menlo, Consolas, monospace;
+    --book-fs-sm: .875rem;
+    --book-fs-base: 1.0625rem;
+    --book-fs-lg: 1.25rem;
+    --book-fs-xl: 1.65rem;
+    --book-fs-2xl: 2.5rem;
+    --book-lh-base: 1.85;
+    --book-measure: 68ch;
+
+    --book-sp-1: .25rem;
+    --book-sp-2: .5rem;
+    --book-sp-3: .75rem;
+    --book-sp-4: 1rem;
+    --book-sp-5: 1.5rem;
+    --book-sp-6: 2.25rem;
+    --book-sp-7: 3.5rem;
+    --book-sp-8: 5rem;
+    --book-radius-sm: 6px;
+    --book-radius-md: 10px;
+    --book-radius-lg: 16px;
+
+    --book-ease-standard: cubic-bezier(.4, 0, .2, 1);
+    --book-ease-emphasized: cubic-bezier(.2, 0, 0, 1);
+    --book-ease-bounce: cubic-bezier(.34, 1.56, .64, 1);
+    --book-dur-fast: 150ms;
+    --book-dur-base: 260ms;
+    --book-dur-slow: 440ms;
+
+    --book-sidebar-w: 272px;
+}
+
+:root[data-theme="dark"] {
+    --book-bg: #14171C;
+    --book-bg-soft: #1A1E24;
+    --book-surface: #1B1F26;
+    --book-ink: #E8E6DE;
+    --book-ink-soft: #B7BCC4;
+    --book-ink-faint: #6D7480;
+    --book-border: #2A2F37;
+    --book-primary: #7C9CC4;
+    --book-primary-soft: rgba(124, 156, 196, .14);
+    --book-accent: #C6B392;
+    --book-accent-soft: rgba(198, 179, 146, .14);
+    --book-danger: #D97A7A;
+    --book-shadow: 0 1px 2px rgba(0, 0, 0, .35), 0 10px 26px -10px rgba(0, 0, 0, .55);
+
+    --book-glow-a: rgba(124, 156, 196, .06);
+    --book-glow-b: rgba(198, 179, 146, .06);
+    --book-page-tint: rgba(198, 179, 146, .12);
+    --book-mote-tint: rgba(124, 156, 196, .22);
+}
+
+/* ---------- Reset & base ---------- */
+* { box-sizing: border-box; }
+html { scroll-behavior: smooth; }
+body.book-body {
+    margin: 0;
+    background: var(--book-bg);
+    color: var(--book-ink);
+    font-family: var(--book-font-sans);
+    font-size: var(--book-fs-base);
+    line-height: 1.5;
+    -webkit-font-smoothing: antialiased;
+    transition: background-color var(--book-dur-slow) var(--book-ease-standard), color var(--book-dur-slow) var(--book-ease-standard);
+    animation: book-page-in var(--book-dur-slow) var(--book-ease-emphasized) both;
+}
+@keyframes book-page-in { from { opacity: 0; } to { opacity: 1; } }
+a { color: var(--book-primary); text-decoration: none; }
+.icon { width: 1.1em; height: 1.1em; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; vertical-align: -.15em; }
+.book-container { max-width: 1280px; margin: 0 auto; padding: 0 var(--book-sp-5); }
+
+/* ---------- Ambient background motion ----------
+   Fixed, decorative, non-interactive layer sitting behind every other
+   element on the page (see the z-index note on .book-shell/.book-footer
+   below -- everything a reader can see or touch is explicitly stacked
+   above it). Two soft drifting light washes plus a handful of open-book
+   glyphs and dust motes that rise and settle, all transform/opacity-only
+   so they stay cheap on the compositor. */
+.book-ambient { position: fixed; inset: 0; z-index: 0; overflow: hidden; pointer-events: none; }
+.book-ambient-glow {
+    position: absolute; width: 38vmax; height: 38vmax; border-radius: 50%;
+    filter: blur(50px); opacity: .7; will-change: transform;
+}
+.book-ambient-glow-a { top: -12%; right: -8%; background: radial-gradient(circle, var(--book-glow-a), transparent 72%); animation: book-drift-a 34s var(--book-ease-standard) infinite alternate; }
+.book-ambient-glow-b { bottom: -14%; left: -8%; background: radial-gradient(circle, var(--book-glow-b), transparent 72%); animation: book-drift-b 42s var(--book-ease-standard) infinite alternate; }
+@keyframes book-drift-a { from { transform: translate(0, 0) scale(1); } to { transform: translate(-6%, 8%) scale(1.12); } }
+@keyframes book-drift-b { from { transform: translate(0, 0) scale(1); } to { transform: translate(8%, -6%) scale(1.08); } }
+
+.book-ambient-page { position: absolute; width: 34px; height: 34px; color: var(--book-page-tint); will-change: transform, opacity; }
+.book-ambient-page-1 { top: 18%; left: 8%; animation: book-page-float-1 22s ease-in-out infinite; }
+.book-ambient-page-2 { top: 62%; left: 88%; width: 44px; height: 44px; animation: book-page-float-2 27s ease-in-out infinite; animation-delay: -6s; }
+.book-ambient-page-3 { top: 82%; left: 20%; width: 26px; height: 26px; animation: book-page-float-3 19s ease-in-out infinite; animation-delay: -11s; }
+@keyframes book-page-float-1 {
+    0%, 100% { transform: translateY(0) rotate(-4deg); opacity: .5; }
+    50% { transform: translateY(-38px) rotate(5deg); opacity: 1; }
+}
+@keyframes book-page-float-2 {
+    0%, 100% { transform: translateY(0) rotate(6deg); opacity: .4; }
+    50% { transform: translateY(-52px) rotate(-5deg); opacity: .9; }
+}
+@keyframes book-page-float-3 {
+    0%, 100% { transform: translateY(0) rotate(-3deg); opacity: .5; }
+    50% { transform: translateY(-28px) rotate(4deg); opacity: 1; }
+}
+
+.book-ambient-mote { position: absolute; width: 5px; height: 5px; border-radius: 50%; background: var(--book-mote-tint); will-change: transform, opacity; }
+.book-ambient-mote-1 { top: 30%; left: 30%; animation: book-mote-rise 16s ease-in-out infinite; }
+.book-ambient-mote-2 { top: 70%; left: 60%; width: 4px; height: 4px; animation: book-mote-rise 20s ease-in-out infinite; animation-delay: -4s; }
+.book-ambient-mote-3 { top: 45%; left: 75%; width: 3px; height: 3px; animation: book-mote-rise 14s ease-in-out infinite; animation-delay: -8s; }
+.book-ambient-mote-4 { top: 15%; left: 55%; animation: book-mote-rise 18s ease-in-out infinite; animation-delay: -12s; }
+@keyframes book-mote-rise {
+    0% { transform: translate(0, 0); opacity: 0; }
+    15% { opacity: .8; }
+    85% { opacity: .5; }
+    100% { transform: translate(12px, -90px); opacity: 0; }
+}
+
+/* Everything a reader interacts with sits in its own stacking context
+   above .book-ambient (z-index: 0), regardless of DOM order. */
+.book-progress-rail, .book-header, .book-sidebar-overlay { position: relative; z-index: 10; }
+.book-sidebar-overlay { position: fixed; }
+.book-shell, .book-footer { position: relative; z-index: 1; }
+
+@media (prefers-reduced-motion: reduce) {
+    body.book-body, .book-sidebar, .book-chapter-pages,
+    .book-ambient-glow, .book-ambient-page, .book-ambient-mote,
+    .book-nav-item, .book-chapter, .book-avatar-ring { animation: none !important; transition: none !important; }
+    .book-content > * { opacity: 1 !important; transform: none !important; }
+}
+
+/* ---------- Scroll progress ---------- */
+.book-progress-rail { top: 0; z-index: 60; height: 3px; background: transparent; position: sticky; }
+.book-progress-fill { height: 100%; width: 0%; background: var(--book-accent); transition: width 80ms linear; }
+
+/* ---------- Running head ---------- */
+.book-header { position: sticky; top: 3px; z-index: 50; background: color-mix(in srgb, var(--book-surface) 90%, transparent); backdrop-filter: blur(8px); border-bottom: 1px solid var(--book-border); box-shadow: 0 0 0 rgba(27, 36, 48, 0); transition: box-shadow var(--book-dur-base) var(--book-ease-standard), background-color var(--book-dur-slow) var(--book-ease-standard); }
+.book-header.is-scrolled { box-shadow: var(--book-shadow); }
+.book-header .book-container { display: flex; align-items: center; gap: var(--book-sp-4); height: 58px; }
+.book-menu-toggle { display: none; background: none; border: none; color: var(--book-ink); cursor: pointer; padding: var(--book-sp-2); transition: transform var(--book-dur-fast) var(--book-ease-bounce); }
+.book-menu-toggle:active { transform: scale(.9); }
+.book-brand { display: flex; align-items: center; gap: var(--book-sp-2); font-weight: 600; color: var(--book-ink); flex-shrink: 0; }
+.book-brand-mark { width: 26px; height: 26px; border-radius: 6px; background: var(--book-primary-soft); color: var(--book-primary); display: grid; place-items: center; transition: transform var(--book-dur-base) var(--book-ease-bounce); }
+.book-brand:hover .book-brand-mark { transform: rotate(-8deg) scale(1.08); }
+.book-brand-mark svg { width: 15px; height: 15px; fill: none; stroke: currentColor; stroke-width: 1.7; }
+.book-running-title { font-family: var(--book-font-serif); font-style: italic; color: var(--book-ink-faint); font-size: var(--book-fs-sm); padding-left: var(--book-sp-4); border-left: 1px solid var(--book-border); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; display: none; }
+.book-search { flex: 1; max-width: 340px; position: relative; display: flex; align-items: center; gap: var(--book-sp-2); background: var(--book-bg-soft); border: 1px solid var(--book-border); border-radius: var(--book-radius-md); padding: 0 var(--book-sp-3); height: 36px; margin-left: auto; transition: border-color var(--book-dur-fast) var(--book-ease-standard), box-shadow var(--book-dur-fast) var(--book-ease-standard); }
+.book-search:focus-within { border-color: var(--book-primary); box-shadow: 0 0 0 3px var(--book-primary-soft); }
+.book-search svg { color: var(--book-ink-faint); flex-shrink: 0; }
+.book-search input { flex: 1; border: none; background: none; outline: none; font: inherit; color: var(--book-ink); }
+.book-search-results { position: absolute; top: calc(100% + 8px); left: 0; right: 0; background: var(--book-surface); border: 1px solid var(--book-border); border-radius: var(--book-radius-md); box-shadow: var(--book-shadow); display: none; overflow: hidden; z-index: 70; }
+.book-search-results.visible { display: block; }
+.book-search-results a { display: block; padding: var(--book-sp-3); color: var(--book-ink); border-bottom: 1px solid var(--book-border); font-size: var(--book-fs-sm); }
+.book-search-results a:hover { background: var(--book-primary-soft); }
+.book-header-right { display: flex; align-items: center; gap: var(--book-sp-1); }
+.book-icon-btn { display: grid; place-items: center; width: 36px; height: 36px; border-radius: var(--book-radius-sm); color: var(--book-ink-soft); background: none; border: none; cursor: pointer; transition: background var(--book-dur-fast) var(--book-ease-standard), color var(--book-dur-fast) var(--book-ease-standard), transform var(--book-dur-fast) var(--book-ease-bounce); }
+.book-icon-btn:hover, .book-icon-btn[aria-pressed="true"] { background: var(--book-primary-soft); color: var(--book-primary); }
+.book-icon-btn:hover { transform: translateY(-1px); }
+.book-icon-btn:active { transform: scale(.92); }
+
+/* ---------- Theme switcher ---------- */
+.theme-switcher { position: relative; }
+.theme-switcher .icon-btn { display: grid; place-items: center; width: 36px; height: 36px; border: none; background: none; border-radius: var(--book-radius-sm); color: var(--book-ink-soft); cursor: pointer; transition: background var(--book-dur-fast) var(--book-ease-standard), transform var(--book-dur-fast) var(--book-ease-bounce); }
+.theme-switcher .icon-btn:hover { background: var(--book-primary-soft); color: var(--book-primary); transform: translateY(-1px) rotate(-8deg); }
+.theme-switcher .icon-btn:active { transform: scale(.92); }
+.theme-switcher .icon-sun { display: none; }
+:root[data-theme="dark"] .theme-switcher .icon-moon { display: none; }
+:root[data-theme="dark"] .theme-switcher .icon-sun { display: inline-block; }
+.theme-menu { position: absolute; right: 0; top: calc(100% + 10px); min-width: 160px; background: var(--book-surface); border: 1px solid var(--book-border); border-radius: var(--book-radius-md); box-shadow: var(--book-shadow); padding: var(--book-sp-2); z-index: 80; animation: book-pop-in var(--book-dur-fast) var(--book-ease-emphasized) both; }
+@keyframes book-pop-in { from { opacity: 0; transform: translateY(-4px) scale(.97); } to { opacity: 1; transform: translateY(0) scale(1); } }
+.theme-option { display: flex; align-items: center; gap: var(--book-sp-2); width: 100%; border: none; background: none; padding: var(--book-sp-2); border-radius: var(--book-radius-sm); cursor: pointer; font: inherit; color: var(--book-ink); text-align: left; transition: background var(--book-dur-fast) var(--book-ease-standard); }
+.theme-option:hover, .theme-option:focus-visible { background: var(--book-primary-soft); outline: none; }
+.theme-swatch { width: 15px; height: 15px; border-radius: 50%; background: var(--swatch-bg); border: 2px solid var(--swatch-fg); }
+.theme-check { margin-left: auto; opacity: 0; color: var(--book-primary); }
+.theme-option[aria-checked="true"] .theme-check { opacity: 1; }
+
+/* ---------- Reader avatar ---------- */
+.book-avatar { position: relative; }
+.book-avatar-btn {
+    position: relative; display: grid; place-items: center; width: 36px; height: 36px;
+    border-radius: 50%; border: none; cursor: pointer; color: #fff;
+    background: linear-gradient(140deg, var(--book-primary), var(--book-accent));
+    transition: transform var(--book-dur-base) var(--book-ease-bounce), box-shadow var(--book-dur-base) var(--book-ease-standard);
+}
+.book-avatar-btn .icon { width: 18px; height: 18px; }
+.book-avatar-btn:hover { transform: scale(1.08); box-shadow: 0 4px 14px -4px var(--book-glow-a); }
+.book-avatar-btn:active { transform: scale(.94); }
+.book-avatar-btn[aria-expanded="true"] { box-shadow: 0 0 0 3px var(--book-primary-soft); }
+.book-avatar-ring {
+    position: absolute; inset: -4px; border-radius: 50%; border: 1.5px solid var(--book-accent);
+    opacity: 0; transform: scale(.85); pointer-events: none;
+    transition: opacity var(--book-dur-base) var(--book-ease-standard), transform var(--book-dur-base) var(--book-ease-standard);
+}
+.book-avatar:hover .book-avatar-ring { opacity: .6; transform: scale(1); animation: book-avatar-pulse 1.8s var(--book-ease-standard) infinite; }
+@keyframes book-avatar-pulse {
+    0%, 100% { box-shadow: 0 0 0 0 var(--book-glow-b); }
+    50% { box-shadow: 0 0 0 4px transparent; }
+}
+.book-avatar-tooltip {
+    position: absolute; top: calc(100% + 8px); right: 0; white-space: nowrap;
+    background: var(--book-ink); color: var(--book-bg); font-size: .72rem; font-weight: 600;
+    padding: 5px 9px; border-radius: var(--book-radius-sm);
+    opacity: 0; transform: translateY(-4px); pointer-events: none;
+    transition: opacity var(--book-dur-fast) var(--book-ease-standard), transform var(--book-dur-fast) var(--book-ease-standard);
+    z-index: 75;
+}
+.book-avatar:hover .book-avatar-tooltip { opacity: 1; transform: translateY(0); }
+.book-avatar-popover[hidden] { display: none; }
+.book-avatar-popover {
+    position: absolute; right: 0; top: calc(100% + 10px); width: 240px;
+    background: var(--book-surface); border: 1px solid var(--book-border); border-radius: var(--book-radius-lg);
+    box-shadow: var(--book-shadow); padding: var(--book-sp-4); z-index: 80;
+    animation: book-pop-in var(--book-dur-base) var(--book-ease-emphasized) both;
+}
+.book-avatar-popover-header { display: flex; align-items: center; gap: var(--book-sp-3); margin-bottom: var(--book-sp-4); }
+.book-avatar-popover-icon { width: 34px; height: 34px; border-radius: 50%; background: linear-gradient(140deg, var(--book-primary), var(--book-accent)); color: #fff; display: grid; place-items: center; flex-shrink: 0; }
+.book-avatar-popover-icon svg { width: 17px; height: 17px; }
+.book-avatar-name { margin: 0; font-weight: 700; font-size: var(--book-fs-sm); color: var(--book-ink); }
+.book-avatar-sub { margin: 0; font-size: .72rem; color: var(--book-ink-faint); }
+.book-avatar-stats { display: grid; grid-template-columns: 1fr 1fr; gap: var(--book-sp-2); margin-bottom: var(--book-sp-4); }
+.book-avatar-stat { text-align: center; background: var(--book-bg-soft); border-radius: var(--book-radius-sm); padding: var(--book-sp-2) var(--book-sp-1); }
+.book-avatar-stat span { display: block; font-family: var(--book-font-serif); font-weight: 700; font-size: var(--book-fs-lg); color: var(--book-primary); }
+.book-avatar-stat label { display: block; font-size: .68rem; color: var(--book-ink-faint); text-transform: uppercase; letter-spacing: .04em; margin-top: 2px; }
+.book-avatar-action {
+    width: 100%; border: none; border-radius: var(--book-radius-sm); padding: var(--book-sp-2) var(--book-sp-3);
+    background: var(--book-primary); color: #fff; font: inherit; font-weight: 600; font-size: var(--book-fs-sm);
+    cursor: pointer; transition: filter var(--book-dur-fast) var(--book-ease-standard), transform var(--book-dur-fast) var(--book-ease-bounce);
+}
+.book-avatar-action:hover { filter: brightness(1.1); }
+.book-avatar-action:active { transform: scale(.97); }
+
+/* ---------- Shell / contents rail ---------- */
+.book-shell { display: flex; max-width: 1280px; margin: 0 auto; align-items: flex-start; transition: max-width var(--book-dur-base) var(--book-ease-standard); }
+.book-sidebar-overlay { display: none; position: fixed; inset: 0; background: rgba(20, 23, 28, .5); z-index: 55; opacity: 0; transition: opacity var(--book-dur-base) var(--book-ease-standard); }
+.book-sidebar-overlay.visible { display: block; opacity: 1; }
+.book-sidebar { width: var(--book-sidebar-w); flex-shrink: 0; position: sticky; top: 61px; max-height: calc(100vh - 61px); overflow-y: auto; padding: var(--book-sp-6) var(--book-sp-4) var(--book-sp-7); transition: width var(--book-dur-base) var(--book-ease-emphasized), opacity var(--book-dur-base) var(--book-ease-standard), padding var(--book-dur-base) var(--book-ease-standard); }
+.book-sidebar-header { display: none; justify-content: space-between; align-items: center; font-weight: 700; margin-bottom: var(--book-sp-3); font-family: var(--book-font-serif); }
+.book-sidebar-close { background: none; border: none; color: var(--book-ink); cursor: pointer; }
+.book-nav ul { list-style: none; margin: 0; padding: 0; }
+
+/* Sidebar stagger-in: each top-level item fades/slides in with a small
+   per-item delay driven by --stagger (set inline per <li> from the nav
+   loop index), so the contents rail reads as settling into place rather
+   than appearing all at once. */
+.book-nav-item, .book-chapter {
+    animation: book-stagger-in var(--book-dur-slow) var(--book-ease-emphasized) both;
+    animation-delay: calc(60ms + var(--stagger, 0) * 40ms);
+}
+@keyframes book-stagger-in { from { opacity: 0; transform: translateX(-8px); } to { opacity: 1; transform: translateX(0); } }
+
+.book-nav-link { display: block; padding: var(--book-sp-1) var(--book-sp-3); border-radius: var(--book-radius-sm); color: var(--book-ink-soft); font-size: var(--book-fs-sm); position: relative; transition: color var(--book-dur-fast) var(--book-ease-standard), transform var(--book-dur-fast) var(--book-ease-standard); }
+.book-nav-link::before { content: ""; position: absolute; left: 0; top: 50%; width: 0; height: 1px; background: var(--book-accent); transition: width var(--book-dur-base) var(--book-ease-emphasized); }
+.book-nav-link:hover { color: var(--book-ink); transform: translateX(2px); }
+.book-nav-link:hover::before { width: var(--book-sp-2); }
+.book-nav-link.active { color: var(--book-primary); font-weight: 700; }
+.book-nav-link.active::before { width: var(--book-sp-2); background: var(--book-primary); }
+.book-nav-item-sub { margin-left: var(--book-sp-3); }
+
+.book-chapter { margin: var(--book-sp-4) 0 var(--book-sp-1); }
+.book-chapter-toggle { width: 100%; display: flex; align-items: center; justify-content: space-between; gap: var(--book-sp-2); background: none; border: none; padding: var(--book-sp-1) var(--book-sp-3); border-radius: var(--book-radius-sm); cursor: pointer; font: inherit; transition: background var(--book-dur-fast) var(--book-ease-standard); }
+.book-chapter-toggle:hover { background: var(--book-bg-soft); }
+.book-chapter-label { font-family: var(--book-font-serif); font-style: italic; font-weight: 700; font-size: var(--book-fs-base); color: var(--book-ink); }
+.book-chapter-arrow { transition: transform var(--book-dur-base) var(--book-ease-emphasized); color: var(--book-ink-faint); }
+.book-chapter.expanded .book-chapter-arrow { transform: rotate(90deg); }
+.book-chapter-pages { list-style: none; margin: 0; padding: 0; overflow: hidden; max-height: 0; opacity: 0; transition: max-height var(--book-dur-base) var(--book-ease-emphasized), opacity var(--book-dur-base) var(--book-ease-standard), margin-top var(--book-dur-base) var(--book-ease-standard); }
+.book-chapter.expanded .book-chapter-pages { max-height: 800px; opacity: 1; margin-top: var(--book-sp-1); }
+
+/* ---------- Page ---------- */
+.book-main { flex: 1; min-width: 0; padding: var(--book-sp-6) var(--book-sp-5) var(--book-sp-8); display: flex; justify-content: center; }
+.book-page { width: 100%; max-width: var(--book-measure); animation: book-fade-up var(--book-dur-slow) var(--book-ease-emphasized) both; animation-delay: 60ms; }
+@keyframes book-fade-up { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
+.book-chapter-eyebrow { font-size: var(--book-fs-sm); color: var(--book-ink-faint); text-transform: uppercase; letter-spacing: .08em; margin: 0 0 var(--book-sp-2); }
+.book-title { font-family: var(--book-font-serif); font-size: var(--book-fs-2xl); font-weight: 700; line-height: 1.2; margin: 0 0 var(--book-sp-3); color: var(--book-ink); }
+.book-rule { text-align: center; color: var(--book-accent); font-size: var(--book-fs-lg); margin: 0 0 var(--book-sp-6); opacity: .8; }
+
+/* ---------- Reading content ---------- */
+.book-content { font-family: var(--book-font-serif); font-size: var(--book-fs-base); line-height: var(--book-lh-base); color: var(--book-ink); }
+
+/* Scroll-in reveal: each direct child starts faded/offset and settles
+   into place as it enters the viewport (JS toggles .is-visible via
+   IntersectionObserver). Falls back to fully visible immediately when
+   JS is unavailable/disabled or prefers-reduced-motion is set -- see
+   the <noscript> override in base.html and the reduced-motion block
+   above. */
+.book-content > * { opacity: 0; transform: translateY(16px); transition: opacity var(--book-dur-slow) var(--book-ease-emphasized), transform var(--book-dur-slow) var(--book-ease-emphasized); }
+.book-content > *.is-visible { opacity: 1; transform: translateY(0); }
+
+.book-content > p:first-of-type::first-letter {
+    font-size: 3.4em; float: left; line-height: .82; padding: .06em .08em 0 0;
+    font-weight: 700; color: var(--book-primary); font-family: var(--book-font-serif);
+}
+.book-content h1 { font-size: var(--book-fs-xl); margin: var(--book-sp-7) 0 var(--book-sp-3); font-weight: 700; }
+.book-content h2 { font-size: 1.4rem; margin: var(--book-sp-7) 0 var(--book-sp-3); font-weight: 700; padding-bottom: var(--book-sp-2); border-bottom: 1px solid var(--book-border); }
+.book-content h3 { font-size: var(--book-fs-lg); margin: var(--book-sp-6) 0 var(--book-sp-2); font-style: italic; color: var(--book-primary); }
+.book-content p { margin: 0 0 var(--book-sp-5); }
+.book-content a { border-bottom: 1px solid var(--book-primary-soft); transition: border-color var(--book-dur-fast) var(--book-ease-standard); }
+.book-content a:hover { border-color: var(--book-primary); }
+.book-content ul, .book-content ol { margin: 0 0 var(--book-sp-5); padding-left: 1.4em; }
+.book-content li { margin-bottom: var(--book-sp-2); }
+.book-content blockquote { margin: 0 0 var(--book-sp-5); padding: var(--book-sp-1) 0 var(--book-sp-1) var(--book-sp-5); border-left: 3px solid var(--book-accent); font-style: italic; color: var(--book-ink-soft); }
+.book-content img { max-width: 100%; border-radius: var(--book-radius-md); border: 1px solid var(--book-border); }
+.book-content table { width: 100%; border-collapse: collapse; margin: 0 0 var(--book-sp-5); font-family: var(--book-font-sans); font-size: var(--book-fs-sm); display: block; overflow-x: auto; }
+.book-content th, .book-content td { padding: var(--book-sp-2) var(--book-sp-3); border-bottom: 1px solid var(--book-border); text-align: left; }
+.book-content th { color: var(--book-primary); font-weight: 700; }
+.book-content code { font-family: var(--book-font-mono); font-size: .82em; background: var(--book-bg-soft); color: var(--book-primary); padding: .15em .4em; border-radius: 4px; }
+.book-content .codehilite { position: relative; margin: 0 0 var(--book-sp-5); border-radius: var(--book-radius-md); overflow: hidden; border: 1px solid var(--book-border); }
+.book-content .codehilite pre { margin: 0; padding: var(--book-sp-4); overflow-x: auto; background: var(--book-bg-soft); font-family: var(--book-font-mono); }
+.book-content .codehilite code { background: none; padding: 0; color: var(--book-ink); }
+.copy-code-btn { position: absolute; top: var(--book-sp-2); right: var(--book-sp-2); font-family: var(--book-font-sans); font-size: .75rem; background: var(--book-surface); border: 1px solid var(--book-border); border-radius: var(--book-radius-sm); padding: 4px 8px; color: var(--book-ink-soft); cursor: pointer; opacity: 0; transition: opacity var(--book-dur-fast) var(--book-ease-standard), transform var(--book-dur-fast) var(--book-ease-bounce); }
+.book-content .codehilite:hover .copy-code-btn { opacity: 1; }
+.copy-code-btn:active { transform: scale(.92); }
+.codehilite .k, .codehilite .kn, .codehilite .kd, .codehilite .kc, .codehilite .kr { color: #7A4B8C; font-weight: 600; }
+.codehilite .s, .codehilite .s1, .codehilite .s2, .codehilite .sb, .codehilite .sc, .codehilite .sd { color: #3F7A5C; }
+.codehilite .c, .codehilite .c1, .codehilite .cm, .codehilite .cs { color: var(--book-ink-faint); font-style: italic; }
+.codehilite .nf, .codehilite .fm { color: var(--book-primary); }
+.codehilite .nc { color: var(--book-accent); font-weight: 600; }
+.codehilite .nb, .codehilite .bp { color: var(--book-primary); }
+.codehilite .o, .codehilite .ow { color: var(--book-accent); }
+.codehilite .mi, .codehilite .mf, .codehilite .m { color: #7A4B8C; }
+.codehilite .err { color: var(--book-danger); }
+
+/* ---------- Page-turn navigation ---------- */
+.book-page-turn { display: grid; grid-template-columns: 1fr 1fr; gap: var(--book-sp-4); margin-top: var(--book-sp-7); padding-top: var(--book-sp-5); border-top: 1px solid var(--book-border); font-family: var(--book-font-sans); }
+.book-page-btn { display: flex; align-items: center; gap: var(--book-sp-3); padding: var(--book-sp-4); border-radius: var(--book-radius-md); transition: transform var(--book-dur-base) var(--book-ease-emphasized), box-shadow var(--book-dur-base) var(--book-ease-standard), background var(--book-dur-base) var(--book-ease-standard); }
+.book-page-btn:hover { transform: translateY(-2px); box-shadow: var(--book-shadow); background: var(--book-surface); }
+.book-page-btn:active { transform: translateY(0) scale(.98); }
+.book-page-next { grid-column: 2; justify-content: flex-end; text-align: right; }
+.book-page-corner { font-size: 1.4rem; color: var(--book-accent); transition: transform var(--book-dur-base) var(--book-ease-emphasized); }
+.book-page-prev:hover .book-page-corner { transform: translateX(-3px); }
+.book-page-next:hover .book-page-corner { transform: translateX(3px); }
+.book-page-label { display: block; font-size: .72rem; text-transform: uppercase; letter-spacing: .08em; color: var(--book-ink-faint); }
+.book-page-title { display: block; font-family: var(--book-font-serif); font-weight: 700; color: var(--book-ink); }
+
+/* ---------- Footer ---------- */
+.book-footer { border-top: 1px solid var(--book-border); padding: var(--book-sp-6) 0; margin-top: var(--book-sp-7); }
+.book-footer-copy { margin: 0; font-size: var(--book-fs-sm); color: var(--book-ink-faint); text-align: center; }
+.book-footer-copy a { color: var(--book-ink-soft); }
+
+/* ---------- Focused reading mode ---------- */
+body.book-focus .book-sidebar { width: 0; padding-left: 0; padding-right: 0; opacity: 0; overflow: hidden; }
+body.book-focus .book-running-title { display: inline; }
+body.book-focus .book-main { padding-top: var(--book-sp-8); }
+
+/* ---------- Cross-page motion (native View Transitions) ----------
+   Progressive enhancement: in browsers that support the CSS View
+   Transitions API (no third-party router or animation library involved),
+   navigating between pages cross-fades and settles instead of hard-
+   cutting. Every other browser just does a normal navigation -- there is
+   no fallback to write, because there's nothing to polyfill against. */
+@media (prefers-reduced-motion: no-preference) {
+    @view-transition { navigation: auto; }
+    @keyframes book-vt-in { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
+    @keyframes book-vt-out { from { opacity: 1; transform: translateY(0); } to { opacity: 0; transform: translateY(-8px); } }
+    ::view-transition-old(root) { animation: book-vt-out var(--book-dur-base) var(--book-ease-standard) both; }
+    ::view-transition-new(root) { animation: book-vt-in var(--book-dur-slow) var(--book-ease-emphasized) both; }
+}
+
+/* ---------- Responsive ---------- */
+@media (max-width: 980px) {
+    .book-search { display: none; }
+    .book-menu-toggle { display: grid; place-items: center; }
+    .book-sidebar-header { display: flex; }
+    .book-sidebar {
+        position: fixed; top: 0; left: 0; height: 100vh; max-height: none;
+        background: var(--book-surface); z-index: 56; width: 280px;
+        transform: translateX(-105%);
+        transition: transform var(--book-dur-base) var(--book-ease-emphasized);
+        box-shadow: var(--book-shadow);
+    }
+    .book-sidebar.open { transform: translateX(0); }
+    .book-page-turn { grid-template-columns: 1fr; }
+    .book-page-next { grid-column: 1; justify-content: flex-start; text-align: left; }
+}
+
+@media (max-width: 480px) {
+    .book-container { padding: 0 var(--book-sp-3); }
+    .book-header .book-container { gap: var(--book-sp-2); }
+    .book-brand-name { display: none; }
+    .book-avatar-popover { right: -8px; width: 220px; }
+}
