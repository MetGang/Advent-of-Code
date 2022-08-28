⍝ https://adventofcode.com/2021/day/8

rawData ← ⊃⎕NGET'input.txt'1

data ← {' '(≠⊆⊢)2⊃'|'(≠⊆⊢)⍵}¨rawData

Solve ← {≢5 6~⍨∊{≢¨⍵}¨⍵}

Solve data
