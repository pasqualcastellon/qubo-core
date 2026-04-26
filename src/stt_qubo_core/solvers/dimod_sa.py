import dimod
import uuid
from dimod.typing import Bias, Variable
from typing import Dict, Tuple, Mapping, cast
from ..ports import QuboSolverPort
from ..models import QuboProblem
from ..result import QuboSolveResult, QuboSolution


class DimodSimulatedAnnealingSolver(QuboSolverPort):
    """
    QUBO solver implemented with dimod's SimulatedAnnealingSampler.
    """
    def solve(self, problem: QuboProblem) -> QuboSolveResult:
        sampler = dimod.SimulatedAnnealingSampler()
        Q = cast(Mapping[Tuple[Variable, Variable], Bias], problem.qubo.data)
        sample_set = sampler.sample_qubo(Q, num_reads=problem.num_reads)

        solutions: list[QuboSolution] = []
        for row in sample_set.data():
            sample: Dict[str, float | int]  = {str(k): int(v) for k, v in row.sample.items()}
            solutions.append(
                QuboSolution(
                    id=str(uuid.uuid4()),
                    sample=sample,
                    energy=float(row.energy),
                )
            )

        return QuboSolveResult(solutions=solutions)
