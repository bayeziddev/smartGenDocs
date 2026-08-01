"""
link_auditor.py
SmartGen Docs -- Link Audit Engine

Crawls the built static site (site/ by default) and reports:
  - internal links pointing to files that do not exist in the build
  - external links that return an error status or fail to connect

Zero third-party dependencies beyond PyYAML (already a core SmartGen Docs
dependency) -- everything else is Python standard library, consistent with
the rest of the project.
"""

from __future__ import annotations

import concurrent.futures
import fnmatch
import html.parser
import json
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional

import yaml

DEFAULT_CONFIG = {
    "site_dir": "site",
    "fail_on": "internal",       # internal | external | both | none
    "concurrency": 10,
    "timeout": 5,
    "retries": 1,
    "ignore": [],
    "cache_file": ".smartgen-cache/link-status.json",
    "report": {
        "json": None,             # defaults to <site_dir>/audit-report.json
        "html": None,             # defaults to <site_dir>/audit-report.html
    },
}


@dataclass
class LinkResult:
    source_page: str
    url: str
    link_type: str          # "internal" | "external"
    status: str              # "ok" | "broken" | "skipped"
    status_code: Optional[int] = None
    error: Optional[str] = None


class _LinkExtractor(html.parser.HTMLParser):
    """Pulls href/src attributes out of a rendered page, no BeautifulSoup needed."""

    TAG_ATTR = {"a": "href", "img": "src", "link": "href", "script": "src"}

    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs) -> None:
        attr_name = self.TAG_ATTR.get(tag)
        if not attr_name:
            return
        for name, value in attrs:
            if name == attr_name and value:
                self.links.append(value)


def _deep_merge(base: dict, override: dict) -> None:
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            _deep_merge(base[key], value)
        else:
            base[key] = value


def load_config(project_root: Path) -> dict:
    """
    Config resolution order (first match wins):
      1. ./smartgen-audit.yml             -- standalone file, no other setup needed
      2. the `audit:` block in smartgen.yml -- for teams that keep one config file
      3. DEFAULT_CONFIG
    """
    config = json.loads(json.dumps(DEFAULT_CONFIG))  # deep copy

    standalone = project_root / "smartgen-audit.yml"
    main_config = project_root / "smartgen.yml"

    loaded = None
    if standalone.exists():
        with open(standalone, "r", encoding="utf-8") as f:
            raw = yaml.safe_load(f) or {}
        loaded = raw.get("audit", raw)  # allow top-level keys or an `audit:` wrapper
    elif main_config.exists():
        with open(main_config, "r", encoding="utf-8") as f:
            full = yaml.safe_load(f) or {}
        loaded = full.get("audit")

    if loaded:
        _deep_merge(config, loaded)

    return config


