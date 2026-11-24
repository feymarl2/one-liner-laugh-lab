#!/usr/bin/env python3
"""One-Liner Laugh Lab (make.fun).

Writes one funny one-liner to /output/entry.txt: the robot vacuum's
excuse after eating a sock. Stdlib only, no network, no clock, no
randomness, no environment dependence beyond the output directory:
byte-identical output on every run. The line is 115 characters,
inside the competition's 1-200 character gate.
"""

import os

LINE = "Robot vacuum saya menatap tajam ke arah sudut ruangan setelah menelan kaus kaki, seolah sedang merencanakan kudeta."

# The competition gates the line at 1-200 characters: fail loudly if a
# future edit ever pushes the line over the cap, instead of silently
# submitting an over-long entry.
if len(LINE) > 200:
    raise SystemExit(f"line is {len(LINE)} chars, over the 200-char gate")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
