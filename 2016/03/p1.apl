⍝ https://adventofcode.com/2016/day/3

rawData ← ⊃⎕NGET'input.txt'1

data ← ↑⍎¨rawData

Solve ← +⌿(∧/2∘⌽<1∘⌽+⊢)

Solve data
