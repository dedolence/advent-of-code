
class Knot():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.head = None    # previous knot in rope
        self.tail = None    # next knot in rope

    def move(self, inst):
        # check position of head relative to this knot
        # then call tail.move()
        diff_x = self.head.x - self.x
        diff_y = self.head.y - self.y

        if abs(diff_x) > 1 or abs(diff_y) > 1:
            if self.x != self.head.x and self.y != self.head.y:
                # need to determine in what quadrant the head is
                # then move diagonally in that direction
                if self.head.x > self.x and self.head.y > self.y:
                    inst = (1,1)
                elif self.head.x > self.x and self.head.y < self.y:
                    inst = (1, -1)
                elif self.head.x < self.x and self.head.y > self.y:
                    inst = (-1, 1)
                elif self.head.x < self.x and self.head.y < self.y:
                    inst = (-1, -1)
            
            self.x += inst[0]
            self.y += inst[1]