File.read!("input.txt")
  |> String.split("\n\n")
  |> Stream.map(fn line ->
    line
    |> String.split("\n")
    |> Stream.map(&String.to_integer/1)
    |> Enum.sum()
  end)
  |> Enum.sort(:desc)
  |> Stream.take(3)
  |> Enum.sum()
  |> IO.puts()
