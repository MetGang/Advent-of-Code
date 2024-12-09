# https://adventofcode.com/2015/day/1

from advent import *

solve = gen.read_file('input.txt') | al.map({ '(': 1, ')': -1 }) | al.sum()

print(solve())
