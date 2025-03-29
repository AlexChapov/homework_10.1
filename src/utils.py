import csv
import json
import logging
import os

import pandas as pd

log_dir = "../logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def reading_json_file(operations: str) -> list[dict]:
    """Принимает json-файл и возвращает список словарей"""
    try:
        with open(operations, "r", encoding="utf-8") as f:
            content = f.read()
        logger.info(f"Файл {operations} открыт на чтение")
        """Если файл, указанный в переменной operations, не сущеcтвует"""
    except FileNotFoundError:
        logger.error(f"Файл {operations} не существует")
        return []

    """Если json-файл (operations) пустой возвращается пустой список"""
    try:
        data = json.loads(content)
        logger.info(f"Данные из файла {operations} прочитаны")
    except json.JSONDecodeError:
        logger.error(f"Ошибка чтения json из файла {operations}")
        return []
    """Если содержимое файла не является списком, то вернется пустой список"""
    if not isinstance(data, list):
        logger.error(f"Содержимое файла {operations} не является объектом типа list")
        return []

    return data


# print(reading_json_file("../data/operations.json"))


def reading_csv(csv_file: str) -> list:
    """Принимает на вход путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях."""
    # Если файл, указанный в переменной csv_file не существует, то вернуть пустой список.
    try:
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            data = list(reader)
            print(f"Данные из файла {csv_file} прочитаны.")
    except FileNotFoundError:
        print(f"Файл {csv_file} не существует.")
        return []

    # Если csv-файл пустой, то вернуть пустой список.
    if not data:
        print(f"Ошибка чтения json из файла {csv_file}.")
        return []

    # Если содержимое файла не является списком (содержит несписок), то вернуть пустой список.
    if not isinstance(data, list):
        print(f"Содержимое файла {csv_file} не является объектом типа list.")
        return []

    return data


def reading_xlsx(xlsx_file: str) -> list:
    """Принимает на вход путь до XLSX-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        excel_data = pd.read_excel(xlsx_file).to_dict(orient="records")
    except FileNotFoundError:
        print(f"Файл {xlsx_file} не существует.")
        return []

    # Если xlsx-файл пустой, то вернуть пустой список.
    if not excel_data:
        print(f"Ошибка чтения json из файла {xlsx_file}.")
        return []

    # Если содержимое файла не является списком (содержит несписок), то вернуть пустой список.
    if not isinstance(excel_data, list):
        print(f"Содержимое файла {xlsx_file} не является объектом типа list.")
        return []

    return excel_data


def read_file(file_path: str) -> list[dict | None]:
    *file_name, file_extension = file_path.split(".")
    content: list = []
    match file_extension:
        case "json":
            content = reading_json_file(file_path)
        case "csv":
            content = reading_csv(file_path)
        case "xlsx":
            content = reading_xlsx(file_path)

    return content
