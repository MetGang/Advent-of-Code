# https://adventofcode.com/2020/day/5

def find_missing(lst):
    lst.sort()
    return [ x for x in range(lst[0], lst[-1] + 1) if x not in lst ]

with open('input.txt', 'r') as file:
    biggest_id = 0
    all_ids = []
    for line in file:
        row = 0
        level = 64
        l = 0
        u = 127
        for v in line[:-4]:
            if v == 'F':
                u -= level
                row = u
            elif v == 'B':
                l += level
                row = l
            level /= 2
        column = 0
        level = 4
        l = 0
        u = 7
        for h in line[-4:-1]:
            if h == 'L':
                u -= level
                column = u
            elif h == 'R':
                l += level
                column = l
            level /= 2
        new_id = row * 8 + column
        all_ids.append(int(new_id))
        if new_id > biggest_id:
            biggest_id = new_id
    # Part one
    print(int(biggest_id))
    # Part two
    print(find_missing(all_ids))
