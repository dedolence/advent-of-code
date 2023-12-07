import re

"""
    How do you isolate the first and last numbers in a mixed alphanumeric string?
    1abc2           [1, 2]
    pqr3stu8vwx     [3, 8]
    a1b2c3d4e5f     [2, 5]
    treb7uchet      [7, 7]
"""
FILENAME = "input.txt"
ANSWER = 0

input = []
with open(FILENAME) as file:
    input = [line.strip() for line in file.readlines()]

for line in input:
    line = re.sub('\D', '', line)       # remove non-digits from string
    nums = int(line[0] + line[-1])      # retain only first and last digit, convert to integer
    ANSWER += nums                      # add to running total


print(ANSWER)