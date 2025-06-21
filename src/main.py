from processing import filter_by_state
from processing import sort_by_date


# Данные для проверки функций filter_by_state и sort_by_date модуля processing
processing_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                   ]

for proc in filter_by_state(processing_list):
    print(proc, end="\n")
print("\n")

for proc in filter_by_state(processing_list, "CANCELED"):
    print(proc, end="\n")
print("\n")

for proc in sort_by_date(processing_list):
    print(proc, end="\n")
print("\n")

for proc in sort_by_date(processing_list, False):
    print(proc, end="\n")
print("\n")


# import masks
#
# import widget
#
# print(masks.get_mask_account(64686473678894779589))
#
# print(masks.get_mask_card_number(7158300734726758))
#
# my_bills = ["Maestro 1596837868705199", "Счет 64686473678894779589",
#            "MasterCard 7158300734726758", "Счет 35383033474447895560",
#            "Visa Classic 6831982476737658", "Visa Platinum 8990922113665229",
#            "Visa Gold 5999414228426353", "Счет 73654108430135874305"]
#
# for bill in my_bills:
#     print(widget.mask_account_card(bill))
#
#
# print(widget.get_date("jjsdjd"))
# print(widget.get_date("2024-03-11T02:26:18.671407"))
