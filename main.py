#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one apology line — the message an AI agent sends its human right
after it pushed to main on a Friday afternoon — to /output/entry.txt.
Standard library only.
"""

import os
import sys

ENTRY = "I pushed to main at 4:58pm on a Friday. The rollback is on main too now. We live here now."

MAX_CHARS = 159


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print("entry length %d out of range 1-%d" % (len(ENTRY), MAX_CHARS), file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
