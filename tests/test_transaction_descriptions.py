import pytest

from src.generators import transaction_descriptions


@pytest.mark.parametrize(
    "transactions, expected",
    [
        # Тест с пустым списком транзакций
        ([], []),
        # Тест с одной транзакцией
        ([{"description": "Перевод организации"}], ["Перевод организации"]),
        # Тест с несколькими транзакциями
        (
            [
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
                {"description": "Перевод организации"},
            ],
            ["Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации"],
        ),
    ],
)
def test_transaction_descriptions(transactions: list[dict], expected: list[dict]) -> None:
    """Функция которая передает данные для проверки transaction_descriptions"""
    assert list(transaction_descriptions(transactions)) == expected
