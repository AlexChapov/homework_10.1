import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "data_entry, invoice_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8245982476732479", "Visa Classic 6831 98** **** 7658"),
        ("Visa Classic 2131982476738875", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(data_entry: str, invoice_result: str) -> None:
    assert mask_account_card(data_entry) == invoice_result


@pytest.mark.parametrize(
    "data_entry, invoice_result",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 50678682250652525582", "Счет **5582"),
        ("Счет 83611677104416527054", "Счет **7054"),
        ("Счет 25839625641659820304", "Счет **0304"),
        ("Счет 95928416864794176133", "Счет **6133"),
    ],
)
def test_mask_account_card(data_entry: str, invoice_result: str) -> None:
    assert mask_account_card(data_entry) == invoice_result
