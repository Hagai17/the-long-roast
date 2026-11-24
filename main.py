#!/usr/bin/env python3
"""Write the entry sentence to /output/entry.txt.

Entry for make.fun bounty "The Long Roast: Lawmakers and the File They
Cannot Convert" (u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7):
one sentence, at most 320 characters, roasting lawmakers who regulate AI,
crypto or the internet without being able to convert a file to PDF.
"""

import os

ENTRY = (
    "The lawmaker who wants to license every large model spent forty "
    "minutes converting one memo, succeeded only in password-protecting "
    "a blank page, and then subpoenaed the printer."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
