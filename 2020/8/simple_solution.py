# https://adventofcode.com/2020/day/8

import copy

with open('./input.txt', 'r') as file:
	data1 = [ { 'opcode': x[:x.index(' ')], 'value': int(x[x.index(' ') + 1:]), 'visited': False } for x in file.read().split('\n')[:-1] ]
	data2 = copy.deepcopy(data1)
	# Part one
	acc = 0
	index = 0
	while True:
		curr = data1[index]
		if curr['visited']:
			break
		if curr['opcode'] == 'acc':
				acc += curr['value']
				index += 1
		elif curr['opcode'] == 'jmp':
				index += curr['value']
		else:
			index += 1
		curr['visited'] = True	
	print(acc)
	# Part two
	def simulate(in_data, i):
		if in_data[i]['opcode'] == 'nop':
			in_data[i]['opcode'] = 'jmp'
		elif in_data[i]['opcode'] == 'jmp':
			in_data[i]['opcode'] = 'nop'
		else:
			return False
		acc = 0
		index = 0
		while True:
			curr = in_data[index]
			if curr['opcode'] == 'nop':
				index += 1
			elif curr['opcode'] == 'acc':
				acc += curr['value']
				index += 1
			elif curr['opcode'] == 'jmp':
				index += curr['value']
			if index >= len(in_data):
				return acc
			elif curr['visited']:
				return None
			curr['visited'] = True
	i = 0
	while i < len(data2):
		result = simulate(copy.deepcopy(data2), i)
		if result:
			print(result)
			break
		i += 1
