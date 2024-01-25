from config import *
import json
from datetime import datetime
import re


def load_json_file():
    """"
    Функция принимает json_file и возвращает словарь
    """
    with open(OPERATIONS, encoding="utf-8") as file:
        json_data = json.load(file)
    return json_data


def get_executed_operations(values):
    """
    Функция фильтрует список оставляя одобренные операции
    """
    executed_operations = []
    for value in values:
        if value == {}:
            continue
        elif value["state"] == "EXECUTED":
            executed_operations.append(value)
    return executed_operations


def sort_operations(operations):
    """
    Функция вывода пяти последних успешных операций
    """
    sort_list = sorted(operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    list_operations = sort_list[:5]
    return list_operations


def format_date(date):
    """
    Функция для сортировки по дате и форматирования вывода даты
    """
    date_operations = []
    for sorted_date in date:
        sort_operations = datetime.strptime(sorted_date["date"], "%Y-%m-%dT%H:%M:%S.%f")
        format_date = f"{sort_operations:%d.%m.%Y}"
        date_operations.append(format_date)
    return date_operations


def mask_card_number(card_numbers):
    """
    Функция маскировки номера карты
    """
    card_number_operations = []
    for card_number in card_numbers:
        if card_number["description"] == "Открытие вклада":
            card_number["from"] = f"Счет пользователя: {card_number['to'][5:]}"
        mask_card = card_number["from"].split()
        mask_card_copy = mask_card.copy()
        del mask_card_copy[-1]
        card_mask = re.findall("....", mask_card[-1])
        number_card = card_mask[0], card_mask[1][0:2] + "**", card_mask[2].replace(card_mask[2], "****"), card_mask[3:]
        mask_number = " ".join(number_card[3])
        card_number_operations.append(f"{' '.join(mask_card_copy)} {' '.join(list(number_card[0:3]))} {mask_number}")
    return card_number_operations


def mask_amount_number(amount_numbers):
    """
    Функция маскировки счёта
    """
    mask_amount_list = []
    for amount_number in amount_numbers:
        format_to_check = re.findall("....", amount_number["to"])
        check_to_format = format_to_check[4:]
        number_amount = check_to_format[0].replace(check_to_format[0], "**"), check_to_format[1]
        amount_mask = "".join(list(number_amount))
        mask_amount_list.append(amount_mask)
    return mask_amount_list