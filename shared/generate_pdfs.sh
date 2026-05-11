#!/usr/bin/env bash
# Generate PDFs for all chapter mini-sheets and part overviews.
# Requirements: chromium (or chromium-browser) available, an HTTP server
# running on $PORT serving the repo root. Run from anywhere; outputs are
# placed alongside each HTML file.
set -u

PORT="${PORT:-8011}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="${CHROME:-chromium}"

# All HTML files we want PDFs for (relative to repo root).
files=(
  "part1_karma/part1_overview.html"
  "part1_karma/ch01_arjuna_visada.html"
  "part1_karma/ch02_sankhya.html"
  "part1_karma/ch03_karma.html"
  "part1_karma/ch04_jnana_karma_sannyasa.html"
  "part1_karma/ch05_karma_sannyasa.html"
  "part1_karma/ch06_dhyana.html"
  "part2_bhakti/part2_overview.html"
  "part2_bhakti/ch07_jnana_vijnana.html"
  "part2_bhakti/ch08_akshara_brahma.html"
  "part2_bhakti/ch09_raja_vidya.html"
  "part2_bhakti/ch10_vibhuti.html"
  "part2_bhakti/ch11_vishva_rupa.html"
  "part2_bhakti/ch12_bhakti.html"
  "part3_jnana/part3_overview.html"
  "part3_jnana/ch13_kshetra_kshetrajna.html"
  "part3_jnana/ch14_guna_traya.html"
  "part3_jnana/ch15_purushottama.html"
  "part3_jnana/ch16_daivasura.html"
  "part3_jnana/ch17_shraddha_traya.html"
  "part3_jnana/ch18_moksha_sannyasa.html"
)

cd "$ROOT"
for f in "${files[@]}"; do
  pdf="${f%.html}.pdf"
  url="http://localhost:${PORT}/${f}"
  rm -f "$pdf"
  "$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="$pdf" --virtual-time-budget=15000 "$url" >/dev/null 2>&1
  size=$(stat -c%s "$pdf" 2>/dev/null || stat -f%z "$pdf" 2>/dev/null || echo "?")
  echo "✓ $pdf  (${size} bytes)"
done
