import math

dial = list(range(100))
with open("input.txt") as file:
    directions = [line.strip() for line in file.readlines()]
pos = 50
count = 0

for turn in directions:
    clicks = range(int(turn[1:]))
    # shoutout u/Farlic for the suggestion for this dict to account for
    # either + or - without needing ifs
    ops = {"L": lambda x, y: x - y, "R": lambda x, y: x + y}
    for i in clicks:
        pos = ops[turn[0]](pos, 1) % len(dial)
        if pos == 0: count += 1

print(count)