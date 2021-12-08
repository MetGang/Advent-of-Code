# https://adventofcode.com/2021/day/8

from itertools import chain

def solve(data):
    mapped = list(map(lambda s: [ len(elem) for elem in s ], data))

    flatten = list(chain(*mapped))

    return flatten.count(2) + flatten.count(3) + flatten.count(4) + flatten.count(7)

with open('input.txt') as file:
    data = [ line[:-1].split(' | ')[1].split(' ') for line in file.readlines() ]

    print(solve(data))
