# sorting comparator

## about
a simple sorting algorithms comparator that can be easily extended by adding new sorting algorithms

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


then generates graphical line charts and .csv files containing data about algorithms' performance for every sample size

comparison is concerned in terms of time of execution and number of dominant operations

## requirements
- python 3
- matplotlib

## usage
just run the following command in your terminal

`python run.py [max_sample_size] [interval] [mode: (lin, poly, exp)]`

defaults:
- max_sample_size = 1000
- interval = 10
- mode = lin

## output
A folder containing:
- two .png files containing line charts for respectively time of execution and
number of dominant operations for each of sorting algorithms and every sample size
- two .csv files containing data about time of operation and
number of dominant operations for each algorithm and every sample size
