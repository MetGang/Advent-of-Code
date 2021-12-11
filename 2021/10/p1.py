# https://adventofcode.com/2021/day/10

CHAR_MAPPING = { ')': '(', ']': '[', '}': '{', '>': '<' }

POINTS_MAPPING = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

def solve(data):
	points = []

	for entry in data:
		stack = []

		for ch in entry:
			if ch in [ '(', '[', '{', '<' ]:
				stack.append(ch)
			else:
				if stack[-1] != CHAR_MAPPING[ch]:
					points.append(POINTS_MAPPING[ch])
					break
				else:
					stack.pop()

	return sum(points)

def parse(content):
	return [ line for line in content.split('\n') ]

with open('input.txt') as file:
	data = parse(file.read()[:-1])

	print(solve(data))

