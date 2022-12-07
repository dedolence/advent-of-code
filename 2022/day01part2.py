f = open("inputs/day1.txt")
groups = [0, 0, 0]
highest = 0
current = 0


def rank(i, t):
    if i >= 2:
        return

    if t > groups[i]:
        groups.insert(i, t)
        groups.pop()
        return
    
    i += 1
    return rank(i, t)


for line in f:
    if line != "\n":
        current += int(line)
    else:
        rank(0, current)
        current = 0

print(sum(groups))