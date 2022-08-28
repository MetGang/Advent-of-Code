⍝ https://adventofcode.com/2021/day/7

rawData ← ⊃⎕NGET'input.txt'1

data ← ⍎⊃rawData

average ← (⌊+/÷≢)data

Solve ← {⌊/+/{2÷⍨⍵×⍵+1}|⍺-⍵}

average Solve data
