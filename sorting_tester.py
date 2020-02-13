import random
from typing import List, Tuple, TextIO

from util.measurable_sorting import MeasurableSorting
from util.mode import Mode
from util import output_tools
import defaults


def generate_random_list(size: int) -> List[int]:
    print("generating random list of size " + str(size) + "...")

    return random.sample(range(0, size), size)


class SortingTester:
    def __init__(self, size: int = defaults.SAMPLE_SIZE,
                 intrvl: int = defaults.SAMPLE_SIZE,
                 incr_mode: Mode = defaults.MODE,
                 sort_algs: List[MeasurableSorting] = defaults.SORTING_ALGORITHMS):
        self.max_sample_size = size
        self.interval = intrvl
        self.mode = incr_mode
        self.sorting_algorithms = sort_algs

        self.validate_config()

        self.output_folder = None
        self.upper_iter_bound = self.mode.get_total_number_of_iterations(self.interval, self.max_sample_size)

    def run(self):
        f_time, f_ops = self.init_output_files()

        print("\nstarting the test...")
        unsorted_list = generate_random_list(self.max_sample_size)

        for current_sample_size, i in self.mode.get_next_sample_size(self.interval, self.upper_iter_bound):
            output_tools.write_to_files(current_sample_size, f_time, f_ops)

            progress_str = self.get_progress_string(i, current_sample_size)
            print(progress_str, end="")

            for count, sorting in enumerate(self.sorting_algorithms):
                sorting.set_list(unsorted_list[:current_sample_size])
                t, ops = sorting.run_and_get_results()
                f_time.write("," + str(t))
                f_ops.write("," + str(ops))

            output_tools.write_to_files("\n", f_time, f_ops)

            print(len(progress_str) * "\r", end="")

        output_tools.close_output_csv_files(f_time, f_ops)

        print("\n\nthe test has ended\n")

    def get_progress_string(self, num_of_iter: int, current: int) -> str:
        info_str = str(num_of_iter) + " / " + str(self.upper_iter_bound) + \
                   " - testing for " + str(current) + " elements..."

        return info_str

    def validate_config(self):
        if self.max_sample_size is None or self.max_sample_size < 1:
            raise ValueError("Max sample size has to be a positive number.")

        if self.interval is None or self.interval < 1 or self.interval > self.max_sample_size:
            raise ValueError("Interval has to be a positive number smaller than max sample size.")

    def print_config_info(self):
        print("max_sample_size set to value of " + str(self.max_sample_size))
        print("interval set to value of " + str(self.interval))
        print("increment mode is set to " + self.mode.name)

        sort_str = "sorting algorithms are "
        for sorting_algorithm in self.sorting_algorithms:
            sort_str += sorting_algorithm.sorting_name + ", "
        sort_str = sort_str[:-2]

        print(sort_str)

    def generate_charts(self):
        print("generating line charts...")
        self.generate_chart_time()
        self.generate_chart_ops()
        print("done! check " + self.output_folder)

    def generate_chart_time(self):
        with open(self.output_folder + defaults.TIME_CSV_NAME) as file:
            output_tools.generate_chart_from_csv(file, "Time of execution comparison",
                                                 "Sample size", "Time [s]",
                                                 self.output_folder + defaults.TIME_CHART_NAME)

    def generate_chart_ops(self):
        with open(self.output_folder + defaults.OPS_CSV_NAME) as file:
            output_tools.generate_chart_from_csv(file, "Number of basic operations comparison",
                                                 "Sample size", "No. of operations",
                                                 self.output_folder + defaults.OPS_CHART_NAME)

    def init_output_files(self) -> Tuple[TextIO, TextIO]:
        self.output_folder = output_tools.get_output_folder(self.mode.name)
        f_time_name, f_ops_name = output_tools.create_output_csv_files(self.output_folder)
        f_time, f_ops = output_tools.open_output_csv_files(f_time_name, f_ops_name)
        output_tools.write_csv_column_names(self.sorting_algorithms, f_time, f_ops)

        return f_time, f_ops
