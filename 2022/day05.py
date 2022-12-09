"""
Create "stacks": lists
"""
import re

# create lists of stacks (along x-axis and not y)
stacks = []
with open("inputs/day5.txt") as file:
    input = file.readlines()
    for col in range(0, len(input[0])):
        stacks.append("")
        for line in range(0,8):
            if input[line][col] not in ["[", "]", " "]:
                stacks[col] += input[line][col]

# remove empty lists and list of trailing newlines
stacks = [stack for stack in stacks if stack != ''][:-1]

# remove stack diagram from input, reduce to only integers
# instructions are now [Digit, Digit, Digit]: move n from x1 to x2
input = [[int(d) for d in re.findall(r"\d+", line.strip())] for line in input[10:]]

for instruction in input:
    amount = instruction[0]
    from_stack = stacks[instruction[1] - 1]
    to_stack = stacks[instruction[2] - 1]
    

    temp_stack = from_stack[:amount]
    stacks[instruction[1] - 1] = from_stack[amount:]
    
    # in part 1, temp_stack gets reversed ([::-1]) to account
    # for the crane moving each object one at a time.
    # for part 2, just remove the ([::-1]) to preserve the
    # order. easy!
    stacks[instruction[2] - 1] = temp_stack[::-1] + to_stack

print("".join([stack[0] for stack in stacks]))