#!/usr/bin/env python3
"""Capture responsive screenshots and verify the live Styles switcher.

Usage:
    python tools/capture_screenshots.py --base-url http://127.0.0.1:8000

Start a local server first, for example:
    python -m http.server 8000 --directory site
"""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright


THEMES = ["default", "book", "education", "techblog", "agency", "medicine", "apiplay"]
PAGES = ["index.html", "getting-started/index.html", "docs/index.html"]


def safe_name(value: str) -> str:
    return value.strip("/").replace("/", "-") or "home"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    parser.add_argument("--output", default="screenshots")
    args = parser.parse_args()

    base_url = args.base_url.rstrip("/")
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        desktop = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        mobile = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)

        checked_pages = 0
        for page in PAGES:
            url = f"{base_url}/{page}"
            desktop.goto(url, wait_until="networkidle")
            desktop.locator("#style-switcher").wait_for(state="visible")
            desktop.screenshot(path=str(output_dir / f"desktop-{safe_name(page)}.png"), full_page=True)

            desktop.locator("#style-switcher-toggle").click()
            options = desktop.locator("#style-switcher-menu .style-option")
            if options.count() != len(THEMES):
                raise AssertionError(f"Expected {len(THEMES)} style options on {url}, found {options.count()}")
            desktop.screenshot(path=str(output_dir / f"desktop-{safe_name(page)}-menu.png"), full_page=True)
            desktop.locator("#style-switcher-toggle").click()
            checked_pages += 1

        mobile.goto(f"{base_url}/getting-started/index.html", wait_until="networkidle")
        mobile.locator("#style-switcher").wait_for(state="visible")
        mobile.screenshot(path=str(output_dir / "mobile-getting-started.png"), full_page=True)
        mobile.locator("#style-switcher-toggle").click()
        if mobile.locator("#style-switcher-menu .style-option").count() != len(THEMES):
            raise AssertionError("Mobile style switcher does not show all theme options")
        mobile.screenshot(path=str(output_dir / "mobile-getting-started-menu.png"), full_page=True)

        mobile.locator('[data-style="medicine"]').click()
        expected_path = "/styles/medicine/getting-started/index.html"
        actual_path = urlparse(mobile.url).path
        if actual_path != expected_path:
            raise AssertionError(f"Style switch navigation changed page: expected {expected_path}, got {actual_path}")

        browser.close()

    print(f"Verified the Styles switcher on {checked_pages} desktop pages and one mobile page.")
    print(f"Screenshots saved to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
