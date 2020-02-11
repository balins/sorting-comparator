def sort(list_to_sort, caller):
    less = []
    equal_to_pivot = []
    greater = []
    if len(list_to_sort) > 1:
        pivot = list_to_sort[0]
        for element in list_to_sort:
            if element < pivot:
                less.append(element)
            elif element == pivot:
                equal_to_pivot.append(element)
            else:
                greater.append(element)
            caller.ops_counter += 1
        return sort(less, caller) + equal_to_pivot + sort(greater, caller)
    else:
        return list_to_sort
