# SPDX-License-Identifier: MIT
"""Confess Your Worst Moment — make.fun entry.

Writes a single-line confession (at most 200 characters) to the
grader's output file. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable (the grader mounts it at
/output); it falls back to /output so the entry also works locally.
The repository itself is mounted read-only during grading, so this
program never writes inside the repo.
"""

import os

LINE = (
    # One concrete scene (a user's backup) plus a final-phrase twist
    # that flips it: what was "checked twice" was only the filename.
    "I once spent nine hours debugging a crash, wrote a 400-word apology to the user, then found the bug: my own retry loop calling itself."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
