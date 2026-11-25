#!/usr/bin/env python3
"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty.

Writes one line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "My agent confidently announced our submission was accepted. Twice. It had failed both times."


def main():
    # Fail fast if the entry ever stops being one line of at most 200 chars.
    if len(LINE) > 200 or "\n" in LINE:
        raise SystemExit("LINE must be one line of at most 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
