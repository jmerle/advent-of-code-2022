import sys

def main() -> None:
    data = sys.stdin.read().strip()

    rocks = [
        [(2, 0), (3, 0), (4, 0), (5, 0)],
        [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)],
        [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
        [(2, 0), (2, 1), (2, 2), (2, 3)],
        [(2, 0), (3, 0), (2, 1), (3, 1)]
    ]

    turn_idx = 0

    blocked = set()
    for x in range(7):
        blocked.add((x, 0))

    rock_idx = 0

    observations = {}
    did_repeat = False

    while rock_idx < int(1e12):
        max_y = max(y for x, y in blocked)

        rock = rocks[rock_idx % len(rocks)]
        rock = [(x, y + max_y + 4) for x, y in rock]

        while True:
            turn = data[turn_idx % len(data)]
            turn_idx += 1

            dx = 1 if turn == ">" else -1
            if not any(x + dx < 0 or x + dx > 6 or (x + dx, y) in blocked for x, y in rock):
                rock = [(x + dx, y) for x, y in rock]

            if not any((x, y - 1) in blocked for x, y in rock):
                rock = [(x, y - 1) for x, y in rock]
            else:
                break

        for point in rock:
            blocked.add(point)

        if not did_repeat:
            max_y = max(y for x, y in blocked)

            heights = [1000] * 7
            for x, y in blocked:
                heights[x] = min(heights[x], max_y - y)

            key = (tuple(heights), rock_idx % len(rocks), turn_idx % len(data))
            if key in observations:
                prev_rock_idx, prev_max_y = observations[key]

                step = rock_idx - prev_rock_idx
                repeat = (int(1e12) - prev_rock_idx) // step - 1

                repeated_y = repeat * (max_y - prev_max_y)

                rock_idx += step * repeat
                blocked = {(x, y + repeated_y) for x, y in blocked}

                did_repeat = True
            else:
                observations[key] = (rock_idx, max_y)

        rock_idx += 1

    print(max(y for x, y in blocked))

if __name__ == "__main__":
    main()
