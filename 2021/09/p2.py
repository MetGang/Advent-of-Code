# https://adventofcode.com/2021/day/9

def traverse(matrix, i, j, w, h):
	matrix[j][i] = 9
	total = 1

	if j > 0 and matrix[j - 1][i] != 9:
		total += traverse(matrix, i, j - 1, w, h)
	if i > 0 and matrix[j][i - 1] != 9:
		total += traverse(matrix, i - 1, j, w, h)
	if j < h - 1 and matrix[j + 1][i] != 9:
		total += traverse(matrix, i, j + 1, w, h)
	if i < w - 1 and matrix[j][i + 1] != 9:
		total += traverse(matrix, i + 1, j, w, h)

	return total

def solve(data):
	h, w = len(data), len(data[0])
	basins = []

	for j in range(h):
		for i in range(w):
			if data[j][i] != 9:
				basins.append(traverse(data, i, j, h, w))

	basins.sort(reverse = True)

	return basins[0] * basins[1] * basins[2]

def parse(content):
	return [ [ int(char) for char in line ] for line in content.split('\n') ]

with open('input.txt') as file:
	data = parse(file.read()[:-1])

	print(solve(data))
