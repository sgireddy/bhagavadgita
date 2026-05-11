# 🕉️ Bhagavad Gītā Trilingual Study Sheets

Color-coded study sheets with full text in **Devanāgarī**, **Telugu**, **IAST**, and **English**, plus word-by-word breakdown tables.

## 📁 Structure

```
.
├── shared/
│   └── gita_style.css                # Shared theme used by all sheets
│
├── part1_karma/                      # Chapters 1–6: Action & the Self
│   ├── part1_overview.html
│   ├── ch01_arjuna_visada.html
│   ├── ch02_sankhya.html
│   ├── ch03_karma.html
│   ├── ch04_jnana_karma_sannyasa.html
│   ├── ch05_karma_sannyasa.html
│   └── ch06_dhyana.html
│
├── part2_bhakti/                     # Chapters 7–12: The Divine & Devotion
│   ├── part2_overview.html
│   ├── ch07_jnana_vijnana.html
│   ├── ch08_akshara_brahma.html
│   ├── ch09_raja_vidya.html
│   ├── ch10_vibhuti.html
│   ├── ch11_vishva_rupa.html
│   └── ch12_bhakti.html
│
├── part3_jnana/                      # Chapters 13–18: Knowledge & Synthesis
│   ├── part3_overview.html
│   ├── ch13_kshetra_kshetrajna.html
│   ├── ch14_guna_traya.html
│   ├── ch15_purushottama.html
│   ├── ch16_daivasura.html
│   ├── ch17_shraddha_traya.html
│   └── ch18_moksha_sannyasa.html
│
└── (existing detailed sheets — kept at top level)
    ├── yada_yada.html                # BG 4.7–4.8
    ├── karmanye_vadhikaraste.html    # BG 2.47–2.48
    └── sthita_prajna.html            # BG 2.54–2.72
```

## 🎨 Color scheme

| Element | Color |
|---|---|
| **देवनागरी** Devanagari | 🔴 deep red |
| **తెలుగు** Telugu | 🟢 forest green |
| *IAST Sanskrit* | 🔵 royal blue, italic |
| Pronunciation guide | 🟢 teal |
| English meaning | 🟣 purple |

## 📦 Fully self-contained (no internet needed)

All fonts (Noto Sans Devanagari, Noto Sans Telugu, Noto Serif) are **bundled locally** in `shared/fonts/`. The HTML files reference them via `@font-face` rules in `shared/gita_style.css`, so the entire repo renders correctly offline — including PDF generation from a fresh clone with no network access.

If you ever need to refresh the fonts (e.g., after a Google Fonts update), run:
```bash
python3 shared/fonts/download.py
```

## 🖨️ Generating PDFs

All HTML files are A4-page-sized and print-friendly. PDFs are generated via headless Chromium:

```bash
# 1. Serve the directory locally (so relative font URLs resolve):
python3 -m http.server 8011 &

# 2. Render any sheet to PDF:
chromium --headless --no-sandbox --print-to-pdf=output.pdf \
  http://localhost:8011/path/file.html
```

Or, simply open any `.html` file in a browser and use **File → Print → Save as PDF**.
