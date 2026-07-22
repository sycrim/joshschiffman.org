#!/usr/bin/env python3
"""Generate staging/vita.pdf by printing staging/vita.html to PDF.

Usage: python3 build_vita.py && python3 build_vita_pdf.py
Requires: pip install playwright && playwright install chromium
"""
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
HTML = ROOT / "staging" / "vita.html"
OUT = ROOT / "staging" / "vita.pdf"

# Set PLAYWRIGHT_CHROMIUM_PATH to point at a specific Chromium binary
# (e.g. a pre-installed one) instead of the one `playwright install` downloads.
CHROMIUM_PATH = os.environ.get("PLAYWRIGHT_CHROMIUM_PATH")


def main():
    if not HTML.exists():
        sys.exit("staging/vita.html not found - run build_vita.py first")

    with sync_playwright() as p:
        launch_args = {"executable_path": CHROMIUM_PATH} if CHROMIUM_PATH else {}
        browser = p.chromium.launch(**launch_args)
        page = browser.new_page()
        page.goto(HTML.resolve().as_uri())
        page.emulate_media(media="print")
        page.pdf(
            path=str(OUT),
            format="Letter",
            print_background=True,
            margin={"top": "0.6in", "bottom": "0.6in", "left": "0.6in", "right": "0.6in"},
        )
        browser.close()
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
