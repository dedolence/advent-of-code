"""
process is as follows:
1) take the input and split it into a list, map all numbers to integers.
2) start a total (our output) at 0. for each equation in our input:
    1) build out a list of all possible combinations of +, *, and ||.
    2) test each one of those operator chains to see if it produces our target.
        1) take first two numbers and perform the operator to them
        2) recurse with the next two numbers until all are operated on.
3) if any chain produces target, return target and add to total.

it is VERY slow, like, it takes several minutes. one way to speed this up would be to forego 
producing a list of all possible operator combinations, and instead test one combination at 
a time, stopping if the target is reached. 

looking through other people's answers and it appears i've overcomplicated this.
i could have just done a recursion the returns three functions for each operator.

feeling pretty bad about this one tbh!
"""

import re

file_name = "input.txt"


def parse_input(file_name) -> list:
    # take input and reduce to a list of digits (as strings)
    with open(file_name) as file:
        raw = [line.strip() for line in file.readlines()]
        equations = [list(map(int, re.findall(r'\d+',_))) for _ in raw]
        return equations


def build_operator_chains(length = 0, chains: list = []):
    # this builds out a list of all possible combinations of +, *, and || for a given length equation
    # if there are x number of operands, then the total amount of combinations will be 3^x
    if len(chains) == 3 ** length:
        return chains
    
    if len(chains) == 0:
        chains = [["+"], ["*"], ["||"]]
        return build_operator_chains(length, chains)
    
    new_chains = []
    for op in chains:
        chain_1 = op.copy() + ["+"]
        chain_2 = op.copy() + ["*"]
        chain_3 = op.copy() + ["||"]
        new_chains.extend([chain_1, chain_2, chain_3])
        
    return build_operator_chains(length, new_chains)


def test_equation(target, operands, operator_chains):
    # runs each possible combination of +, *, and || through a test 
    for chain in operator_chains:
        if test_chain(target, operands, chain):
            return target
    return False


def eval_chain(a, b, o):
    if o == "||":
        return int(f"{a}{b}")
    else:
        return eval(f"{a}{o}{b}")


def test_chain(target, operands, operators, running_total = 0):
    # tests a single chain of +, *, and || to see if they produce the target number
    if len(operands) == 0:
        if running_total == target: return True
        else: return False

    if running_total == 0:
        running_total = operands[0]
        return test_chain(target, operands[1:], operators, running_total)
    
    # test for concatenation
    running_total = eval_chain(running_total, operands[0], operators[0])
    
    return test_chain(target, operands[1:], operators[1:], running_total)
    

total = 0
equations = parse_input(file_name)
for eq in equations:
    target = eq[0]
    operands = eq[1:]
    # there will be one fewer operator than operand, e.g. 1 + 1 + 1 is 3 operands, 2 operators
    length_of_operator_chain = len(operands) - 1
    operator_chains = build_operator_chains(length_of_operator_chain)
    total += test_equation(target, operands, operator_chains)
print(total)