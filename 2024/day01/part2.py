with open("input.txt") as file:
    # go through list once, divying up numbers into inputs and frequencies
    inputs = []
    frequencies = []
    for line in file.readlines():
        inputs.append(int(line[0]))
        frequencies.append(int(line[-2]))

    values = []
    for i in inputs:
        c = frequencies.count(i)
        values.append(i * c)

    print(sum(values))