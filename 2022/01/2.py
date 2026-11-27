# https://adventofcode.com/2022/day/1

from advent import *

solver = (
    gn.read_file('input.txt')
    | tt.split_by('\n\n')
    | sq.map(
        tt.split_by('\n')
        | sq.map(int)
        | sq.sum()
    )
    | sq.sort_with(op.gt)
    | sq.take(3)
    | sq.sum()
)

print(solver())
