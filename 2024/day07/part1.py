"""
    888-633-3797
    act #: 1002236955
"""
import re

file_name = "test.txt"


def parse_input(file_name) -> list:
    with open(file_name) as file:
        raw = [line.strip() for line in file.readlines()]
        operators = [list(map(int, re.findall('\d+',_))) for _ in raw]
        return operators

operators = parse_input(file_name)

total = 0

for o in operators:
    sum_product = o[0]
    factors = o[1:]