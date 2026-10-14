PYTHON ?= python3
.PHONY: test lab1 lab2 doctor

test:
	$(PYTHON) -m unittest discover -s tests -v

lab1:
	$(PYTHON) labs/01-first-hpc-job/hello.py --output outputs/hello.json

lab2:
	$(PYTHON) labs/02-parallel-parameter-sweeps/sweep.py --outdir outputs/sweep
	$(PYTHON) labs/02-parallel-parameter-sweeps/aggregate.py --indir outputs/sweep

doctor:
	$(PYTHON) tools/hpc_doctor.py
