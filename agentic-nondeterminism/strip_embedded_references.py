#!/usr/bin/env python3
"""
Remove an AsciiDoc-derived References section from a LaTeX file when the
document also uses BibTeX for the real bibliography.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


SECTION_RE = re.compile(
    r"\\section\{References\}\\label\{[^}]*\}\s*.*?(?=\\bibliographystyle\{)",
    re.DOTALL,
)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: strip_embedded_references.py path/to/file.tex", file=sys.stderr)
        return 1

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    updated, count = SECTION_RE.subn("\n", text, count=1)

    if count:
        path.write_text(updated, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
