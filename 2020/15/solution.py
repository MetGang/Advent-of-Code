# https://adventofcode.com/2020/day/15

def compute(content, iter_count):
    predata = [ int(num) for num in content[:-1].split(',') ]
    last = predata[-1]
    data = { int(num): index for index, num in enumerate(predata) }

    for turn in range(len(data), iter_count):
        if last in data:
            old_last = data[last]
            data[last] = turn - 1
            last = turn - old_last - 1
        else:
            data[last] = turn - 1
            last = 0

    return last

def part_1(content):
    return compute(content[:], 2020)

def part_2(content):
    return compute(content[:], 30000000)

with open('input.txt', 'r') as file:
    content = file.read()

    # Part one
    print(part_1(content))

    # Part two
    print(part_2(content))
