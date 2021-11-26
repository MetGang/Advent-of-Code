# https://adventofcode.com/2018/day/3

def solve(data):
    fabric = dict()

    for claim in data:
        index = claim[0]
        area = claim[1]

        for i in range(index[0], index[0] + area[0]):
            for j in range(index[1], index[1] + area[1]):
                cell = fabric.get((i, j), 0)
                fabric[(i, j)] = cell + 1

    fabric_values = list(fabric.values())

    return len(fabric_values) - fabric_values.count(1)

def parse(line):
    splitted = line.split(' ')

    index = tuple(int(x) for x in splitted[2][:-1].split(','))
    area = tuple(int(x) for x in splitted[3].split('x'))

    return ( index, area )

with open('input.txt') as file:
    data = [ parse(x[:-1]) for x in file.readlines() ]

    print(solve(data))
