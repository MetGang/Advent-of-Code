# https://adventofcode.com/2021/day/12

def solve(data):
	paths = [ ([ 'start' ], True) ]
	total = 0

	while paths:
		path, can_route = paths.pop()
		connections = data[path[-1]]

		for c in connections:
			if c == 'start':
				continue
			elif c == 'end':
				total += 1
			elif (c not in path) or (c.isupper()):
				paths.append(([ *path, c ], can_route))
			elif can_route:
				paths.append(([ *path, c ], False))

	return total

def parse(content):
	nodes = dict()

	for line in content.split('\n'):
		first, second = line.split('-')

		if first not in nodes:
			nodes[first] = []

		nodes[first].append(second)

		if second not in nodes:
			nodes[second] = []

		nodes[second].append(first)

	return nodes

with open('input.txt') as file:
	data = parse(file.read()[:-1])

	print(solve(data))
