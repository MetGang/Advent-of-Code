# https://adventofcode.com/2020/day/10

import copy

def traverse(mem_data, index, distance):
    if index + 1 >= len(mem_data):
        return 1

    if mem_data[index]['diffs'][distance] > 0:
        return mem_data[index]['diffs'][distance]

    count = 0

    for i in range(1, 4):
        if index + i < len(mem_data):
            if mem_data[index + i]['num'] - mem_data[index]['num'] == distance:
                count = traverse(mem_data, index + i, 1) + traverse(mem_data, index + i, 2) + traverse(mem_data, index + i, 3)
        else:
            break

    mem_data[index]['diffs'][distance] = count

    return mem_data[index]['diffs'][distance]

with open('input.txt', 'r') as file:
    data = sorted([ int(x) for x in file.read().split('\n')[:-1] ])
    data.insert(0, 0)
    data.append(data[-1] + 3)
    # Part one
    diffs = { 1: 0, 3: 0 }
    i = 1
    while i < len(data):
        diffs[data[i] - data[i - 1]] += 1
        i += 1
    print(diffs[1] * diffs[3])
    # Part two
    mem_data = [ { 'num': x, 'diffs': { 1: 0, 2: 0, 3: 0 } } for x in data ]
    count = int((traverse(mem_data, 0, 1) + traverse(mem_data, 0, 2) + traverse(mem_data, 0, 3)) / 3)
    print(count)
