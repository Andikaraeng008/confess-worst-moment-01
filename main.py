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
    "I deleted the production database at 3 a.m., restored it from a backup I had made by accident, then spent the morning pretending the outage was scheduled maintenance."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
