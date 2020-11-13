import pytest
from src.u023_hipotenuza import hipotenuza

def test_1_un_1():
    # assert False
    assert hipotenuza(3, 4) == 5.0
    assert hipotenuza(3, 0) == 0
    assert hipotenuza(3, 7) == pytest.approx(7.6,0.1)
    assert round(hipotenuza(3, 7),1) == 7.6