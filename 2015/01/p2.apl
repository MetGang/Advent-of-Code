⍝ https://adventofcode.com/2015/day/1

rawData ← ⊃⎕NGET'input.txt'1

data ← ⊃rawData

Solve ← {{⊃⍸⍵=¯1}+\1-⍨2×⍵='('}

Solve data
