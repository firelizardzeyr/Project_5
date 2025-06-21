""" Этот модуль содержит функции для работы с новыми возможностями приложения"""

from masks import get_mask_account, get_mask_card_number


def mask_account_card(input_str: str = "") -> str | None:
    """Эта функция возвращает замаскированный номер счёта или карты
    Строка типа Visa Platinum 7000792289606361 или Счет 73654108430135874305
    должна вернуть Visa Platinum 7000 79** **** 6361 или Счет **4305"""

    # разделяем счет/карту и номер
    bill_number = input_str[::-1][: input_str[::-1].index(" ")][::-1]
    product_name = input_str[::-1][input_str[::-1].index(" "):][::-1]

    # Маскируем счет/карту и выводим результат
    if product_name.lower() == "счет ":
        return f"Счет {get_mask_account(int(bill_number))}"
    elif len(bill_number) == 16:
        return f"{product_name}{get_mask_card_number(int(bill_number))}"
    else:
        return None


def get_date(full_date: str = "") -> str | None:
    """Эта функция принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой
    в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""
    if full_date[0:4].isdigit() and full_date[5:7].isdigit() and full_date[8:10].isdigit():
        return f"{full_date[8:10]}.{full_date[5:7]}.{full_date[0:4]}"
    else:
        return None
