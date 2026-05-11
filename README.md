# 🕉️ Bhagavad Gītā — Trilingual Study Sheets

A complete set of color-coded study sheets for the **entire Bhagavad Gītā**, with text in **Devanāgarī**, **Telugu**, **IAST**, and **English**, plus word-by-word breakdown tables for the most-quoted verse(s) of every chapter.

**Fully self-contained** — fonts are bundled locally, so everything renders correctly offline (HTML and PDF) from any clone.

## 📚 What's included

### Detailed verse-by-verse sheets
| File | Passage | Theme |
|---|---|---|
| [`yada_yada.html`](yada_yada.html) | BG 4.7–4.8 | The principle of *avatāra* — divine descent |
| [`karmanye_vadhikaraste.html`](karmanye_vadhikaraste.html) | BG 2.47–2.48 | The foundation of *Karma-Yoga* (*samatvaṁ yoga ucyate*) |
| [`sthita_prajna.html`](sthita_prajna.html) | BG 2.54–2.72 (19 verses) | The portrait of the person of steady wisdom — *brahma-nirvāṇa* |

### Per-chapter mini-sheets (with essential verses + word-by-word)

**📕 [Part I — Karma-kāṇḍa](part1_karma/)** &nbsp;·&nbsp; Action & the Self (Ch 1–6)
- [Overview (Ch 1–6)](part1_karma/part1_overview.html)
- [Ch 1 — Arjuna-Viṣāda Yoga](part1_karma/ch01_arjuna_visada.html)
- [Ch 2 — Sāṅkhya Yoga](part1_karma/ch02_sankhya.html)
- [Ch 3 — Karma Yoga](part1_karma/ch03_karma.html)
- [Ch 4 — Jñāna-Karma-Sannyāsa Yoga](part1_karma/ch04_jnana_karma_sannyasa.html)
- [Ch 5 — Karma-Sannyāsa Yoga](part1_karma/ch05_karma_sannyasa.html)
- [Ch 6 — Dhyāna Yoga](part1_karma/ch06_dhyana.html)

**📘 [Part II — Bhakti-kāṇḍa](part2_bhakti/)** &nbsp;·&nbsp; The Divine & Devotion (Ch 7–12)
- [Overview (Ch 7–12)](part2_bhakti/part2_overview.html)
- [Ch 7 — Jñāna-Vijñāna Yoga](part2_bhakti/ch07_jnana_vijnana.html)
- [Ch 8 — Akṣara-Brahma Yoga](part2_bhakti/ch08_akshara_brahma.html)
- [Ch 9 — Rāja-Vidyā Rāja-Guhya Yoga](part2_bhakti/ch09_raja_vidya.html)
- [Ch 10 — Vibhūti Yoga](part2_bhakti/ch10_vibhuti.html)
- [Ch 11 — Viśva-Rūpa-Darśana Yoga](part2_bhakti/ch11_vishva_rupa.html)
- [Ch 12 — Bhakti Yoga](part2_bhakti/ch12_bhakti.html)

**📙 [Part III — Jñāna-kāṇḍa](part3_jnana/)** &nbsp;·&nbsp; Knowledge & Synthesis (Ch 13–18)
- [Overview (Ch 13–18)](part3_jnana/part3_overview.html)
- [Ch 13 — Kṣetra-Kṣetrajña Yoga](part3_jnana/ch13_kshetra_kshetrajna.html)
- [Ch 14 — Guṇa-Traya Yoga](part3_jnana/ch14_guna_traya.html)
- [Ch 15 — Puruṣottama Yoga](part3_jnana/ch15_purushottama.html)
- [Ch 16 — Daivāsura-Sampad Yoga](part3_jnana/ch16_daivasura.html)
- [Ch 17 — Śraddhā-Traya Yoga](part3_jnana/ch17_shraddha_traya.html)
- [Ch 18 — Mokṣa-Sannyāsa Yoga](part3_jnana/ch18_moksha_sannyasa.html) ⭐ (the grand finale — includes BG 18.66, the *charama-śloka*)

Every HTML file has a matching `.pdf` next to it (generated via headless Chromium).

## 🎨 Color scheme

| Element | Color |
|---|---|
| **देवनागरी** Devanāgarī | 🔴 deep red |
| **తెలుగు** Telugu | 🟢 forest green |
| *IAST Sanskrit* | 🔵 royal blue, italic |
| Pronunciation guide | 🟢 teal |
| English meaning | 🟣 purple |

## 📁 Repository layout

```
.
├── shared/
│   ├── gita_style.css          # Single source of truth for the theme
│   ├── generate_pdfs.sh        # Script to regenerate all 21 mini-sheet PDFs
│   └── fonts/                  # Self-hosted Noto woff2 files (~580 KB total)
│       ├── noto-devanagari-{500,700}.woff2
│       ├── noto-telugu-{500,700}.woff2
│       ├── noto-serif-{400,700}.woff2
│       ├── noto-serif-400-italic.woff2
│       └── download.py         # Refresh script (re-fetches from Google Fonts)
│
├── part1_karma/                # 6 chapters + overview (HTML + PDF each)
├── part2_bhakti/               # 6 chapters + overview (HTML + PDF each)
├── part3_jnana/                # 6 chapters + overview (HTML + PDF each)
│
└── yada_yada.{html,pdf}                 # 3 detailed verse-by-verse sheets
    karmanye_vadhikaraste.{html,pdf}
    sthita_prajna.{html,pdf}
```

## 🖨️ Regenerating PDFs

PDFs are committed to the repo so they're available immediately. To regenerate them after editing HTML:

```bash
# 1. Serve the repo root locally (so relative font URLs resolve):
python3 -m http.server 8011 &

# 2. Regenerate all 21 mini-sheet PDFs at once:
bash shared/generate_pdfs.sh
```

Or simply open any `.html` file in a browser and use **File → Print → Save as PDF**.
