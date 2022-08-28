⍝ https://adventofcode.com/2017/day/4

rawData ← ⊃⎕NGET'input.txt'1

Solve ← +/{∧/≠{⍵[⍋⍵]}¨⍵⊆⍨' '≠⍵}¨

Solve rawData
