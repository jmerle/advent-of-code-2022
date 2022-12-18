import sys

def main() -> None:
    data = sys.stdin.read().strip()

    cubes = set()
    for line in data.splitlines():
        x, y, z = map(int, line.split(","))
        cubes.add((x, y, z))

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

    print(t)

if __name__ == "__main__":
    main()
