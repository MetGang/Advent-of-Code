# https://adventofcode.com/2015/day/3

from advent import *

mapping = {
    '>': ( 1,  0),
    '<': (-1,  0),
    'v': ( 0,  1),
    '^': ( 0, -1),
}

adder = lambda a, b: (a[0] + b[0], a[1] + b[1])
lhs = al.take_every(2) | al.scan(adder, (0, 0)) | list
rhs = al.drop_every(2) | al.scan(adder, (0, 0)) | list
foo = fun.to(list) | cb.train(lhs, op.add, rhs)

solve = gen.read_file('input.txt') | al.map(mapping) | foo | al.distinct() | al.tally()

print(solve())
