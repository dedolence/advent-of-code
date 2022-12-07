with open("inputs/day03.txt") as file:
    input = [string.strip() for string in file.readlines()]

""" 
input = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]
"""

key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority_key = {key[i]: i+1 for i in range(0, 52)}  # {'a': 1, 'b': 2, ...}
priorities = 0

for string in input:
    # int() because division creates a float and throws slice error
    half = int(len(string)/2)
    # reduce to a set to avoid double counting the matching character
    tup = (set(string[:half]), set(string[-half:]))
    for char in tup[0]:
        if char in tup[1]:
            priorities += priority_key[char]

print(priorities)