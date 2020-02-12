from util.measurable_sorting import MeasurableSorting


def sort(list_to_sort: list, caller: MeasurableSorting) -> list:
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for index in range(0, len(list_to_sort) - 1):
            if list_to_sort[index] > list_to_sort[index + 1]:
                is_sorted = False
                list_to_sort[index], list_to_sort[index + 1] = list_to_sort[index + 1], list_to_sort[index]
            caller.ops_counter += 1
    return list_to_sort
