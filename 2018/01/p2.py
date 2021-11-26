# https://adventofcode.com/2018/day/1

from functools import reduce

def solve(data):
    occurrences = dict()
    fr = 0

    while True:
        for num in data:
            fr += num
            occ = occurrences.get(fr, 0)

            if occ == 1:
                return fr
            else:
                occurrences[fr] = 1


with open('input.txt') as file:
    data = [ int(x) for x in file.readlines() ]

    print(solve(data))
