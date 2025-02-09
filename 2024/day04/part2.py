"""
    Find every "A".
    Get a 3x3 with an A at the center.
    Build a string of in the shape of a / and a \.
    Check to see if the strings are either MAS or SAM.
    If both slashes match, add to total.
"""

with open("input.txt") as file:
    # pad the input to avoid negative index wraparound
    input_grid = ["." + line.strip() + "." for line in file.readlines()]
    pad_row = "." * len(input_grid[0])
    input_grid = [pad_row] + input_grid + [pad_row]

total = 0
for y, row in enumerate(input_grid):
    for x, col in enumerate(row):
        if input_grid[y][x] == "A":
            block = [input_grid[y-1][x-1:x+2], input_grid[y][x-1:x+2], input_grid[y+1][x-1:x+2]]
            forward = block[0][0] + block[1][1] + block[2][2]
            backwards = block[0][2] + block[1][1] + block[2][0]
            if (forward == "MAS" or forward == "SAM") \
                and (backwards == "MAS" or backwards == "SAM"):
                total += 1

print(total)