import pytest
import requests
import responses
from main import fetch_rates, API_URL

FAKE_RESPONSE = {
    "Valute": {
        "USD": {"Nominal": 1, "Value": 92.5},
        "JPY": {"Nominal": 100, "Value": 63.2},
    }
}

@responses.activate
def test_fetch_rates_ok():
    responses.add(responses.GET, API_URL, json=FAKE_RESPONSE, status=200)
    rates = fetch_rates()
    assert "USD" in rates
    assert rates["USD"]["Value"] == 92.5
    assert rates["JPY"]["Nominal"] == 100

@responses.activate
def test_fetch_rates_server_error():
    responses.add(responses.GET, API_URL, status=500)
    with pytest.raises(requests.HTTPError):
        fetch_rates()

@responses.activate
def test_fetch_rates_timeout():
    responses.add(responses.GET, API_URL, body=requests.Timeout())
    with pytest.raises(requests.RequestException):
        fetch_rates()