# https://adventofcode.com/2021/day/4

import numpy as np

def winning_board(matrix):
    v = np.any(np.logical_and.reduce(matrix, 1))
    h = np.any(np.logical_and.reduce(matrix, 0))
    return v or h

def solve(data):
    head, tail = data

    n = len(tail) // 25

    m_tail = np.reshape(tail, (n, 5, 5))
    blank = np.zeros((n, 5, 5), dtype = np.bool8)

    for key in head:
        for i in range(len(m_tail)):
            blank[i] = np.logical_or(blank[i], m_tail[i] == key)

            if winning_board(blank[i]):
                return key * np.sum(m_tail[i][~blank[i]])

    return None

def parse(content):
    chunks = content.split('\n\n')

    head = np.array([ np.int32(key) for key in chunks[0].split(',') ])
    tail = np.array([ np.int32(num) for num in ' '.join(chunks[1:]).split() ])

    return head, tail

with open('input.txt') as file:
    data = parse(file.read()[:-1])

    print(solve(data))
