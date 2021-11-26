# https://adventofcode.com/2019/day/2

import copy

EXPECTED = 19690720

def solve(data, noun, verb):
    data[1] = noun
    data[2] = verb

    for i in range(0, len(data), 4):
        opcode = data[i]
        f_pos = data[i + 1]
        s_pos = data[i + 2]
        o_pos = data[i + 3]

        match opcode:
            case 1:
                data[o_pos] = data[f_pos] + data[s_pos]
            case 2:
                data[o_pos] = data[f_pos] * data[s_pos]
            case 99:
                break

    return data[0]

with open('input.txt') as file:
    data = [ int(x) for x in file.read().split(',') ]

    # Brute force ftw
    for noun in range(0, 100):
        for verb in range(0, 100):
            if solve(copy.deepcopy(data), noun, verb) == EXPECTED:
                print(100 * noun + verb)
                break
