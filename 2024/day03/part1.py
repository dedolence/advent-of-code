import re

#input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open("input.txt") as file:
    input = file.read()

p = re.compile("mul\(\d{1,3},\d{1,3}\)")

matches = p.findall(input)

total = 0

for m in matches:
    nums = re.findall("\d+", m)
    total += int(nums[0]) * int(nums[1])

print(total)