from collections import namedtuple
from time import sleep
import os

Step = namedtuple("Tile", ["x", "y", "d"])
#Step.__eq__ = lambda a, b: (a.x == b.x) and (a.y == b.y)

class Grid:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.starting_pos: Step
        self.grid = []
        self.working_grid = self.grid.copy()
        
    def __str__(self):
        for line in self.working_grid:
            print(line)

    def generate_grid(self):
        with open(self.file_name) as file:
            grid = ["*" + line.strip() + "*" for line in file.readlines()]
            pad_row = "*" * len(grid[0])
            grid = [pad_row] + grid + [pad_row]
            self.grid = grid

    def find_starting_position(self, grid: list = None):
        if grid == None:
            self.generate_grid()
            grid = self.grid
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col == "^":
                    self.starting_pos = Step(x, y, 0)   # 0 is the default direction (up)
                    line = self.grid[y]
                    line = list(line)
                    line[x] = "."
                    line = "".join(line)
                    self.grid[y] = line
                    self.working_grid = self.grid
    
    def add_obstacle(self, obstacle_pos: Step):
        self.working_grid = self.grid.copy()
        x, y, _ = obstacle_pos
        line = list(self.working_grid[y])
        line[x] = "#"
        line = "".join(line)
        self.working_grid[y] = line

    def reset_grid(self):
        self.working_grid = self.grid.copy()

    def draw_grid(self, guard_position: Step, dt = .25):
        os.system("cls")
        gx = guard_position.x
        gy = guard_position.y
        sprites = ("^", ">", "v", "<")
        gs = sprites[guard_position.d]
        grid = self.working_grid.copy()
        line = grid[gy]
        line = list(line)
        line[gx] = gs
        line = "".join(line)
        grid[gy] = line
        for line in grid:
            print(line)
        print(f"({gx, gy, guard_position.d})")
        sleep(dt)
    

class Guard:
    def __init__(self, grid: Grid, draw: bool):
        self.starting_pos: Step = grid.starting_pos
        self.current_pos: Step = grid.starting_pos
        self.grid: Grid = grid
        self.directions: tuple = ((0, -1), (1, 0), (0, 1), (-1, 0))
        self.direction: int = self.current_pos.d
        self.out_of_bounds: bool = False
        self.loop: bool = False
        self.draw: bool = draw
        self.steps_taken: list = [self.starting_pos]
        self.next_pos: Step
    
    def reset(self):
        self.current_pos = self.starting_pos

    def get_next_pos(self) -> Step:
        dx = self.directions[self.current_pos.d][0]
        dy = self.directions[self.current_pos.d][1]
        next_char = self.grid.working_grid[self.current_pos.y + dy][self.current_pos.x + dx]
        if next_char == "#":
            self.change_direction()
            dx = self.directions[self.current_pos.d][0]
            dy = self.directions[self.current_pos.d][1]
        self.next_pos = Step(self.current_pos.x + dx, self.current_pos.y + dy, self.current_pos.d)
        return self.next_pos

    def take_step(self):
        next_char = self.grid.working_grid[self.next_pos.y][self.next_pos.x]
        if next_char == "*":
            self.out_of_bounds = True
            return
        self.update_position(self.next_pos)

    def change_direction(self):
        new_direction = (self.current_pos.d + 1) % len(self.directions)
        self.current_pos = Step(self.current_pos.x, self.current_pos.y, new_direction)

    def update_position(self, next_pos):
        self.current_pos = next_pos
        if self.current_pos in self.steps_taken:
            self.loop = True
            return
        else:
            self.steps_taken.append(self.current_pos)
            self.steps_taken = list(set(self.steps_taken))

    def patrol(self) -> bool:
        while not self.out_of_bounds:
            if self.draw:
                self.grid.draw_grid(self.current_pos)
            self.get_next_pos()
            self.take_step()
            if self.loop:
                return True
        return False




grid = Grid("test.txt")
grid.generate_grid()
grid.find_starting_position()


def find_loops(test_guard: Guard, control_guard: Guard, loops: int = 0):
    # test_guard resets at every iteration and runs the path from the beginning
    # control_guard maintains its last position so we know where next to put an obstacle,
    # and when to end the simulation.
    while not control_guard.out_of_bounds:
        obstacle_pos = control_guard.get_next_pos()
        test_guard.grid.add_obstacle(obstacle_pos)
        patrol = test_guard.patrol()
        if patrol: loops += 1
        test_guard.reset()
        control_guard.take_step()
    return loops


def find_loops(test, control, loops):
    # control starts off one step ahead of test. if it's out of bounds then we're done
    if control.out_of_bounds:
        return loops
    # set an obstacle in test's path based on where control is
    obstacle_pos = control.current_pos
    test.grid.add_obstacle(obstacle_pos)

    # run the test simulation
    if test.patrol():
        loops += 1
    
    # move control forward, reset test
    control.current_pos = control.next_pos
    test.reset()

    return find_loops(test, control, loops)




test_guard = Guard(grid, False)
control_guard = Guard(grid, False)
find_loops(test_guard, control_guard)