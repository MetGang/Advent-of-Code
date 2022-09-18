[Advent of Code - Day 2 of 2021](https://adventofcode.com/2021/day/2)

# Languages

* [APL](#apl)
* [Python](#python)

# Solutions

### APL

###### Part 1
```apl
rawData ← ⊃⎕NGET'input.txt'1

forward ← 0,⍨⊢
down ← 0,⊢
up ← 0,-∘⊢

data ← ↑⍎¨rawData

Solve ← ×/+⌿

Solve data
```

###### Part 2
```apl
rawData ← ⊃⎕NGET'input.txt'1

forward ← 0,⍨⊢
down ← 0,⊢
up ← 0,-∘⊢

data ← ↑⍎¨rawData

Solve ← {+/⍵[;1]×+/⍵[;1]×+\⍵[;2]}

Solve data
```

### Python

###### Part 1
```python
def solve(data):
    position = 0
    depth = 0

    for cmd, value in data:
        match cmd:
            case 'forward':
                position += value
            case 'up':
                depth -= value
            case 'down':
                depth += value
    
    return position * depth

def parse(content):
    mapper = lambda x: (x[0], int(x[1]))

    return [ mapper(line.split(' ')) for line in content.split('\n') ]

with open('input.txt') as file:
    print(solve(parse(file.read())))
```

###### Part 2
```python
def solve(data):
    position = 0
    depth = 0
    aim = 0

    for cmd, value in data:
        match cmd:
            case 'forward':
                position += value
                depth += value * aim
            case 'up':
                aim -= value
            case 'down':
                aim += value
    
    return position * depth

def parse(content):
    mapper = lambda x: (x[0], int(x[1]))

    return [ mapper(line.split(' ')) for line in content.split('\n') ]

with open('input.txt') as file:
    print(solve(parse(file.read())))
```
