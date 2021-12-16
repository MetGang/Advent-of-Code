# https://adventofcode.com/2021/day/16

def skip_literal(stream):
    index = 0

    while stream[index] == '1':
        index += 5
    
    index += 5

    return index

def decode_packet(tree, stream, index):
    version = int(stream[index:index + 3], 2)
    type_id = int(stream[index + 3:index + 6], 2)

    tree['version'] = version
    tree['nodes'] = []

    if type_id == 4:
        offset = skip_literal(stream[index + 6:])

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

def sum_versions(tree):
    if tree['nodes']:
        return tree['version'] + sum(map(sum_versions, tree['nodes']))
    else:
        return tree['version']

def solve(stream):
    tree = dict()

    decode_packet(tree, stream, 0)

    return sum_versions(tree)

def parse(content):
    return ''.join([ bin(int(char, 16))[2:].zfill(4) for char in content ])

with open('input.txt') as file:
    data = parse(file.read()[:-1])

    print(solve(data))
