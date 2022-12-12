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

    source = None
    target = None

    for y in range(h):
        for x in range(w):
            grid[y][x] = Node(x, y, ord(grid[y][x]))

            if grid[y][x].level == ord("S"):
                source = grid[y][x]
                source.level = ord("a")
                source.dist = 0
            elif grid[y][x].level == ord("E"):
                target = grid[y][x]
                target.level = ord("z")

    queue = deque()
    queue.append(source)

    while len(queue) > 0:
        node = queue.popleft()

        if node == target:
            path = []

            while node is not None:
                path.append(node)
                node = node.prev

            print(len(path) - 1)
            return

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

    print("No path found")

if __name__ == "__main__":
    main()
