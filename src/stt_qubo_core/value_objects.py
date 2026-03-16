from pydantic import BaseModel, Field, field_validator


class QuboDict(BaseModel):
    """
    QUBO dictionary represented as a map ((i, j) -> float).
    Keys are normalized so that i <= j.
    """
    data: dict[tuple[int, int], float] = Field(default_factory=dict)

    @field_validator("data", mode="before")
    @classmethod
    def normalize_keys(cls, val: dict) -> dict[tuple[int, int], float]:
        if not isinstance(val, dict):
            raise TypeError("QUBO data must be a dict")

        normalized: dict[tuple[int, int], float] = {}
        for k, v in val.items():
            if isinstance(k, str): # allow "i,j"
                parts = k.split(",")
                if len(parts) != 2:
                    raise ValueError(f"Invalid QUBO key: {k}")
                i, j = map(int, parts)
            elif isinstance(k, tuple) and len(k) == 2:
                i, j = k
            else:
                raise ValueError(f"Invalid QUBO key type: {k}")

            key = (i, j) if i <= j else (j, i)
            normalized[key] = float(v)

        return normalized

    def variables_count(self) -> int:
        """Return an upper bound on the number of variables referenced."""
        if not self.data:
            return 0
        return 1 + max(max(i, j) for (i, j) in self.data.keys())
