⍝ https://adventofcode.com/2021/day/3

rawData ← ⊃ ⎕NGET 'input.txt' 1

data ← ⍎¨↑rawData

MostCommon ← ((2÷⍨≢)≤+⌿)
LeastCommon ← ((2÷⍨≢)>+⌿)

Solve ← ((2⊥MostCommon)×(2⊥LeastCommon))

Solve data
