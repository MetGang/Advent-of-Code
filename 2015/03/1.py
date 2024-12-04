# https://adventofcode.com/2015/day/3

from advent import *

mapping = {
    '>': ( 1,  0),
    '<': (-1,  0),
    'v': ( 0,  1),
    '^': ( 0, -1),
}

adder = lambda a, b: (a[0] + b[0], a[1] + b[1])

solve = read_file('input.txt') | map(mapping) | scan(adder, (0, 0)) | set | tally()

print(solve())
