from collections import defaultdict
from .. import loader

file_name = "test.txt"

def get_input(file_name):
    rows = []
    with open(file_name) as file:
        rows = [line.strip() for line in file.readlines()]
    return rows

def find_antannas(rows):
    points = defaultdict(list)
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            if rows[y][x] != ".":
                points[rows[y][x]].append((x, y))
    return points


rows = loader.get_input()
antennas = find_antannas(rows)

