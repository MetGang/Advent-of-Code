# https://adventofcode.com/2015/day/1

from advent import *

solver = (
    gn.read_file('input.txt')
    | sq.map({ '(': 1, ')': -1 })
    | sq.sum()
)

print(solver())
