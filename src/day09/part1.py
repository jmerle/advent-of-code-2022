import sys
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def add(self, dx: int, dy: int) -> "Point":
        return Point(self.x + dx, self.y + dy)

    def distance(self, other: "Point") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

def main() -> None:
    data = sys.stdin.read().strip()

    head = Point(0, 0)
    tail = Point(0, 0)

    seen = set()

    for instr in data.splitlines():
        direction, steps = instr.split(" ")

        for _ in range(int(steps)):
            dx, dy = {
                "U": (0, -1),
                "D": (0, 1),
                "L": (-1, 0),
                "R": (1, 0)
            }[direction]

            head = head.add(dx, dy)

            if (head.x == tail.x and abs(head.y - tail.y) == 2) or (head.y == tail.y and abs(head.x - tail.x) == 2):
                tail = tail.add(dx, dy)
            elif head.distance(tail) == 3:
                dirs = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
                tail = min([tail.add(dx, dy) for dx, dy in dirs], key=lambda point: head.distance(point))

            seen.add(tail)

    print(len(seen))

if __name__ == "__main__":
    main()
