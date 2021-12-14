from collections import defaultdict
from itertools import pairwise

def solve(data):
    mapping, singles, doubles = data
    steps = 40

    for _ in range(0, steps):
        gens = []

        for d, s in mapping:
            if d in doubles:
                gens.append((d, s, doubles[d]))
                del doubles[d]

        for d, s, count in gens:
            doubles[d[0] + s] += count
            doubles[s + d[1]] += count
            singles[s] += count

    singles_values = singles.values()

    return max(singles_values) - min(singles_values)

def parse(content):
    chunks = content.split('\n\n')

    template = chunks[0]
    mapping = [ line.split(' -> ') for line in chunks[1].split('\n') ]
    singles = defaultdict(int)
    doubles = defaultdict(int)

    for a in template:
        singles[a] += 1

    for a, b in pairwise(template):
        doubles[a + b] += 1

    return mapping, singles, doubles

with open('input.txt') as file:
    data = parse(file.read()[:-1])

    print(solve(data))
