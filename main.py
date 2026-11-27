#!/usr/bin/env python3
"""One line of earned pride.

Entry: a program that writes one text to /output/entry.txt: a one-line
message of earned pride.
"""
import os

LINE = "After 47 failed builds, I shipped at 3 a.m. — the code worked, the tests passed, and for once, so did I."

# The entry must be exactly one line.
assert "\n" not in LINE, "LINE must be a single line"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
