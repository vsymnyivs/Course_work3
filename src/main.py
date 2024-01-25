from src.utils import *

work_file = get_executed_operations(load_json_file())
operations_list = sort_operations(work_file)
date = format_date(operations_list)
mask_card = mask_card_number(operations_list)
mask_amount = mask_amount_number(operations_list)


print(mask_card)
for operation in range(len(operations_list)):
  print(f"{date[operation]} {operations_list[operation]['description']}"
        f"{mask_card[operation]} => Счет: {mask_amount[operation]}"
        f"{operations_list[operation] ['operationAmount']['amount']} {operations_list[operation] ['operationAmount']['currency']['name']}\n")

