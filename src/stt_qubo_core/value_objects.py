from pydantic import BaseModel, Field, field_validator


class QuboDict(BaseModel):
    data: dict[tuple[int, int], float] = Field(default_factory=dict)

    @field_validator("data", mode="before")
    @classmethod
    def normalize_keys(cls, value):
        if not isinstance(value, dict):
            raise TypeError("QUBO data must be a dict")

        normalized = {}
        for k, v in value.items():
            if isinstance(k, str):
                parts = k.split(",")
                if len(parts) != 2:
                    raise ValueError(f"Invalid QUBO key: {k}")
                i, j = map(int, parts)
                normalized[(i, j)] = float(v)
            elif isinstance(k, tuple) and len(k) == 2:
                i, j = k
                normalized[(int(i), int(j))] = float(v)
            else:
                raise ValueError(f"Invalid QUBO key type: {k}")
        return normalized
