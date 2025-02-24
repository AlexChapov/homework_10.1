from src.masks import get_mask_account, get_mask_card_number

"""Получение данных на вход"""
#data_entry = input("Введите данные карты: ")
#getting_the_date = input("Введите дату: ")


def mask_account_card(data_entry: str) -> str:
    """Функция создающая маску для полученных данных карт, счета"""
    if data_entry[:4] == "Счет":
        if len(data_entry) == 25:
            invoice_result = get_mask_account(data_entry)
        else:
            return "Неверный номер счета!"
    else:
        invoice_result = get_mask_card_number(data_entry)
    return invoice_result



def get_date(getting_the_date: str) -> str:
    """Функция создающая дату в формате ДД.ММ.ГГГГ"""
    if len(getting_the_date) == 26:
        conclusion = f"{getting_the_date[8:10]}.{getting_the_date[5:7]}.{getting_the_date[:4]}"
        return conclusion
    else:
        conclusion = "Неправильный формат даты/время"
        return conclusion


"""Функция "print" с целью проверки работы"""
#print(mask_account_card(data_entry))
#print(get_date(getting_the_date))
