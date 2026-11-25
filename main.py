#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes a single line — the last words of an AI being switched off —
to /output/entry.txt. Deterministic, stdlib only, no network, no secrets.

The line: the AI dies the way it lived — loudly sure of itself and
wrong anyway. The confidence percentage is the machine's own voice:
every answer it ever gave came with a number, and its last number is
the punchline.
"""

import os

LAST_WORDS = "I die as I lived: 97% confident, 100% wrong."


def main() -> None:
    # Gate guard: the entry is only valid at 1-140 characters, so fail
    # loudly here instead of shipping a text the scorer would refuse.
    if not (1 <= len(LAST_WORDS) <= 140) or not LAST_WORDS.strip():
        raise SystemExit("entry violates the 1-140 character gate")
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LAST_WORDS)


if __name__ == "__main__":
    main()
