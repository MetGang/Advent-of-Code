# https://adventofcode.com/2021/day/11

import numpy as np

INT32_MIN = np.iinfo(np.int32).min

def solve(matrix):
	h, w = np.shape(matrix)
	total = 0

	for _ in range(100):
		matrix += 1

		while not np.all(matrix < 10):
			for j in range(h):
				for i in range(w):
					if matrix[j][i] > 9:
						matrix[j][i] = INT32_MIN

						if j > 0 and i > 0:
							matrix[j - 1][i - 1] += 1
						if j > 0:
							matrix[j - 1][i] += 1
						if j > 0 and i < w - 1:
							matrix[j - 1][i + 1] += 1
						if i > 0:
							matrix[j][i - 1] += 1
						if i < w - 1:
							matrix[j][i + 1] += 1
						if j < h - 1 and i > 0:
							matrix[j + 1][i - 1] += 1
						if j < h - 1:
							matrix[j + 1][i] += 1
						if j < h - 1 and i < w - 1:
							matrix[j + 1][i + 1] += 1

		mask = matrix < 0

		total += mask.sum()

		matrix[mask] = 0

	return total

def parse(content):
	return np.array([ np.array([ np.int32(char) for char in line ]) for line in content.split('\n') ])

with open('input.txt') as file:
	data = parse(file.read()[:-1])

	print(solve(data))
