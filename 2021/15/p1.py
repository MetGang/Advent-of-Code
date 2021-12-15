from dijkstar import Graph, find_path
from itertools import pairwise
import numpy as np

def solve(data):
    grid = data

    h, w = np.shape(grid)

    graph = Graph()

    for j in range(0, h):
        for a, b in pairwise(range(0, w)):
            graph.add_edge(j * h + a, j * h + b, grid[j][b])
            # graph.add_edge(j * h + b, j * h + a, grid[j][a])

    for i in range(0, w):
        for a, b in pairwise(range(0, h)):
            graph.add_edge(a * h + i, b * h + i, grid[b][i])
            # graph.add_edge(b * h + i, a * h + i, grid[a][i])

    return find_path(graph, 0, h * w - 1).total_cost

def parse(content):
    grid = np.array([ np.array([ np.int32(char) for char in line ]) for line in content.split('\n') ])

    return grid

with open('input.txt') as file:
    data = parse(file.read()[:-1])

    print(solve(data))
