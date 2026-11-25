#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes one two-line robot confession to /output/entry.txt:
line 1 owns one specific mistake, line 2 names the lesson and the fix.
Pure Python standard library, no network, deterministic output.
"""

import os

ENTRY = (
    "I'm sorry — I set your alarm for six in the evening instead of six in "
    "the morning, and you slept straight through your job interview.\n"
    "I've learned that morning and evening are not details I can guess at, "
    "so now I read the hour back to you out loud and wait for your yes "
    "before I set anything."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
