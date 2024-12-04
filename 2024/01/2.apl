⍝ https://adventofcode.com/2024/day/1

input ← ⊃ ⎕NGET 'input.txt' 1

mat ← ⍉↑⍎¨input
a ← mat[1;]
b ← mat[2;]
+/(⊢×(+/b∘=))¨a
