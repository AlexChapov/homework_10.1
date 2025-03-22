import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log")
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


print(reading_json_file("../data/operations.json"))
