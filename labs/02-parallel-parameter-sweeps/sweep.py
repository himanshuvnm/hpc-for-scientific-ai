#!/usr/bin/env python3
"""Independent heat-equation parameter sweep; standard library only."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from time import perf_counter

DIFFUSIVITIES = (0.05, 0.1, 0.2, 0.4)
GRID_INTERVALS = 128
TIME_STEP = 0.00005
STEPS = 200


def solve(alpha: float, intervals: int = GRID_INTERVALS, dt: float = TIME_STEP,
          steps: int = STEPS) -> dict:
    if intervals < 2 or dt <= 0 or steps < 1 or alpha <= 0:
        raise ValueError("Use intervals>=2, dt>0, steps>=1, alpha>0")
    dx = 1.0 / intervals
    diffusion_number = alpha * dt / (dx * dx)
    if diffusion_number > 0.5:
        raise ValueError("Unstable explicit finite-difference step (alpha*dt/dx^2>0.5)")
    x = [i * dx for i in range(intervals + 1)]
    u = [math.sin(math.pi * xi) for xi in x]
    initial_energy = sum(ui * ui for ui in u) * dx
    start = perf_counter()
    for _ in range(steps):
        next_u = u[:]
        for i in range(1, intervals):
            next_u[i] = u[i] + diffusion_number * (u[i - 1] - 2 * u[i] + u[i + 1])
        next_u[0] = 0.0
        next_u[-1] = 0.0
        u = next_u
    elapsed_seconds = perf_counter() - start
    t = dt * steps
    exact = [math.exp(-alpha * math.pi**2 * t) * math.sin(math.pi * xi) for xi in x]
    err2 = sum((a - b)**2 for a, b in zip(u, exact)) * dx
    reference2 = sum(b * b for b in exact) * dx
    final_energy = sum(ui * ui for ui in u) * dx
    return {
        "alpha": alpha,
        "grid_intervals": intervals,
        "steps": steps,
        "dt": dt,
        "final_time": t,
        "diffusion_number": diffusion_number,
        "relative_l2_error": math.sqrt(err2 / reference2),
        "initial_energy": initial_energy,
        "final_energy": final_energy,
        "elapsed_seconds": elapsed_seconds,
    }


def execute(task_index: int, outdir: Path) -> Path:
    if task_index not in range(len(DIFFUSIVITIES)):
        raise ValueError(f"task-index must be from 0 to {len(DIFFUSIVITIES)-1}")
    result = solve(DIFFUSIVITIES[task_index])
    result["task_index"] = task_index
    outdir.mkdir(parents=True, exist_ok=True)
    destination = outdir / f"case_{task_index}.json"
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"case {task_index}: alpha={result['alpha']:.2f}, error={result['relative_l2_error']:.3e}, saved {destination}")
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-index", type=int, default=None,
                        help="0..3; omit to execute all tasks locally")
    parser.add_argument("--outdir", type=Path, default=Path("outputs/sweep"))
    args = parser.parse_args()
    indices = range(len(DIFFUSIVITIES)) if args.task_index is None else (args.task_index,)
    for i in indices:
        execute(i, args.outdir)


if __name__ == "__main__":
    main()
