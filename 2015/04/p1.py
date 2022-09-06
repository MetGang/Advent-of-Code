# https://adventofcode.com/2015/day/4

from hashlib import md5

def solve(data):
    number = 0

    while True:
        full_str = (data + str(number)).encode('ascii')
        if md5(full_str).hexdigest().startswith('00000'):
            return number
        number += 1

def parse(content):
    return content

with open('input.txt') as file:
    data = parse(file.read().strip())

    print(solve(data))
