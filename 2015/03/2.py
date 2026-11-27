# https://adventofcode.com/2015/day/3

from advent import *

mapping = {
    '>': ( 1,  0),
    '<': (-1,  0),
    'v': ( 0,  1),
    '^': ( 0, -1),
}

adder = lambda a, b: (a[0] + b[0], a[1] + b[1])
santa = sq.drop_every(2) | sq.scan(adder, (0, 0)) | fn.to(list)
robot = sq.take_every(2) | sq.scan(adder, (0, 0)) | fn.to(list)
combine = fn.to(list) | cb.train(santa, op.add, robot)

solver = (
    gn.read_file('input.txt')
    | sq.map(mapping)
    | combine
    | sq.distinct()
    | sq.tally()
)

print(solver())
