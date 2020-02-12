from timeit import default_timer as timer


class MeasurableSorting:
    def __init__(self, sorting_algorithm: callable, sorting_name: str):
        self.sorting_algorithm = sorting_algorithm
        self.sorting_name = sorting_name
        self.results_time = [0.0]
        self.results_ops = [0]
        self.ops_counter = 0
        self.unsorted_list = []

    def set_list(self, input_list: list):
        self.unsorted_list = input_list[:]

    def run_and_save(self):
        start = timer()
        self.sorting_algorithm.sort(self.unsorted_list, self)
        end = timer()
        self.save_results(end - start)

    def save_results(self, t: float):
        self.results_time.append(t)
        self.results_ops.append(self.ops_counter)
        self.ops_counter = 0
