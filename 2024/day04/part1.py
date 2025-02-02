

with open("test.txt") as file:
    input = [line.strip() for line in file.readlines()]

def horizontal(input):
    return "".join(input)

def vertical(input):
    vert = []
    s = ""
    for i, col in enumerate(input[0]):
        for row in input:
            s += row[i]
        vert.append(s)
        s = ""
    return "".join(vert)

def diagonal(input):
    


def count_xmases(input: str):
    return input.count("XMAS") + input.count("SAMX")

print("Horizontal XMASes: ", count_xmases(horizontal(input)))
print("Vertical XMASes: ", count_xmases(vertical(input)))