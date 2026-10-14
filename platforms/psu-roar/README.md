# Penn State Roar — Slurm adaptation

**State:** scripts are **illustrative / locally syntax-checked only**. They are not certified to run on any specific Roar allocation, partition, or module stack. Use [the official Roar batch-jobs guide](https://docs.icds.psu.edu/running-jobs/batch-jobs/) as the operational authority.

## Before submission

- Have a valid account and permitted partition from your cluster administrator. A paid allocation may use an SLA partition rather than a hardware partition.
- In both scripts, replace `REPLACE_WITH_ACCOUNT` and `REPLACE_WITH_PARTITION` with values **you are authorized to use**.
- Check `python3 --version` in an appropriate allocated environment and arrange your environment activation if necessary.
- Work from the repository root and write outputs to suitable storage; do not put heavy data on shared home filesystems.

## Lab 01

```bash
sbatch platforms/psu-roar/slurm/01-first-job.sbatch
squeue -u "$USER"
```

## Lab 02 — independent tasks

```bash
sbatch platforms/psu-roar/slurm/02-parameter-array.sbatch
squeue -u "$USER"
```

After the array has fully completed, run `aggregate.py` on an appropriately allocated low-resource environment. Do not aggregate while array tasks are still writing their results.

## What to measure

Submission/job ID, queue wait, elapsed time, allocated cores/memory, application accuracy, and CPU usage. Sanitize all reports before publishing.

**Important:** do not change the science code simply because the scheduler changes; demonstrate that different launch paths execute the same calculation.
