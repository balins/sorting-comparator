import matplotlib.pyplot as plt


def write_to_files(text, *files):
    for file in files:
        file.write(str(text))


def init_csv_files(output_folder: str, sort_algs: list) -> tuple:
    file_time_name = output_folder + "/results-time"
    file_ops_name = output_folder + "/results-ops"
    file_time = open(file_time_name + ".csv", "w")
    file_ops = open(file_ops_name + ".csv", "w")
    write_first_csv_row(sort_algs, file_time, file_ops)

    return file_time, file_ops


def write_first_csv_row(sort_algs: list, *files):
    for file in files:
        first_row = "sample size"

        for sorting in sort_algs:
            first_row += "," + sorting.sorting_name

        first_row += "\n"

        file.write(first_row)


def generate_charts(sortings: list, output_folder: str, x_axis: list):
    for sorting in sortings:
        plt.plot(x_axis, sorting.results_time, label=sorting.sorting_name)

    plt.title('Operating time comparison')
    plt.ylabel('Time [s]')
    plt.xlabel('Sample size')
    plt.legend()
    plt.savefig(output_folder + '/chart-time.png', dpi=150)
    plt.clf()

    for sorting in sortings:
        plt.plot(x_axis, sorting.results_ops, label=sorting.sorting_name)

    plt.title("Dominant operations number comparison")
    plt.ylabel('No. of operations')
    plt.xlabel('Sample size')
    plt.legend()
    plt.savefig(output_folder + '/chart-ops.png', dpi=150)
