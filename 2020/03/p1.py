# https://adventofcode.com/2020/day/3

def traverse(data, slope_x, slope_y):
    count = 0
    x = 0
    y = 0

    while y < len(data):
        count += data[y][x % len(data[y])] == '#'
        x += slope_x
        y += slope_y

    return count

def solve(data):
    return traverse(data, 3, 1)

def parse(content):
    return content.split('\n')

with open('input.txt') as file:
    data = parse(file.read().strip())

    print(solve(data))
