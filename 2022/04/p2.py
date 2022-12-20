def overlaps(nums):
    x1, x2, y1, y2 = nums
    return x2 >= y1 and y2 >= x1

def solve(data):
    return sum(map(overlaps, data))

def parse(content):
    return ( map(int, line.replace(',', '-').split('-')) for line in content.split('\n') )

with open('input.txt') as file:
    print(solve(parse(file.read())))
