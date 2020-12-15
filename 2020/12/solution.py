# https://adventofcode.com/2020/day/12

def part_1(data):
    x = y = direction = 0
    dirs = [ 0, 1, 2, 3 ]
    for entry in data:
        c = entry['cmd']
        v = entry['value']
        if c == 'F':
            c = [ 'E', 'N', 'W', 'S' ][direction]
        if c == 'N':
            y += v
        elif c == 'S':
            y -= v
        elif c == 'E':
            x += v
        elif c == 'W':
            x -= v
        elif c == 'L':
            direction = dirs[(direction + v // 90) % 4]
        elif c == 'R':
            direction = dirs[(direction - v // 90) % 4]
    return abs(x) + abs(y)

def part_2(data):
    x = y = 0
    wx = 10
    wy = 1
    for entry in data:
        c = entry['cmd']
        v = entry['value']
        if c == 'F':
            x += wx * v
            y += wy * v
        if c == 'N':
            wy += v
        elif c == 'S':
            wy -= v
        elif c == 'E':
            wx += v
        elif c == 'W':
            wx -= v
        elif c == 'L':
            if v == 180:
                wx, wy = -wx, -wy
            elif v == 90:
                wx, wy = -wy, wx
            elif v == 270:
                wx, wy = wy, -wx
        elif c == 'R':
            if v == 180:
                wx, wy = -wx, -wy
            elif v == 90:
                wx, wy = wy, -wx
            elif v == 270:
                wx, wy = -wy, wx
    return abs(x) + abs(y)

with open('input.txt', 'r') as file:
    data = [ { 'cmd': x[:1], 'value': int(x[1:]) } for x in file.read().split('\n')[:-1] ]

    # Part one
    print(part_1(data))

    # Part two
    print(part_2(data))
