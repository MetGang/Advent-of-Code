# https://adventofcode.com/2021/day/8

def hash(iterable):
    return ''.join(sorted(iterable))

def get_mapping(inputs):
    set_1 = inputs[0]
    set_7 = inputs[1]
    set_4 = inputs[2]
    set_8 = inputs[9]

    set_inter_235 = inputs[3] & inputs[4] & inputs[5]
    set_inter_069 = inputs[6] & inputs[7] & inputs[8]

    set_3 = (set_inter_235) | set_1
    set_9 = (set_inter_235) | set_4
    set_0 = set_8 - ((set_3 & set_4) - set_1)
    set_5 = (set_inter_069) | ((set_3 & set_4) - set_1)
    set_6 = set_5 | (set_0 - set_1)
    set_2 = (set_inter_235) | ((set_9 - set_5) | (set_8 - set_9))

    return {
        hash(set_0): '0',
        hash(set_1): '1',
        hash(set_2): '2',
        hash(set_3): '3',
        hash(set_4): '4',
        hash(set_5): '5',
        hash(set_6): '6',
        hash(set_7): '7',
        hash(set_8): '8',
        hash(set_9): '9',
    }

def solve(data):
    total = 0

    for segment in data:
        inputs = sorted([ set(out) for out in segment[0] ], key = len)
        outputs = segment[1]

        mapping = get_mapping(inputs)

        mapped = map(lambda out: mapping[hash(out)], outputs)

        total += int(''.join(mapped))

    return total

with open('input.txt') as file:
    data = [ [ part.split(' ') for part in line[:-1].split(' | ') ] for line in file.readlines() ]

    print(solve(data))
