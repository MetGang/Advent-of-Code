# https://adventofcode.com/2021/day/9

def solve(data):
    h, w = len(data), len(data[0])
    total = 0

    for j in range(h):
        for i in range(w):
            current = data[j][i]

            if j > 0 and current >= data[j - 1][i]:
                continue
            if i > 0 and current >= data[j][i - 1]:
                continue
            if j < h - 1 and current >= data[j + 1][i]:
                continue
            if i < w - 1 and current >= data[j][i + 1]:
                continue

            total += current + 1

    return total

def parse(content):
    return [ [ int(char) for char in line ] for line in content.split('\n') ]

with open('input.txt') as file:
    data = parse(file.read()[:-1])

    print(solve(data))
