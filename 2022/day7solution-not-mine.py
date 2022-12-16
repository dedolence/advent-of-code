# import modules
from collections import defaultdict

# initialise variables
terminal_output = []
filepath = []
sizes = defaultdict(int)
total = 0
max_size = 100000

# read input file
with open('inputs/day7.txt', 'r') as file:
    for line in file:
        terminal_output.append(line.strip())

# parse input commands
for line in terminal_output:
    # change directories
    if(line.startswith('$ cd')):
        directory = line.split()[-1]
        # go to previous directory
        if(directory == '..'):
            filepath.pop()
        # add directory to filepath
        else:
            filepath.append(directory)
    
    # list contents
    elif(line.startswith('$ ls')):
        continue
    
    # parse ls output for sizes
    else:
        size, _ = line.split()
        if(size.isdigit()):
            size = int(size)
            for i in range(len(filepath)):
                sizes['/'.join(filepath[:i+1])] += size

# calculate sum of directories with size at most 100k
for key, value in sizes.items():
    if(value <= max_size):
        total += value

# print answer
print(total)
