import sys

def main() -> None:
    data = sys.stdin.read().strip()

    grid = []
    for line in data.splitlines():
        grid.append([int(ch) for ch in line])

    width = len(grid[0])
    height = len(grid)

    max_score = 0

    for y in range(height):
        for x in range(width):
            if y == 0 or x == 0 or y == height - 1 or x == width - 1:
                continue

            score = 1

            row = grid[y]
            col = [row[x] for row in grid]

            t = 0
            for i in range(x - 1, -1, -1):
                t += 1
                if row[i] >= grid[y][x]:
                    break
            score *= t

            t = 0
            for i in range(x + 1, width):
                t += 1
                if row[i] >= grid[y][x]:
                    break
            score *= t

            t = 0
            for i in range(y - 1, -1, -1):
                t += 1
                if col[i] >= grid[y][x]:
                    break
            score *= t

            t = 0
            for i in range(y + 1, height):
                t += 1
                if col[i] >= grid[y][x]:
                    break
            score *= t

            max_score = max(max_score, score)

    print(max_score)


if __name__ == "__main__":
    main()
