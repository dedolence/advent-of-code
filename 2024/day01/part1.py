"""
    Parse two columns into two lists.
    Order both lists ascending.
    Find difference between values at index n of each list.
    Answer: sum total of differences.
"""
column_a = []
column_b = []

with open("input.txt") as file:
    line_counter = 0
    for line in file.readlines():
        a, b = line.split("   ")
        column_a.append(int(a))
        column_b.append(int(b))
        
a, b = sorted(column_a), sorted(column_b)

paired = list(zip(a, b))

differences = map(lambda d: abs(d[1] - d[0]), paired)

print(sum(list(differences)))