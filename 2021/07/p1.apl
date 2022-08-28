⍝ https://adventofcode.com/2021/day/7

rawData ← ⊃⎕NGET'input.txt'1

data ← ⍎⊃rawData

median ← {⍵[⍋⍵]⊃⍨2÷⍨≢⍵}data

Solve ← {⌊/+/|⍺-⍵}

median Solve data
