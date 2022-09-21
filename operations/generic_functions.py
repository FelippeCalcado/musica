from DATABASE import database_control


def list_reorderer(first_item, original_list):
    part_1 = original_list[original_list.index(first_item):]
    part_2 = original_list[:original_list.index(first_item)]
    final_list = part_1 + part_2
    return final_list

def dict_creator(keys, itens):
    dict = {}
    for num, key in enumerate(keys):
        dict[key] = itens[num]
    return dict

def get_data(data:str):
    return database_control.dict_data[data]

