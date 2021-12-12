# https://adventofcode.com/2021/day/8

from itertools import chain

def solve(data):
    mapped = map(lambda s: [ len(elem) for elem in s ], data)

    flatten = list(chain(*mapped))

    return len(flatten) - flatten.count(5) - flatten.count(6)

def parse(content):
	return [ line.split(' | ')[1].split(' ') for line in content.split('\n') ]

with open('input.txt') as file:
	data = parse(file.read()[:-1])

	print(solve(data))
