"""CPU-only smoke and numerical tests for the first two teaching labs."""
from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HELLO = ROOT / "labs/01-first-hpc-job/hello.py"
SWEEP = ROOT / "labs/02-parallel-parameter-sweeps/sweep.py"
AGGREGATE = ROOT / "labs/02-parallel-parameter-sweeps/aggregate.py"


class Tests(unittest.TestCase):
    def test_lab01_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "one.json"
            second = Path(tmp) / "two.json"
            for target in (first, second):
                subprocess.run([sys.executable, str(HELLO), "--seed", "7", "--output", str(target)],
                               cwd=ROOT, check=True, capture_output=True, text=True)
            a = json.loads(first.read_text())
            b = json.loads(second.read_text())
            self.assertEqual(a["checksum"], b["checksum"])
            self.assertEqual(a["iterations"], 1000)
            self.assertTrue(0 < a["checksum"] < 1)

    def test_sweep_aggregation(self):
        with tempfile.TemporaryDirectory() as tmp:
            outdir = Path(tmp) / "sweep"
            subprocess.run([sys.executable, str(SWEEP), "--outdir", str(outdir)],
                           cwd=ROOT, check=True, capture_output=True, text=True)
            subprocess.run([sys.executable, str(AGGREGATE), "--indir", str(outdir)],
                           cwd=ROOT, check=True, capture_output=True, text=True)
            self.assertTrue((outdir / "summary.csv").is_file())
            for i in range(4):
                result = json.loads((outdir / f"case_{i}.json").read_text())
                self.assertLess(result["relative_l2_error"], 0.001)
                self.assertLess(result["final_energy"], result["initial_energy"])
                self.assertLessEqual(result["diffusion_number"], 0.5)

    def test_indexed_matches_serial(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp) / "all", Path(tmp) / "one"
            subprocess.run([sys.executable, str(SWEEP), "--outdir", str(a)],
                           cwd=ROOT, check=True, capture_output=True)
            subprocess.run([sys.executable, str(SWEEP), "--task-index", "2", "--outdir", str(b)],
                           cwd=ROOT, check=True, capture_output=True)
            result_a = json.loads((a / "case_2.json").read_text())
            result_b = json.loads((b / "case_2.json").read_text())
            self.assertEqual(result_a["relative_l2_error"], result_b["relative_l2_error"])
            self.assertEqual(result_a["final_energy"], result_b["final_energy"])

    def test_bad_index_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run([sys.executable, str(SWEEP), "--task-index", "9", "--outdir", tmp],
                                  cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("task-index must be", proc.stderr)


if __name__ == "__main__":
    unittest.main()
