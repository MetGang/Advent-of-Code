⍝ https://adventofcode.com/2019/day/1

rawData ← ⊃ ⎕NGET 'input.txt' 1

data ← ⍎¨rawData

Solve ← {+/⍵-⍨{⍵≤0:0⋄⍵+∇(2-⍨⌊⍵÷3)}¨⍵}

Solve data
