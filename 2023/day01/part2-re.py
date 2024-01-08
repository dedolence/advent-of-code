"""
    Fails: does not account for overlapping words. "oneight" returns only "one" not "eight".
"""

import re

filename = "input.txt"
answer = 0
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

input = ["8zfgtfnxvjjxgptxkpkdb1gkndcsbgvzxgqg1oneightq"]
for line in input:
    subs = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    print(subs)
    firstlast = [subs[0], subs[-1]]
    for i, w in enumerate(firstlast):
        if w in values:
            firstlast[i] = values[w]
    answer += int("".join(firstlast))
    
print(answer)