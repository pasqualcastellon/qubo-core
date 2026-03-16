import pytest
from typing import Dict, Tuple, cast
from src.value_objects import QuboDict


def test_qubodict_normalizes_string_keys_and_orders():
    raw = cast(Dict[Tuple[int, int], float], {
        "1,0": -0.5,
        "0,0": 1.0,
        (2, 3): 2.0,
    })
    q = QuboDict(data=raw)
    # claus normalitzades i ordenades (i<=j)
    assert q.data[(0, 0)] == 1.0
    assert q.data[(0, 1)] == -0.5
    assert q.data[(2, 3)] == 2.0
    # recompte de variables (upper bound)
    assert q.variables_count() >= 4  # 0..3

def test_qubodict_rejects_bad_keys():
    with pytest.raises(ValueError):
        raw = cast(Dict[Tuple[int, int], float], {
            "bad": 1.5
        })
        QuboDict(data=raw)
