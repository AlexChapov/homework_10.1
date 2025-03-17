import json


def reading_json_file(operations: str) -> list[dict]:
    """Принимает json-файл и возвращает список словарей"""
    try:
        with open(operations, "r", encoding="utf-8") as f:
            content = f.read()
        # print(f"Файл {operations} открыт на чтение")
        """Если файл, указанный в переменной operations, не сущаетвует"""
    except FileNotFoundError:
        print(f"Файл {operations} не существует")
        return []

    """Если json-файл (operations) пустой возвращается пустой список"""
    try:
        data = json.loads(content)
        # print(f"Данные из файла {operations} прочитаны")
    except json.JSONDecodeError:
        print(f"Ошибка чтения json из файла {operations}")
        return []
    """Если содержимое файла не является списком, то вернется пустой список"""
    if not isinstance(data, list):
        print(f"Содержимое файла {operations} не является объектом типа list")
        return []

    return data


print(reading_json_file("../data/operations.json"))
