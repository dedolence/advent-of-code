"""
    i think i have a better way of doing this using while() instead of recursion in part 2.
"""

import os, sys
from time import sleep
sys.setrecursionlimit(10000)

def draw(x: int, y: int):
    os.system('clear')
    new_grid = default_grid
    line = [c for c in new_grid[y]]
    line[x] = "O"
    line = "".join(line)
    new_grid[y] = line
    for line in new_grid:
        print(line)
    

with open("input.txt") as file:
    # because python allows negative indices i like to pad
    # these grids with a terminal character, in this case *
    grid = ["*" + line.strip() + "*" for line in file.readlines()]
    pad_row = "*" * len(grid[0])
    grid = [pad_row] + grid + [pad_row]
    default_grid = grid

# trajectories of the guard, in order of the turns she makes, delta x, delta y
directions = ((0, -1), (1, 0), (0, 1), (-1, 0))

def loop(grid: list, x: int, y: int, directions: tuple, current_dir: int = 0, visited: list = [], i: int = 0):
    # grid = whole field grid
    # x, y = current guard position
    # directions = tuple containing the possible directions the guard can walk
    # current_dir = index of the tuple indicating guard's current trajectory
    #print(i)
    dx, dy = directions[current_dir][0], directions[current_dir][1]
    next_tile = grid[y + dy][x + dx]
    visited.append((x, y))

    if next_tile == "*":
        return visited
    
    if next_tile == "#":
        # alter direction but don't alter current tile
        # this equation makes it so the index loops back to 0 when it reaches the last tuple
        current_dir = (current_dir + 1) % len(directions)
    else:
        # alter current tile but don't change direction
        x += dx
        y += dy
    
    #draw(x, y)
    return loop(grid, x, y, directions, current_dir, visited, i + 1)


# find starting position
def get_start():
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "^":
                return (x, y)


init = get_start()
x, y = init[0], init[1]
visited = loop(grid, x, y, directions, 0, [])
# visited is a list of all coordinates visited by the guard, but includes duplicates
print(len(set(visited)))