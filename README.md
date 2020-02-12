# sorting comparator

## about
a simple sorting algorithms comparator that can be easily extended by new ones

tests all of the given sortings algorithms for consecutive sample sizes:

- if mode is set to `lin` (linear):

    1 * `interval` elements, 2 * `interval` elements,
    3 * `interval` elements, ..., floor(`max_sample_size`/`interval`) elements

- if mode is set to `poly` (polynomial):

    `interval`^1 elements, `interval`^2 elements,
    `interval`^3 elements, ..., floor(log(`max_sample_size`, base=`interval`)) elements

- if mode is set to `exp` (exponential):

    2^(1 * `interval`) elements, 2^(2 * `interval`) elements,
    2^(3 * `interval`) elements, ..., floor(log(`max_sample_size`, base=`2 ^ interval`) elements


then generates line charts and .csv files containing data about algorithms' performance for every sample size

comparison is concerned in terms of time of execution and number of dominant operations

repo contains also some sample data for each of modes and default sorting algorithms

## requirements
- python 3.5+
- matplotlib

## usage from command line
just run the following command in your terminal

`python run.py [max_sample_size] [interval] [mode (lin, poly, exp)]`

defaults:
- max_sample_size = 1000
- interval = 10
- mode = lin

sorting algorithms used by default are bubble sort, insertion sort and quicksort

defaults can be changed in `defaults.py` module

## usage in external modules
create `SortingTester` instance with custom parameters or pass `None`s to use defaults

then just call its run() and/or other methods

## output
A folder containing:
- two .png files containing line charts for respectively time of execution and
number of dominant operations for each of sorting algorithms and every sample size
- two .csv files containing data about time of operation and
number of dominant operations for each algorithm and every sample size

## extending by custom sortings
custom sorting is a module containing a function implementing interface `sort(list_to_sort: list, caller: MeasurableSorting) -> list`

custom sorting should sort and return input list and increment caller's field `ops_counter` for every performed dominant operation

custom sorting should be placed in `sorting` directory and the directory's `__init__.py` should be updated to export new sorting module