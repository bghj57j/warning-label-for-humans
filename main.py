# Writes the one warning to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# Real label rhythm: contents under pressure, do not shake.
import os
LINE = "WARNING: Contents under pressure. This human runs on caffeine and three hours of sleep — do not shake, and never ask how the weekend was."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # same output on every run
