import math
import os
import random
import time
from typing import Iterator

from util.mode import Mode
from util.output_tools import *
import defaults


def generate_random_list(size: int) -> List[int]:
    print("\ngenerating random list of size " + str(size) + "...")

    return random.sample(range(0, size), size)


def get_number_of_iterations(mode: Mode, interval: int, max_sample_size: int) -> int:
    if mode == Mode.LINEAR:
        return math.floor(max_sample_size / interval)
    elif mode == Mode.POLYNOMIAL:
        return math.floor(math.log(max_sample_size, interval))
    else:
        return math.floor(math.log(max_sample_size, 2 ** interval))


class SortingTester:
    def __init__(self, size: int, intrvl: int, incr_mode: Mode, sort_algs: List[MeasurableSorting]):
        self.max_sample_size = size
        self.interval = intrvl
        self.mode = incr_mode
        self.sorting_algorithms = sort_algs
        self.x_axis = [0]
        self.output_folder = "./" + self.mode.name + "_" + time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())

        self.fill_missing_data()

        self.upper_iter_bound = get_number_of_iterations(self.mode, self.interval, self.max_sample_size)

    def run(self):
        os.mkdir(self.output_folder)
        f_time, f_ops = init_csv_files(self.output_folder, self.sorting_algorithms)

        unsorted_list = generate_random_list(self.max_sample_size)

        print("test is running...\n")

        for current_sample_size, i in self.get_next_sample_size():
            write_to_files(current_sample_size, f_time, f_ops)
            self.x_axis.append(current_sample_size)

            info_str = self.get_info_string(i, current_sample_size)
            print(info_str, end="")

            for count, sorting in enumerate(self.sorting_algorithms):
                sorting.set_list(unsorted_list[:current_sample_size])
                sorting.run_and_save()
                f_time.write("," + str(sorting.results_time[-1]))
                f_ops.write("," + str(sorting.results_ops[-1]))

            f_time.write("\n")
            f_ops.write("\n")

            print(len(info_str) * "\r", end="")

        print("\n")
        f_time.close()
        f_ops.close()

        print("the test has ended")

    def get_next_sample_size(self) -> Iterator[int, int]:
        i = 1

        while i <= self.upper_iter_bound:
            if self.mode == Mode.LINEAR:
                res = self.interval * i
            elif self.mode == Mode.POLYNOMIAL:
                res = self.interval ** i
            else:
                res = 2 ** (i * self.interval)
            yield res, i
            i += 1

    def get_info_string(self, num_of_iter: int, current: int) -> str:
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

    def fill_missing_data(self):
        if self.max_sample_size is None or self.max_sample_size < 1:
            self.max_sample_size = defaults.SAMPLE_SIZE

        if self.interval is None or self.interval < 1 or self.interval > self.max_sample_size:
            self.interval = defaults.INTERVAL

        if self.sorting_algorithms is None or len(self.sorting_algorithms) == 0:
            self.sorting_algorithms = defaults.SORTING_ALGORITHMS

