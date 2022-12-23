"""
    Advent of Code Day 09 solution by Nathaniel Hoyt.
    https://github.com/dedolence

    -p --part       1 or 2  Choose which puzzle part to run; default 2.
    -v --visualize          Visualization on if present; default off.
    -s --step               Manually step instructions; default off.
    -d --delay      float   Delay to sleep between instructions if manual 
                            step is off. Default 0.5 seconds.
"""

from typing import List, Tuple
from time import sleep
import os, sys, getopt, math

FILEPATH = "inputs/test.txt"
P_1 = False
P_2 = True
VISUALISE = True
VISUALIZE_REFRESH_RATE = 0.5    # time in seconds
MANUAL_STEP = False     # manually increment instructions

# Type alias for a formatted instruction
Instr = Tuple[int, int]

class Rope():
    def __init__(self, knots: int) -> None:
        self.knots: list[RopeKnot] = []
        for i in range(knots):
            self.knots.append(RopeKnot(i))
        self.head = self.knots[0]
        self.tail = self.knots[-1]
        self.head.head = True
        self.tail.tail = True

    def move(self, inst: Instr) -> None:
        """
            Moves head then initiates a check on each knot in sequence,
            telling them to move if required.
        """
        self.head.move(inst)


class RopeKnot():
    def __init__(self, i) -> None:
        self.x = 0
        self.y = 0
        self.head = False
        self.tail = False
        self._positions = [(0,0)]
        self.sprite = str(i)
    
    def move(self, pos: tuple[int, int]) -> None:
        self.x += pos[0]
        self.y += pos[1]
        if self.tail:
            self._positions.append(pos)
        return

    def get_positions(self) -> int:
        return len(set(self._positions))

    def get_sprite(self) -> str:
        if self.head:
            return "H"
        elif self.tail:
            return "T"
        else:
            return self.sprite


class Grid():
    def __init__(self, rope: Rope) -> None:
        self.width = 60
        self.height = 18
        self.origin_x = self.width // 2
        self.origin_y = self.height // 2
        self.delta: int = 1
        self.rope: Rope = rope
        self.head: RopeKnot = rope.head
        self.tail: RopeKnot = rope.tail
        self.inst = None
        self.reset()


    def display(self) -> None:
        os.system("clear")
        reversed_points = self.points
        reversed_points.reverse()
        for line in reversed_points:
            print("".join(line))
        print("=" * (self.width + 1))
        print("Tail total unique positions: ", self.tail.get_positions())
        print("Current instruction: ", self.inst)
        for knot in self.rope.knots[:len(self.rope.knots)//2]:
            print(f"{knot.get_sprite()}: ({knot.x}, {knot.y})", end="     ")
        print()
        for knot in self.rope.knots[len(self.rope.knots)//2:]:
            print(f"{knot.get_sprite()}: ({knot.x}, {knot.y})", end="     ")
        print()


    def reset(self) -> None:
        """
            Resets the grid to blank dots to refres before updating.
        """
        self.points: list = []
        for i in range(self.height):
            self.points.append([])
            for n in range(self.width + 2):
                if n == self.width + 1:
                    self.points[i].append("\n")
                else:
                    self.points[i].append(".")
        
        self.points[self.origin_y][self.origin_x] = "s"


    def update(self, inst) -> None:
        """
            Displays the rope on the grid by changing the dots at
            specific indexes to different characters.
        """
        self.inst = inst
        self.reset()
        for knot in self.rope.knots:
            # normalize position to account for origin not being
            # at (0,0)
            new_x = knot.x + self.origin_x
            new_y = knot.y + self.origin_y

            # account for out-of-bounds coordinates
            if new_x > self.width - 1:
                new_x -= self.width

            if new_y > self.height - 1:
                new_y -= self.height

            try:
                self.points[new_y][new_x] = knot.get_sprite()
            except:
                print("New_x:", new_x)
                print("New_y:", new_y)
                os._exit(0)


def feed_rope(instrs: List[Instr], rope: Rope, visualize: bool = False) -> int:
    """
        Feeds instructions one at a time to a Rope instance,
        which moves its children (knots), and returns the unique
        positions recorded by its last child (tail).
    """
    if visualize:
        grid = Grid(rope)
        grid.update(None)
        grid.display()
        if MANUAL_STEP:
            input()
        else:
            sleep(VISUALIZE_REFRESH_RATE)  

    for i, inst in enumerate(instrs):
        rope.move(inst)
        if visualize:
            grid.update(inst)
            grid.display()
            if MANUAL_STEP:
                input()
            else:
                sleep(VISUALIZE_REFRESH_RATE)
    
    return rope.tail.get_positions()


def process_instructions(input) -> List[Instr]:
    """
        Parses instructions as single-unit movements on an X,Y plane.
        E.g.: "R 3" becomes, "[(1,0), (1,0), (1,0)].
    """
    parsed_ins = []
    for line in input:
        #ins = parse_line(line)
        dir, quant = line.split()
        match dir:
            case "R":
                delta = (1, 0)
            case "L":
                delta = (-1, 0)
            case "U":
                delta = (0, 1)
            case "D":
                delta = (0, -1)
        parsed_ins += [(delta)] * int(quant)
    return parsed_ins


def main() -> None:
    # format input
    input = [line.strip() for line in open(FILEPATH)]
    insts = process_instructions(input)
    part_1_rope = Rope(2)
    part_2_rope = Rope(10)

    if (P_1):
        print("Part one: ", feed_rope(insts, part_1_rope, VISUALISE))
        if (P_2):
            input("Press any key to move to part 2.")
    
    if (P_2):
        print("Part two: ", feed_rope(insts, part_2_rope, VISUALISE))


if __name__ == "__main__":
    abort = False
    args_list = sys.argv[1:]
    options = "hp:vsd:"
    long_options = ["help", "part=", "visualize", "step", "delay="]
    try:
        args, vals = getopt.getopt(args_list, options, long_options)
        for a, c in args:

            if a in ("-h", "--help"):
                print(__doc__)
                abort = True
                break

            if a in ("-p", "--part"):
                if int(c) == 1:
                    P_1 = True
                    P_2 = False
                elif int(c) == 2:
                    P_1 = False
                    P_2 = True
                else:
                    continue
            
            if a in ("-v", "--visualize"):
                VISUALIZE = True

            if a in ("-s", "--step"):
                MANUAL_STEP = True

            elif a in ("-d", "--delay"):
                VISUALIZE_REFRESH_RATE = float(c)
    except getopt.error as e:
        print(str(e))
    
    if not abort:
        main()