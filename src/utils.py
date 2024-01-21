from config import *
import json
from datetime import datetime


def load_json_file():
    with open(OPERATIONS, encoding="utf-8") as file:
        json_data = json.load(file)
    return json_data


def get_executed_operations(values):
    executed_operations = []
    for value in values:
        if value == {}:
            continue
        else:
            executed_operations.append(value)
    return executed_operations


