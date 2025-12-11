dial = list(range(100))
with open("input.txt") as file:
    directions = [line.strip() for line in file.readlines()]
pos = 50
count = 0

for turn in directions:
    inc = int(turn[1:])     # how many clicks to turn dial
    if turn[0] == "R":
        pos = (pos + inc) % len(dial)   # using modulo to cycle back through array if out of bounds
    elif turn[0] == "L":
        pos = (pos - inc) % len(dial)
    if dial[pos] == 0:
        count += 1

print(count)