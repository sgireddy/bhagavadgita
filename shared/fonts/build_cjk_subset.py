"""Build a tiny Noto Sans SC subset containing only the CJK characters used
in the reflections (currently the Lao Tzu Tao Te Ching ch. 8 quote).

Strategy:
1. Download Noto Sans SC Regular full TTF from the Google Fonts public CDN
   (one-time; the output woff2 is then committed to the repo so users
   never need to fetch it again).
2. Subset it down to only the codepoints we actually use.
3. Save as ``noto-cjk-sc-subset.woff2``.

Result: a few-KB font file that resolves the tofu boxes for Chinese text
in offline PDF generation, while keeping the repo size negligible.
"""
from __future__ import annotations

import io
import pathlib
import urllib.request

HERE = pathlib.Path(__file__).parent
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

# Every Chinese character that appears anywhere in our reflections.
# Currently just the Tao Te Ching ch. 8 opening line plus its pinyin tone marks.
# Add more characters here if future essays cite more Chinese sources.
NEEDED_CHARS = "上善若水。水善利萬物而不爭"
# Also include any other CJK punctuation we might use:
NEEDED_CHARS += "，。、；：「」『』《》〈〉？！"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req) as resp:
        return resp.read()


def main() -> None:
    # Step 1: get the full Noto Sans SC Regular TTF (this is the variable
    # font from the official Google Fonts repository on GitHub).
    src_url = (
        "https://raw.githubusercontent.com/notofonts/noto-cjk/main/"
        "Sans/OTF/SimplifiedChinese/NotoSansCJKsc-Regular.otf"
    )
    print(f"Fetching {src_url} ...")
    src_bytes = fetch(src_url)
    print(f"  downloaded {len(src_bytes):,} bytes")

    # Step 2: subset down to just the codepoints we need.
    from fontTools.ttLib import TTFont
    from fontTools.subset import Subsetter, Options

    font = TTFont(io.BytesIO(src_bytes))

    opts = Options()
    opts.flavor = "woff2"
    opts.with_zopfli = True
    opts.desubroutinize = True   # smaller CFF
    opts.layout_features = []    # drop OpenType layout features we don't need
    opts.name_IDs = ["*"]
    opts.notdef_outline = True   # keep .notdef so the engine has something
    opts.recalc_bounds = True
    opts.recalc_timestamp = False
    opts.drop_tables += ["FFTM", "DSIG", "vhea", "vmtx"]

    subs = Subsetter(options=opts)

    unicodes = set(ord(c) for c in NEEDED_CHARS)
    print(f"Subsetting to {len(unicodes)} unique codepoints: {sorted(unicodes)}")
    subs.populate(unicodes=unicodes)
    subs.subset(font)

    # Step 3: flavor as woff2 and save.
    out_path = HERE / "noto-cjk-sc-subset.woff2"
    font.flavor = "woff2"
    font.save(out_path)
    out_size = out_path.stat().st_size
    print(f"✓ wrote {out_path.name} ({out_size:,} bytes)")


if __name__ == "__main__":
    main()
