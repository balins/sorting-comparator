from timeit import default_timer as timer
from typing import Tuple


class MeasurableSorting:
    def __init__(self, sorting_algorithm: callable, sorting_name: str = None):
        self.sorting_algorithm = sorting_algorithm
        self.sorting_name = sorting_name
        self.sorting_name = getattr(sorting_algorithm, '__name__') if sorting_name is None else sorting_name
        self.unsorted_list = []

    def set_list(self, input_list: list):
        self.unsorted_list = input_list[:]

    def run_and_get_results(self) -> Tuple[float, int]:
        start = timer()
        ops_counter = self.sorting_algorithm.sort(self.unsorted_list)
        end = timer()
        return end - start, ops_counter
