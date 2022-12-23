import sys
from collections import defaultdict

def main() -> None:
    data = sys.stdin.read().strip()

    elves = set()
    directions = [
        [(-1, -1), (0, -1), (1, -1)],
        [(-1, 1), (0, 1), (1, 1)],
        [(-1, -1), (-1, 0), (-1, 1)],
        [(1, -1), (1, 0), (1, 1)]
    ]

    all_directions = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            all_directions.append((dx, dy))

    for y, line in enumerate(data.splitlines()):
        for x, ch in enumerate(line):
            if ch == "#":
                elves.add((x, y))

    round = 0
    while True:
        new_locations = {}
        proposed_counts = defaultdict(int)

        for x, y in elves:
            if all((x + dx, y + dy) not in elves for dx, dy in all_directions):
                new_locations[(x, y)] = (x, y)
                continue

            proposed_cell = None

            for direction in directions:
                if all((x + dx, y + dy) not in elves for dx, dy in direction):
                    proposed_cell = (x + direction[1][0], y + direction[1][1])
                    break

            if proposed_cell is None:
                new_locations[(x, y)] = (x, y)
            else:
                new_locations[(x, y)] = proposed_cell
                proposed_counts[proposed_cell] += 1

        new_elves = set()
        for elve, new_elve in new_locations.items():
            if proposed_counts[new_elve] > 1:
                new_elves.add(elve)
            else:
                new_elves.add(new_elve)

        if elves == new_elves:
            print(round + 1)
            break

        elves = new_elves
        directions = directions[1:] + [directions[0]]
        round += 1

if __name__ == "__main__":
    main()
