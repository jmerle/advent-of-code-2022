import sys

def main() -> None:
    data = sys.stdin.read().strip()

    width = None
    height = None

    blizzards = set()
    for y, line in enumerate(data.splitlines()[1:-1]):
        height = y + 1
        width = len(line) - 2

        for x, ch in enumerate(line[1:-1]):
            if ch == ">":
                blizzards.add((x, y, 1, 0))
            elif ch == "<":
                blizzards.add((x, y, -1, 0))
            elif ch == "v":
                blizzards.add((x, y, 0, 1))
            elif ch == "^":
                blizzards.add((x, y, 0, -1))

    locations = {(0, -1)}
    minute = 0

    while True:
        if (width - 1, height) in locations:
            print(minute)
            break

        new_blizzards = set()
        blocked = set()
        for x, y, dx, dy in blizzards:
            new_x, new_y = x + dx, y + dy
            if new_x == -1:
                new_x = width - 1
            if new_x == width:
                new_x = 0
            if new_y == -1:
                new_y = height - 1
            if new_y == height:
                new_y = 0

            new_blizzards.add((new_x, new_y, dx, dy))
            blocked.add((new_x, new_y))

        new_locations = set()
        for x, y in locations:
            if x == 0 and y == -1:
                new_locations.add((x, y))
                if (0, 0) not in blocked:
                    new_locations.add((0, 0))
                continue

            if x == width - 1 and y == height - 1 and (x, y + 1) not in blocked:
                new_locations.add((x, y + 1))
                break

            if (x, y) not in blocked:
                new_locations.add((x, y))
            if x < width - 1 and (x + 1, y) not in blocked:
                new_locations.add((x + 1, y))
            if x > 0 and (x - 1, y) not in blocked:
                new_locations.add((x - 1, y))
            if y < height - 1 and (x, y + 1) not in blocked:
                new_locations.add((x, y + 1))
            if y > 0 and (x, y - 1) not in blocked:
                new_locations.add((x, y - 1))

        blizzards = new_blizzards
        locations = new_locations
        minute += 1

if __name__ == "__main__":
    main()
