"""Unsent: The Micro-Confession Sprint entry.

Writes a two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line written exactly as it was typed.
"""

import os

ENTRY = (
    "To: Dad\n"
    "I sold the guitar you gave me when I was sixteen, and every time "
    "I hear one now I wish I had kept the one thing you were proud of "
    "me for."
)

OUT_PATH = "/output/entry.txt"


def describe(text):
    """Return a one-line summary of the entry for the run log."""
    lines = text.split("\n")
    return (
        f"to={lines[0][4:].strip()!r} "
        f"message_chars={len(lines[1])} total_chars={len(text)} lines={len(lines)}"
    )


def main():
    text = ENTRY
    lines = text.split("\n")
    assert 1 <= len(text) <= 260, f"full text must be 1-260 chars, got {len(text)}"
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert lines[0].startswith("To: "), "first line must be the To: line"
    assert len(lines[1]) <= 200, f"message line must be <=200 chars, got {len(lines[1])}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {OUT_PATH}: {len(text)} chars, {len(lines)} lines")
    print(describe(text))


if __name__ == "__main__":
    main()
