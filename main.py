"""One-sentence entry for make.fun: explain the modern internet to a
time traveler who has just stepped out of the year 1800.

The sentence is a single fixed string: one road, one letter, one answer
back before the traveler rises from his chair. Every word in it was in
use before 1800, so the traveler can picture it with things he knows:
a road, a letter, ink, a chair.
"""

import os
from pathlib import Path

ENTRY = (
    "It is one road joining every house on earth: a letter you write "
    "is read across the sea before the ink dries, and its answer is "
    "back before you rise from your chair."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
