import pytest
from src.u023_hipotenuza import hipotenuza

def test_simple():
    assert hipotenuza(3, 4) == 5.0

def test_normal():
    assert hipotenuza(3, 7) == pytest.approx(7.6157731058)

def test_a_nulle():
    assert hipotenuza(0, 5) == 0

def test_b_nulle():
    assert hipotenuza(3, 0) == 0

def test_abi_nulle():
    assert hipotenuza(0, 0) == 0

def test_a_negative():
    assert hipotenuza(-1, 4) == 0

def test_b_negative():
    assert hipotenuza(1, -4) == 0

def test_abi_negative():
    assert hipotenuza(-1, -4) == 0