import io
from random import randint
import random
from unittest.mock import Mock
import compoundInterest

def test_monkeyCalculator_noSmiles_prints_correct_result(capfd, monkeypatch):
    principal_1 = 1200
    time_1 = 2
    rate_1 = 5.4
    principal_2 = 12345
    time_2 = 8
    rate_2 = 6.7
    principal_3 = 50
    time_3 = 1
    rate_3 = 1
    input = [principal_1, time_1, rate_1, principal_2, time_2, rate_2, principal_3, time_3, rate_3]
    monkeypatch.setattr('builtins.input', lambda _:input.pop(0))
    compoundInterest.calculateCompoundInterest()

    out, err = capfd.readouterr()
    expected = "Compound Interest: 133.1\n---\nCompound Interest: 8394.89\n---\nCompound Interest: 0.5\n"
    assert out == expected
