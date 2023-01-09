from collections import defaultdict
from timeit import timeit

FILENAME = "inputs/day14.txt"
MAX_Y = 0
ROWS = defaultdict(list)

def parse_input() -> defaultdict[list]:
    global MAX_Y, ROWS

    rocks = [line.strip().split(' -> ') for line in open(FILENAME).readlines()]
    for rock in rocks:
        points = [tuple(map(int, coord.split(','))) for coord in rock] #[(x, y)]
        for i, p in enumerate(points[:-1]):
            x, y = points[i]
            n, m = points[i + 1]

            # set max_y to get lowest row for setting the floor boundary
            MAX_Y = max(y, m, MAX_Y) 

            if x == n:
                # same column, different row
                r = range(y, m + 1) if y < m else range(m, y + 1)
                for i in r:
                    ROWS[i] = list(set(ROWS[i] + [x]))
            else:
                # same row, different column
                (a, b) = (x, n) if x < n else (n, x)
                ROWS[y] = list(set(ROWS[y] + [i for i in range(a, b + 1)]))
    
    # index of floor
    MAX_Y += 2
    return ROWS


def generate_sand(x, y):
    if check_pos(x, y + 1):
        return generate_sand(x, y + 1)
    elif check_pos(x - 1, y + 1):
        return generate_sand(x - 1, y + 1)
    elif check_pos(x + 1, y + 1):
        return generate_sand(x + 1, y + 1)
    else:
        return (x, y)


def check_pos(x, y):
    if y == MAX_Y: return False
    else:
        return True if x not in ROWS[y] else False


def part_two():
    ROWS = parse_input()
    grains = 0
    while True:
        grains += 1
        grain = generate_sand(500, 0)
        if grain[0] == 500 and grain[1] == 0:
            break
        else:
            ROWS[grain[1]].append(grain[0])
    return grains


if __name__ == "__main__":
    print("Part two: ", part_two())
    
    """
        # for getting average time to execute:
        # averages about 3 seconds on one iteration
        
        result = timeit(part_two, number=1)
        print(f"Elapsed time", result)
    """