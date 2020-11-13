import pytest
from src.u033_paari import skaitlu_vardnica

def test_kaut_ko():
    # assert False
    skaitlu_vardnica("viens one") == {'viens': 'one'}
    skaitlu_vardnica("viens one divi two") == {'viens': 'one', 'divi': 'two'}