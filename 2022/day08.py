"""
    - The input is padded with "x"s all around to help check for the 
    edges, i.e.:
        x x x x x x x
        x 3 0 3 7 3 x
        x 2 5 5 1 2 x
        x 6 5 3 3 2 x
        x 3 3 5 4 9 x
        x 3 5 3 9 0 x
        x x x x x x x
    - The grid is flattened to a single one-line string, i.e.:
        "xxxxxxx30373xx25512xx65..."
    - For each character of the input string, if it is a digit, check if it is
    visible in each of the four directions.
    - Visibility is checked recursively by adding an offset to the tree's index.
    Checking vertically is done by setting the offset to the length of a row.
    - If an edge is reached (an "x"), a ValueError will be thrown, indicating
    that the tree is visible all the way to an edge.
    - Otherwise, the heights are compared; if shorter, the function is called
    again with the next neighbor; if taller, the function returns false (the 
    tree is not visible in that direction).
    - Meanwhile, each time a shorter tree is encountered, that tree's scenic
    score is incremented, as stored in a dict, with the key as the tree's index,
    and the value being a list of 4 integers, one score for each direction.
"""

from collections import defaultdict
from math import prod

visible: int = 0                    # Part 1
scenic_trees = defaultdict(list)    # Part 2

# format puzzle input
all_lines: list = ["x" + line.strip() + "x" 
    for line in open("inputs/day8.txt")]
line_length: int = len(all_lines[0])
treeline: str = "".join(["x" * line_length] + all_lines + ["x" * line_length])

def visible_in_direction(
    i: int, 
    x: int, 
    offset: int,
    c: int = 0) -> bool:

    try:
        if int(treeline[x + offset]) >= int(treeline[i]):
            scenic_trees[i].append(c+1)
            return False
        
        else:
            return visible_in_direction(i, x + offset, offset, c + 1)
    
    except ValueError:
        scenic_trees[i].append(c)
        return True
    

def main():
    global visible

    for i, tree in enumerate(treeline):
        if tree.isdigit():
            top = visible_in_direction(i, i, -line_length)
            left = visible_in_direction(i, i, -1)
            right = visible_in_direction(i, i, 1)
            bottom = visible_in_direction(i, i, line_length)

            if right or left or top or bottom: 
                visible += 1

    scenic_score = max(map(lambda t: prod(t[1]), scenic_trees.items()))

    print("Part one: ", visible)
    print("Part two: ", scenic_score)


if __name__ == "__main__":
    main()
