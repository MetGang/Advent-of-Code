# https://adventofcode.com/2018/day/1

def solve(data):
    return sum(data)

with open('input.txt') as file:
    data = [ int(x) for x in file.readlines() ]

    print(solve(data))
