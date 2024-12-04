⍝ https://adventofcode.com/2024/day/1

input ← ⊃ ⎕NGET 'input.txt' 1

SortAsc ← ⊂∘⍋⌷⊢

mat ← ⍉↑⍎¨input
a ← SortAsc mat[1;]
b ← SortAsc mat[2;]
+/|a-b
