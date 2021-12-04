# https://adventofcode.com/2021/day/4

import numpy as np

def winning_board(matrix):
    v = np.any(np.logical_and.reduce(matrix, 1))
    h = np.any(np.logical_and.reduce(matrix, 0))
    return v or h

def solve(data):
    head = np.array([ np.int32(x) for x in data[0].split(',') ])
    tail = np.array([ np.int32(x) for x in ' '.join(data[1:]).replace('\n', ' ').split(' ') if x != '' ])

    n = len(tail) // 25

    m_tail = np.reshape(tail, (n, 5, 5))
    blank = np.zeros((n, 5, 5), dtype = np.bool8)

    for key in head:
        for i in range(len(m_tail)):
            blank[i] = np.logical_or(blank[i], m_tail[i] == key)

            if winning_board(blank[i]):
                return key * np.sum(m_tail[i][~blank[i]])

    return None

with open('input.txt') as file:
    data = [ x for x in file.read().split('\n\n') ]

    print(solve(data))
