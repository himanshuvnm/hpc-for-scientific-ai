# Argonne ALCF Aurora — PBS Professional adaptation

**State:** examples are **illustrative, not executed on Aurora**. ALCF schedules whole nodes and requires authorization and resource settings. Running a tiny CPU teaching example on an Aurora node is generally a **poor use of scarce allocation time**; work locally first, and submit only as part of a justified, permitted training or research allocation.

Read the official [Aurora running-jobs guidance](https://docs.alcf.anl.gov/aurora/running-jobs-aurora/) and check the current queue, account, filesystem, and software-environment rules before any submission.

## Before submission

1. Obtain an approved ALCF project and queue policy. The example templates use `debug` and `home:flare`, matching common documented examples; these may not be correct for your project.
2. **Replace `REPLACE_WITH_PROJECT`** in each PBS file; verify and adjust queue/filesystems/wall time based on the current documentation. Treat these values as configurable examples.
3. Ensure you have a usable `python3` interpreter in the scheduled environment (modules/venv may be required). `python3` is not guaranteed to be the desired interpreter by default.
4. Submit from the repository root, which must be accessible within the allocation. Some storage paths require explicit filesystem requests.
5. Use local execution to understand the concepts before reserving a node for a tiny workload.

## Examples — only after approval

```bash
qsub platforms/alcf-aurora/pbs/01-first-job.pbs
qstat -u "$USER"
```

The second example runs all four diffusivities **within a single PBS allocation**, rather than requesting four separate full nodes:

```bash
qsub platforms/alcf-aurora/pbs/02-parameter-sweep.pbs
```

There is no claim that these templates are cost-effective Aurora production workloads. A later course module should instead use scientifically justified accelerator-scale workloads and performance profiling.
