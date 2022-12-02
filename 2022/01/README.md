[Advent of Code - Day 1 of 2022](https://adventofcode.com/2022/day/1)

# Languages

* [Elixir](#elixir)
* [Python](#python)

# Solutions

### Elixir

###### Part 1
```elixir
File.read!("input.txt")
  |> String.split("\n\n")
  |> Enum.map(fn line ->
    line
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
    |> Enum.sum()
  end)
  |> Enum.max()
  |> IO.puts()
```

###### Part 2
```elixir
File.read!("input.txt")
  |> String.split("\n\n")
  |> Enum.map(fn line ->
    line
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
    |> Enum.sum()
  end)
  |> Enum.sort(:desc)
  |> Enum.take(3)
  |> Enum.sum()
  |> IO.puts()
```

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
