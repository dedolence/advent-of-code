from collections import defaultdict
from itertools import combinations

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


rows = get_input(file_name)
antennas = find_antannas(rows)
print(antennas)
for symbol in antennas:
    pairs = list(combinations(antennas[symbol], 2))
    for pair in pairs:
        # the pairs are processed by row, descending. so a will always be "higher" than b
        # (8, 1), (5, 2)
        a, b = pair
        x1, x2 = a[0], b[0]
        y1, y2 = a[1], b[1]
        slope_x = abs(x2 - x1)  # = 5 - 8 = -3 = 3
        slope_y = abs(y2 - y1)  # = 2 - 1 =  1 = 1