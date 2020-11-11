import pytest
from src.u021_summa import summa

def test_1_un_1():
    assert summa(1, 1) == 2

def test_negative():
    assert summa(1, -1) == 0

def test_decimal():
    assert summa(2.5, 1.2) == 3.7