⍝ https://adventofcode.com/2021/day/7

rawData ← ⊃ ⎕NGET 'input.txt' 1

data ← ⍎⊃rawData

Solve ← {⌊/+/{2÷⍨⍵×⍵+1}|⍵∘.-⍨⍳⌈/⍵}

Solve data
