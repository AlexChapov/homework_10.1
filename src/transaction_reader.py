import csv
import pandas as pd
import logging
import os


log_dir = "../logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


logger = logging.getLogger("transaction_reader")
file_handler = logging.FileHandler("../logs/transaction_reader.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def reading_csv_file(transaction_csv: str) -> list:
    """Принимает на вход путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(transaction_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            data = list(reader)
            logger.info(f"Данные из файла {transaction_csv} прочитаны.")
    except FileNotFoundError:
        """Если файл, указанный в переменной csv_file не существует, то вернуть пустой список"""
        logger.error(f"Файл {transaction_csv} не существует.")
        return []

    """Если csv-файл пустой, то вернуть пустой список"""
    if not data:
        logger.error(f"Ошибка чтения json из файла {transaction_csv}.")
        return []

    """Если содержимое файла не является списком, то вернется пустой список"""
    if not isinstance(data, list):
        logger.error(f"Содержимое файла {transaction_csv} не является объектом типа list.")
        return []

    return data


def reading_xlsx_file(transaction_xlsx: str) -> list:
    """Принимает на вход путь до XLSX-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        excel_data = pd.read_excel(transaction_xlsx).to_dict(orient="records")
    except FileNotFoundError:
        logger.error(f"Файл {transaction_xlsx} не существует.")
        return []

    """Если xlsx-файл пустой, то вернуть пустой список"""
    if not excel_data:
        logger.error(f"Ошибка чтения json из файла {transaction_xlsx}.")
        return []

    """Если содержимое файла не является списком (содержит несписок), то вернуть пустой список"""
    if not isinstance(excel_data, list):
        logger.error(f"Содержимое файла {transaction_xlsx} не является объектом типа list.")
        return []

    return excel_data



print(reading_csv_file("../data/transactions.csv"))
print(reading_xlsx_file("../data/transactions_excel.xlsx"))