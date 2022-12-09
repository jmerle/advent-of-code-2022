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
    tails = [Point(0, 0) for _ in range(9)]

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

            for i in range(9):
                nxt = head if i == 0 else tails[i - 1]
                tail = tails[i]

                if (nxt.x == tail.x and abs(nxt.y - tail.y) == 2) or (nxt.y == tail.y and abs(nxt.x - tail.x) == 2):
                    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                elif nxt.distance(tail) >= 3:
                    dirs = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
                else:
                    continue

                tails[i] = min([tail.add(dx, dy) for dx, dy in dirs], key=lambda point: nxt.distance(point))

            seen.add(tails[-1])

    print(len(seen))

if __name__ == "__main__":
    main()
