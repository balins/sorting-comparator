import sortings
from util.measurable_sorting import MeasurableSorting
from util.mode import Mode

SAMPLE_SIZE = 1000
INTERVAL = 10
MODE = Mode.LINEAR
SORTING_ALGORITHMS = [
    MeasurableSorting(sortings.bubble_sort, "bubble sort"),
    MeasurableSorting(sortings.insertion_sort, "insertion sort"),
    MeasurableSorting(sortings.quicksort, "quicksort")
]
TIME_CSV_NAME = "results-time.csv"
OPS_CSV_NAME = "results-ops.csv"
TIME_CHART_NAME = "chart-time.png"
OPS_CHART_NAME = "chart-ops.png"
