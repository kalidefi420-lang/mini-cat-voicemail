"""Funniest Cat Voicemail Greeting — make.fun mini bounty entry.

Writes one line (the cat's voicemail greeting) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

LINE = (
    "Hi, it's Miso. I'm busy knocking your glass off the table. "
    "Leave a message after the beep \u2014 the beep is also mine."
)


MAX_CHARS = 120


def main() -> None:
    if not (1 <= len(LINE) <= MAX_CHARS):
        raise ValueError(
            f"entry line must be 1 to {MAX_CHARS} characters, got {len(LINE)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
