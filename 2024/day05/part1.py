"""
This feels a bit messy/brute-force.
Every page in the update has a given number of pages that must come before it.
So we create a dict where each key is a page, and its value is a list of these
pages that must come before it.
We then go through the pages in an update, checking each page against all the
pages that come before it, and making sure they appear in our master list of
leading pages. If a number ISN'T in that list, it is breaking the rule, because
that list is exhaustive.
"""

from collections import defaultdict
from typing import List

with open("input.txt") as file:
    inp = file.read().split("\n\n")
    rules = [line.strip() for line in inp[0].split("\n")]   # ['47|53', '97|13', ...]
    updates = [line.strip() for line in inp[1].split("\n")]   # ['75,47,61,53,29', '97,61,53,29,13', ...]


def parse_rules(rules: List[list]) -> defaultdict:
    # each key has a list of values that must come BEFORE the key
    d = defaultdict(list)
    for r in rules:
        a, b = r.split("|")
        d[b].append(a)
    return d


def check_update(update: List[int], rules: defaultdict) -> bool:
    for i, page in enumerate(update):
        leading = update[:i]
        for l in leading:
            if l not in rules[page]: return False
    return True        

correct = []
for update in updates:
    update = [i for i in update.split(",")]
    if check_update(update, parse_rules(rules)):
        correct.append(int(update[len(update)//2])) # // is floor division, i always forget this one

print(sum(correct))