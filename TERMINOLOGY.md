# Terminology and scope

**HPC for Scientific AI — From Your Laptop to a Supercomputer**

The terms in this document are **operational definitions for this educational repository**, not claims that every research community uses identical boundaries. In particular, **AI for Science** is a widely used name for the broader research area; **Scientific AI** is used here as a concise description of AI serving scientific inquiry. Sources are provided below.

## 1. Foundational terms

### High-performance computing (HPC)

**High-performance computing (HPC)** is the use of parallel algorithms, high-performance processors and accelerators, memory systems, interconnects, storage, and software infrastructure to carry out computational work at a scale or speed that would be impractical with simpler computing resources.

- HPC can use multicore CPUs, GPUs, multiple interconnected nodes, high-throughput job arrays, or combinations of these resources.
- A supercomputer is an HPC system, but learning HPC concepts does **not** require access to a supercomputer.
- Merely running a small serial Python script on a supercomputer does not make the algorithm parallel or scalable.

### Scientific computing

**Scientific computing** uses computational and numerical methods to formulate, approximate, simulate, analyze, or solve scientific and engineering problems. It includes, for example, numerical linear algebra, optimization, ordinary and partial differential equations, and uncertainty quantification. **Scientific computing does not automatically involve AI or ML.**

### Artificial intelligence (AI) and machine learning (ML)

**Artificial intelligence (AI)** is a broad field concerned with computational systems performing capabilities such as inference, planning, reasoning, perception, learning, or decision-making. **Machine learning (ML)** is an important area of AI in which models learn patterns or relationships from data or experience rather than relying entirely on explicitly programmed rules. Some AI systems are not based on learned models.

## 2. Scientific Artificial Intelligence (Scientific AI)

**Working definition:** Scientific AI is the development or application of AI methods to advance scientific modeling, prediction, inference, experimentation, analysis, or discovery.

Its scope can include machine learning surrogates, scientific foundation models, generative models for scientific data, automated experiment design, and AI-assisted scientific reasoning. The related and more established label **AI for Science** is used by the US Department of Energy to encompass applications of AI and related methods to scientific problems, including those integrated with simulation and scalable computing [1].

Scientific purpose does not, by itself, establish scientific validity. Evaluation must address relevant scientific properties, uncertainty, and reproducibility as appropriate to the problem.

## 3. Scientific Machine Learning (SciML)

**Working definition:** Scientific machine learning is the development and application of ML methods in scientific and engineering modeling, computation, prediction, inference, or discovery, often drawing on scientific knowledge, numerical methods, or mechanistic models.

A useful **conceptual slogan**, not a mathematical equality, is:

> **Scientific ML = Scientific computing + machine learning.**

The SciML software ecosystem uses this formulation [2], while the *SIAM Journal on Scientific Computing* places ML methods for scientific mathematical modeling within the scientific computing literature [3]. SciML **does not require** that every model embed a differential equation or an explicit physical constraint; scientific data-driven surrogates are also within scope. Physics-informed and hybrid mechanistic-learning models are notable subareas, not the whole field.

## 4. HPC for Scientific AI

**Working definition:** HPC for Scientific AI is the development and use of scalable computing systems, parallel algorithms, and reproducible computational workflows to support AI-enabled scientific research, including model training, inference, simulation-coupled learning, data processing, and large-scale evaluation.

This repository treats **HPC as the enabling computational layer**, rather than claiming that all AI for Science requires a supercomputer. Some scientific AI experiments are small enough for a laptop; HPC becomes relevant when workload size, time-to-solution, memory, I/O, or parallel experimentation justify it.

## 5. HPC for Scientific Machine Learning (HPC for SciML)

**Working definition:** HPC for SciML is the application and development of high-performance computing methods and systems for scalable scientific machine-learning workloads, including distributed model training, accelerator execution, data pipelines, checkpointing, parallel evaluation, and performance optimization.

**HPC for SciML is a more focused expression than HPC for Scientific AI.** It specifically addresses the learning-based part of scientific AI workloads. In this repository, it is a major technical topic within the broader HPC-for-Scientific-AI curriculum.

## 6. Compare the terms

| Term | Primary concern | Representative example |
| --- | --- | --- |
| Scientific computing | Compute a scientific or engineering solution | Numerically solve the heat equation |
| HPC | Execute computation efficiently at scale | Distribute parameter sweeps with a scheduler |
| Scientific AI / AI for Science | Use AI to advance scientific inquiry | Automatically propose experiments or train a weather foundation model |
| SciML | Use or develop ML methods for scientific problems | Learn a surrogate for a PDE solution operator |
| HPC for Scientific AI | Scale AI-enabled scientific research workflows | Perform large-scale scientific inference and analysis on accelerators |
| HPC for SciML | Scale the ML aspects of scientific workflows | Train and validate a scientific diffusion model across multiple GPUs |
| AI for HPC | Use AI to improve computing systems | Predict job runtime or autotune numerical kernels |

**The direction of benefit matters:** *HPC for AI* uses computing systems to enable AI workloads; *AI for HPC* uses AI methods to improve HPC systems. They can overlap, but they are not synonyms.

## 7. What the current labs do—and do not—demonstrate

- **Lab 01: Your first scientific job** teaches portable execution, environment reporting, and scheduler concepts. It is an HPC foundations exercise, **not an AI model**.
- **Lab 02: Parallel parameter sweeps** solves a numerical heat equation for different parameters, checks accuracy, and illustrates task parallelism. It is **scientific computing and an HPC workflow**, not machine learning.
- Future scientific ML labs will introduce actual learned models and compare accuracy, computational efficiency, and scientific validity against numerical or observational reference data.

Learning the computational foundations *before* training scientific models is an intentional pedagogical progression. We will not label an exercise “AI” unless it actually uses an AI method.

## 8. The repository's scope

The project uses the name **`hpc-for-scientific-ai`** because it covers both general HPC foundations and the broader scientific AI ecosystem. **Scientific machine learning is a central focus**, but we do not want the title to exclude other AI-for-Science workflows such as planning, intelligent automation, or scientific inference.

Our educational standard is: **correctness first, reproducibility throughout, scalability when justified.** Students should be able to explain *what* is being computed, *why* it is scientifically meaningful, *whether* the results are valid, and *how efficiently* the computation uses resources.

## References and terminology notes

1. Argonne, Oak Ridge, and Berkeley national laboratory community, *AI for Science: Report on the Department of Energy Town Halls on Artificial Intelligence (AI) for Science* (2020), Executive Summary. https://publications.anl.gov/anlpubs/2020/03/158802.pdf
2. SciML Open Source Scientific Machine Learning, *SciML: Differentiable Modeling and Simulation Combined with Machine Learning*. https://docs.sciml.ai/
3. H. De Sterck, “New SISC Section on Scientific Machine Learning,” *SIAM Journal on Scientific Computing* **46**(1) (2024), vii–viii. https://doi.org/10.1137/23M160832X
4. U.S. DOE Office of Science, *DOE Explains...Machine Learning*. https://www.energy.gov/science/doe-explainsmachine-learning
5. U.S. DOE Advanced Scientific Computing Research, *Artificial Intelligence*. https://science.osti.gov/ascr/Research/Artificial-Intelligence-AI

These references support the conceptual scope and disciplinary usage. The numbered definitions in this file are **written for this repository**, not quotations or formally endorsed definitions from those organizations.
