# https://adventofcode.com/2020/day/1

from advent import *

solver = (
    gn.read_file('input.txt')
    | tt.split_by('\n')
    | sq.map(int)
    | fn.to(list) | cb.train(sq.map(op.sub.left(2020)), op.intersection, fn.identity())
    | sq.product()
)

print(solver())
