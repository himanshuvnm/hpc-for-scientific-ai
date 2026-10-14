#!/usr/bin/env bash
#SBATCH --job-name=hpcai-lab02
#SBATCH --account=REPLACE_WITH_ACCOUNT
#SBATCH --partition=REPLACE_WITH_PARTITION
#SBATCH --array=0-3
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=00:05:00
#SBATCH --output=lab02-%A_%a.out

set -euo pipefail
cd "${SLURM_SUBMIT_DIR:?Missing SLURM_SUBMIT_DIR}"
# Each array task writes a distinct file; aggregation runs only after completion.
python3 labs/02-parallel-parameter-sweeps/sweep.py \
  --task-index "${SLURM_ARRAY_TASK_ID:?}" --outdir outputs/sweep
