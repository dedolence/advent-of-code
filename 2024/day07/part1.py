"""
292 = 11 ? 6 ? 16 ? 20

[+,+,+]
[+,+,*]
[+,*,*]

[*,*,*]
[*,*,+]
[*,+,+]

[*,+,*]
[+,*,+]


            [+, +, +]
    [+, +]
            [+, +, *]
[+]         
            [+, *, +]
    [+, *]
            [+, *, *]

            [*, +, +]
    [*, +]
            [*, +, *]
[*]
            [*, *, +]
    [*, *]
            [*, *, *]


for test in operands:
    take each test and make two copies. add a + to one and a * to the other
    return with new lists

operands = []
operands = [[+], [*]]
operands = [[+, +], [+, *], [*, +], [*, *]]
...
"""

"""
    This works but it's really slow :(
"""

import re

file_name = "input.txt"


def parse_input(file_name) -> list:
    # take input and reduce to a list of digits (as strings)
    with open(file_name) as file:
        raw = [line.strip() for line in file.readlines()]
        equations = [list(map(int, re.findall(r'\d+',_))) for _ in raw]
        return equations


def build_operator_chains(eqs: int, ops: list = []):
    # this builds out a list of all possible combinations of + and * for a given length equation
    # if there are x number of operators, then the total amount of combinations will be 2^x
    if len(ops) == 2 ** eqs:
        return ops
    
    if len(ops) == 0:
        ops = [["+"], ["*"]]
        return build_operator_chains(eqs, ops)
    
    new_ops = []
    for op in ops:
        o1 = op.copy() + ["+"]
        o2 = op.copy() + ["*"]
        new_ops.append(o1)
        new_ops.append(o2)

    return build_operator_chains(eqs, new_ops)


def parse_chain(operands, chain, i = 0):
    if len(operands) == 0:
        return i
    
    if i == 0:
        i = operands[0]
        return parse_chain(operands[1:], chain, i)
    
    s = f"{i}{chain[0]}{operands[0]}"
    i = eval(s)
    return parse_chain(operands[1:], chain[1:], i)
    


def test_equation(eq):
    target = eq[0]
    operands = eq[1:]
    operator_chains = build_operator_chains(len(eq) - 2)
    totals = [parse_chain(operands, chain) for chain in operator_chains]
    if target in totals: return target
    return False


equations = parse_input(file_name)
total = 0

for eq in equations:
    total += test_equation(eq)

print(total)