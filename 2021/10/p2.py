# https://adventofcode.com/2021/day/10

CHAR_MAPPING = { ')': '(', ']': '[', '}': '{', '>': '<' }

VALUES_MAPPING = { '(': 1, '[': 2, '{': 3, '<': 4 }

def solve(data):
    results = []

    for entry in data:
        stack = []

        for ch in entry:	
            if ch in [ '(', '[', '{', '<' ]:
                stack.append(ch)
            else:
                if stack[-1] != CHAR_MAPPING[ch]:
                    break
                else:
                    stack.pop()
        else:
            stack.reverse()
            points = 0

            for value in stack:
                points *= 5
                points += VALUES_MAPPING[value]

            results.append(points)

    results.sort()

    return results[len(results) // 2]

def parse(content):
    return [ line for line in content.split('\n') ]

with open('input.txt') as file:
    data = parse(file.read()[:-1])

    print(solve(data))
