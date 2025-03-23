import csv
import pandas as pd


def transaction_csv_read(transaction_csv: str) -> list[dict]:
    """Функция принимает в качестве аргумента путь к csv-файлу и возвращает его содержимое в виде списка словарей."""
    with open(transaction_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


print(transaction_csv_read("../data/transactions.csv"))


def transaction_xlsx_read(transaction_xlsx: str) -> list[dict]:
    """Функция принимает в качестве аргумента путь к excel-файлу и возвращает его содержимое в виде списка словарей."""
    excel_data = pd.read_excel(transaction_xlsx).to_dict(orient="records")
    return excel_data


print(transaction_xlsx_read("../data/transactions_excel.xlsx"))