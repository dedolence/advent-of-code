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

# find start and end points
for i in range(HEIGHT):
    for j in range(WIDTH):
        if MAZE[i][j] == "S":
            ORIGIN = (j, i)
        if MAZE[i][j] == "E":
            ENDPOINT = (j, i)

# change "S" and "E" to "a" and "z" respectively
# so the position checks return correctly
MAZE[ORIGIN[1]][ORIGIN[0]] = "a"
MAZE[ENDPOINT[1]][ENDPOINT[0]] = "z"

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
    return filter(lambda p: c + 1 >= ord(MAZE[p[1]][p[0]]), neighbors)


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

        if current == ENDPOINT:
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