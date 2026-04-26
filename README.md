# qubo-core

Reusable QUBO core library for solving Quadratic Unconstrained Binary Optimization problems, designed for API and HPC execution.

## Installation

```bash
pip install stt-qubo-core
```

## Usage

```python
from stt_qubo_core import (
    QuboProblem, QuboDict,
    QuboService, DimodSimulatedAnnealingSolver
)

qubo = QuboDict(data={
    (0, 0): -1.0,
    (1, 1): -1.0,
    (0, 1):  2.0,
})

problem = QuboProblem(qubo=qubo, num_reads=100)
service = QuboService(solver=DimodSimulatedAnnealingSolver())
result = service.solve(problem)

for sol in result.solutions:
    print(sol.energy, sol.sample)
```

### Custom solver

Implement the `QuboSolverPort` protocol and inject it into `QuboService`:

```python
from stt_qubo_core import QuboProblem, QuboSolverPort, QuboSolveResult, QuboService

class MyRemoteSolver:
    def solve(self, problem: QuboProblem) -> QuboSolveResult:
        ...

service = QuboService(solver=MyRemoteSolver())
```

## Development

```bash
pip install -e ".[dev]"
pytest tests/
```

## License

MIT
