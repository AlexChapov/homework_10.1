import pytest

from src.processing import filter_by_state


def test_filter_by_state_none() -> None:
    assert filter_by_state([]) == []


def test_filter_by_state(dictionaries: list) -> None:
    assert filter_by_state(dictionaries) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]
