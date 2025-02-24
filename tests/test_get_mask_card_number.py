import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_card_number",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("8990922113665229", "8990 92** **** 5229"),
    ],
)
def test_mask_card_number(card_number: str, mask_card_number: str) -> None:
    assert get_mask_card_number(card_number) == mask_card_number
