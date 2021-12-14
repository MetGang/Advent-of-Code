# https://adventofcode.com/2021/day/13

def solve(data):
    dots, direction, position = data
    
    dots_result = set()

    if direction:
        for x, y in dots:
            if x > position:
                dots_result.add((-x + position + position, y))
            else:
                dots_result.add((x, y))
    else:
        for x, y in dots:
            if y > position:
                dots_result.add((x, -y + position + position))
            else:
                dots_result.add((x, y))

    return len(dots_result)

def parse(content):
    chunks = content.split('\n\n')
    
    dots = set(tuple(int(pos) for pos in line.split(',')) for line in chunks[0].split('\n'))

    cmd = chunks[1].split('\n')[0]
    direction = 'x' in cmd
    position = int(cmd[cmd.index('=') + 1:])

    return dots, direction, position

with open('input.txt') as file:
    data = parse(file.read()[:-1])
    
    print(solve(data))
