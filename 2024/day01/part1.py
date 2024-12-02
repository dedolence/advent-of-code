input = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()


a = []
b = []
for line in input.split("\n"):
    a.append(int(line[0]))
    b.append(int(line[-1]))

a, b = sorted(a), sorted(b)