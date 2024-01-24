from src.utils import *

work_file = get_executed_operations(load_json_file())
operations_list = sort_operartions(work_file)
operations = format_date(operations_list)
mask_card = mask_card_number(operations_list)
mask_amount = mask_amount_number(operations_list)


for operation in operations_list:
    print(f"{operations(operation['date'])} {operation['description']}")
