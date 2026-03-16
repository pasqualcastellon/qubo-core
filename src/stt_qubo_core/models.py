from pydantic import BaseModel, Field
from .value_objects import QuboDict

class QuboProblem(BaseModel):
    qubo: QuboDict
    num_reads: int = Field(default=100, gt=0)
