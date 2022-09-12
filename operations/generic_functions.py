def reordered_list(first_item, original_list):
    part_1 = original_list[original_list.index(first_item):]
    part_2 = original_list[:original_list.index(first_item)]
    final_list = part_1 + part_2
    return final_list


# TESTES

def main():
    l1 = [1,2,3,4,5]
    fi = 5
    new_list = reordered_list(fi, l1)
    return new_list

if __name__ == '__main__':
    nl = main()
    print(nl)