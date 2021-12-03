⍝ https://adventofcode.com/2021/day/3

rawData ← ⊃ ⎕NGET 'input.txt' 1

data ← ⍎¨↑rawData

MostCommon ← ≢>(2×+⌿)
LeastCommon ← ≢≤(2×+⌿)

Recurse ← {⍺←1 ⋄ 1=≢⍵:∊⍵ ⋄ c←⍵[;⍺] ⋄ w←⍵⌿⍨c=⍺⍺ c ⋄ (⍺+1)∇ w}

Solve ← (2⊥MostCommon Recurse)×(2⊥LeastCommon Recurse)

Solve data
