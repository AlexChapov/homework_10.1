def get_mask_card_number(card_number: str) -> str:
    """Функция создающая маску для номера карты"""
    return f"{card_number[:-12]} {card_number [-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция создающая маску для номера счета"""
    return f"{account_number[:-21]} **{account_number[-4:]}"
