#!/usr/bin/env python3

"""https://adventofcode.com/2019/day/1
"""

import itertools
import math
import typing


total: int = sum((it2 := itertools.tee(map(fuel := lambda mass: math.floor(int(mass) / 3) - 2,
                                           open('input.txt'))))[0])
assert total == 3305115
print(total)


def iter_fuel(val: int) -> typing.Generator[int, None, None]:
    while val > 0:
        yield val
        val = fuel(val)


total_fuel: int = sum(
                      sum(iter_fuel(f)) for f in it2[1]
                      )
assert total_fuel == 4954799
print(total_fuel)
