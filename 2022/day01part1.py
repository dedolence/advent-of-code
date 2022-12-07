f = open("inputs/day1.txt")
highest = 0
current = 0
for line in f:
    if line != "\n":
        current += int(line)
    else:
        if current > highest:
            highest = current 
        current = 0

print(highest)