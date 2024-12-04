# https://adventofcode.com/2015/day/1

from advent import *

solve = read_file('input.txt') | map({ '(': 1, ')': -1 }) | scan(op.add) | index(-1) | (op.add >> 1)

print(solve())
