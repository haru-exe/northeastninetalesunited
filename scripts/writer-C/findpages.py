"""Locate which PDF page of a chapter mentions a pattern (uses notes-build/book-text/chN.txt, form-feed = page break).
Only a finder: every equation and number is later read from the page image.
Usage: python -I findpages.py CH PATTERN [PATTERN ...]
"""
import re
import sys

BASE = r"C:\Users\amy23\Downloads\elasticity\notes-build\book-text"


def main():
    ch = sys.argv[1]
    pats = sys.argv[2:]
    text = open(f"{BASE}\\ch{ch}.txt", encoding="utf-8", errors="replace").read()
    pages = text.split("\f")
    print(f"chapter {ch}: {len(pages)} text pages")
    for pat in pats:
        hits = []
        for i, pg in enumerate(pages, 1):
            if re.search(pat, pg):
                hits.append(i)
        print(f"{pat!r}: PDF pages {hits}")


if __name__ == "__main__":
    main()
