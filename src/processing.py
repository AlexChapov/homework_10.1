from typing import Dict, List, Union

dictionaries = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(
    dictionaries: list[dict], state: str = "EXECUTED"
) -> tuple[list[dict], list[dict]]:
    """Функция принимает на вход список словарей и возвращает сортированные списки по
    значению для ключа state (EXECUTED и CANCELED)"""
    new_list_1 = []
    new_list_2 = []

    for i in dictionaries:
        if i.get("state") == "EXECUTED":
            new_list_1.append(i)
        else:
            new_list_2.append(i)
    return new_list_1


print(filter_by_state(dictionaries))


def sort_by_date(
    dictionaries: List[Dict[str, Union[str, int]]], revers_str: bool = True
) -> List[Dict[str, Union[str, int]]]:
    """Функция возвращающая список отсортированный по дате (по убыванию)"""
    sorted_list = sorted(dictionaries, key=lambda x: x["date"], reverse=revers_str)

    return sorted_list


print(sort_by_date(dictionaries))
