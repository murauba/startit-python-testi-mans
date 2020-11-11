import pytest
from src.u022_linears_vienadojums import vienadojums

def test_visi_vieni():
    assert vienadojums(1, 1, 1.1) == 2.1

def test_negativs_b():
    assert vienadojums(3, 1, -2) == 1.0

def test_decimali():
    assert vienadojums(2.0, 2, -5) == -1.0
