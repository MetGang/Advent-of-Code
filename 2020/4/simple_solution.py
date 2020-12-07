# https://adventofcode.com/2020/day/4

import re

# Part one
with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')
    data = [ [ x[:3] for x in record.replace('\n', ' ').split(' ') ] for record in data ]
    data[-1].pop()
    count = 0
    for record in data:
        count += (len(record) == 8 or (len(record) == 7 and 'cid' not in record))
    print(count)

# Part two
with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')
    data = [ { x[:3]: x[4:] for x in record.replace('\n', ' ').split(' ') } for record in data ]
    data[-1] = { k: v for k, v in data[-1].items() if k }
    count = 0
    for record in data:
        if len(record) == 8 or (len(record) == 7 and 'cid' not in record):
            valid_fields = 0
            if len(record['byr']) == 4 and (int(record['byr']) >= 1920 and int(record['byr']) <= 2002):
                valid_fields += 1
            if len(record['iyr']) == 4 and (int(record['iyr']) >= 2010 and int(record['iyr']) <= 2020):
                valid_fields += 1
            if len(record['eyr']) == 4 and (int(record['eyr']) >= 2020 and int(record['eyr']) <= 2030):
                valid_fields += 1
            if re.search('[0-9]+cm', record['hgt']):
                num = int(record['hgt'][:record['hgt'].index('cm')])
                if num >= 150 and num <= 193:
                    valid_fields += 1
            if re.search('[0-9]+in', record['hgt']):
                num = int(record['hgt'][:record['hgt'].index('in')])
                if num >= 59 and num <= 76:
                    valid_fields += 1
            if re.search('#[0-9a-f]{6}', record['hcl']):
                valid_fields += 1
            if re.search('(amb|blu|brn|gry|grn|hzl|oth)', record['ecl']):
                valid_fields += 1
            if re.search('^[0-9]{9}$', record['pid']):
                valid_fields += 1
            count += valid_fields == 7
    print(count)
