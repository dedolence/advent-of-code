"""
This works but i don't like it as much as my recursive solution which crashes Python.
All it does is look for the index of the start of a "don't()" block, read ahead until
it finds the index of the next "do()" and slices out that chunk, then just sends it to
the regex function from part 1's solution.
"""

import re

#input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def reduce_instructions(input: str):
    for i in range(len(input)):
        if input[i:].startswith("don't()"):
            n = i
            while input[n:n+4] != "do()":
                n += 1
            input = input[0:i] + input[n:]
    return input


with open("input.txt") as file:
    input = file.read()
    input = reduce_instructions(input)

p = re.compile("mul\(\d{1,3},\d{1,3}\)")

matches = p.findall(input)

total = 0

for m in matches:
    nums = re.findall("\d+", m)
    total += int(nums[0]) * int(nums[1])

print(total)