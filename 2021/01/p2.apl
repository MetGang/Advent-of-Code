⍝ https://adventofcode.com/2021/day/1

rawData ← ⊃ ⎕NGET 'input.txt' 1

data ← ⍎¨rawData

Solve ← {+/2</3+/⍵}

Solve data
