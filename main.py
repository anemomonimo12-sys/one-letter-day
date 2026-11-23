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

# The day, in one word: zero sleep, body on autopilot, brain offline.
WORD = "zombie"
# The letter is the word's first letter -- and Z is the sleep glyph (Zzz),
# so the letter and the word behind it point at the same picture.
LETTER = WORD[0].upper()
OUTPUT_PATH = "/output/entry.txt"


def write_entry(letter: str) -> None:
    """Write exactly one letter, nothing else, to the entry file."""
    if len(letter) != 1 or not letter.isalpha():
        raise ValueError("entry must be exactly one letter")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(letter)


def main() -> None:
    write_entry(LETTER)


if __name__ == "__main__":
    main()
