# https://adventofcode.com/2020/day/2

from collections import Counter

def solve(data):
    count = 0

    for lowest, highest, letter, password in data:
        occurs = Counter(password)[letter]
        count += occurs >= lowest and occurs <= highest

    return count

def parse(content):
    parsed = []

    for line in content.split('\n'):
        splitted = line.replace('-', ' ').replace(':', '').split(' ')
        splitted[0] = int(splitted[0])
        splitted[1] = int(splitted[1])
        parsed.append(splitted)

    return parsed

with open('input.txt') as file:
    data = parse(file.read().strip())

    print(solve(data))
