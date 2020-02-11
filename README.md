# sorting comparator

## about
a simple sorting algorithms comparator that can be easily extended by adding new sorting algorithms

tests all of the given sortings algorithms for consecutive sample sizes:

1 * `interval` elements, 2 * `interval` elements, 
3 * `interval` elements, ..., floor(`max_sample_size`/`interval`) elements

then generates graphical line charts and .csv files containing data about algorithms' performance for every sample size

comparison is concerned in terms of time of execution and number of dominant operations

## requirements
- python 3
- matplotlib

## usage
just run the following command in your terminal

`python sorting_tester.py [max_sample_size] [interval]`

defaults:
- max_sample_size = 1000
- interval = 10

## output
A folder containing:
- two .png files containing line charts for respectively time of execution and 
number of dominant operations for each of sorting algorithms and every sample size
- two .csv files containing data about time of operation and
number of dominant operations for each algorithm and every sample size
