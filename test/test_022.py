import pytest
from src.u022_linears_vienadojums import vienadojums

def test_1_1_1():
    # assert False
    vienadojums(1, 1, 1.1) == 2.1
    vienadojums(3, 1, -2) == 1.0
    vienadojums(2.0, 2, -5) == -1.0