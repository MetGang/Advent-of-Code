def contains(nums):
    x1, x2, y1, y2 = nums
    return (x1 >= y1 and x2 <= y2) or (y1 >= x1 and y2 <= x2)

def solve(data):
    return sum(map(contains, data))

def parse(content):
    return ( map(int, line.replace(',', '-').split('-')) for line in content.split('\n') )

with open('input.txt') as file:
    print(solve(parse(file.read())))
