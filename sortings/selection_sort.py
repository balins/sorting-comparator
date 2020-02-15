def sort(list_to_sort: list) -> int:
    ops_counter = 0

    for i in range(len(list_to_sort)):
        min_loc = i

        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[min_loc]:
                min_loc = j
            ops_counter += 1

        list_to_sort[min_loc], list_to_sort[i] = list_to_sort[i], list_to_sort[min_loc]

    return ops_counter
