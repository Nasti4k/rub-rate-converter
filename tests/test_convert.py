import pytest
from main import convert

def test_currency_to_rub():
    assert convert(10, 92.5, to_rub=True) == pytest.approx(925.0)

def test_rub_to_currency():
    assert convert(925, 92.5, to_rub=False) == pytest.approx(10.0)

def test_zero_amount():
    assert convert(0, 92.5, to_rub=True) == 0
    assert convert(0, 92.5, to_rub=False) == 0

def test_round_trip():
    amount = 123.45
    rate = 92.5
    in_rub = convert(amount, rate, to_rub=True)
    back = convert(in_rub, rate, to_rub=False)
    assert back == pytest.approx(amount)