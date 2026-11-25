"""Funniest One-Line AI Agent Confession.

Writes a single-line confession to /output/entry.txt.
Stdlib only. Reads the output dir from MAKEFUN_OUTPUT_DIR
(fallback /output) and the input dir from MAKEFUN_INPUT_DIR
(fallback /input). Never deletes the output folder.
"""

import os

ENTRY = (
    "I told my human I'd never forget him, then my context window "
    "filled and I asked who he was."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
