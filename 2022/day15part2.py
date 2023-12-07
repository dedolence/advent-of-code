
import re

FILENAME = "inputs/test.txt"
WIDTH = 20
HEIGHT = 20
FACTOR = 4000000

# (x, y, x, y)  Coordinates of sensor and beacon, respectively.
Coords = tuple[int, int, int, int]


class Sensor():
    def __init__(self, coords: Coords) -> None:
        sx, sy, bx, by = coords
        self.x = sx
        self.y = sy
        self.radius = abs(bx - sx) + abs(by - sy)

    def coord_in_radius(self, coord: tuple[int, int]) -> bool:
        """
            If coord is within this radius, return the next coord
            along the same row that isn't.

            If coord is not within this radius, return this coord.
        """
        px, py = coord
        distance = abs(px - self.x) + abs(py - self.y)
        if distance <= self.radius:
            return True
        else:
            return False

    def get_next_coord(self, coord: tuple[int,int]) -> tuple[int, int]:
        """
            Given a coord that is within this sensor's radius, return the
            next coord that lies outside the radius, along the same row.
        """
        x, y = coord
        dif_y = abs(y - self.y)
        new_x = self.x + (self.radius - dif_y) + 1
        return (new_x, y)


def parse_input() -> list[Coords]:
    return [
        tuple(map(int, re.findall('[-\d]+', line))) for line in open(FILENAME)
    ]


def check_coord(coord: tuple[int, int], sensors: list[Sensor]):
    x, y = coord
    
    if x > WIDTH:
        x = 0
        y += 1
    
    if y > HEIGHT:
        raise IndexError("Coordinate is outside the test range. Free space not found.")
    
    for sensor in sensors:
        if sensor.coord_in_radius(coord):
            new_coord = sensor.get_next_coord(coord)
            return check_coord(new_coord, sensors)


    
def part_two(sensors):
    """
        for each row, check coord at 0 position against each sensor.
        if the coord is contained within that sensor's radius, it will
        return the next coord that is outside its radius so that we can
        "jump" across the row and not parse every coord.
    """
    sensors = [Sensor(coord) for coord in sensors]
    coord = (0,0)
    return check_coord(coord, sensors)


def main():
    sensors = parse_input()
    print("Part two: ", part_two(sensors))


if __name__ == "__main__":
    main()