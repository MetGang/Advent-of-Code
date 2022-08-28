⍝ https://adventofcode.com/2017/day/2

rawData ← ⊃⎕NGET'input.txt'1

data ← ⍎¨rawData

Solve ← +/(÷/{⍵[{∊(≠/¨⍵)/⍵}⍸~×1|∘.÷⍨⍵]})¨

Solve data
