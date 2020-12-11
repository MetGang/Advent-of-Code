# https://adventofcode.com/2020/day/11

def adjencent_occupied_count(data, x, y, w, h):
	count = 0

	if x > 0 and data[y][x - 1][0] == '#':
		count += 1
	if y > 0 and data[y - 1][x][0] == '#':
		count += 1
	if x < w - 1 and data[y][x + 1][0] == '#':
		count += 1
	if y < h - 1 and data[y + 1][x][0] == '#':
		count += 1
	if x > 0 and y > 0 and data[y - 1][x - 1][0] == '#':
		count += 1
	if x > 0 and y < h - 1 and data[y + 1][x - 1][0] == '#':
		count += 1
	if x < w - 1 and y > 0 and data[y - 1][x + 1][0] == '#':
		count += 1
	if x < w - 1 and y < h - 1 and data[y + 1][x + 1][0] == '#':
		count += 1

	return count

def farmost_occupied_count(data, x, y, w, h, debug):
	count = 0
	d = min(w, h)

	for i in range(w):
		if x - i > 0:
			if data[y][x - i - 1][0] == 'L':
				break
			if data[y][x - i - 1][0] == '#':
				count += 1
				if debug:
					print('Debug: ', -1, 0)
				break
	for j in range(h):
		if y - j > 0:
			if data[y - j - 1][x][0] == 'L':
				break
			if data[y - j - 1][x][0] == '#':
				count += 1
				if debug:
					print('Debug: ', 0, -1)
				break
	for i in range(w):
		if x + i < w - 1:
			if data[y][x + i + 1][0] == 'L':
				break
			if data[y][x + i + 1][0] == '#':
				count += 1
				if debug:
					print('Debug: ', 1, 0)
				break
	for j in range(h):
		if y + j < h - 1:
			if data[y + j + 1][x][0] == 'L':
				break
			if data[y + j + 1][x][0] == '#':
				count += 1
				if debug:
					print('Debug: ', 0, 1)
				break
	for k in range(d):
		if x - k > 0 and y - k > 0:
			if data[y - k - 1][x - k - 1][0] == 'L':
				break
			if data[y - k - 1][x - k - 1][0] == '#':
				count += 1
				if debug:
					print('Debug: ', -1, -1)
				break
	for k in range(d):
		if x - k > 0 and y + k < h - 1:
			if data[y + k + 1][x - k - 1][0] == 'L':
				break
			if data[y + k + 1][x - k - 1][0] == '#':
				count += 1
				if debug:
					print('Debug: ', -1, 1)
				break
	for k in range(d):
		if x + k < w - 1 and y - k > 0:
			if data[y - k - 1][x + k + 1][0] == 'L':
				break
			if data[y - k - 1][x + k + 1][0] == '#':
				count += 1
				if debug:
					print('Debug: ', 1, -1)
				break
	for k in range(d):
		if x + k < w - 1 and y + k < h - 1:
			if data[y + k + 1][x + k + 1][0] == 'L':
				break
			if data[y + k + 1][x + k + 1][0] == '#':
				count += 1
				if debug:
					print('Debug: ', 1, 1)
				break

	return count

# Part one
with open('input.txt', 'r') as file:
	data = [ [ [ y, y ] for y in x ] for x in file.read().split('\n')[:-1] ]
	w = len(data[0])
	h = len(data)
	found_change = True
	while found_change:
		for y in range(h):
			row = data[y]
			for x in range(w):
				cell = row[x]
				cell[0] = cell[1]
		found_change = False
		for y in range(h):
			row = data[y]
			for x in range(w):
				cell = row[x]
				if cell[0] == 'L' and adjencent_occupied_count(data, x, y, w, h) == 0:
					cell[1] = '#'
					found_change = True
				if cell[0] == '#' and adjencent_occupied_count(data, x, y, w, h) >= 4:
					cell[1] = 'L'
					found_change = True
	count = 0
	for row in data:
		count += sum(map(lambda c: c[0] == '#' if c is not None else 0, row))
	print(count)

# Part two
with open('input.txt', 'r') as file:
	data = [ [ [ y, y ] for y in x ] for x in file.read().split('\n')[:-1] ]
	w = len(data[0])
	h = len(data)
	found_change = True
	while found_change:
		for y in range(h):
			row = data[y]
			for x in range(w):
				cell = row[x]
				cell[0] = cell[1]
		found_change = False
		for y in range(h):
			row = data[y]
			for x in range(w):
				cell = row[x]
				if cell[0] == 'L' and farmost_occupied_count(data, x, y, w, h, False) == 0:
					cell[1] = '#'
					found_change = True
				if cell[0] == '#' and farmost_occupied_count(data, x, y, w, h, False) >= 5:
					cell[1] = 'L'
					found_change = True
	count = 0
	for row in data:
		count += sum(map(lambda c: c[0] == '#' if c is not None else 0, row))
	print(count)
