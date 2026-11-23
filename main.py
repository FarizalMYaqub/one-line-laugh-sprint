"""One-Line Laugh Sprint entry.

Writes one original funny line about everyday life to /output/entry.txt.
The line is a fixed string: the program is deterministic on purpose, so
every run produces the exact same entry.
"""

import os

LINE = "My houseplants started a group chat without me, and I'm pretty sure they're planning to leave for someone who remembers water exists."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 200


def validate(line):
    """The gate only accepts UTF-8 text of 1 to 200 chars, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    line.encode("utf-8")
    return line


def main():
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
