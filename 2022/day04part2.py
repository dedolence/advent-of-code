t = 0
for line in open(0):
    a, b = line.split(",")
    ar = [i for i in range(int(a.split('-')[0]), int(a.split('-')[1])+1)]
    br = [i for i in range(int(b.split('-')[0]), int(b.split('-')[1])+1)]
    if set(ar) & set(br):
        t += 1

print(t)