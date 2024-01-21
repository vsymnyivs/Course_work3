from config import *
import json
from datetime import datetime


def load_json_file():
    with open(OPERATIONS, encoding="utf-8") as file:
        json_data = json.load(file)
    return json_data


