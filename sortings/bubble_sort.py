def sort(list_to_sort: list) -> int:
    ops_counter = 0

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for index in range(0, len(list_to_sort) - 1):
            if list_to_sort[index] > list_to_sort[index + 1]:
                is_sorted = False
                list_to_sort[index], list_to_sort[index + 1] = list_to_sort[index + 1], list_to_sort[index]
            ops_counter += 1

    return ops_counter
