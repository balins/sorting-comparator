from util.measurable_sorting import MeasurableSorting


def sort(list_to_sort: list, caller: MeasurableSorting) -> list:
    for index in range(1, len(list_to_sort)):
        current = list_to_sort[index]
        while index > 0 and list_to_sort[index - 1] > current:
            list_to_sort[index] = list_to_sort[index - 1]
            index -= 1
            caller.ops_counter += 1
        list_to_sort[index] = current
    return list_to_sort
