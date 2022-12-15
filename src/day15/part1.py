import re
import sys

def main() -> None:
    data = sys.stdin.read().strip()

    sensors: list[tuple[int, int, int]] = []
    units = set()

    for line in data.splitlines():
        sx, sy, bx, by = map(int, re.findall(r"(-?\d+)", line))

        distance = abs(sx - bx) + abs(sy - by)

        sensors.append((sx, sy, distance))
        units.add(sx + sy * 1j)
        units.add(bx + by * 1j)

    total = 0
    y = 2_000_000
    for x in range(-10_000_000, 10_000_000):
        if x + y * 1j in units:
            continue

        if any(abs(sx - x) + abs(sy - y) <= distance for sx, sy, distance in sensors):
            total += 1

    print(total)

if __name__ == "__main__":
    main()
