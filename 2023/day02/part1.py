import re
filename = "test.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

red:    <= 12
green:  <= 13
blue:   <= 14
"""

for i, line in enumerate(input, start=1):
    sets = line.split(";")
    splits = [re.findall('\d+\s[r|g|b]', s) for s in sets]
    """ for s in sets:
        splits.append(re.findall('\d+\s[r|g|b]', s))
         """

    print(splits)