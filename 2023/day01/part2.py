"""
    I really am not super proud of this answer. It works, but at the cost of several nested for loops
    (one for iterating over every line, then iterating over each character, then iterating over values).

    One approach I didn't try is looking for the first value, then reversing the string and doing it again.
"""

filename = "input.txt"
values = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
pairs = []

# format input
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]


for line in input:
    digits = []

    for i,c in enumerate(line):
        if line[i].isdigit():
            digits.append(line[i])

        else:
            for k in values.keys():
                if line[i:].startswith(k):
                    digits.append(values[k])

    pairs.append(int(f"{digits[0]}{digits[-1]}"))

print(sum(pairs))