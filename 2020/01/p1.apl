⍝ https://adventofcode.com/2020/day/1

rawData ← ⊃ ⎕NGET 'input.txt' 1

data ← ⍎¨rawData

Solve ← ×/⊢∩2020∘-

Solve data
