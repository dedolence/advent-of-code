t = 0
# feed input by running script: python3 day04part1.py < inputs/day4.txt
for line in open(0):
    a, b = line.split(",")
    ar = [i for i in range(int(a.split('-')[0]), int(a.split('-')[1])+1)]
    br = [i for i in range(int(b.split('-')[0]), int(b.split('-')[1])+1)]
    if all(item in ar for item in br) or all(item in br for item in ar):
        t += 1
print(t)