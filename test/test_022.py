import pytest
from src.u022_linears_vienadojums import vienadojums

def test_1_1_1():
    # assert False
    assert vienadojums(1, 1, 1.1) == 2.1
    assert vienadojums(3, 1, -2) == 1.0
    assert vienadojums(2.0, 2, -5) == -1.0