[Advent of Code - Day 1 of 2022](https://adventofcode.com/2022/day/1)

# Languages

* [Python](#python)

# Solutions

### Python

###### Part 1
```python
def solve(data):
    return max(map(sum, data))

def parse(content):
    return ( ( int(num) for num in line.split('\n') ) for line in content.split('\n\n') )

with open('input.txt') as file:
    print(solve(parse(file.read())))
```

###### Part 2
```python
def solve(data):
    return sum(sorted(map(sum, data))[-3:])

def parse(content):
    return ( ( int(num) for num in line.split('\n') ) for line in content.split('\n\n') )

with open('input.txt') as file:
    print(solve(parse(file.read())))
```
