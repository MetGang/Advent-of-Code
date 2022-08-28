⍝ https://adventofcode.com/2021/day/2

rawData ← ⊃⎕NGET'input.txt'1

forward ← 0,⍨⊢
down ← 0,⊢
up ← 0,-∘⊢

data ← ↑⍎¨rawData

Solve ← ×/+⌿∘⊢

Solve data
