transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list[dict[str, str | int]], currency_code="USD") -> list[dict[str, str | int]]:
    """Функция принимает на вход список словарей, представляющих транзакции, возвращает
    транзакции, где валюта операции соответствует заданной (['code'] == 'USD')"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


trans = filter_by_currency(transactions)

print(next(trans))
print(next(trans))
print(next(trans))


def transaction_descriptions(transactions: list[dict[str, str | int]]) -> list[dict[str]]:
    """Функция принимает список словарей с банковскими операциями
    и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


description = transaction_descriptions(transactions)

print(next(description))
print(next(description))
print(next(description))
print(next(description))
print(next(description))


def card_number_generator(start: int, stop: int) -> list[str]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX"""
    while True:
        for num in range(start, stop + 1):
            number = "0" * (16 - len(str(num))) + str(num)
            string_to_return = ""
            block_counter = 0
            for digit in number:
                block_counter += 1
                if block_counter <= 4:
                    string_to_return += digit
                else:
                    string_to_return += " " + digit
                    block_counter = 1
            yield string_to_return


number_card = card_number_generator(1, 9999999999999999)

print(next(number_card))
print(next(number_card))
print(next(number_card))
print(next(number_card))
print(next(number_card))
