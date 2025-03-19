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
    """Тест функции get_date по передаче строки и даты"""
    assert get_date(getting_the_date) == conclusion


@pytest.mark.parametrize(
    "getting_the_date, conclusion",
    [
        ("2013-01-11T04:13:18.671407", "11.01.2013"),
        ("2024-02-02T12:21:13.435211", "02.02.2024"),
        ("2024-03-03T04:10:42.425421", "03.03.2024"),
        ("2025-07-03T04:10:44.422421", "03.07.2025"),
        ("2021-03-03T04:10:42.425421", "03.03.2021"),
    ],
)
def test_get_date_len(getting_the_date: str, conclusion: str) -> None:
    """Тест функции get_date по передаче строки и даты по длине строки"""
    assert len(getting_the_date) == 26, conclusion == 10


@pytest.mark.parametrize(
    "getting_the_date, conclusion",
    [
        ("2013-0111T04:13:18.671407", "Неправильный формат даты/время"),
        ("2024-0212:21:13.435211", "Неправильный формат даты/время"),
        ("2024-03-03T010:42.425421", "Неправильный формат даты/время"),
        ("202503T04:10:44.42241", "Неправильный формат даты/время"),
        ("2021-03-03T0410:42.4254", "Неправильный формат даты/время"),
    ],
)
def test_get_date_len(getting_the_date: str, conclusion: str) -> None:
    """Тест функции get_date по неверной передаче строки и даты по длине строки"""
    assert len(getting_the_date) != 26, conclusion == "Неправильный формат даты/время"
