# https://adventofcode.com/2020/day/3

def traverse(slope_x, slope_y):
    data = [ line[:-1] for line in open('input.txt') ]
    count = 0
    x = 0
    y = 0

    while y < len(data):
        count += data[y][x % len(data[y])] == '#'
        x += slope_x
        y += slope_y
    
    return count

# Part one
print(traverse(3, 1))

# Part two
print(traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2))
