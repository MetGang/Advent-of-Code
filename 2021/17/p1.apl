⍝ https://adventofcode.com/2021/day/17

rawData ← ⊃⎕NGET'input.txt'1

data ← {3⊃⍎¨⍵⊆⍨~⍵∊'target :xy=.,'}⊃rawData

Solve ← 2÷⍨⊢×1∘+

Solve data
