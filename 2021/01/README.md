[Advent of Code - Day 1 of 2021](https://adventofcode.com/2021/day/1)

# Languages

* [APL](#apl)
* [Elixir](#elixir)
* [Python](#python)
* [Rust](#rust)
* [Scala](#scala)

# Solutions

### APL

###### Part 1
```apl
rawData ← ⊃⎕NGET'input.txt'1

data ← ⍎¨rawData

Solve ← +/2</⊢

Solve data
```

###### Part 2
```apl
rawData ← ⊃⎕NGET'input.txt'1

data ← ⍎¨rawData

Solve ← +/2</3+/⊢

Solve data
```

### Elixir

###### Part 1
```elixir
File.read!("input.txt")
  |> String.split("\n")
  |> Enum.map(&String.to_integer/1)
  |> Enum.chunk_every(2, 1, :discard)
  |> Enum.count(fn [a, b] -> a < b end)
  |> IO.puts()
```

###### Part 2
```elixir
File.read!("input.txt")
  |> String.split("\n")
  |> Enum.map(&String.to_integer/1)
  |> Enum.chunk_every(4, 1, :discard)
  |> Enum.count(fn [a, _, _, d] -> a < d end)
  |> IO.puts()
```

### Python

###### Part 1
```python
def solve(data):
    return sum(map(lambda x: x[0] < x[-1], zip(data, data[1:])))

def parse(content):
    return [ int(line) for line in content.split('\n') ]

with open('input.txt') as file:
    print(solve(parse(file.read())))
```

###### Part 2
```python
def solve(data):
    return sum(map(lambda x: x[0] < x[-1], zip(data, data[3:])))

def parse(content):
    return [ int(line) for line in content.split('\n') ]

with open('input.txt') as file:
    print(solve(parse(file.read())))
```

### Rust

###### Part 1
```rust
fn main() {
    let raw_data = include_str!("input.txt");

    let result = raw_data
        .lines()
        .map(|x| x.parse::<u16>().unwrap())
        .collect::<Vec<u16>>()
        .windows(2)
        .filter(|x| x.first() < x.last())
        .count();

    println!("{}", result);
}
```

###### Part 2
```rust
fn main() {
    let raw_data = include_str!("input.txt");

    let result = raw_data
        .lines()
        .map(|x| x.parse::<u16>().unwrap())
        .collect::<Vec<u16>>()
        .windows(4)
        .filter(|x| x.first() < x.last())
        .count();

    println!("{}", result);
}
```

### Scala

###### Part 1
```scala
import scala.io.Source.fromFile

object Hello {
    def main(args: Array[String]) = {
        val rawData = fromFile("input.txt").mkString
        
        val result = rawData
            .split("\n")
            .map(_.toInt)
            .sliding(2)
            .map(x => x.head < x.last)
            .count(_ == true)
        
        print(result)
    }
}
```

###### Part 2
```scala
import scala.io.Source.fromFile

object Hello {
    def main(args: Array[String]) = {
        val rawData = fromFile("input.txt").mkString
        
        val result = rawData
            .split("\n")
            .map(_.toInt)
            .sliding(4)
            .map(x => x.head < x.last)
            .count(_ == true)
        
        print(result)
    }
}
```
