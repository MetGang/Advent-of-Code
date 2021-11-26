# https://adventofcode.com/2018/day/2

def solve(data):
    for i, w1 in enumerate(data):
        for j, w2 in enumerate(data):
            if i == j:
                continue

            mapped = list(map(lambda x: 0 if x[0] == x[1] else 1, zip(w1, w2)))

            if sum(mapped) == 1:
                ret = list(w1)

                del ret[mapped.index(1)]

                return ''.join(ret)

with open('input.txt') as file:
    data = [ x[:-1] for x in file.readlines() ]

    print(solve(data))
