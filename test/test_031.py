import pytest
from src.u031_virs_videja import lielaku_skaits

def test_kaut_ko():
    # assert False
    lielaku_skaits([1, 3, 5]) == 1
    lielaku_skaits([100, 10, 180]) == 2