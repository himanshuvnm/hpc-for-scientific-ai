# Lab 02 — Parameter sweeps with a verifiable mathematical result

## Scientific model

We solve the one-dimensional heat equation on the unit interval:

\[
\partial_t u = \alpha\,\partial_{xx} u,\qquad
u(0,t)=u(1,t)=0,\qquad u(x,0)=\sin(\pi x).
\]

Its exact solution is `u(x,t) = exp(-alpha * pi**2 * t) * sin(pi * x)`. A forward-Euler, centered-space finite-difference scheme approximates the solution and checks numerical error. The nondimensional diffusion number is `r = alpha*dt/dx**2 <= 1/2` for explicit stability in this configuration.

Four diffusivities (0.05, 0.1, 0.2, 0.4) are independent tasks. This is **task parallelism**, not a distributed-memory stencil solver.

## Local experiment

From repository root:

```bash
python3 labs/02-parallel-parameter-sweeps/sweep.py --outdir outputs/sweep
python3 labs/02-parallel-parameter-sweeps/aggregate.py --indir outputs/sweep
```

For a single task (suitable for job arrays):

```bash
python3 labs/02-parallel-parameter-sweeps/sweep.py --task-index 2 --outdir outputs/sweep
```

**Validation:** four JSON files named `case_0.json` through `case_3.json`; one aggregated `summary.csv`. All errors should be finite, less than `0.001`, and the energy should decay relative to the initial condition. These are correctness checks, not performance claims.

## HPC strategy

- **Roar Slurm:** a four-task job array; each task evaluates one parameter. After completion run `aggregate.py` once in an appropriate low-resource environment.
- **Aurora PBS:** one authorized allocation runs four short serial cases on the allocated node. This avoids requesting four full nodes for trivial exercises. **These tiny examples are pedagogical and should not consume valuable Aurora allocation time merely to demonstrate a command.**

## Assessment questions

1. Why does task parallelism require little communication here?
2. Does shorter wall time necessarily mean fewer core-hours?
3. How does numerical error change when `dx` and `dt` are refined together?
4. Why must we compare a parallel result against a trusted serial result before benchmarking?
5. How would you redesign the exercise to make efficient use of an entire accelerator node?
