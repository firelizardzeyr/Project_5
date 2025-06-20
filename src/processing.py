""" Этот модуль содержит функции фильтрации и сортировки """


def filter_by_state(proc_list: list, state: str = "EXECUTED") -> list:
    """ Эта функция возвращает новый список словарей, содержащий
    только те словари, у которых ключ state соответствует
    указанному значению."""

    return [my_process for my_process in proc_list if my_process.get("state") == state]


def sort_by_date(proc_list: list, is_reverse: bool = True) -> list:
    """Эта функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна
    возвращать новый список, отсортированный по дате (ключ = date)"""

    return sorted(proc_list, key=lambda my_process: my_process.get("date"), reverse=is_reverse)
