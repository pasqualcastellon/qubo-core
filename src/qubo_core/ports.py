from typing import Protocol
from .models import QuboProblem
from .result import QuboSolveResult


class QuboSolverPort(Protocol):
    def solve(self, problem: QuboProblem) -> QuboSolveResult: ...
