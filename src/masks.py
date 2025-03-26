import logging
import os

log_dir = "../logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


logger = logging.getLogger("masks")
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция создающая маску для номера карты"""
    if len(card_number) == 16:
        mask_card_number = f"{card_number[:-12]} {card_number [-12:-10]}** **** {card_number[-4:]}"
        logger.info(f"Задаем формат маски для номера счета {card_number}")
        return mask_card_number
    else:
        logger.error("Ошибка. Проверьте длину номера карты. Он должен содержать 16 символов")
        return "Неправильно введен номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция создающая маску для номера счета"""
    if len(account_number) == 25:
        mask_account_number = f"{account_number[:-21]} **{account_number[-4:]}"
        logger.info(f"Задаем формат маски для номера счета {account_number}")
        return mask_account_number
    else:
        logger.error("Ошибка. Проверьте длину счета. Он должен содержать 20 символов")
        return "Неправильно введен счет"


# Проверка
# print(get_mask_card_number("1596837868705199"))
# print(get_mask_account("Счет 64686473678894779589"))
# print(get_mask_card_number("1596837868"))
# print(get_mask_account("Счет 646864736788947"))
