import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

"""
(-1, -1)    (0, -1)     (+1, -1)
(-1,  0)    (0,  0)     (+1,  0)
(-1, +1)    (0, +1)     (+1, +1)
"""
""" 
this method searches around groups of numbers

nums = {}

def parse_line(line):
    line_iter = re.finditer("\d+", line)
    for match_obj in line_iter:
        # num.group() = the number itself
        # num.span() = beginning/end index of the number. +/- 1 to account for edges
        b = match_obj.span()[0] - 1
        e = match_obj.span()[1] + 1
        nums[match_obj.group()] = (b, e)

parse_line("..35..633.")

print(nums) 
"""

"""
this method searches around symbols
"""
symbols = set()
for line in input:
    for i, c in enumerate(line):
        if c != '.' and not c.isdigit():
            symbols.add(c)

print(symbols)