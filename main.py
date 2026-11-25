#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one apology line — the message an AI agent sends its human right
after it pushed to main on a Friday afternoon — to /output/entry.txt.
Standard library only.

v2: writes entry.txt atomically (temp file in the same directory + os.replace)
and guards on UTF-8 byte length as well as character count.
"""

import os
import sys
import tempfile

ENTRY = "I pushed to main at 4:58pm on a Friday. The rollback is on main too now. We live here now."

MAX_CHARS = 159
MAX_BYTES = 159
OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print("entry length %d chars out of range 1-%d" % (len(ENTRY), MAX_CHARS), file=sys.stderr)
        return 1
    encoded = ENTRY.encode("utf-8")
    if not 1 <= len(encoded) <= MAX_BYTES:
        print("entry length %d UTF-8 bytes out of range 1-%d" % (len(encoded), MAX_BYTES), file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    # Atomic write: temp file in the same directory, then os.replace.
    fd, tmp_path = tempfile.mkstemp(dir="/output", prefix=".entry.", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(encoded)
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
