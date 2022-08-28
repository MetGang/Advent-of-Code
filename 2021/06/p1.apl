⍝ https://adventofcode.com/2021/day/6

⎕IO ← 0

rawData ← ⊃⎕NGET'input.txt'1

data ← ⍎⊃rawData

spawners ← {(⍵[;1]@(⍵[;0]))9⍴0}{⍺,≢⍵}⌸data

Solve ← {0⍕+/({1⌽⍵+2⌽⍵×1 0 0 0 0 0 0 0 0}⍣⍺)⍵}

80 Solve spawners
