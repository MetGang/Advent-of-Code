[Advent of Code - Day 6 of 2022](https://adventofcode.com/2022/day/6)

# Languages

* [Python](#python)

# Solutions

### Python

###### Part 1
```python
def solve(data):
    N = 4
    return [ len(set(data[i:i + N])) == N for i in range(len(data) - N) ].index(True) + N

with open('input.txt') as file:
    print(solve(file.read()))
```

###### Part 2
```python
def solve(data):
    N = 14
    return [ len(set(data[i:i + N])) == N for i in range(len(data) - N) ].index(True) + N

with open('input.txt') as file:
    print(solve(file.read()))
```
