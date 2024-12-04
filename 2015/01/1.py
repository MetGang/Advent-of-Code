# https://adventofcode.com/2015/day/1

from advent import *

solve = read_file('input.txt') | map({ '(': 1, ')': -1 }) | sum()

print(solve())
