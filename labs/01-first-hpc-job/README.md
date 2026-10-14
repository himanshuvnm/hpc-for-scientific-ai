# Lab 01 — First scientific job

**Goal:** distinguish *the scientific program* from *the system used to launch it*.

**Prerequisites:** Python 3.10+; no third-party dependencies.

## Run locally

```bash
python3 labs/01-first-hpc-job/hello.py --seed 42 --iterations 1000 --output outputs/hello.json
```

**Expected outcome:** a JSON object containing `lab`, `seed`, `iterations`, `checksum`, `python_version`, `scheduler`, `job_id`, and `timestamp_utc`; `checksum` should be reproducible across platforms for the same seed/iterations. `job_id` should be null on a typical laptop.

## Cluster execution

Follow the corresponding platform guide. The same Python program is invoked by a Slurm or PBS script after requesting resources.

- Roar: [`../../platforms/psu-roar/README.md`](../../platforms/psu-roar/README.md)
- Aurora: [`../../platforms/alcf-aurora/README.md`](../../platforms/alcf-aurora/README.md)

### Reflection

1. Which parts of `hello.py` are independent of the cluster?
2. What is a resource allocation? What belongs in the job script rather than Python?
3. How do you check a nonzero exit status, and where do standard output and error go?
4. What is the difference between a test that works locally and a verified HPC deployment?
