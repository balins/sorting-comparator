import csv
import os
import time
from typing import Tuple, TextIO

import matplotlib.pyplot as plt

import defaults


def create_output_folder(mode_name: str):
    folder_name = "." + os.path.sep + mode_name + "_"\
                  + time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()) + os.path.sep
    os.mkdir(folder_name)
    return folder_name


def create_output_csv_files(output_folder: str) -> Tuple[str, str]:
    file_time_name = output_folder + defaults.TIME_CSV_NAME
    file_ops_name = output_folder + defaults.OPS_CSV_NAME

    return file_time_name, file_ops_name


def open_output_csv_files(time_filename: str, ops_filename: str) -> Tuple[TextIO, TextIO]:
    file_time = open(time_filename, "w")
    file_ops = open(ops_filename, "w")

    return file_time, file_ops


def close_output_csv_files(*files: TextIO):
    for file in files:
        file.close()


def write_to_files(text: str, *files: TextIO):
    for file in files:
        file.write(str(text))


def write_csv_column_names(sort_algs: list, *files: TextIO):
    for file in files:
        first_row = "sample size"

        for sorting in sort_algs:
            first_row += "," + sorting.sorting_name

        first_row += "\n"

        file.write(first_row)


def import_from_csv(csv_file: TextIO):
    reader = csv.reader(csv_file, delimiter=",")
    column_names = next(reader)
    name_to_list_of_values = {col: list() for col in column_names}

    for row in reader:
        for name in column_names:
            first = float(row.pop(0))
            name_to_list_of_values[name].append(first)

    return name_to_list_of_values


def generate_chart_from_csv(csv_file: TextIO, title: str, x_label: str, y_label: str, output_filename: str):
    data = import_from_csv(csv_file)
    x_axis = [0, *data.pop("sample size")]

    for sorting_name in data:
        plt.plot(x_axis, [0, *data[sorting_name]], label=sorting_name)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.savefig(output_filename, dpi=150)
    plt.clf()
