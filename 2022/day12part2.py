"""
    Uses a breadth-first search algorithm with tracking paths.
    Borrowed/stole extensively from the tutorial code found here: 
    https://www.redblobgames.com/pathfinding/a-star/introduction.html
"""

from queue import Queue

FILENAME = "inputs/day12.txt"

MAZE = [[i for i in row.strip()] for row in open(FILENAME).readlines()]
HEIGHT = len(MAZE)
WIDTH = len(MAZE[0])

# since this is part 2, origin will be "E"
# and the "S" becomes a regular "a"
for i in range(HEIGHT):
    for j in range(WIDTH):
        if MAZE[i][j] == "S":
            MAZE[i][j] = "a"
        if MAZE[i][j] == "E":
            ORIGIN = (j, i)

MAZE[ORIGIN[1]][ORIGIN[0]] = "z"

def get_neighbors(coord: tuple[int, int]) -> list[tuple[int, int]]:
    x = coord[0]
    y = coord[1]
    cardinal_dirs = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]

    #filter out coordinates outside the grid
    neighbors = filter(
        lambda p: p[0] in range(WIDTH) and p[1] in range(HEIGHT),
        cardinal_dirs)

    # filter out neighbors that don't pass elevation check
    c = ord(MAZE[y][x])
    return filter(lambda p: ord(MAZE[p[1]][p[0]]) + 1 >= c, neighbors)


def main():
    frontier = Queue()
    frontier.put(ORIGIN)

    # Given path A -> B, came_from[B] == A.
    # If not concerned about paths, this could just be
    # a list of visited points.
    came_from = dict()
    came_from[ORIGIN] = None

    while not frontier.empty():
        current = frontier.get()

        # once an "a" is reached, set it as the endpoint
        if MAZE[current[1]][current[0]] == "a":
            ENDPOINT = current
            break

        for next in get_neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    # now get path from start to finish by walking
    # backwards from the endpoint.
    current = ENDPOINT
    path = []
    while current != ORIGIN:
        path.append(current)
        current = came_from[current]
    
    # for debugging
    # path.append(ORIGIN)
    # path.reverse()

    print(len(path))


if __name__ == "__main__":
    main()