# https://adventofcode.com/2021/day/2

def solve(data):
    commands = data

    position = 0
    depth = 0
    aim = 0

    for cmd, value in commands:
        match cmd:
            case 'forward':
                position += value
                depth += value * aim
            case 'up':
                aim -= value
            case 'down':
                aim += value
    
    return position * depth

def parse(content):
    mapper = lambda x: (x[0], int(x[1]))

    return [ mapper(line.split(' ')) for line in content.split('\n') ]

with open('input.txt') as file:
    print(solve(parse(file.read())))
