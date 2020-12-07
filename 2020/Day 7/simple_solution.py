# https://adventofcode.com/2020/day/7

def rchop(string, suffixes):
    for suffix in suffixes:
        if string.endswith(suffix):
            string = string[: -len(suffix)]
    return string

def traverse_for_any(to_find, key, database):
    count = 0
    if database[key] != []:
        for child in database[key]:
            if child['name'] == 'shiny gold':
                return True
            else:
                count += traverse_for_any(to_find, child['name'], database)
    return count != 0

def count_bags_in(key, database):
    count = 0
    if database[key] != []:
        for child in database[key]:
            count += child['quantity'] + child['quantity'] * count_bags_in(child['name'], database)
    return count

with open('input.txt') as file:
    database = { x[: x.index('bags') - 1]: [ { 'name': z[z.index(' ') + 1 :], 'quantity': int(z[: z.index(' ')]) } for z in [ rchop(y, [ 'no other bags', ' bags', ' bag' ]) for y in x[x.index('contain') + 8 :].split(', ') ] if z ] for x in file.read().split('.\n')[:-1] }
    # Part one
    count = 0
    for key in database:
        count += traverse_for_any('shiny gold', key, database)
    print(count)
    # Part two
    count = count_bags_in('shiny gold', database)
    print(count)
