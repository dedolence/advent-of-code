import os, time

class RopeEnd():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.positions = [(0,0)]
    
    def move(self, pos: tuple):
        self.x = pos[0]
        self.y = pos[1]
        self.positions.append(pos)


class Grid():
    """
        Purely for visualization.
    """
    def __init__(self) -> None:
        self.delta = 0.05    # refresh rate
        self.width: int = 48
        self.height: int = 16
        self.origin_x: int = self.width // 2
        self.origin_y: int = self.height // 2
        self.head = {"x": 0, "y": 0}
        self.tail = {"x": 0, "y": 0}
        self.reset_grid()
        
    def reset_grid(self) -> None:
        self.points: list = []
        for i in range(self.height + 1):
            self.points.append([])
            for n in range(self.width + 2):
                if n == self.width + 1:
                    self.points[i].append("\n")
                else:
                    self.points[i].append(".")

        self.points[self.origin_y][self.origin_x] = "s"

    def update(self, h: tuple, t: tuple) -> None:
        self.reset_grid()
        self.head["x"] = self.origin_x + h[0] if self.origin_x + h[0] < self.width else 0 + h[0]
        self.head["y"] = self.origin_y + h[1] if self.origin_y + h[1] < self.height else 0 + h[1]
        self.tail["x"] = self.origin_x + t[0] if self.origin_x + t[0] < self.width else 0 + t[0]
        self.tail["y"] = self.origin_y + t[1] if self.origin_y + t[1] < self.height else 0 + t[1]
        
        try:
            self.points[self.tail["y"]][self.tail["x"]] = "T"
            self.points[self.head["y"]][self.head["x"]] = "H"
        except:
            print("Attempted coordinates:")
            print(f"Head: [{self.tail['y']}][{self.tail['x']}]")
            print(f"Tail: [{self.head['y']}][{self.head['x']}]")


    def display(self, tail: RopeEnd) -> None:
        os.system("clear")
        reversed_points = self.points
        reversed_points.reverse()
        for line in reversed_points:
            print("".join(line))
        print("===================")
        print("Tail positions: ", len(set(tail.positions)))
        print(f"Head position: ({self.head['x']}, {self.head['y']})")
        print(f"Tail position: ({self.tail['x']}, {self.tail['y']})")


def process_instructions(input) -> list:
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


def main(input):
    head = RopeEnd()
    tail = RopeEnd()
    insts = process_instructions(input)

    #grid = Grid()
    #grid.update((head.x, head.y), (tail.x, tail.y))
    #grid.display(tail)

    for i, ins in enumerate(insts):

        # first update the head location
        head.move((head.x + ins[0], head.y + ins[1]))

        # check how far behind the tail is
        dif_x = abs(head.x - tail.x)
        dif_y = abs(head.y - tail.y)

        # check if tail needs to move (distance > 1)
        if dif_x > 1 or dif_y > 1:
            
            # checks whether head and tail are in different columns and
            # rows, which would require the tail to move diagonally.
            if head.x != tail.x and head.y != tail.y:

                # for diagonal movement, the tail gets placed in the same
                # axis as the head, then its position is incremented normally.
                if dif_x > dif_y:
                    new_pos = (tail.x + ins[0], head.y)
                else:
                    new_pos = (head.x, tail.y + ins[1])
                
            else:
                # no diagonal movement required so just move the tail exactly
                # according to the instructions.
                new_pos = (tail.x + ins[0], tail.y + ins[1])
            
            tail.move(new_pos)

        #grid.update((head.x, head.y), (tail.x, tail.y))
        #grid.display(tail)
        #time.sleep(grid.delta)
    
    print("Part one: ", len(set(tail.positions)))


if __name__ == "__main__":
    # format input
    input = [line.strip() for line in open("inputs/day9.txt")]
    main(input)