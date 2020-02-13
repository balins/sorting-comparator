import math
from enum import Enum
from typing import Tuple


class Mode(Enum):
    LINEAR = "lin"
    POLYNOMIAL = "poly"
    EXPONENTIAL = "exp"

    def get_total_number_of_iterations(self, interval: int, max_sample_size: int) -> int:
        if self == Mode.LINEAR:
            return math.floor(max_sample_size / interval)
        elif self == Mode.POLYNOMIAL:
            return math.floor(math.log(max_sample_size, interval))
        else:
            return math.floor(math.log(max_sample_size, 2 ** interval))

    def get_next_sample_size(self, interval: int, max_iter: int) -> Tuple[int, int]:
        i = 1

        while i <= max_iter:
            if self == Mode.LINEAR:
                res = interval * i
            elif self == Mode.POLYNOMIAL:
                res = interval ** i
            else:
                res = 2 ** (i * interval)
            yield res, i
            i += 1
