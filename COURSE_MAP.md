# Curriculum and learning objectives

Before starting, read [Terminology and scope](TERMINOLOGY.md) to distinguish HPC, scientific computing, Scientific AI, and Scientific ML. The foundational numerical labs are not themselves AI methods.

The project is designed as a modular university laboratory companion. Weeks are suggested, not required.

| Week | Topic | Measurable learning outcome | Deliverable |
| --- | --- | --- | --- |
| 1 | Computing architecture | Distinguish core, node, accelerator, and interconnect | Resource diagram |
| 2 | Shell, SSH, storage | Transfer and locate files safely | Reproducible environment inventory |
| 3 | Scheduling | Interpret a job script and submit a correctly sized job | Lab 01 report |
| 4 | Environments | Explain module and venv isolation | Environment specification |
| 5 | Numerical correctness | Quantify discretization error | Heat equation validation |
| 6 | Task parallelism | Compare serial vs independent task execution | Lab 02 sweep |
| 7 | MPI and communication | Distinguish compute scaling from communication cost | MPI exercise (planned) |
| 8 | Performance | Calculate strong/weak scaling efficiency | Scaling report (planned) |
| 9 | Accelerator models | Explain GPU execution and memory movement | GPU portability lab (planned) |
| 10 | Distributed ML | Evaluate DDP throughput and checkpoints | Training report (planned) |
| 11 | Scientific I/O | Explain throughput, chunking, and reproducibility | Data workflow (planned) |
| 12 | Capstone | Defend accuracy, efficiency, and resource budget | Reproducibility package (planned) |

## Assessment philosophy

Evaluate **correctness, scientific reasoning, reproducibility, resource stewardship, and communication** rather than reward short runtimes alone. Avoid forcing students to reserve scarce cluster resources for trivial tasks.
