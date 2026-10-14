# Contributing

Contributions are welcome: corrections, improved explanations, new labs, test coverage, and responsibly validated cluster scripts.

1. Open an issue describing the learning objective or correction.
2. Keep machine-independent Python separate from platform-specific submission scripts.
3. For a lab, include prerequisites, commands, expected outputs, tests, and discussion questions.
4. For a platform recipe, name the platform and software versions, account/queue prerequisites, and whether a real submission was verified. Never publish allocation identifiers, privileged endpoints, proprietary files, or credentials.
5. Run `python3 -m unittest discover -s tests -v` before sending a change.

Style: Python 3.10+ standard library where feasible, explicit `main()` functions, type hints, fixed seeds, relative paths, small CPU smoke tests. Clearly mark benchmarks as illustrative unless backed by execution records and method descriptions.
