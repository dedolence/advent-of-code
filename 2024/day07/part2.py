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


for test in operators:
    take each test and make two copies. add a + to one and a * to the other
    return with new lists

operators = []
operators = [[+], [*]]
operators = [[+, +], [+, *], [*, +], [*, *]]
...
"""

"""
    This works but it's really slow :(
"""

import re

file_name = "test.txt"


def parse_input(file_name) -> list:
    # take input and reduce to a list of digits (as strings)
    with open(file_name) as file:
        raw = [line.strip() for line in file.readlines()]
        equations = [list(map(int, re.findall(r'\d+',_))) for _ in raw]
        return equations


def build_operator_chains(l: int, ops: list = []):
    # this builds out a list of all possible combinations of + and * for a given length equation
    # if there are x number of operators, then the total amount of combinations will be 2^x
    if len(ops) == 2 ** l:
        return ops
    
    if len(ops) == 0:
        ops = [["+"], ["*"]]
        return build_operator_chains(l, ops)
    
    new_ops = []
    for op in ops:
        o1 = op.copy() + ["+"]
        o2 = op.copy() + ["*"]
        new_ops.append(o1)
        new_ops.append(o2)

    return build_operator_chains(l, new_ops)


def parse_chain(operands, chain):
    pass


def mate_lists(operands, operators):
    # operators will always be 1 shorter than operands
    # add an extra operator that does nothing to the end
    operators += ["+0"]

    c = []
    for i, o in enumerate(operands):
        c += [operands[i]] + [operators[i]]
    
    return c


def test_equation(eq):
    target = eq[0]
    operands = eq[1:]
    operator_chains = build_operator_chains(len(operands) - 1)  # there will be 1 fewer operators than operands
    mated_lists = [mate_lists(operands, chain) for chain in operator_chains]
    print(mated_lists)
    


equations = parse_input("test.txt")
for eq in equations:
    test_equation(eq)