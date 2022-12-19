def solve(data):
    return max(map(sum, data))

def parse(content):
    return ( map(int, line.split('\n')) for line in content.split('\n\n') )

with open('input.txt') as file:
    print(solve(parse(file.read())))
