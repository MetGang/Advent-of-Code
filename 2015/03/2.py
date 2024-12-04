# https://adventofcode.com/2015/day/3

from advent import *

mapping = {
    '>': ( 1,  0),
    '<': (-1,  0),
    'v': ( 0,  1),
    '^': ( 0, -1),
}

adder = lambda a, b: (a[0] + b[0], a[1] + b[1])

foo = train(take_every(2, 0) | scan(adder, (0, 0)) | list, op.add, take_every(2, 1) | scan(adder, (0, 0)) | list)

solve = read_file('input.txt') | map(mapping) | list | foo | set | tally()

print(solve())
