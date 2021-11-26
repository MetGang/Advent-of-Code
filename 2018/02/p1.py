# https://adventofcode.com/2018/day/2

from collections import Counter

def solve(data):
    twos = 0
    threes = 0

    for word in data:
        counted_values = Counter(word).values()
        twos += 2 in counted_values
        threes += 3 in counted_values

    return twos * threes

with open('input.txt') as file:
    data = [ x for x in file.readlines() ]

    print(solve(data))
