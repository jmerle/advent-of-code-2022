import sys

def main() -> None:
    data = sys.stdin.read().strip()

    grid = []
    for line in data.splitlines():
        grid.append([int(ch) for ch in line])

    width = len(grid[0])
    height = len(grid)

    t = 0
    for y in range(height):
        for x in range(width):
            if y == 0 or x == 0 or y == height - 1 or x == width - 1:
                t += 1
            else:
                row = grid[y]
                col = [row[x] for row in grid]
                val = grid[y][x]

                if max(row[:x]) < val or max(row[x+1:]) < val or max(col[:y]) < val or max(col[y+1:]) < val:
                    t += 1

    print(t)

if __name__ == "__main__":
    main()
