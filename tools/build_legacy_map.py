#!/usr/bin/env python3
"""Keeps links to the previous README's section anchors working, invisibly.

    python3 tools/build_legacy_map.py

The previous README used long bilingual heading anchors (for example
`#-paths-to-money--пути-к-деньгам`). Other pages and repositories may still link to them, so
each of those anchors is kept as an empty `<a name="…">` placed directly above the README
section that now covers the same topic. Nothing is rendered; the README itself does not refer
to its earlier layout. The anchor lines are generated (marker `<!-- legacy-anchors -->`); do
not edit them by hand.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inventory import inventory  # noqa: E402

ARCHIVE = "archive/README_2026-11-19_pre-showcase.md"
MARK = "<!-- legacy-anchors -->"
# (first line, last line) of the archived README -> heading of the README.md section that covers it
RANGES = [
    (1, 35, "## At a glance"), (36, 57, "## Quick navigation"), (58, 84, "## What this study is"),
    (85, 264, "## Hypotheses and design"), (265, 303, "## Data and methods"), (304, 349, "## Hypotheses and design"),
    (350, 367, "## Glossary"), (368, 428, "## Results so far"), (429, 440, "## Data and methods"),
    (441, 446, "## Timeline"), (447, 462, "## OSF preregistration"), (463, 474, "## Patent connection"),
    (475, 489, "## Research team"), (490, 502, "## Ethics, IP and security"), (503, 510, "## Research team"),
    (511, 555, "## Navigation and structure"), (556, 589, "## ASRP ecosystem"), (590, 601, "## Contact"),
    (602, 688, "## Glossary"), (689, 694, "## License"), (695, 712, "## Status and roadmap"), (713, 720, "## Quick navigation"),
]


def main():
    heads = inventory(open(ARCHIVE, encoding="utf-8").read())["headings"]
    by_section = {}
    for h in heads:
        for a, b, sec in RANGES:
            if a <= h["line"] <= b:
                by_section.setdefault(sec, []).append(h["anchor"])
    lines = [ln for ln in open("README.md", encoding="utf-8").read().split("\n") if not ln.startswith(MARK)]
    out, placed = [], set()
    for ln in lines:
        if ln in by_section and ln not in placed:
            placed.add(ln)
            out.append(MARK + "".join('<a name="%s"></a>' % a for a in by_section[ln]))
        out.append(ln)
    missing = set(by_section) - placed
    if missing:
        raise SystemExit("README.md has no section for: %s" % sorted(missing))
    open("README.md", "w", encoding="utf-8").write("\n".join(out))
    print("README.md: %d legacy anchors kept above %d sections" % (sum(len(v) for v in by_section.values()), len(placed)))


if __name__ == "__main__":
    main()
