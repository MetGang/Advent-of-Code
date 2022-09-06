# https://adventofcode.com/2020/day/2

def solve(data):
    count = 0

    for lowest, highest, letter, password in data:
        first = password[lowest - 1]
        second = password[highest - 1]
        count += (first == letter or second == letter) and not first == second

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
