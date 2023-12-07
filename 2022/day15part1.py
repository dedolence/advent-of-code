"""
    For sensor, S, and beacon, B, the distance between the two, radius,
    can be extended vertically from the sensor. However far past the row
    in question that radius extends will form the base of two triangles,
    each of which represent locations where the beacon CANNOT be.

    So, we don't need to do breadth-first in all directions; just need the
    sides of a triangle where the BFS search would intersect with the row in 
    question.
    <--------S-------->       Distance from S to B extends horizontally and  
     \       |       /        vertically.
      \      |      /          
       B     |     /           
    ----\####|####/-----  # = spots that the missing beacon can't be because
         \ A | B /            they fall within sensor S's detection radius.
          \  |  /             this range is determined by the length of the base
           \ | /              of triangles A, and B.
            \|/                
             V
"""

from timeit import timeit
import re
from collections import defaultdict

FILENAME = "inputs/day15.txt"
Y        = 10 if "test" in FILENAME else 2000000
ROW      = defaultdict(bool)

# (x, y, x, y)  Sensor x, y and beacon x, y, respectively.
Coords = tuple[int, int, int, int]


def parse_input() -> list[Coords]:
    return [
        tuple(map(int, re.findall('[-\d]+', line))) for line in open(FILENAME)
    ]


def part_one(coords: Coords) -> int:
    for coord in coords:
        sx, sy, bx, by = coord
        radius = abs(bx - sx) + abs(by - sy)
        xrange = range(0)

        # If the sensor's detection radius extends past the row,
        # that distance, for each side, can be added to the set of
        # locations where the beacon cannot be.
        if sy < Y and sy + radius > Y:
            extension = abs(Y - (sy + radius))
            xrange = range(sx - extension, sx + extension)

        elif sy > Y and sy - radius < Y:
            extension = abs((sy - radius) - Y)
            xrange = range(sx - extension, sx + extension)

        for i in xrange:
            ROW[i] = True

    return len(ROW)


def main():
    coords = parse_input()
    print("Part one:", part_one(coords))

    # 0.55s
    #print("Time for part one: ", timeit(lambda: part_one(coords), number=1))


if __name__ == "__main__":
    main()