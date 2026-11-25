"""Monday Morning Punchlines — one joke about Monday mornings.

The program writes a single joke to /output/entry.txt.
Standard library only; no network, no third-party packages.
"""

import os
from pathlib import Path

JOKE = "Monday is the one subscription I never signed up for, yet it renews every week and the cancel button is greyed out."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    # Mode 0644 so the sealed scorer can read the file.
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
