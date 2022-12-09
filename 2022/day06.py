def detect(set_length):
    with open("inputs/day6.txt") as input:
        line = input.readline()
        for i in range(0, len(line)):
            if len(set(line[i:i+set_length])) == set_length:
                return i+set_length

print("Part 1: ", detect(4))
print("Part 2: ", detect(14))