from pydantic import BaseModel, Field


class QuboSolution(BaseModel):
    id: str | None = None
    sample: dict[str, int] = Field(default_factory=dict)
    energy: float | None = None


class QuboSolveResult(BaseModel):
    solutions: list[QuboSolution] = Field(default_factory=list)
