import sys
from collections import deque
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    x: int
    y: int

    level: int

    dist: int = 1e9
    prev: Optional["Node"] = None

def main() -> None:
    data = sys.stdin.read().strip()

    grid = [list(line) for line in data.splitlines()]

    w = len(grid[0])
    h = len(grid)

    sources = []
    target = None

    for y in range(h):
        for x in range(w):
            grid[y][x] = Node(x, y, ord(grid[y][x]))

            if grid[y][x].level == ord("S") or grid[y][x].level == ord("a"):
                sources.append(grid[y][x])
                grid[y][x].level = ord("a")
                grid[y][x].dist = 0
            elif grid[y][x].level == ord("E"):
                target = grid[y][x]
                target.level = ord("z")

    min_steps = 1e9

    for source in sources:
        for y in range(h):
            for x in range(w):
                grid[y][x].dist = 1e9
                grid[y][x].prev = None

        source.dist = 0

        queue = deque()
        queue.append(source)

        while len(queue) > 0:
            node = queue.popleft()

            if node == target:
                path = []

                while node is not None:
                    path.append(node)
                    node = node.prev

                min_steps = min(min_steps, len(path) - 1)
                break

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = node.x + dx, node.y + dy
                if x < 0 or x >= w or y < 0 or y >= h:
                    continue

                neighbor = grid[y][x]
                if neighbor.level - node.level > 1:
                    continue

                dist = node.dist + 1
                if dist < neighbor.dist:
                    neighbor.dist = dist
                    neighbor.prev = node
                    queue.append(neighbor)

    print(min_steps)

if __name__ == "__main__":
    main()
