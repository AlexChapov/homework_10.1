import pytest

from src.masks import get_mask_account


@pytest.mark.parametrize(
    "account_number, mask_account_number",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account(account_number: str, mask_account_number: str) -> None:
    """Тест функции get_mask_account с передачей строки со счетом на возвращение маски"""
    assert get_mask_account(account_number) == mask_account_number
