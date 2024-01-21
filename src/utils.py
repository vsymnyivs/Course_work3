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
        else:
            executed_operations.append(value)
    return executed_operations


def sort_operations(data):
    """
    Функция ждя сортировки по дате и форматирования вывода даты
    """
    date_operations = []
    for sort_date in data:
        sorted_operations = datetime.strptime(sort_date["date"], "%Y-%m-%dT%H:%M:%S.%f")
        formate_date = f"{sorted_operations:%d.%m.%Y}"
        date_operations.append(formate_date)
    return date_operations


def slide_operations():
    pass


# print(sort_operations(get_executed_operations(load_json_file())))
