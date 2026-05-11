"""Download the only-script-needed Noto font files locally.

Strategy:
- We only need the script range that contains the actual Unicode codepoints we use.
  - Devanagari range  (U+0900-097F) for Devanagari font
  - Telugu range      (U+0C00-0C7F) for Telugu font
  - Latin range       (U+0000-00FF) for Noto Serif (Roman / IAST)
- For each font, fetch the matching @font-face block from the Google Fonts CSS
  (using a real browser User-Agent so we get woff2 URLs) and download just
  those .woff2 files.
"""
from __future__ import annotations

import pathlib
import re
import urllib.request

HERE = pathlib.Path(__file__).parent
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

CSS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Noto+Sans+Devanagari:wght@500;700"
    "&family=Noto+Sans+Telugu:wght@500;700"
    "&family=Noto+Serif:ital,wght@0,400;0,700;1,400"
    "&display=swap"
)

# Map (font_family_name, weight, italic, script_marker) -> output filename
WANT = {
    ("Noto Sans Devanagari", 500, False, "devanagari"): "noto-devanagari-500.woff2",
    ("Noto Sans Devanagari", 700, False, "devanagari"): "noto-devanagari-700.woff2",
    ("Noto Sans Telugu",     500, False, "telugu"):     "noto-telugu-500.woff2",
    ("Noto Sans Telugu",     700, False, "telugu"):     "noto-telugu-700.woff2",
    ("Noto Serif",           400, False, "latin"):      "noto-serif-400.woff2",
    ("Noto Serif",           700, False, "latin"):      "noto-serif-700.woff2",
    ("Noto Serif",           400, True,  "latin"):      "noto-serif-400-italic.woff2",
}


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req) as resp:
        return resp.read()


def main() -> None:
    css_text = fetch(CSS_URL).decode()
    # Split into @font-face blocks, each prefixed with /* <script> */ comment.
    blocks = re.split(r"/\*\s*([\w-]+)\s*\*/\s*", css_text)
    # blocks[0] is preamble; then [script, ff-block, script, ff-block, ...]
    pairs = list(zip(blocks[1::2], blocks[2::2]))

    found: dict[tuple, str] = {}
    for script, block in pairs:
        m_family = re.search(r"font-family:\s*'([^']+)'", block)
        m_weight = re.search(r"font-weight:\s*(\d+)", block)
        m_style  = re.search(r"font-style:\s*(\w+)", block)
        m_url    = re.search(r"url\(([^)]+\.woff2)\)", block)
        if not (m_family and m_weight and m_style and m_url):
            continue
        key = (m_family.group(1), int(m_weight.group(1)), m_style.group(1) == "italic", script)
        if key in WANT and key not in found:
            found[key] = m_url.group(1)

    missing = set(WANT) - set(found)
    if missing:
        print(f"⚠️  Could not find URLs for: {missing}")

    for key, url in found.items():
        out = HERE / WANT[key]
        print(f"→ {out.name}   ({key[0]} {key[1]}{'/italic' if key[2] else ''} / {key[3]})")
        data = fetch(url)
        out.write_bytes(data)
        print(f"   {len(data):,} bytes")


if __name__ == "__main__":
    main()
