"""Этот модуль содержит функции, возвращающие маски номеров счета
и карты"""


def get_mask_card_number(card_number: int) -> str:
    """Принимает номер карты int, выдаёт замаскированный str вида
    ХХХХ ХХ** **** ХХХХ"""

    new_mask: str = (
        f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** \
{str(card_number)[-4:]}"
    )

    return new_mask


def get_mask_account(account_number: int) -> str:
    """Принимает номер аккаунта int, выдаёт замаскированный" str вида
    **ХХХХ"""

    new_mask: str = f"**{str(account_number)[-4:]}"

    return new_mask
