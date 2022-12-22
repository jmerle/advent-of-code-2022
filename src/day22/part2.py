import re
import sys
from dataclasses import dataclass
from typing import Optional

@dataclass
class Tile:
    x: int
    y: int
    wall: bool

    left: Optional[tuple["Tile", int]] = None
    right: Optional[tuple["Tile", int]] = None
    up: Optional[tuple["Tile", int]] = None
    down: Optional[tuple["Tile", int]] = None

    def get_neighbor(self, facing: int) -> Optional[tuple["Tile", int]]:
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
        if (tile.x - 1, tile.y) in tiles:
            tile.left = tiles[(tile.x - 1, tile.y)], -1
        else:
            # if tile.y in range(1, 5):
            #     tile.left = tiles[(8 - tile.y + 4, 5)], 1
            # elif tile.y in range(5, 9):
            #     tile.left = tiles[(16 - tile.y + 5, 12)], 3
            # else:
            #     tile.left = tiles[(8 - tile.y + 9, 8)], 3
            if tile.y in range(1, 51):
                tile.left = tiles[(1, 51 - tile.y + 100)], 0
            elif tile.y in range(51, 101):
                tile.left = tiles[(tile.y - 50, 101)], 1
            elif tile.y in range(101, 151):
                tile.left = tiles[(51, 151 - tile.y)], 0
            else:
                tile.left = tiles[(tile.y - 100, 1)], 1

        if (tile.x + 1, tile.y) in tiles:
            tile.right = tiles[(tile.x + 1, tile.y)], -1
        else:
            # if tile.y in range(1, 5):
            #     tile.right = tiles[(16, 5 - tile.y + 8)], 2
            # elif tile.y in range(5, 9):
            #     tile.right = tiles[(8 - tile.y + 13, 9)], 1
            # else:
            #     tile.right = tiles[(12, 13 - tile.y)], 2
            if tile.y in range(1, 51):
                tile.right = tiles[(100, 51 - tile.y + 100)], 2
            elif tile.y in range(51, 101):
                tile.right = tiles[(tile.y + 50, 50)], 3
            elif tile.y in range(101, 151):
                tile.right = tiles[(150, 151 - tile.y)], 2
            else:
                tile.right = tiles[(tile.y - 100, 150)], 3

        if (tile.x, tile.y - 1) in tiles:
            tile.up = tiles[(tile.x, tile.y - 1)], -1
        else:
            # if tile.x in range(1, 5):
            #     tile.up = tiles[(5 - tile.x + 8, 1)], 1
            # elif tile.x in range(5, 9):
            #     tile.up = tiles[(9, tile.x - 4)], 0
            # elif tile.x in range(9, 13):
            #     tile.up = tiles[(tile.x - 8, 5)], 1
            # else:
            #     tile.up = tiles[(12, 17 - tile.x + 4)], 2
            if tile.x in range(1, 51):
                tile.up = tiles[(51, tile.x + 50)], 0
            elif tile.x in range(51, 101):
                tile.up = tiles[(1, tile.x + 100)], 0
            else:
                tile.up = tiles[(tile.x - 100, 200)], -1

        if (tile.x, tile.y + 1) in tiles:
            tile.down = tiles[(tile.x, tile.y + 1)], -1
        else:
            # if tile.x in range(1, 5):
            #     tile.down = tiles[(5 - tile.x + 8, 12)], 3
            # elif tile.x in range(5, 9):
            #     tile.down = tiles[(9, 9 - tile.x + 8)], 0
            # elif tile.x in range(9, 13):
            #     tile.down = tiles[(13 - tile.x, 8)], 3
            # else:
            #     tile.down = tiles[(1, 17 - tile.x + 4)], 0
            if tile.x in range(1, 51):
                tile.down = tiles[(tile.x + 100, 1)], -1
            elif tile.x in range(51, 101):
                tile.down = tiles[(50, tile.x + 100)], 2
            else:
                tile.down = tiles[(100, tile.x - 50)], 2

    for command in re.findall(r"(\d+|[A-Z])", path.strip()):
        if command.isdigit():
            for _ in range(int(command)):
                neighbor = current_tile.get_neighbor(facing)
                if neighbor is None:
                    break

                next_tile, next_facing = neighbor
                if next_tile.wall:
                    break

                current_tile = next_tile
                if next_facing > -1:
                    facing = next_facing
        elif command == "R":
            facing = (facing + 1) % 4
        else:
            facing = (facing - 1) % 4

    print(current_tile.y * 1000 + current_tile.x * 4 + facing)

if __name__ == "__main__":
    main()
