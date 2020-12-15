# https://adventofcode.com/2020/day/9

def is_valid(data, value):
    for i in data:
        s = value - i
        if s in data:
            return True
    return False

def foo(data, index, threshold):
    range_sum = 0
    first = index
    while True:
        range_sum += data[index]
        if range_sum == threshold:
            subdata = sorted(data[first:index + 1])
            return subdata[0] + subdata[-1]
        elif range_sum > threshold:
            return None
        index += 1

with open('input.txt', 'r') as file:
    data = [ int(x) for x in file.read().split('\n')[:-1] ]
    # Part one
    i = 25
    index = len(data) - 1
    while i < len(data):
        if not is_valid(data[i - 25:i], data[i]):
            index = i
            break
        i += 1
    print(data[index])
    # Part two
    ii = 0
    while ii < len(data):
        result = foo(data, ii, data[index])
        if result is not None:
            print(result)
            break
        ii += 1
