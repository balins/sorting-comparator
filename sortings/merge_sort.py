ops_counter = 0


def sort(list_to_sort: list) -> int:
    merge_sort(list_to_sort)
    return ops_counter


def merge_sort(list_to_sort: list) -> list:
    if len(list_to_sort) < 2:
        return list_to_sort[:]
    else:
        middle = int(len(list_to_sort) / 2)
        left = merge_sort(list_to_sort[:middle])
        right = merge_sort(list_to_sort[middle:])
        return merge(left, right)


def merge(left: list, right: list) -> list:
    global ops_counter

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        ops_counter += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
