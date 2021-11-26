# https://adventofcode.com/2018/day/1

from functools import reduce

def solve(data):
    return reduce(lambda a, b: a + b, data)

with open('input.txt') as file:
    data = [ int(x) for x in file.readlines() ]

    print(solve(data))
