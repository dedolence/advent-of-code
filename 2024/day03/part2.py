import re

# set start and ending triggers to the input
input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

p1 = re.compile("""
    \S+
    don't\(\)\S+do\(\)
""", re.VERBOSE | re.MULTILINE)

print(p1.findall(input))