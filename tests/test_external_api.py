from src.external_api import currency_conversion, API_KEY
from unittest.mock import patch, MagicMock


def test_currency_conversion(transaction_api):
    rub_transaction = currency_conversion(transaction_api)
    assert rub_transaction == "31957.58"


@patch("requests.get")
def test_transaction_rub(mock_get):
    mock_get.return_value.json.return_value = {"result": 95.0}
    mock_get.return_value.status_code = 200
    transaction = {"operationAmount": {"amount": "1", "currency": {"code": "EUR"}}}
    result = currency_conversion(transaction)
    assert result == 95.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1", headers={"apikey": API_KEY}
    )