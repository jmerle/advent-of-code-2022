import sys
from collections import defaultdict
from pathlib import Path

def main() -> None:
    data = sys.stdin.read().strip()

    current_dir = Path("/")
    dir_sizes = defaultdict(int)

    for line in data.splitlines():
        if line.startswith("$ cd"):
            current_dir = (current_dir / line[5:]).resolve()
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            continue
        else:
            size = int(line.split(" ")[0])
            dir_sizes[current_dir] += size
            for parent in current_dir.parents:
                dir_sizes[parent] += size

    print(sum(v for v in dir_sizes.values() if v <= 100000))

if __name__ == "__main__":
    main()
