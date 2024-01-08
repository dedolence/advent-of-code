
"""
    Fails. The answer is wrong due to line.index() returning the FIRST index encountered
    of the digit in question. 8 appears twice, at [21] and [26], but when the iterator 
    gets to the last instance, it calls line.index() which returns only 8's first 
    instance [21].
"""
filename = "input.txt"
answer = 0
values = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

# format input
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]


input = ["bjgtmdrgrrrpxndlmvmgl829428"]
input = ["two356two"]
for line in input:
    # create and sort a list by the index of any number that is a word that appears in the line
    num1 = sorted([(line.index(word),  values[word]) for word in values.keys() if word in line])
    print(num1)

    # create and sort a list by the index of any number that is a digit that appears in the line
    num2 = sorted([(line.index(char), char) for char in line if char.isdigit()])
    print(num2)

    # combine into one list, sorted by their index in the line
    nums = sorted(num1 + num2)
    print(nums)

    # take the first and last of those and cast them to an integer
    outernums = int(nums[0][1] + nums[-1][1])
    print(outernums)

    # add that integer to the running total
    answer += outernums
   
print(answer)