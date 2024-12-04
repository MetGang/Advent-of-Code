# https://adventofcode.com/2022/day/1

from advent import *

solve = read_file('input.txt') | txt.split_by('\n\n') | map(txt.split_by('\n') | map(int) | sum()) | sort(op.gt) | take(3) | sum()

print(solve())
