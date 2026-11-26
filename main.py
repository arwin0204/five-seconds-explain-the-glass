#!/usr/bin/env python3
"""Five Seconds to Explain the Glass -- make.fun bounty entry.

Writes the single sentence a house cat would say in its own defence
in the five seconds after sweeping a glass off the table: no apology,
no confession, just the most convincing case the cat can make for
itself. Pure Python 3.13 standard library; no network, no randomness,
no clock. Writes only to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

ENTRY = (
    "I was conducting an official floor inspection and the glass kindly "
    "volunteered as my test subject — it failed, the floor passed, inspection complete."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry is {len(ENTRY)} chars, must be 1-200", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
