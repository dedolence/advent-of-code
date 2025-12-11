
from collections import defaultdict
from typing import List
import sys

sys.setrecursionlimit(10**5)        # love having to do this

with open("input.txt") as file:
    inp = file.read().split("\n\n")
    rules = [line.strip() for line in inp[0].split("\n")]   # ['47|53', '97|13', ...]
    updates = [line.strip() for line in inp[1].split("\n")]   # ['75,47,61,53,29', '97,61,53,29,13', ...]


# create two dicts:
# leading: for each key page, a list of pages that must come BEFORE it
# trailing: for each key page, a list of pages that must come AFTER it
leading = defaultdict(list)
trailing = defaultdict(list)
for rule in rules:
    a, b = rule.split("|")
    leading[int(b)].append(int(a))
    trailing[int(a)].append(int(b))


def check_update(update: List[int]) -> bool:
    for i, page in enumerate(update):
        leads = update[:i]
        for l in leads:
            if l not in leading[page]: return False
    return True


def fix_update(update, i = 1):
    # bubble sort!
    if i == len(update):
        return update
    
    a, b = update[i - 1], update[i]

    if a not in leading[b] or b not in trailing[a]:
        update[i - 1], update[i] = update[i], update[i - 1]
        return fix_update(update)
    
    return fix_update(update, i + 1)


correct = []
incorrect = []
for update in updates:
    update = [int(i) for i in update.split(",")]
    if check_update(update):
        correct.append(update[len(update)//2])
    else:
        incorrect.append(fix_update(update)[len(update)//2])

    
print(f"Part 1: {sum(correct)}")
print(f"Part 2: {sum(incorrect)}")
