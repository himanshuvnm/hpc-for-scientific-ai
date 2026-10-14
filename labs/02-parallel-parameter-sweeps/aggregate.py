#!/usr/bin/env python3
"""Validate independent case outputs and create a sorted summary CSV."""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

EXPECTED_ALPHAS = (0.05, 0.1, 0.2, 0.4)


def aggregate(indir: Path) -> list[dict]:
    rows = []
    for index, alpha in enumerate(EXPECTED_ALPHAS):
        source = indir / f"case_{index}.json"
        if not source.is_file():
            raise FileNotFoundError(f"Missing task {index}: {source}")
        value = json.loads(source.read_text(encoding="utf-8"))
        if value.get("task_index") != index or not math.isclose(value.get("alpha", -1), alpha):
            raise ValueError(f"Wrong task label or alpha in {source}")
        error = float(value["relative_l2_error"])
        if not (math.isfinite(error) and 0 <= error < 0.001):
            raise ValueError(f"Numerical accuracy check failed in {source}: {error}")
        if not float(value["final_energy"]) < float(value["initial_energy"]):
            raise ValueError(f"Energy did not decay in {source}")
        rows.append(value)
    destination = indir / "summary.csv"
    columns = ["task_index", "alpha", "relative_l2_error", "elapsed_seconds",
               "initial_energy", "final_energy", "grid_intervals", "steps", "dt"]
    with destination.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--indir", type=Path, default=Path("outputs/sweep"))
    args = parser.parse_args()
    rows = aggregate(args.indir)
    print(f"Validated {len(rows)} independent cases; saved {args.indir / 'summary.csv'}")
    for row in rows:
        print(f"  alpha={row['alpha']:.2f} | relative L2 error={row['relative_l2_error']:.3e}")


if __name__ == "__main__":
    main()
