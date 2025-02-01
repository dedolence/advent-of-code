"""
Well I quite liked this solution, which i think WOULD have worked, except it hits
a recursion limit. then if i set the limit higher i end up just getting a seg fault
and python crashes. 
"""

import re

def reduce_instructions(input: str, output: str = "", flag: bool = True):
    if input == "":
        return output
    
    if input.startswith("do()"):
        flag = True
    if input.startswith("don't()"):
        flag = False

    if flag:
        output += input[0]

    return reduce_instructions(input[1:], output, flag)


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