#!/usr/bin/env python3
"""Portable, dependency-free scientific job with a deterministic checksum."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import platform
import random
from datetime import datetime, timezone


def run(seed: int = 42, iterations: int = 1000) -> dict:
    if iterations < 1:
        raise ValueError("iterations must be >= 1")
    rng = random.Random(seed)
    checksum = sum(rng.random() for _ in range(iterations)) / iterations
    slurm_job = os.environ.get("SLURM_JOB_ID")
    pbs_job = os.environ.get("PBS_JOBID")
    scheduler = "slurm" if slurm_job else "pbs" if pbs_job else "local/unknown"
    return {
        "lab": "01-first-hpc-job",
        "seed": seed,
        "iterations": iterations,
        "checksum": round(checksum, 12),
        "python_version": platform.python_version(),
        "scheduler": scheduler,
        "job_id": slurm_job or pbs_job,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--output", type=Path, default=Path("outputs/hello.json"))
    args = parser.parse_args()
    result = run(args.seed, args.iterations)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"Saved: {args.output}")


if __name__ == "__main__":
    main()
