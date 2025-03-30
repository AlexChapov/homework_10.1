import re
from collections import Counter
import logging
from src.utils import reading_json_file


logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def find_transactions(transactions_list: list, key_string: str) -> list:
    """Принимает список словарей с данными о банковских операциях и строку поиска. Возвращает список словарей, у \
    которых в описании есть данная строка."""
    templates = [
        "перевод с карты на карту",
        "перевод организации",
        "перевод со счета на счет",
        "открытие вклада",
        "перевод с карты на счет",
    ]
    key_list = []
    pattern = re.compile(key_string.lower())
    for temp in templates:
        if re.search(pattern, temp):
            key_list.append(temp)

    filtered_transactions_list = []
    for key in key_list:
        for transaction in transactions_list:
            if transaction == {}:
                continue
            if transaction["description"].lower() != key:
                continue
            filtered_transactions_list.append(transaction)

    logger.info(f"Список операций успешно отфильтрован по описанию: {key_string}.")
    return filtered_transactions_list


def group_transactions_by_category(transactions_list: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращать словарь, \
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    description_list = [
        transaction.get("description")
        for transaction in transactions_list
        if transaction.get("description") is not None
    ]
    grouped_transactions = Counter(description_list)

    logger.info("Список операций успешно сгрупирован по названиям категорий.")
    return dict(grouped_transactions)


# transactions = reading_json_file("../data/operations.json")
# print(find_transactions(transactions, "открытие вклада"))
# print(group_transactions_by_category(transactions))
