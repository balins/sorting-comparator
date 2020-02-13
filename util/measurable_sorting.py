from timeit import default_timer as timer


class MeasurableSorting:
    def __init__(self, sorting_algorithm: callable, sorting_name: str = None):
        self.sorting_algorithm = sorting_algorithm
        self.sorting_name = sorting_name
        self.sorting_name = getattr(sorting_algorithm, '__name__') if sorting_name is None else sorting_name
        self.results_time = [0.0]
        self.results_ops = [0]
        self.unsorted_list = []

    def set_list(self, input_list: list):
        self.unsorted_list = input_list[:]

    def run_and_save(self):
        start = timer()
        ops_counter = self.sorting_algorithm.sort(self.unsorted_list)
        end = timer()
        self.save_results(end - start, ops_counter)

    def save_results(self, t: float, ops_counter: int):
        self.results_time.append(t)
        self.results_ops.append(ops_counter)
