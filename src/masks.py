def get_mask_card_number(card_number: str) -> str:
    """Функция создающая маску для номера карты"""
    mask_card_number = f"{card_number[:-12]} {card_number [-12:-10]}** **** {card_number[-4:]}"

    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция создающая маску для номера счета"""
    if len(account_number) == 25:
        mask_account_number = f"{account_number[:-21]} **{account_number[-4:]}"
        return mask_account_number
    else:
        return "Неправильно введет счет"
