import pytest

from src.generators import filter_by_currency


@pytest.mark.parametrize(
    "transactions, currency_code, expected",
    [
        # Тест с пустым списком транзакций
        ([], "USD", []),
        # Тест с одной транзакцией, которая совпадает по валюте
        (
            [{"operationAmount": {"currency": {"code": "USD"}}}],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
        # Тест с одной транзакцией, которая не совпадает по валюте
        ([{"operationAmount": {"currency": {"code": "EUR"}}}], "USD", []),
        # Тест с несколькими транзакциями, из которых одна совпадает по валюте
        (
            [
                {"operationAmount": {"currency": {"code": "EUR"}}},
                {"operationAmount": {"currency": {"code": "USD"}}},
                {"operationAmount": {"currency": {"code": "GBP"}}},
            ],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
        # Тест с несколькими транзакциями, все из которых совпадают по валюте
        (
            [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}, {"operationAmount": {"currency": {"code": "USD"}}}],
        ),
    ],
)
def test_filter_by_currency(transactions: list[dict], currency_code: str, expected: list[dict]) -> None:
    assert list(filter_by_currency(transactions, currency_code)) == expected
