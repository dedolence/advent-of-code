file = open("inputs/day7.txt")
input = [line.strip() for line in file.readlines()]

dirs = {}
for line in input:
    if "$ cd" in line:
        l = line.split()
        name = l[2]
        dirs[name] = 0

for i in range(0, len(input)):
    line = input[i].split()
    if line[0].isnumeric():
        cursor = i
        while True:
            cursor -= 1
            l = input[cursor].split()
            if "$" in l and "cd" in l:
                dirs[l[2]] += int(line[0])
                break

t = 0
for dir in dirs:
    size = dirs[dir]
    if size <= 100000:
        t += size

print(t)