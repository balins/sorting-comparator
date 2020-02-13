import os
import random
import time

from util.mode import Mode
from util.output_tools import *
import defaults


def generate_random_list(size: int) -> List[int]:
    print("\ngenerating random list of size " + str(size) + "...")

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

        self.x_axis = [0]
        self.output_folder = "./" + self.mode.name + "_" + time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
        self.upper_iter_bound = self.mode.get_total_number_of_iterations(self.interval, self.max_sample_size)

    def run(self):
        os.mkdir(self.output_folder)
        f_time, f_ops = init_csv_files(self.output_folder, self.sorting_algorithms)

        unsorted_list = generate_random_list(self.max_sample_size)

        print("test is running...\n")

        for current_sample_size, i in self.mode.get_next_sample_size(self.interval, self.upper_iter_bound):
            write_to_files(current_sample_size, f_time, f_ops)
            self.x_axis.append(current_sample_size)

            progress_str = self.get_progress_string(i, current_sample_size)
            print(progress_str, end="")

            for count, sorting in enumerate(self.sorting_algorithms):
                sorting.set_list(unsorted_list[:current_sample_size])
                sorting.run_and_save()
                f_time.write("," + str(sorting.results_time[-1]))
                f_ops.write("," + str(sorting.results_ops[-1]))

            f_time.write("\n")
            f_ops.write("\n")

            print(len(progress_str) * "\r", end="")

        print("\n")
        f_time.close()
        f_ops.close()

        print("the test has ended")

    def get_progress_string(self, num_of_iter: int, current: int) -> str:
        info_str = str(num_of_iter) + " / " + str(self.upper_iter_bound) + \
                   " - testing for " + str(current) + " elements..."

        return info_str

    def generate_charts(self):
        print("generating line charts...")
        generate_charts(self.sorting_algorithms, self.output_folder, self.x_axis)
        print("done! check your working directory")

    def print_config_info(self):
        print("max_sample_size set to value of " + str(self.max_sample_size))
        print("interval set to value of " + str(self.interval))
        print("increment mode is set to " + self.mode.name)

        sort_str = "sorting algorithms are "
        for sorting_algorithm in self.sorting_algorithms:
            sort_str += sorting_algorithm.sorting_name + ", "
        sort_str = sort_str[:-2]

        print(sort_str)

    def validate_config(self):
        if self.max_sample_size < 1:
            raise ValueError("Max sample size has to be a positive number.")

        if self.interval < 1 or self.interval > self.max_sample_size:
            raise ValueError("Interval has to be a positive number smaller than max sample size.")

