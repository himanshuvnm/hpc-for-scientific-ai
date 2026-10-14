# Assignment 01 — Reproducible scientific jobs (Lab 01 + Lab 02)

**Submission:** a short PDF or Markdown report plus `summary.csv` (with private metadata removed). No HPC access required.

1. Run Lab 01 locally with two seeds; state which JSON fields change and why.
2. Run all four Lab 02 tasks and aggregate their results.
3. Re-run task index 2 alone; compare the `relative_l2_error` against the all-task run with a stringent absolute tolerance such as `1e-12`.
4. Derive the closed-form heat-equation solution for a sine-wave initial condition.
5. Explain how the same code can be launched by Slurm and PBS without rewriting the solver.
6. Explain why a four-task sweep may not justify reserving a full Aurora node.

**Required evidence:** commands, version of Python, table of alpha/error, one paragraph about reproducibility, and resource-budget reflection.
