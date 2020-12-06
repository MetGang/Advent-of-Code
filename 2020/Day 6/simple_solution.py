# https://adventofcode.com/2020/day/6

full_set = set([ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ])

with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')
    # Part one
    count = sum([ len(set(record.replace('\n', ''))) for record in data ])
    print(count)
    # Part two
    count = sum([ len(full_set.intersection(*[ set(x) for x in record.rstrip().split('\n') ])) for record in data ])
    print(count)
