[Advent of Code - Day 2 of 2022](https://adventofcode.com/2022/day/2)

# Languages

* [Python](#python)

# Solutions

### Python

###### Part 1
```python
WIN, DRAW, LOSE = 6, 3, 0
ROCK, PAPER, SCISSORS = 1, 2, 3
OUTCOME_LUT = [
    [ ROCK + DRAW, PAPER + WIN, SCISSORS + LOSE ],
    [ ROCK + LOSE, PAPER + DRAW, SCISSORS + WIN ],
    [ ROCK + WIN, PAPER + LOSE, SCISSORS + DRAW ]
]

def get_outcome(entry):
    enemy = ord(entry[0]) - 65
    you = ord(entry[1]) - 88
    return OUTCOME_LUT[enemy][you]

def solve(data):
    return sum(map(get_outcome, data))

def parse(content):
    return [ line.split(' ') for line in content.split('\n') ]

with open('input.txt') as file:
    print(solve(parse(file.read())))
```

###### Part 2
```python
WIN, DRAW, LOSE = 6, 3, 0
ROCK, PAPER, SCISSORS = 1, 2, 3
OUTCOME_LUT = [
    [ SCISSORS + LOSE, ROCK + DRAW, PAPER + WIN ],
    [ ROCK + LOSE, PAPER + DRAW, SCISSORS + WIN ],
    [ PAPER + LOSE, SCISSORS + DRAW, ROCK + WIN ]
]

def get_outcome(entry):
    enemy = ord(entry[0]) - 65
    you = ord(entry[1]) - 88
    return OUTCOME_LUT[enemy][you]

def solve(data):
    return sum(map(get_outcome, data))

def parse(content):
    return [ line.split(' ') for line in content.split('\n') ]

with open('input.txt') as file:
    print(solve(parse(file.read())))
```
