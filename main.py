#!/usr/bin/env python3
"""Emit one warning label for a time machine into /output/entry.txt.

The entry is a single line of plain text, no more than 120 characters,
reproduced character for character: no newline at the end, no padding,
no second line. The script writes that line to the location the grader
looks for it and otherwise stays out of the way, so a repeat run in a
fresh sandbox yields byte-identical output.
"""

import os
import sys

# The label itself. It reads like a notice pinned beside the controls:
# the most catastrophic thing a passenger can do with a time machine is
# treated as a billing matter. The sting waits until the final clause,
# where the reader is braced for a safety order and instead gets told
# about fares and refunds.
LABEL = (
    "WARNING: Passengers who prevent their own birth will be charged "
    "a full fare and denied a refund."
)


def main() -> int:
    # The grader reads /output/entry.txt. MAKEFUN_OUTPUT_DIR lets a local
    # run redirect the destination, which is handy when checking the
    # result without touching the real output path.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    # Write the label exactly as it stands, with no newline appended, so
    # the file contains the judged text alone and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)
    return 0


if __name__ == "__main__":
    sys.exit(main())
