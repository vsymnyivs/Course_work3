from config import *
import json
from datetime import datetime


def load_json_file():
    """"
    Функция принимает json_file и возвращает словарь
    """
    with open(OPERATIONS, encoding="utf-8") as file:
        json_data = json.load(file)
    return json_data


def get_executed_operations(values):
    """
    Функция фильтрует список оставляя удачновыполненные операции
    """
    executed_operations = []
    for value in values:
        if value == {}:
            continue
        elif value["state"] == "EXECUTED":
            executed_operations.append(value)
    return executed_operations


def sort_date(operations):
    """
    Функция сортировки по дате
    """
    sort_list = sorted(operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"))
    list_operations = sort_list[:5]
    return list_operations


def format_date(date):
    """
    Функция ждя сортировки по дате и форматирования вывода даты
    """
    date_operations = []
    for sorted_date in date:
        sort_operations = datetime.strptime(sorted_date["date"], "%Y-%m-%dT%H:%M:%S.%f")
        formate_date = f"{sort_operations:%d.%m.%Y}"
        date_operations.append(formate_date)
    return date_operations




print(format_date(sort_date(get_executed_operations(load_json_file()))))
