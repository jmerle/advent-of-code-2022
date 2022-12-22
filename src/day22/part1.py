import re
import sys
from dataclasses import dataclass
from typing import Optional

@dataclass
class Tile:
    x: int
    y: int
    wall: bool

    left: Optional["Tile"] = None
    right: Optional["Tile"] = None
    up: Optional["Tile"] = None
    down: Optional["Tile"] = None

    def get_neighbor(self, facing: int) -> Optional["Tile"]:
        if facing == 0:
            return self.right
        elif facing == 1:
            return self.down
        elif facing == 2:
            return self.left
        else:
            return self.up

def main() -> None:
    data = sys.stdin.read()

    board, path = data.split("\n\n")

    tiles: dict[tuple[int, int], Tile] = {}
    current_tile = None
    facing = 0

    for y, line in enumerate(board.splitlines()):
        for x, ch in enumerate(line):
            if ch == " ":
                continue

            tile = Tile(x + 1, y + 1, ch == "#")

            tiles[(x + 1, y + 1)] = tile
            if current_tile is None:
                current_tile = tile

    for tile in tiles.values():
        tile.left = tiles[(tile.x - 1, tile.y)] if (tile.x - 1, tile.y) in tiles else tiles[(max(x for x, y in tiles.keys() if y == tile.y), tile.y)]
        tile.right = tiles[(tile.x + 1, tile.y)] if (tile.x + 1, tile.y) in tiles else tiles[(min(x for x, y in tiles.keys() if y == tile.y), tile.y)]
        tile.up = tiles[(tile.x, tile.y - 1)] if (tile.x, tile.y - 1) in tiles else tiles[(tile.x, max(y for x, y in tiles.keys() if x == tile.x))]
        tile.down = tiles[(tile.x, tile.y + 1)] if (tile.x, tile.y + 1) in tiles else tiles[(tile.x, min(y for x, y in tiles.keys() if x == tile.x))]

    for command in re.findall(r"(\d+|[A-Z])", path.strip()):
        if command.isdigit():
            for _ in range(int(command)):
                next_tile = current_tile.get_neighbor(facing)
                if next_tile is None or next_tile.wall:
                    break

                current_tile = next_tile
        elif command == "R":
            facing = (facing + 1) % 4
        else:
            facing = (facing - 1) % 4

    print(current_tile.y * 1000 + current_tile.x * 4 + facing)

if __name__ == "__main__":
    main()
