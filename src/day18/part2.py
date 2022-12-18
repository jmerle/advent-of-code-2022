import sys
from collections import deque

def solve(cubes: set[tuple[int, int, int]]) -> int:
    t = 0
    for x, y, z in cubes:
        n = 6

        if (x - 1, y, z) in cubes:
            n -= 1
        if (x, y - 1, z) in cubes:
            n -= 1
        if (x, y, z - 1) in cubes:
            n -= 1
        if (x + 1, y, z) in cubes:
            n -= 1
        if (x, y + 1, z) in cubes:
            n -= 1
        if (x, y, z + 1) in cubes:
            n -= 1

        t += n

    return t

def main() -> None:
    data = sys.stdin.read().strip()

    cubes = set()
    for line in data.splitlines():
        x, y, z = map(int, line.split(","))
        cubes.add((x, y, z))

    others = set()
    for x in range(max(x for x, y, z in cubes) + 1):
        for y in range(max(y for x, y, z in cubes) + 1):
            for z in range(max(z for x, y, z in cubes) + 1):
                if (x, y, z) not in cubes:
                    others.add((x, y, z))

    queue = deque()
    queue.append((0, 0, 0))

    while len(queue) > 0:
        cube = queue.popleft()

        if cube not in others:
            continue

        others.remove(cube)
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            queue.append((cube[0] + dx, cube[1] + dy, cube[2] + dz))

    print(solve(cubes) - solve(others))

if __name__ == "__main__":
    main()
