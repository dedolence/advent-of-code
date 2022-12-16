"""
Sadly i could NOT get this one and had to look up someone else's answer.
i was close!
"""

from collections import defaultdict

INPUT: list = [line.strip() for line in open("inputs/day7.txt")]
TOTAL_DISK_SIZE = 70000000
REQUIRED_UNUSED_SPACE = 30000000
FILEPATHS: list = []
SIZES: defaultdict = defaultdict(int)
DELETION_SIZE = 0   # must delete this much to free up enough space
FREE_SPACE = 0
MAXSIZE = 100000
TOTAL = 0
BIG_DEEZE = []

for line in INPUT:
    if line.startswith("$ ls"):
        continue

    elif line.startswith("$ cd"):
        l = line.split()
        if l[2] == "..":
            FILEPATHS.pop()
        else:
            FILEPATHS.append(l[2] if l[2] != "/" else "root")
            
    else:
        if line.split()[0].isdigit():
            for i in range(len(FILEPATHS)+1):
                join = "/".join(FILEPATHS[:i])
                size = int(line.split()[0])
                SIZES[join] += size

# calculate how much we need to delete for part 2
FREE_SPACE = TOTAL_DISK_SIZE - SIZES['']
DELETION_SIZE = REQUIRED_UNUSED_SPACE - FREE_SPACE

for dir in SIZES:
    if SIZES[dir] <= MAXSIZE:
        TOTAL += SIZES[dir]

    if SIZES[dir] >= DELETION_SIZE:
        BIG_DEEZE.append(SIZES[dir])

print("Part one: ", TOTAL)
print("Part two: ", min(BIG_DEEZE))