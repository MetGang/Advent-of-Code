⍝ https://adventofcode.com/2017/day/1

rawData ← ⊃⎕NGET'input.txt'1

data ← ⊃rawData

Solve ← {+/⍎¨⍵/⍨⍵=(2÷⍨≢⍵)⌽⍵}

Solve data
