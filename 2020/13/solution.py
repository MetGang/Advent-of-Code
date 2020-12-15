# https://adventofcode.com/2020/day/13

def part_1(content):
    predata = content.split('\n')[:-1]
    timestamp = int(predata[0])
    ids = [ int(x) for x in predata[1].split(',') if x != 'x' ]
    bus_ts = timestamp * 2
    bus_id = 0
    for bus in ids:
        next_multiple = (timestamp // bus + 1) * bus
        if next_multiple < bus_ts:
            bus_ts = next_multiple
            bus_id = bus
    return (bus_ts - timestamp) * bus_id

def part_2(content):
    timestamp = 0
    ids = [ { 'id': int(x), 'offset': index } for index, x in enumerate(content.split('\n')[1].split(',')) if x != 'x' ]
    multiplier = 1
    for bus in ids:
        while (timestamp + bus['offset']) % bus['id'] > 0:
            timestamp += multiplier
        multiplier *= bus['id']		
    return timestamp

with open('input.txt', 'r') as file:
    content = file.read()

    # Part one
    print(part_1(content))

    # Part two
    print(part_2(content))
