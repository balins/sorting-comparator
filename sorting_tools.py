from timeit import default_timer as timer
import matplotlib.pyplot as plt


class Sorting:
    def __init__(self, sorting_algorithm, sorting_name):
        self.sorting_algorithm = sorting_algorithm
        self.sorting_name = sorting_name
        self.results_time = [0.0]
        self.results_ops = [0]
        self.ops_counter = 0
        self.unsorted_list = []

    def set_list(self, input_list):
        self.unsorted_list = input_list[:]

    def run_sort(self):
        self.sorting_algorithm.sort(self.unsorted_list, self)

    def run_and_save_results(self):
        start = timer()
        self.run_sort()
        end = timer()
        self.results_time.append(end - start)
        self.results_ops.append(self.ops_counter)
        self.ops_counter = 0


def generate_charts(sortings, t_started, x_axis):
    for sorting in sortings:
        plt.plot(x_axis, sorting.results_time, label=sorting.sorting_name)

    plt.title('Operating time comparison')
    plt.ylabel('Time [s]')
    plt.xlabel('Sample size')
    plt.legend()
    plt.savefig("./" + t_started + '/-chart-time.png', dpi=150)
    plt.clf()

    for sorting in sortings:
        plt.plot(x_axis, sorting.results_ops, label=sorting.sorting_name)

    plt.title("Dominant operations number comparison")
    plt.ylabel('No. of operations')
    plt.xlabel('Sample size')
    plt.legend()
    plt.savefig("./" + t_started + '/chart-ops.png', dpi=150)
