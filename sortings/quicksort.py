ops_counter = 0


def sort(list_to_sort: list) -> int:
    quicksort(list_to_sort)
    return ops_counter


def quicksort(list_to_sort: list) -> list:
    global ops_counter
    less = []
    equal_to_pivot = []
    greater = []
    if len(list_to_sort) > 1:
        pivot = list_to_sort[0]
        for element in list_to_sort:
            if element < pivot:
                less.append(element)
            elif element > pivot:
                greater.append(element)
            else:
                equal_to_pivot.append(element)
            ops_counter += 1
        return quicksort(less) + equal_to_pivot + quicksort(greater)
    else:
        return list_to_sort
