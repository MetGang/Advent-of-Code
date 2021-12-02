# https://adventofcode.com/2021/day/2

def solve(data):
    position = 0
    depth = 0

    for ( cmd, v ) in data:
        match cmd:
            case 'forward':
                position += v
            case 'up':
                depth -= v
            case 'down':
                depth += v
    
    return position * depth

def parse(line):
    splitted = line.split(' ')

    return ( splitted[0], int(splitted[1]) )

with open('input.txt') as file:
    data = [ parse(x[:-1]) for x in file.readlines() ]

    print(solve(data))
