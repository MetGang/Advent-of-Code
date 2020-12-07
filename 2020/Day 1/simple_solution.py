# https://adventofcode.com/2020/day/1

nums = [ int(line) for line in open('input.txt') ]

# Part one
for i in nums:
    s = 2020 - i
    for j in nums:
        if s == j:
            print(i * j)

# Part two
for i in nums:
    s1 = 2020 - i
    for j in nums:
        s2 = s1 - j
        for k in nums:
            if s2 == k:
                print(i * j * k)
