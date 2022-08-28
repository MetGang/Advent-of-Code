⍝ https://adventofcode.com/2015/day/2

rawData ← ⊃⎕NGET'input.txt'1

data ← 2⊃¨'x'⎕VFI¨rawData

Solve ← {+/{(×/⍵)++/2×2↑⍵[⍋⍵]}¨⍵}

Solve data
