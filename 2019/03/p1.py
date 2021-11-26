# https://adventofcode.com/2019/day/3

def get_wire_placement(wire):
    x = 0
    y = 0
    placement = set()

    for opcode, value in wire:
        match opcode:
            case 'L':
                for i in range(x, x - value - 1, -1):
                    placement.add((i, y))
                x -= value
            case 'R':
                for i in range(x, x + value + 1, 1):
                    placement.add((i, y))
                x += value
            case 'D':
                for j in range(y, y - value - 1, -1):
                    placement.add((x, j))
                y -= value
            case 'U':
                for j in range(y, y + value + 1, 1):
                    placement.add((x, j))
                y += value

    return placement


with open('input.txt') as file:
    data = [ [ ( x[:1], int(x[1:]) ) for x in line.split(',') ] for line in file.read().split('\n')[:-1] ]

    f_wire = data[0]
    s_wire = data[1]

    f_placement = get_wire_placement(f_wire)
    s_placement = get_wire_placement(s_wire)

    placements_intersections = f_placement.intersection(s_placement)

    distances = list(map(lambda coord: abs(coord[0]) + abs(coord[1]), placements_intersections))
    
    distances.remove(0)

    print(min(distances))
