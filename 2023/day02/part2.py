"""
    Reduces each input line to a key/value; key being the color and value being the number.
    Iterates over the sets and keeps the highest value.
"""

# setup
import re
filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]
total = 0



# logic
for line in input:
    game = {"r": 0, "g": 0, "b": 0}
    reduced = re.findall('\d+\s[r|g|b]', line)  # = ['3 b', '4 r', '1 r', '2 g', '6 b', '2 g']
    for i in reduced:
        n, l = i.split(" ")
        n = int(n)
        if n > game[l]: game[l] = n
    power = game["r"] * game["g"] * game["b"]
    total += power

print(total)