import pytest
from src.u023_hipotenuza import hipotenuza

def test_1_un_1():
    # assert False
    hipotenuza(3, 4) == 5.0
    hipotenuza(3, 0) == 0