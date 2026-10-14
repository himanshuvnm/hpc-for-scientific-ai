# Getting started in 10 minutes

The first two labs can be completed on any laptop with Python 3.10 or newer. **Do not run compute-heavy experiments on HPC login nodes.**

## First: clarify the terms

Read [Terminology and scope](TERMINOLOGY.md). The first two labs teach scientific computing and HPC foundations; they do not train an AI model. Later labs will introduce scientific machine learning.

## 1. Check prerequisites

```bash
python3 --version
git --version
```

You do **not** need Conda, NumPy, PyTorch, SSH, or a supercomputer for the first exercises.

## 2. Run Lab 01

From the repository root:

```bash
python3 labs/01-first-hpc-job/hello.py --seed 42 --output outputs/hello.json
```

Inspect `outputs/hello.json`: it records the timestamp, Python version, computational checksum, and whether the program detected a scheduler job ID. The checksum is deterministic for a fixed seed and iteration count.

## 3. Run Lab 02

```bash
python3 labs/02-parallel-parameter-sweeps/sweep.py --outdir outputs/sweep
python3 labs/02-parallel-parameter-sweeps/aggregate.py --indir outputs/sweep
```

You should obtain four results, each testing the one-dimensional heat equation at a different diffusivity. The numerical solution is compared with a closed-form analytic solution.

## 4. Verify your setup

```bash
python3 -m unittest discover -s tests -v
python3 tools/hpc_doctor.py
```

The doctor prints only local, non-secret hints. Review its output before sharing it publicly.

## 5. Preview the teaching website locally

```bash
python3 -m http.server 8000 --directory docs
```

Open `http://localhost:8000` in a browser. Stop the preview with Ctrl+C. The site is dependency-free; remote Google Fonts have system-font fallbacks.

## 6. Move to a cluster only after local success

- For Roar, read [`platforms/psu-roar/README.md`](platforms/psu-roar/README.md).
- For Aurora, read [`platforms/alcf-aurora/README.md`](platforms/alcf-aurora/README.md).
- Check allocation and quota policies; submit from an appropriate login/submission host, **not** a compute node unless site policy says otherwise.
- Validate Python access *inside the scheduled environment* before running a batch script.

## Questions for reflection

Why does a successful laptop run not imply a successful cluster job? Which environment differences can change the result? How would you prove that distributed tasks produced the same outputs as a serial run?
