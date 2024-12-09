# https://adventofcode.com/2015/day/3

from advent import *

mapping = {
    '>': ( 1,  0),
    '<': (-1,  0),
    'v': ( 0,  1),
    '^': ( 0, -1),
}

adder = lambda a, b: (a[0] + b[0], a[1] + b[1])

solve = gen.read_file('input.txt') | al.map(mapping) | al.scan(adder, (0, 0)) | al.distinct() | al.tally()

print(solve())
