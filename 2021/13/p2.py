# https://adventofcode.com/2021/day/13

import operator

def solve(data):
    dots, folds = data

    for fold in folds:
        direction, position = fold
        dots_result = set()

        for x, y in dots:
            if direction:
                if x > position:
                    dots_result.add((-x + position + position, y))
                else:
                    dots_result.add((x, y))
            else:
                if y > position:
                    dots_result.add((x, -y + position + position))
                else:
                    dots_result.add((x, y))

        dots = dots_result

    width = max(dots, key = operator.itemgetter(0))[0] + 1
    height = max(dots, key = operator.itemgetter(1))[1] + 1

    result = []

    for i in range(0, height):
        line = list(' ' * width)

        for x, y in dots:
            if y == i:
                line[x] = '#'

        result.append(''.join(line))

    return '\n'.join(result)

def parse(content):
    chunks = content.split('\n\n')
    
    dots = set(tuple(int(pos) for pos in line.split(',')) for line in chunks[0].split('\n'))
    folds = list()

    for cmd in chunks[1].split('\n'):
        direction = 'x' in cmd
        position = int(cmd[cmd.index('=') + 1:])

        folds.append((direction, position))

    return dots, folds

with open('input.txt') as file:
    data = parse(file.read()[:-1])
    
    print(solve(data))
