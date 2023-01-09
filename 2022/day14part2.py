"""
    FAILURE. Takes hours and hours and hours. No good! Looks cool though...
    See day14part2-2.py for the correct solution.

    Advent of Code Day 14 (part two) solution by Nathaniel Hoyt.
    https://github.com/dedolence

    -h --help               Display this text.
    -v --visualize          Visualization on if present; default off.
    -s --step               Manually step instructions; default off.
    -d --delay      float   Delay to sleep between instructions if manual 
                            step is off. Default 0.5 seconds.
"""

import os, time, sys, getopt
from numpy import sign
from typing import Callable, List

VISUALIZE = False
REFRESH_RATE = 0.1
FILENAME = "inputs/day14.txt"
PART = 1
MANUAL_STEP = False

class Grain():
    def __init__(self, x: int, y: int, check_pos: Callable[[int, int], bool]) -> None:
        self.x = x
        self.y = y
        self.settled = False
        self.check_pos = check_pos
        self.sprite = "O"
        self.pause_on_settle = 1

    def move(self) -> bool:
        # try moving down
        if self.check_pos(self.x, self.y + 1):
            self.y += 1
        
        # try moving down/left
        elif self.check_pos(self.x - 1, self.y + 1):
            self.x -= 1
            self.y += 1
        
        # try moving down/right
        elif self.check_pos(self.x + 1, self.y + 1):
            self.x += 1
            self.y += 1
        
        # can't move at all
        else:
            self.settled = True
            if VISUALIZE:
                time.sleep(self.pause_on_settle)


class Field():
    def __init__(self, rocks, width, height, origin) -> None:
        self.width = width
        self.height = height
        self.originX = origin[0]
        self.originY = origin[1]
        self.rock_points = rocks
        self.blank_sprite = "."
        self.rock_sprite = "#"
        self.origin_sprite = "+"
        self.sand: List[Grain] = []
        self.window_height = 20     # how many rows to print at any one time
        self.update()               # start the display

    def cont(self) -> bool:
        """
            Checks whether the last sand grain has reached the top.
        """
        if len(self.sand) > 0:
            last_sand:Grain = self.sand[-1:][0]
            if (last_sand.x == self.originX and last_sand.y == self.originY):
                return False
        return True
    
    def run(self) -> int:
        """
            Produces new grains of sand. Ends and returns when self.cont is 
            set to False. Pauses while self.ready is set to False to allow 
            sand to settle to the bottom. Returns number of sand grains gen-
            erated.
        """
        while self.cont():

            grain = Grain(self.originX, self.originY, self.check_pos)
            self.sand.append(grain)

            while grain.settled == False:
                grain.move()
                self.update()
            
        return len(self.sand)

    def check_pos(self, x: int, y: int):
        """
            Get an (x, y) coord and check to see if there is anything blocking
            a grain of sand from moving there.

            If the x position is out of bounds, add a column to let it fall.
        """
        if x in range(self.width) and y in range(self.height):
            point = self.all_points[y][x]
            if point == self.blank_sprite:
                return True
            else:
                return False
        elif x not in range(self.width) and y in range(self.height):
            if x < 0:
                self.add_column(True)
            if x >= self.width:
                self.add_column()
            return True
        else:
            return False

    def add_column(self, x: bool = False):
        """
            The floor is supposed to extend infinitely horizontally. 
            For the sake of visually rendering this, a new column will
            get added dynamically whenever a grain of sand needs it.
            
            x = True if add to the left side.
        """
        # ...#...   width + 1
        # ....#...  all x values + 1
        self.width += 1
        if x:
            # add a column to the left. increase width by 1 and add 1
            # to all X values (origin, rocks, grains).
            self.width +=1
            self.rock_points = list(map(lambda p: (p[0] + 1, p[1]), self.rock_points))
            self.originX += 1
            for grain in self.sand:
                grain.x += 1
        self.update()

    def update(self):
        """
            Rebuilds the matrix of sprites then calls display() to print 
            them to screen.
        """
        self.build_matrix()
        if VISUALIZE:
            self.display()
            time.sleep(REFRESH_RATE)
        elif MANUAL_STEP:
            input()
 
    def build_matrix(self):
        """
            Creates a 2d matrix list containing lists for each row in the
            terminal output. each row is itself a list containing each
            individual sprite character, which are then joined into a single
            string in display() and printed to the terminal.
        """ 
        self.all_points: list[list[str]] = []

        # draw a blank field
        for y in range(self.height + 1):
            self.all_points.append([])
            for x in range(self.width + 1):
                if x == self.width:
                    self.all_points[y].append("\n")
                elif y == self.height:
                    # draw floor
                    self.all_points[y].append(self.rock_sprite)
                else:
                    self.all_points[y].append(self.blank_sprite)
        
        # draw rock sprites
        for coord in self.rock_points:
            self.all_points[coord[1]][coord[0]] = self.rock_sprite

        # draw sand origin
        self.all_points[self.originY][self.originX] = self.origin_sprite

        # draw in sand
        for grain in self.sand:
            self.all_points[grain.y][grain.x] = grain.sprite

    def display(self):
        """
            Clears terminal window and prints each line of the matrix to 
            screen along with some additional information.
        """
        os.system("clear")

        grain_y = self.sand[-1].y if len(self.sand) else 0
        window_y = max(0, grain_y - (self.window_height - 2))

        #for line in self.all_points:
        for i in range(self.window_height):
            print("".join(self.all_points[i + window_y]))
        print("=" * (self.width + 1))
        if len(self.sand):
            print("X: ", self.sand[-1].x)
            print("Y: ", self.sand[-1].y)
            print("Grains counted: ", len(self.sand))


def parse_input() -> list[tuple[int, int]]:
    """
        Turns each line of input (a single rock structure) into a list of 
        tuples with int x and y coordinates.
    """
    with open(FILENAME) as file:
        lines = [line.strip().split(" -> ") for line in file.readlines()]
    
    all_rock_points: list[tuple[int, int]] = []
    
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
            all_rock_points.append(cc)  # append current coord
            while cc != nc:             # fill in gaps until next coord
                cc = (cc[0] + dc[0], cc[1] + dc[1])
                all_rock_points.append(cc)

    return all_rock_points


def get_dimensions(rock_points) -> dict:
        """
            Finds the max dimensions in X and Y plane.
            Normalizes the X dimension so it starts at index 1 (with index 0 
            to account for a drop off into ~tHe VoId~). pads outer border too.
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
        height = high_y + 2     # two for floor
        origin = 500 - offset_x
        return {
            'width': width, 
            'height': height, 
            'rocks': rock_points, 
            'origin': (origin, 0)
            }


def main():
    rock_points = parse_input()
    dimensions = get_dimensions(rock_points)
    field = Field(
        dimensions["rocks"],
        dimensions["width"],
        dimensions["height"],
        dimensions["origin"]
    )

    part_two = field.run()
    print("Part two: ", part_two)


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