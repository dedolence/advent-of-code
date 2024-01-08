filename = "input.txt"
values = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

"""
two1nine            = 2 + 9 = 11
eightwothree        = 8 + 3 = 11
abcone2threexyz     = 1 + 3 = 4
xtwone3four         = 2 + 4 = 6
4nineeightseven2    = 4 + 2 = 6
zoneight234         = 1 + 4 = 5
7pqrstsixteen       = 7 + 6 = 7
"""


# format input
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

#input = ["8zfgtfnxvjjxgptxkpkdb1gkndcsbgvzxgqg1oneightq"]

pairs = []

for line in input:
    l = len(line)
    ds = []
    for i,c in enumerate(line):
        if line[i].isdigit():
            ds.append(line[i])
        else:
            for k in values.keys():
                if line[i:].startswith(k):
                    ds.append(values[k])
    pairs.append(int(f"{ds[0]}{ds[-1]}"))

print(sum(pairs))