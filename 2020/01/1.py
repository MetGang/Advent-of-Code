# https://adventofcode.com/2020/day/1

from advent import *

intersection = lambda a, b: set(a) & set(b)

solver = (
    gn.read_file('input.txt')
    | tt.split_by('\n')
    | sq.map(int)
    | fn.to(list) | cb.train(sq.map(op.sub.left(2020)), intersection, fn.identity())
    | sq.product()
)

print(solver())
