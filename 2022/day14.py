"""
    Advent of Code Day 14 (part one) solution by Nathaniel Hoyt.
    https://github.com/dedolence

    -h --help               Display this text.
    -v --visualize          Visualization on if present; default off.
    -s --step               Manually step instructions; default off.
    -d --delay      float   Delay to sleep between instructions if manual 
                            step is off. Default 0.5 seconds.
"""

import os, time, sys, getopt
from numpy import sign

VISUALIZE = False
REFRESH_RATE = 0.1
FILENAME = "inputs/test.txt"
PART = 1
MANUAL_STEP = False

class Field():
    """
        Represents the scanned field. On instantiation, draws in rocks. Then incrementally creates a new grain of sand, calling its move() method until it can no longer move, at which point the grain will become settled and Field will generate a new grain of sand, and so forth.
    """
    def __init__(self, rock_points, width, height, origin) -> None:
        self.rock_points = rock_points
        self.width = width
        self.height = height
        self.origin = origin
        self.all_points: list[list[str]] = []
        self.rock_sprite = "#"
        self.blank_sprite = "."
        self.origin_sprite = "+"
        self.sand: list[Grain] = []
        self.ready = True
        self.end_con = False    # true when we need to stop execution
        self.update()

    def check_pos(self, pos: tuple[int, int]) -> bool:
        """
            Get an (x, y) coord and check to see if there is anything blocking
            a grain of sand from moving there.
        """
        try:
            point = self.all_points[pos[1]][pos[0]]
            if point == self.blank_sprite:
                return True
            else:
                return False
        except IndexError:
            self.end_con = True
            return False
            
    def gen_grain(self):
        while self.ready:
            if self.end_con:
                self.sand.pop()
                self.update()
                return len(self.sand)
            new_grain = Grain(self.origin[0], self.origin[1], self)
            self.sand.append(new_grain)
            new_grain.move()

    def set_tiles(self):
        self.all_points: list = []

        # draw a blank field
        for y in range(self.height + 1):
            self.all_points.append([])
            for x in range(self.width + 1):
                if x == self.width:
                    self.all_points[y].append("\n")
                else:
                    self.all_points[y].append(self.blank_sprite)
        
        # draw rock sprites
        for coord in self.rock_points:
            self.all_points[coord[1]][coord[0]] = self.rock_sprite

        # draw sand origin
        self.all_points[self.origin[1]][self.origin[0]] = self.origin_sprite

        # draw in sand
        for grain in self.sand:
            self.all_points[grain.y][grain.x] = grain.sprite

    def display(self) -> None:

        os.system("clear")

        for line in self.all_points:
            print("".join(line))
        print("=" * (self.width + 1))
        print("End condition: ", self.end_con)
        if len(self.sand):
            print("X: ", self.sand[-1].x)
            print("Y: ", self.sand[-1].y)
            print("Grains counted: ", len(self.sand))
        
    def update(self) -> None:
        self.set_tiles()
        if VISUALIZE:
            self.display()
            time.sleep(REFRESH_RATE)
        elif MANUAL_STEP:
            input()


class Grain():
    def __init__(self, x: int, y: int, field: Field) -> None:
        self.x = x
        self.y = y
        self.sprite = "o"
        self.field = field
        self.settled = False

    def move(self) -> None:
        while self.settled == False:
            self.field.update()
            #input()

            # try moving down
            if self.field.check_pos((self.x, self.y + 1)):
                self.y += 1
            
            # try moving down/left
            elif self.field.check_pos((self.x - 1, self.y + 1)):
                self.x -= 1
                self.y += 1
            
            # try moving down/right
            elif self.field.check_pos((self.x + 1, self.y + 1)):
                self.x += 1
                self.y += 1
            
            # can't move at all
            else:
                self.settled = True
                self.field.ready = True


def parse_input() -> list[tuple[int, int]]:
    """
        Turns each line of input (a single rock structure) into a list of tuples with int x and y coordinates.
    """
    with open(FILENAME) as file:
        lines = [line.strip().split(" -> ") for line in file.readlines()]
    
    all_points: list[tuple[int, int]] = []
    
    for line in lines:
        coords: list[tuple[int, int]] = [
            (int(x), int(y)) for x,y in map(lambda c: tuple(c.split(',')), line)
        ]
        
        for i in range(len(coords) - 1):
            cc = coords[i]              # current coord
            nc = coords[i + 1]          # next coord
            dx = nc[0] - cc[0]          # difference in x
            dy = nc[1] - cc[1]          # difference in y
            dc = (sign(dx), sign(dy))   # single-unit to fill in the gap between current and new
            all_points.append(cc)       # append current coord
            while cc != nc:             # fill in gaps until next coord
                cc = (cc[0] + dc[0], cc[1] + dc[1])
                all_points.append(cc)

    return all_points


def get_dimensions(rock_points) -> dict:
        """
            Finds the max dimensions in X and Y plane.
            Normalizes the X dimension so it starts at index 1 (with index 0 to account for a drop off into ~tHe VoId~). pads outer border too.
        """
        low_x = 0
        high_x = 0
        low_y = 0
        high_y = 0
        offset_x = 0
        offset_y = 0
        for i, rock in enumerate(rock_points):
            if i == 0:
                low_x = rock[0]
                high_x = rock[0]
                low_y = rock[1]
                high_y = rock[1]
            else:
                if rock[0] < low_x:
                    low_x = rock[0]
                elif rock[0] > high_x:
                    high_x = rock[0]
                if rock[1] < low_y:
                    low_y = rock[1]
                elif rock[1] > high_y:
                    high_y = rock[1]
        
        offset_x = low_x - 1
        offset_y = 0
        new_rocks = []
        # normalize the rocks so they start at width[1]
        for rock in rock_points:
            new_rocks.append((rock[0] - offset_x, rock[1] - offset_y))
        rock_points = new_rocks

        # set field dimensions
        width = high_x - offset_x + 2
        height = high_y
        origin = 500 - offset_x
        return {'width': width, 'height': height, 'rocks': rock_points, 'origin': (origin, 0)}


def main():
    rock_points = parse_input()
    dimensions = get_dimensions(rock_points)
    field = Field(
        dimensions["rocks"],
        dimensions["width"],
        dimensions["height"],
        dimensions["origin"]
    )

    part_one = field.gen_grain()
    print("Part one: ", part_one)


if __name__ == "__main__":
    abort = False
    args = sys.argv[1:]
    options = "hp:vsd:"
    long_options = ["help", "part=", "visualize", "step", "delay="]
    try:
        args, vals = getopt.getopt(args, options, long_options)
        for a, c in args:

            if a in ("-h", "--help"):
                print(__doc__)
                abort = True
                break
            
            if a in ("-v", "--visualize"):
                VISUALIZE = True

            if a in ("-s", "--step"):
                VISUALIZE = True
                MANUAL_STEP = True

            elif a in ("-d", "--delay"):
                MANUAL_STEP = False
                VISUALIZE = True
                REFRESH_RATE = float(c)

    except getopt.error as e:
        print(str(e))

    if not abort:
        main()