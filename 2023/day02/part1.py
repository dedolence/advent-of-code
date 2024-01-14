"""
    So ugly! 
"""
import re
filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

total = 0
limits = {"r": 12, "g": 13, "b": 14}

def validate_set(s):
    """
        Splits each set: ["3 g", "4 r"] -> [["3", "g"], ["4", "r"]]
        Then checks the integer against its corresponding letter in the
        limits dict.
    """
    sp = [i.split(" ") for i in s]
    return all([int(j[0]) <= limits[j[1]] for j in sp])

for i, line in enumerate(input, start=1):
    """
        The first step is to reduce each line (game) into its individual sets.
        Each set is simplified to just the number and a single letter, like ["3 g", "4 r"].
        It then runs each set through a validation, and if they all return True, 
        that game's number gets added to the total.
    """
    sets = [re.findall('\d+\s[r|g|b]', s) for s in line.split(";")]
    if all([validate_set(s) for s in sets]): total += i

print(total)