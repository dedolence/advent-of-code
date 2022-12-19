"""
    1: pad the input with "x"s to help check for edges.
    2: flatten the 2-d input to a 1-d string.
    3: For each tree, recursively check the next tree in line by adding
        or subtracting an offset (+/- 1 for the X dimension, or +/- length
        of the line to check other rows.)

    Test input reference: 

    x x x x x x x     0  - 6
    x 3 0 3 7 3 x     7  - 13
    x 2 5 5 1 2 x     14 - 20
    x 6 5 3 3 2 x     21 - 27
    x 3 3 5 4 9 x     28 - 34
    x 3 5 3 9 0 x     35 - 41
    x x x x x x x     42 - 48
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
    """
        Recursively checks neighboring trees by getting their value using 
        an index of the treeline string. Offset controls the "direction" to 
        find neighbors in, equaling the length of a row for searching in the
        vertical directions.

        Attempts to cast the neighbor to an int, which will fail if an edge is
        reached (edges are "x"s).

        Compares the tree heights, returning False and adds one to the tree's
        scenic score if the neighbor is as tall or taller.

        If the neighbor is shorter, adds one to its scenic score and calls
        itself to check the next neighbor in line.
    """
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

    # takes the dict of keys (tree indices) and values (list of 4 scenic
    # scores, one for each direction) and flattens it to just the product
    # of those scores, then returns the highest value.
    scenic_score = max(map(lambda t: prod(t[1]), scenic_trees.items()))

    print("Part one: ", visible)
    print("Part two: ", scenic_score)


if __name__ == "__main__":
    main()
