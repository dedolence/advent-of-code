"""
what is the condition that triggers a loop?
same direction, same position.
so a list of directions and positions:
[(d1, p1), (d2, p2), (d3, p3), (d4, p4)]
if the next added d/p is (d2, p2), then it will cause a loop:
[(d2, p2), (d3, p3), (d4, p4)]

so, starting at the second guard position, add an obstacle at each
point, then count ahead from that obstacle. if the guard leaves the
area, discard that obstacle and start again. if the guard ends up
at the same position with the same trajectory, add to the loop counter.

don't have to start from the beginning each time. whether a loop is
found or not, start from the position of that obstacle.
"""


def new_direction(current_direction: int = 0) -> int:
    # increment to the last one, then loop back to 0
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
    return (current_direction + 1) % len(directions)


def find_starting_position(grid: list) -> tuple:
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "^":
                return (x, y)

        
def get_grid(file_name: str) -> list:
    with open(file_name) as file:
        grid = ["*" + line.strip() + "*" for line in file.readlines()]
        pad_row = "*" * len(grid[0])
        grid = [pad_row] + grid + [pad_row]
        return grid

loop_counter = 0
grid = get_grid("test.txt")
starting_pos = find_starting_position(grid)
obstacle_pos = []
directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
direction = 0
visited = []

def loop(grid: list, x: int, y: int, directions: tuple, current_dir: int = 0) -> list:
    # grid = whole field grid
    # x, y = current guard position
    # directions = tuple containing the possible directions the guard can walk
    # current_dir = index of the tuple indicating guard's current trajectory
    #print(i)
    dx, dy = directions[current_dir][0], directions[current_dir][1]
    next_tile = grid[y + dy][x + dx]
    visited.append((x, y))

    if next_tile == "*":
        return
    
    if next_tile == "#":
        # alter direction but don't alter current tile
        # this equation makes it so the index loops back to 0 when it reaches the last tuple
        current_dir = (current_dir + 1) % len(directions)
    else:
        # alter current tile but don't change direction
        x += dx
        y += dy
    
    #draw(x, y)
    return loop(grid, x, y, directions, current_dir)

guard_path = loop(grid, starting_pos[0], starting_pos[1], directions, direction)
print(len(visited))

def obstacle(grid: list, original_path: list, loops: list, current_index: int = 0):
    if current_index == len(original_path):
        # reached the end of the path and checked every possible obstacle
        return loops
    
    current_tile: tuple = original_path[current_index]
    next_tile: tuple = original_path[current_index + 1]
    x, y = current_tile

    