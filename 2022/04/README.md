[Advent of Code - Day 4 of 2022](https://adventofcode.com/2022/day/4)

# Languages

* [Python](#python)

# Solutions

### Python

###### Part 1
```python
def contains(nums):
    x1, x2, y1, y2 = nums
    return (x1 >= y1 and x2 <= y2) or (y1 >= x1 and y2 <= x2)

def solve(data):
    return sum(map(contains, data))

def parse(content):
    return ( ( int(num) for num in line.replace(',', '-').split('-') ) for line in content.split('\n') )

with open('input.txt') as file:
    print(solve(parse(file.read())))
```

###### Part 2
```python
def overlaps(nums):
    x1, x2, y1, y2 = nums
    return x2 >= y1 and y2 >= x1

def solve(data):
    return sum(map(overlaps, data))

def parse(content):
    return ( ( int(num) for num in line.replace(',', '-').split('-') ) for line in content.split('\n') )

with open('input.txt') as file:
    print(solve(parse(file.read())))
```
