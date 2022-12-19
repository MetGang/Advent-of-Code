def solve(data):
    return sum(sorted(map(sum, data))[-3:])

def parse(content):
    return ( map(int, line.split('\n')) for line in content.split('\n\n') )

with open('input.txt') as file:
    print(solve(parse(file.read())))
