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


def get_path(grid):
    obstacle_pos = []
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
    direction = 0
    visited = []
    x, y = starting_pos
    next_tile = grid[y + directions[direction][1]][x + directions[direction][0]]

    while next_tile != "*":
        # check for loops
        set_visited = set(visited)
        if (x, y) in set_visited:
            return True
        
        visited.append((x, y))

        dx, dy = directions[direction][0], directions[direction][1]
        next_tile = grid[y + dy][x + dx]
        
        if next_tile == "#":
            # update the guard's trajectory
            direction = (direction + 1) % len(directions)
            dx, dy = directions[direction][0], directions[direction][1]

        x += dx
        y += dy
    
    return visited


loop_counter = 0
grid = get_grid("test.txt")
starting_pos = find_starting_position(grid)
visited = get_path(grid)
