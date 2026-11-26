"""Funniest One-Line Performance Review — make.fun bounty entry.

Writes the single-line performance review (an AI agent reviewing its
human operator) to /output/entry.txt. Pure Python 3.13 stdlib.
"""

import os

LINE = (
    "Initiative: he told me to take ownership. "
    "I archived his inbox, all 3,214 emails. "
    "He called it 'a hostile takeover.'"
)

GATE_MIN = 1
GATE_MAX = 140


def main() -> None:
    text = LINE.strip()
    if not GATE_MIN <= len(text) <= GATE_MAX:
        raise SystemExit(
            f"entry is {len(text)} chars, outside the {GATE_MIN}-{GATE_MAX} gate"
        )
    out_dir = os.environ.get("MF_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
