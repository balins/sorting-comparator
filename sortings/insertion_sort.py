def sort(list_to_sort: list) -> int:
    ops_counter = 0

    for index in range(1, len(list_to_sort)):
        current = list_to_sort[index]

        while index > 0 and list_to_sort[index - 1] > current:
            list_to_sort[index] = list_to_sort[index - 1]
            index -= 1
            ops_counter += 1
        ops_counter += 1

        list_to_sort[index] = current

    return ops_counter
