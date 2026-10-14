#!/usr/bin/env python3
"""Non-invasive local HPC readiness hints. Review output before sharing."""
from __future__ import annotations

import platform
import shutil
import sys


def main() -> None:
    print("HPC for Scientific AI — environment hints (no network calls)")
    print(f"Python: {platform.python_version()}")
    print(f"Platform: {sys.platform}")
    for command in ("git", "ssh", "sbatch", "squeue", "qsub", "qstat"):
        print(f"{command}: {'found' if shutil.which(command) else 'not found'}")
    print("Scheduler commands are optional for the laptop-only labs.")
    print("No GPU checks performed. Never share secret job scripts or allocations.")


if __name__ == "__main__":
    main()
