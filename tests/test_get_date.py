import pytest

from src.widget import get_date

@pytest.mark.parametrize(
    "getting_the_date, conclusion",
    [
        ("2023-01-11T04:13:18.671407", "11.01.2023"),
        ("2024-02-02T12:21:13.435211", "02.02.2024"),
        ("2025-03-03T04:10:42.425421", "03.03.2025"),
        ("2025-07-03T04:10:44.422421", "03.07.2025"),
        ("2024-03-03T04:10:42.425421", "03.03.2024"),
    ],
)

def test_get_date(getting_the_date: str, conclusion: str) -> None:
    assert get_date(getting_the_date) == conclusion
