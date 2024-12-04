⍝ https://adventofcode.com/2024/day/3

input ← ∊⊃ ⎕NGET 'input.txt' 1

+/⍎¨('mul\((\d+),(\d+)\)' ⎕S '\1×\2' ⊢ ('don''t\(\).*?do\(\)' ⎕R '' ⊢ input))
