#!/usr/bin/env python3
"""One Letter for Your Day.

Writes exactly one letter to /output/entry.txt: "Z".

The letter stands for "zombie" -- a day spent shuffling through on zero
sleep, body on autopilot and brain offline. Z is the universal glyph for
sleep (Zzz), and "zombie" is the sharpest, funniest, truest picture of
such a day: it lands at once, and it is the first word anyone reaches
for behind the letter Z.
"""

import os

LETTER = "Z"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
