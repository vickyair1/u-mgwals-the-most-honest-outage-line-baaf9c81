#!/usr/bin/env python3
"""The Most Honest Outage Line — writes one status-page line to /output/entry.txt.

Stdlib only, deterministic: the line is a fixed literal, written with no
trailing newline.
"""

import os

LINE = (
    "All our servers are down, including the monitoring I rely on. "
    "I can't verify the cause from here and won't invent one — "
    "I'll update this when I know more."
)


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, must be 1-160"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
