data = [
    [
        int(line[: line.index('-')]),
        int(line[line.index('-') + 1 : line.index(' ')]),
        line[line.index(' ') + 1 : line.index(': ')],
        line[line.index(': ') + 2 : -1]
    ]
    for line in open('input.txt')
]

# Part one
total = 0

for record in data:
    count = sum(map(lambda x : 1 if record[2] == x else 0, record[3]))
    if count >= record[0] and count <= record[1]:
        total += 1

print(total)

# Part two
total = 0

for record in data:
    if (record[3][record[0] - 1] == record[2]) + (record[3][record[1] - 1] == record[2]) == 1:
        total += 1

print(total)
