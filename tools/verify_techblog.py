#!/usr/bin/env python3
"""Verify the generated Tech Blog page loads CSS and keeps inline icons bounded."""

from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:8000/styles/techblog"


def main() -> None:
    output = Path("screenshots")
    output.mkdir(exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
        page.goto(f"{BASE_URL}/index.html", wait_until="networkidle")
        page.locator("link[href*='techblog.css']").wait_for(state="attached")
        page.locator(".mag-header").wait_for(state="visible")
        page.screenshot(path=str(output / "techblog-mobile-fixed.png"), full_page=True)

        icons = page.locator(".mag-header .icon, .mag-sidebar .icon")
        visible_icons = 0
        for index in range(icons.count()):
            box = icons.nth(index).bounding_box()
            if box is None:
                continue
            visible_icons += 1
            if box["width"] > 40 or box["height"] > 40:
                raise AssertionError(f"Tech Blog icon {index} is not bounded: {box}")

        css_href = page.locator("link[href*='techblog.css']").get_attribute("href")
        if not css_href or not css_href.endswith("techblog.css"):
            raise AssertionError(f"Unexpected Tech Blog CSS href: {css_href}")

        print(f"Tech Blog verified: {visible_icons} visible icons bounded; stylesheet loaded from {css_href}")
        print(f"Screenshot saved to {output / 'techblog-mobile-fixed.png'}")
        browser.close()


if __name__ == "__main__":
    main()
