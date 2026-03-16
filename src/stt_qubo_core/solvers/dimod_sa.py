import dimod
from ..models import QuboProblem
from ..result import QuboSolveResult, QuboSolution


class DimodSimulatedAnnealingSolver:
    def solve(self, problem: QuboProblem) -> QuboSolveResult:
        sampler = dimod.SimulatedAnnealingSampler()
        sample_set = sampler.sample_qubo(problem.qubo.data, num_reads=problem.num_reads)

        solutions = []
        for row in sample_set.data():
            sample = {str(k): int(v) for k, v in row.sample.items()}
            solutions.append(
                QuboSolution(
                    sample=sample,
                    energy=float(row.energy),
                )
            )

        return QuboSolveResult(solutions=solutions)
