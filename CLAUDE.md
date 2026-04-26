# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Run a single test
pytest tests/test_value_objects.py::test_qubodict_normalizes_string_keys_and_orders

# Build the package
hatch build
```

## Architecture

This is a Python library (`stt-qubo-core`) for solving QUBO (Quadratic Unconstrained Binary Optimization) problems, structured with a **hexagonal / ports-and-adapters** pattern.

### Data flow

```
QuboProblem(qubo: QuboDict, num_reads)
    → QuboService.solve()
        → QuboSolverPort.solve()   ← any solver implements this Protocol
            → QuboSolveResult(solutions: list[QuboSolution])
```

### Layers

| File | Role |
|------|------|
| `value_objects.py` | `QuboDict` — the QUBO matrix as `dict[(i,j) → float]`. Keys are normalized so `i ≤ j` on ingestion; accepts tuple or `"i,j"` string keys. |
| `models.py` | `QuboProblem` — Pydantic input model wrapping a `QuboDict` + `num_reads`. |
| `result.py` | `QuboSolution` + `QuboSolveResult` — Pydantic output models. |
| `ports.py` | `QuboSolverPort` — a `typing.Protocol` with a single `solve(problem) → QuboSolveResult` method. Any solver must satisfy this interface. |
| `services.py` | `QuboService` — accepts any `QuboSolverPort`, calls it, then normalises the result (assigns UUIDs to solutions without IDs, coerces sample keys to `str`). |
| `solvers/dimod_sa.py` | `DimodSimulatedAnnealingSolver` — bundled concrete solver using `dimod.SimulatedAnnealingSampler`. |

### Adding a new solver

Implement the `QuboSolverPort` Protocol (no inheritance needed) and inject it into `QuboService`:

```python
class MyCustomSolver:
    def solve(self, problem: QuboProblem) -> QuboSolveResult:
        ...

service = QuboService(solver=MyCustomSolver())
```

## Package details

- PyPI name: `stt-qubo-core`; importable as `stt_qubo_core`
- Python ≥ 3.10 required (uses `dict[tuple[int, int], float]` type syntax)
- Build backend: `hatchling`
