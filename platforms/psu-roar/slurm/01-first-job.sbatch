#!/usr/bin/env bash
#SBATCH --job-name=hpcai-lab01
#SBATCH --account=REPLACE_WITH_ACCOUNT
#SBATCH --partition=REPLACE_WITH_PARTITION
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=00:05:00
#SBATCH --output=lab01-%j.out

set -euo pipefail
cd "${SLURM_SUBMIT_DIR:?Missing SLURM_SUBMIT_DIR}"
# Activate an approved Python environment here if python3 is not ready.
python3 labs/01-first-hpc-job/hello.py --output outputs/hello.json
