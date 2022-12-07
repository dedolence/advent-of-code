with open("inputs/day03.txt") as file:
    all_lines = [line.strip() for line in file.readlines()]

key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority_key = {key[i]: i+1 for i in range(0, 52)}

def find_common_item(group):
    """
        Remove duplicates from each item using set(),
        then count the occurences of each character.
    """
    joined = ''.join([''.join(set(item)) for item in group])
    for char in joined:
        if joined.count(char) == len(group):
            return char


def group_and_reduce(input: list, grouping: int, common_items: list = []):
    """
        Groups puzzle inputs, finds their common item, reduces the
        input, and returns itself until the input list is empty.
    """
    if len(input) == 0:
        return common_items

    common_item = find_common_item(input[:grouping])
    common_items.append(priority_key[common_item])
    input = input[grouping:]
    return group_and_reduce(input, grouping, common_items)


def part_1(input):
    """
        Takes each line of input and splits it in half.
    """
    output = []
    for line in input:
        output.append(line[:int(len(line)/2)])
        output.append(line[int(len(line)/2):])
    return output

print("Part 1: ", sum(group_and_reduce(part_1(all_lines), 2, [])))
print("Part 2: ", sum(group_and_reduce(all_lines, 3, [])))