#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            value_1 = my_list_1[i] if i < len(my_list_1) else 0
            value_2 = my_list_2[i] if i < len(my_list_2) else 0

            if isinstance(value_1, (int, float)) and isinstance(value_2, (int, float)):
                if value_2 == 0:
                    print("division by 0")
                    result.append(0)
                else:
                    result.append(value_1 / value_2)
            else:
                print("wrong type")
                result.append(0)
        except IndexError:
            result.append(0)
            print("out of range")

    return result
