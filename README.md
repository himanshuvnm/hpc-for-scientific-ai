# HPC for Scientific AI

**From Your Laptop to a Supercomputer**

A teaching-first, openly developed guide to **high-performance computing (HPC), parallel programming, scientific Python, and reproducible scientific AI**. Learn concepts on your own computer before adapting them to institutional HPC systems, including **Penn State Roar (Slurm)** and **ALCF Aurora (PBS Professional)**.

> **Status: v0.1.1 terminology update.** The Python labs and automated tests can be run locally. Scheduler templates are **educational examples, not yet tested on live Roar or Aurora allocations**. Do not submit them until you have reviewed local rules and replaced placeholders.

## What does “Scientific AI” mean?

**Scientific AI** refers here to AI methods used to advance scientific modeling, prediction, inference, experimentation, or discovery. **Scientific machine learning (SciML)** is the machine-learning part of this area, connecting data-driven learning with scientific modeling or computation.

**HPC for Scientific AI** teaches the scalable computing methods needed to run AI-enabled scientific workflows; **HPC for SciML** focuses more specifically on scientific machine-learning training, inference, and evaluation. HPC and scientific computing are also valuable independently of AI: the first two labs teach those foundations before introducing learned models.

Read **[Terminology and scope](TERMINOLOGY.md)** for precise definitions, comparisons, examples and authoritative references. These are *operational definitions for this course*, not claims of universal disciplinary agreement.

## Choose your path

| I am a... | Start here | What I will learn |
| --- | --- | --- |
| Student with Python experience | [Quick start](GETTING_STARTED.md) | Reproducible computing and your first batch job |
| HPC beginner | [Lab 01](labs/01-first-hpc-job/README.md) | Nodes, environments, schedulers, and execution records |
| Researcher working with multiple simulations | [Lab 02](labs/02-parallel-parameter-sweeps/README.md) | Job arrays, parameter sweeps, and result verification |
| Roar user | [PSU Roar notes](platforms/psu-roar/README.md) | Slurm account/partition choices and job submission |
| Aurora user | [ALCF Aurora notes](platforms/alcf-aurora/README.md) | PBS project/filesystem requests and resource stewardship |
| Instructor | [Instructor materials](instructor/syllabus.md) | Reusable lessons and assessment rubric |

## First run — no cluster account required

Requirements: **Python 3.10+**, a shell, and Git. No Conda and no third-party Python packages are required for v0.1.

```bash
python3 labs/01-first-hpc-job/hello.py --output outputs/hello.json
python3 labs/02-parallel-parameter-sweeps/sweep.py --outdir outputs/sweep
python3 labs/02-parallel-parameter-sweeps/aggregate.py --indir outputs/sweep
python3 -m unittest discover -s tests -v
```

Generated outputs are ignored by Git. The lab results are designed to be portable; hostnames, private paths, accounts, and full job logs should **not** be published without review.

## Course roadmap

1. HPC architecture and resource models
2. Linux, SSH, filesystem navigation, and remote development
3. Scheduling jobs (Slurm, PBS)
4. Python environments, modules, storage, and quotas
5. Scientific Python and numerical correctness
6. Parallel Python, MPI, and shared-memory programming
7. Profiling, strong/weak scaling, and performance measurement
8. GPU computing: CUDA and Intel XPU (planned)
9. Distributed training with PyTorch (planned)
10. Large scientific datasets and I/O (planned)
11. Workflow resilience, checkpointing, and reproducibility (planned)
12. Scientific ML capstone (planned)

See [COURSE_MAP.md](COURSE_MAP.md) for learning objectives and assessment design, and [ROADMAP.md](ROADMAP.md) for release milestones.

## Repository map

```text
hpc-for-scientific-ai/
├── TERMINOLOGY.md         # precise definitions and scope
├── docs/                  # dependency-free GitHub Pages landing site
├── labs/                  # runnable, small scientific experiments
├── platforms/             # machine-specific submission examples
├── instructor/            # syllabus, assignments, rubrics
├── tests/                 # CPU-only automated correctness checks
├── tools/                 # local environment inspection
├── .github/workflows/     # continuous integration
└── GETTING_STARTED.md     # first-use instructions
```

## How this repository is different

- **Concept first, cluster second:** programs run locally before they run on institutional HPC.
- **Correctness before speed:** exercises include numerical checks and explicit expected results.
- **Portable execution:** scheduler-specific scripts call the **same Python** implementation.
- **Responsible use of allocations:** request only authorized resources; Aurora examples are not intended to justify trivial production-node experiments.
- **Evidence over claims:** local tests are marked as tested; actual cluster examples and performance comparisons will be marked verified only after on-system execution.

## Website

A dependency-free website lives in [`docs/index.html`](docs/index.html), ready for GitHub Pages. After creating the GitHub repository, follow [PUBLISHING.md](PUBLISHING.md) to select **Deploy from a branch → main → /docs**. The current v0.1 website intentionally uses plain HTML/CSS to make the first release immediately publishable without a Node build. A richer documentation framework can be added later.

## Important usage notes

This is an **independent educational project**, not an official Penn State or Argonne user guide. Platform behavior changes: consult the [Roar documentation](https://docs.icds.psu.edu/) and [ALCF Aurora documentation](https://docs.alcf.anl.gov/aurora/) before submitting jobs. Never commit credentials, internal allocations, unpublished datasets, private paths, or unreviewed operational logs.

## Attribution and contributing

Project lead: **Himanshu Singh**. See [CONTRIBUTING.md](CONTRIBUTING.md) for proposals, corrections, and new platform recipes. Source code uses the [MIT License](LICENSE). Contact the maintainer before redistributing substantial third-party tutorial content; credit each source explicitly.
