# https://adventofcode.com/2021/day/16

from math import prod

def decode_literal(stream):
    value = ''
    index = 0

    while stream[index] == '1':
        value += stream[index + 1:index + 5]
        index += 5
    
    value += stream[index + 1:index + 5]
    index += 5

    return int(value, 2), index

def decode_packet(tree, stream, index):
    version = int(stream[index:index + 3], 2)
    type_id = int(stream[index + 3:index + 6], 2)

    tree['version'] = version
    tree['type_id'] = type_id
    tree['nodes'] = []

    if type_id == 4:
        value, offset = decode_literal(stream[index + 6:])
        tree['value'] = value

        return index + offset + 6
    else:
        len_type_id = int(stream[index + 6])

        if len_type_id == 0:
            sub_length = int(stream[index + 6: index + 22], 2)
            offset = index + 22

            while offset < index + 22 + sub_length:
                tree['nodes'].append(dict())
                offset = decode_packet(tree['nodes'][-1], stream, offset)
            
            return offset
        else:
            sub_count = int(stream[index + 7:index + 18], 2)
            offset = index + 18

            for _ in range(0, sub_count):
                tree['nodes'].append(dict())
                offset = decode_packet(tree['nodes'][-1], stream, offset)
            
            return offset

def obtain_values(tree):
    match tree['type_id']:
        case 0:
            return sum(map(obtain_values, tree['nodes']))
        case 1:
            return prod(map(obtain_values, tree['nodes']))
        case 2:
            return min(map(obtain_values, tree['nodes']))
        case 3:
            return max(map(obtain_values, tree['nodes']))
        case 4:
            return tree['value']
        case 5:
            return int(obtain_values(tree['nodes'][0]) > obtain_values(tree['nodes'][1]))
        case 6:
            return int(obtain_values(tree['nodes'][0]) < obtain_values(tree['nodes'][1]))
        case 7:
            return int(obtain_values(tree['nodes'][0]) == obtain_values(tree['nodes'][1]))

def solve(stream):
    tree = dict()

    decode_packet(tree, stream, 0)

    return obtain_values(tree)

def parse(content):
    return ''.join([ bin(int(char, 16))[2:].zfill(4) for char in content ])

with open('input.txt') as file:
    data = parse(file.read()[:-1])

    print(solve(data))
