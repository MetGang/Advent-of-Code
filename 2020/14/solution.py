# https://adventofcode.com/2020/day/14

def part_1(content):
    data = [ record for record in content.split('\n') ][:-1]
    memory = {}
    current_mask = ''
    for record in data:
        if record.startswith('mask'):
            current_mask = record[record.rfind(' ') + 1:]
        else:
            mem_index = int(record[record.index('[') + 1:record.index(']')])
            pre_value = format(int(record[record.rfind(' ') + 1:]), 'b')
            value = list('0' * (len(current_mask) - len(pre_value)) + pre_value)
            for i in range(len(value)):
                if current_mask[i] != 'X':
                    value[i] = current_mask[i]
            memory[mem_index] = int(''.join(value), 2)
    return sum(map(lambda x: memory[x], memory))

def get_all_x_permutations(str_value):
    indices = [ i for i, x in enumerate(str_value) if x == 'X' ]
    ret = []
    for i in range(2 ** len(indices)):
        new = list(str_value)
        for index in indices:
            new[index] = str(i % 2)
            i //= 2
        ret.append(''.join(new))
    return ret

def part_2(content):
    data = [ record for record in content.split('\n') ][:-1]
    memory = {}
    current_mask = ''
    for record in data:
        if record.startswith('mask'):
            current_mask = record[record.rfind(' ') + 1:]
        else:
            pre_mem_index = format(int(record[record.index('[') + 1:record.index(']')]), 'b')
            mem_index = list('0' * (len(current_mask) - len(pre_mem_index)) + pre_mem_index)
            for i in range(len(mem_index)):
                if current_mask[i] != '0':
                    mem_index[i] = current_mask[i]
            value = int(record[record.rfind(' ') + 1:])
            for perm in get_all_x_permutations(mem_index):
                memory[int(perm, 2)] = value
    return sum(map(lambda x: memory[x], memory))

with open('input.txt', 'r') as file:
    content = file.read()

    # Part one
    print(part_1(content))

    # Part two
    print(part_2(content))
