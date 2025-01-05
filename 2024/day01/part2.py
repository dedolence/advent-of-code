with open("input.txt") as input:
    inputs = []
    frequencies = []
    for line in input.readlines():
        line = line.strip()
        a, b = line.split("   ")
        inputs.append(int(a))
        frequencies.append(int(b))

    similarities = []

    for num in inputs:
        c = frequencies.count(num)
        similarities.append(num * c)

    print(sum(similarities))