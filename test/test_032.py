import pytest
from src.u032_augosi_skaitli import ir_augoss

def test_kaut_ko():
    # assert False
    assert ir_augoss([1, 3, 5]) == True
    assert ir_augoss([100, 10, 180]) == False
    assert ir_augoss([]) == True