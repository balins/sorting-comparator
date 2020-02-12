import sys

from util import defaults
from util.mode import Mode
from util.sorting_tester import SortingTester

if __name__ == "__main__":
    max_sample_size, interval, mode, sorting_algorithms = None, None, None, None
    if len(sys.argv) > 1:
        max_sample_size = int(sys.argv[1])

    if len(sys.argv) > 2:
        interval = int(sys.argv[2])

    try:
        mode = Mode(str(sys.argv[3]))
    except (IndexError, ValueError) as e:
        mode = defaults.MODE

    st = SortingTester(max_sample_size, interval, mode, list())

    st.print_config_info()
    st.run()
    st.generate_charts()
