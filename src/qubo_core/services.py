import uuid
from .models import QuboProblem
from .ports import QuboSolverPort
from .result import QuboSolveResult, QuboSolution


class QuboService:
    def __init__(self, solver: QuboSolverPort):
        self._solver = solver

    def solve(self, problem: QuboProblem) -> QuboSolveResult:
        raw = self._solver.solve(problem)

        normalized = []
        for solution in raw.solutions:
            normalized.append(
                QuboSolution(
                    id=solution.id or str(uuid.uuid4()),
                    sample={str(k): int(v) for k, v in solution.sample.items()},
                    energy=solution.energy,
                )
            )

        return QuboSolveResult(solutions=normalized)
