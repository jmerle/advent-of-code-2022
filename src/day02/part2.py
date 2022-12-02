import sys
from pathlib import Path

def main() -> None:
    data = (Path(__file__).parent / sys.argv[1]).read_text(encoding="utf-8").strip()

    s = 0
    for line in data.splitlines():
        a, b = line.split(" ")

        if a == "A":
            s += {
                "X": 3 + 0,
                "Y": 1 + 3,
                "Z": 2 + 6
            }[b]
        elif a == "B":
            s += {
                "X": 1 + 0,
                "Y": 2 + 3,
                "Z": 3 + 6
            }[b]
        elif a == "C":
            s += {
                "X": 2 + 0,
                "Y": 3 + 3,
                "Z": 1 + 6
            }[b]

    print(s)

if __name__ == "__main__":
    main()
