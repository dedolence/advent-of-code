with open("input.txt") as file:
    # because python allows negative index values we need to add a border
    # of "." all the way around to prevent wraparound false-positives.
    input = ["." + line.strip() + "." for line in file.readlines()]
    pad_row = "." * len(input[0])
    input = [pad_row] + input + [pad_row]


def check(coords, direction):
    row, col = coords 
    x, y = direction

    def rec(i = 0, s = ""):
        if i == 4: return s
        else:
            try:
                s += input[row + y * i][col + x * i]    # shoutout PEMDAS
            except IndexError:
                return False
            return rec(i + 1, s)
        
    return rec() == "XMAS"


total = 0
for r, row in enumerate(input):
    for c, char in enumerate(row):
        total += check((r, c), (0, 1))      # i actually hate the repetition here
        total += check((r, c), (0, -1))     # (and i hate nested for loops)
        total += check((r, c), (1, 0))      # but at the moment i can't think of 
        total += check((r, c), (-1, 0))     # a way that avoids it.
        total += check((r, c), (1, 1))
        total += check((r, c), (1, -1))
        total += check((r, c), (-1, -1))
        total += check((r, c), (-1, 1))


print(total)