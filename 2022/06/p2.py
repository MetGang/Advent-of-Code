def solve(data):
    N = 14
    return [ len(set(data[i:i + N])) == N for i in range(len(data) - N) ].index(True) + N

with open('input.txt') as file:
    print(solve(file.read()))
