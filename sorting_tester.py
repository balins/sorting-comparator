import math
import os
import sys
import random
import time

import sortings
from sorting_tools import *


class SortingTester:
    DEFAULT_SAMPLE_SIZE = 1000
    DEFAULT_INTERVAL = 10
    DEFAULT_SORTING_ALGORITHMS = [
        Sorting(sortings.bubble_sort, "bubble sort"),
        Sorting(sortings.insertion_sort, "insertion sort"),
        Sorting(sortings.quicksort, "quicksort")
    ]

    def __init__(self, size, intrvl, sort_algs):
        self.max_sample_size = size
        self.interval = intrvl
        self.sorting_algorithms = sort_algs
        self.x_axis = [0]
        self.t_started = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())

        if max_sample_size is None or max_sample_size < 1:
            self.max_sample_size = self.DEFAULT_SAMPLE_SIZE

        if interval is None or interval < 1 or interval > max_sample_size:
            self.interval = self.DEFAULT_INTERVAL

        if sorting_algorithms is None:
            self.sorting_algorithms = self.DEFAULT_SORTING_ALGORITHMS

    def run(self):
        os.mkdir("./" + self.t_started)
        f_time, f_ops = self.init_csv_files()

        current_sample_size = self.interval
        unsorted_list = random.sample(range(0, self.max_sample_size), self.max_sample_size)

        print("Test is running...")

        while current_sample_size <= self.max_sample_size:
            f_time.write(str(current_sample_size))
            f_ops.write(str(current_sample_size))
            self.x_axis.append(current_sample_size)

            info_str = str(math.floor(current_sample_size / interval)) + \
                       " / " + str(math.floor(max_sample_size / interval)) + "..."
            print(info_str, end="")

            for count, sorting in enumerate(self.sorting_algorithms):
                sorting.set_list(unsorted_list[:current_sample_size])
                sorting.run_and_save_results()
                f_time.write("," + str(sorting.results_time[-1]))
                f_ops.write("," + str(sorting.results_ops[-1]))

            f_time.write("\n")
            f_ops.write("\n")
            current_sample_size += self.interval

            print(len(info_str) * "\r", end="")

    def generate_charts(self):
        print("Generating line charts...")
        generate_charts(self.sorting_algorithms, self.t_started, self.x_axis)
        print("Done! Check your working directory.")

    def init_csv_files(self):
        filename1 = self.t_started + "/results-time"
        filename2 = self.t_started + "/results-ops"
        file1 = open(filename1 + ".csv", "w")
        file2 = open(filename2 + ".csv", "w")
        self.write_first_csv_row(file1)
        self.write_first_csv_row(file2)

        return file1, file2

    def write_first_csv_row(self, file):
        first_row = "sample size"

        for sorting in self.sorting_algorithms:
            first_row += "," + sorting.sorting_name

        first_row += "\n"

        file.write(first_row)


if __name__ == "__main__":
    max_sample_size, interval, sorting_algorithms = None, None, None
    if len(sys.argv) > 1:
        max_sample_size = int(sys.argv[1])
        if len(sys.argv) > 2:
            interval = int(sys.argv[2])

    st = SortingTester(max_sample_size, interval, sorting_algorithms)
    print("max_sample_size set to value of " + str(st.max_sample_size))
    print("interval set to value of " + str(st.interval))

    sort_str = "sorting algorithms are "
    for sorting_algorithm in st.sorting_algorithms:
        sort_str += sorting_algorithm.sorting_name + ", "
    sort_str = sort_str[:-2]

    print(sort_str)

    st.run()
    st.generate_charts()
