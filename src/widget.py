from masks import get_mask_account, get_mask_card_number


def mask_account_card(input_str: str = "") -> str | None:
    """Эта функция возвращает замаскированный номер счёта или карты
    Строка типа Visa Platinum 7000792289606361 или Счет 73654108430135874305
    должна вернуть Visa Platinum 7000 79** **** 6361 или Счет **4305"""

    # разделяем счет/карту и номер
    product_name: str = ""
    bill_number: int = 0
    while input_str.find(" ") > 0:
        product_name += input_str[: input_str.find(" ") + 1]
        input_str = input_str[input_str.find(" ") + 1:]

    if input_str.isdigit:
        bill_number = int(input_str)

    # Проверяем наличие номера
    if bill_number == 0:
        return None

    # Маскируем счет/карту и выводим результат
    if product_name.lower() == "счет ":
        return f"Счет {get_mask_account(bill_number)}"
    elif len(str(bill_number)) == 16:
        return f"{product_name}{get_mask_card_number(bill_number)}"
    else:
        return None


def get_date(full_date: str = "") -> str | None:
    """Эта функция принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой
    в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""
    if full_date[0:4].isdigit() and full_date[5:7].isdigit() and full_date[8:10].isdigit():
        return f"{full_date[8:10]}.{full_date[5:7]}.{full_date[0:4]}"