def _is_external(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://")


def _should_ignore(url: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(url, pattern) for pattern in patterns)


def crawl_site(site_dir: Path) -> list[tuple[Path, str]]:
    """Returns (source_html_file, raw_href) pairs for every link in the build."""
    found: list[tuple[Path, str]] = []
    for html_file in site_dir.rglob("*.html"):
        text = html_file.read_text(encoding="utf-8", errors="ignore")
        parser = _LinkExtractor()
        parser.feed(text)
        for link in parser.links:
            if link.startswith(("#", "mailto:", "tel:", "javascript:")):
                continue
            found.append((html_file, link))
    return found


def check_internal(source_file: Path, url: str, site_dir: Path) -> LinkResult:
    clean_url = url.split("#")[0].split("?")[0]
    if not clean_url:
        return LinkResult(str(source_file), url, "internal", "ok")

    if clean_url.startswith("/"):
        target = site_dir / clean_url.lstrip("/")
    else:
        target = (source_file.parent / clean_url).resolve()

    if target.is_dir():
        target = target / "index.html"

    if target.exists():
        return LinkResult(str(source_file), url, "internal", "ok")
    return LinkResult(
        str(source_file), url, "internal", "broken",
        error="File not found in build output",
    )


def check_external(
    source_file: Path, url: str, timeout: int, retries: int, cache: dict
) -> LinkResult:
    if url in cache:
        cached = cache[url]
        return LinkResult(
            str(source_file), url, "external",
            cached["status"], cached.get("status_code"), cached.get("error"),
        )

    last_error = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(
                url, method="HEAD",
                headers={"User-Agent": "SmartGenDocs-LinkAuditor/1.0"},
            )
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                code = resp.getcode()
                status = "ok" if code < 400 else "broken"
                cache[url] = {"status": status, "status_code": code}
                return LinkResult(str(source_file), url, "external", status, code)
        except urllib.error.HTTPError as e:
            if attempt == retries:
                code = e.code
                status = "ok" if code < 400 else "broken"
                cache[url] = {"status": status, "status_code": code}
                return LinkResult(str(source_file), url, "external", status, code)
        except Exception as e:  # noqa: BLE001 -- network layer, deliberately broad
            last_error = str(e)
            time.sleep(0.5)

    cache[url] = {"status": "broken", "error": last_error}
    return LinkResult(str(source_file), url, "external", "broken", error=last_error)


def write_reports(report: dict, config: dict, site_dir: Path) -> None:
    json_path = Path(config["report"]["json"] or site_dir / "audit-report.json")
    html_path = Path(config["report"]["html"] or site_dir / "audit-report.html")

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    broken = [r for r in report["results"] if r["status"] == "broken"]
    rows = "\n".join(
        f"<tr><td>{r['source_page']}</td><td>{r['url']}</td>"
        f"<td>{r['link_type']}</td><td>{r.get('status_code') or r.get('error') or ''}</td></tr>"
        for r in broken
    )
    html_doc = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>SmartGen Docs -- link audit report</title>
<style>
body{{font-family:sans-serif;max-width:960px;margin:40px auto;padding:0 20px;color:#1C1B29}}
table{{width:100%;border-collapse:collapse;font-size:14px}}
th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid #E4E2DA}}
th{{background:#EEECFC}}
.summary{{margin-bottom:24px;font-size:15px}}
</style></head><body>
<h1>Link audit report</h1>
<div class="summary">Checked {report['total_links_checked']} links --
{report['broken_internal']} broken internal, {report['broken_external']} broken external</div>
<table><tr><th>Source page</th><th>URL</th><th>Type</th><th>Status</th></tr>{rows}</table>
</body></html>"""
    html_path.write_text(html_doc, encoding="utf-8")


def print_summary(report: dict) -> None:
    print(f"\nLink audit: checked {report['total_links_checked']} links")
    print(f"  broken internal: {report['broken_internal']}")
    print(f"  broken external: {report['broken_external']}")
    if report["broken_internal"] or report["broken_external"]:
        print("\nBroken links:")
        for r in report["results"]:
            if r["status"] == "broken":
                print(
                    f"  [{r['link_type']}] {r['source_page']} -> {r['url']} "
                    f"({r.get('status_code') or r.get('error')})"
                )


def run_audit(project_root: str = ".") -> dict:
    root = Path(project_root).resolve()
    config = load_config(root)
    site_dir = root / config["site_dir"]

    if not site_dir.exists():
        print(
            f"error: build output not found at {site_dir} -- run `smartgen-docs build` first",
            file=sys.stderr,
        )
        sys.exit(1)

    cache_path = root / config["cache_file"]
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}

    raw_links = crawl_site(site_dir)
    results: list[LinkResult] = []
    internal_jobs: list[tuple[Path, str]] = []
    external_jobs: list[tuple[Path, str]] = []

    for source_file, url in raw_links:
        if _should_ignore(url, config["ignore"]):
            link_type = "external" if _is_external(url) else "internal"
            results.append(LinkResult(str(source_file), url, link_type, "skipped"))
            continue
        (external_jobs if _is_external(url) else internal_jobs).append((source_file, url))

    for source_file, url in internal_jobs:
        results.append(check_internal(source_file, url, site_dir))

    with concurrent.futures.ThreadPoolExecutor(max_workers=config["concurrency"]) as pool:
        futures = [
            pool.submit(check_external, source_file, url, config["timeout"], config["retries"], cache)
            for source_file, url in external_jobs
        ]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    cache_path.write_text(json.dumps(cache, indent=2), encoding="utf-8")

    broken_internal = [r for r in results if r.link_type == "internal" and r.status == "broken"]
    broken_external = [r for r in results if r.link_type == "external" and r.status == "broken"]

    report = {
        "total_links_checked": len(results),
        "broken_internal": len(broken_internal),
        "broken_external": len(broken_external),
        "results": [asdict(r) for r in results],
    }

    write_reports(report, config, site_dir)
    print_summary(report)

    fail_on = config["fail_on"]
    should_fail = (
        (fail_on == "internal" and broken_internal)
        or (fail_on == "external" and broken_external)
        or (fail_on == "both" and (broken_internal or broken_external))
    )
    if should_fail:
        sys.exit(1)

    return report