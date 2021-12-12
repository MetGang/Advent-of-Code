# https://adventofcode.com/2021/day/11

import numpy as np

INT32_MIN = np.iinfo(np.int32).min

def solve(data):
    h, w = np.shape(data)
    total = 0
    step = 1

    while True:
        data += 1

        while not np.all(data < 10):
            for j in range(h):
                for i in range(w):
                    if data[j][i] > 9:
                        data[j][i] = INT32_MIN

                        if j > 0 and i > 0:
                            data[j - 1][i - 1] += 1
                        if j > 0:
                            data[j - 1][i] += 1
                        if j > 0 and i < w - 1:
                            data[j - 1][i + 1] += 1
                        if i > 0:
                            data[j][i - 1] += 1
                        if i < w - 1:
                            data[j][i + 1] += 1
                        if j < h - 1 and i > 0:
                            data[j + 1][i - 1] += 1
                        if j < h - 1:
                            data[j + 1][i] += 1
                        if j < h - 1 and i < w - 1:
                            data[j + 1][i + 1] += 1

        mask = data < 0

        total += mask.sum()

        data[mask] = 0

        if np.all(data == 0):
            return step
        
        step += 1

def parse(content):
    return np.array([ np.array([ np.int32(char) for char in line ]) for line in content.split('\n') ])

with open('input.txt') as file:
    data = parse(file.read()[:-1])

    print(solve(data))
