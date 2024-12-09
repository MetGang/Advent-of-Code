# https://adventofcode.com/2022/day/1

from advent import *

solve = gen.read_file('input.txt') | txt.split_by('\n\n') | al.map(txt.split_by('\n') | al.map(int) | al.sum()) | al.sort(op.gt) | al.take(3) | al.sum()

print(solve())
