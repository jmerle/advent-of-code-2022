import sys
from pathlib import Path

def main() -> None:
    data = (Path(__file__).parent / sys.argv[1]).read_text(encoding="utf-8").strip()

    m = []

    for sec in data.split("\n\n"):
        total = 0

        for line in sec.splitlines():
            total += int(line)

        m.append(total)

    print(sum(sorted(m, reverse=True)[:3]))

if __name__ == "__main__":
    main()
