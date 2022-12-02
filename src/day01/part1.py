import sys

def main() -> None:
    data = sys.stdin.read().strip()

    m = 0

    for sec in data.split("\n\n"):
        total = 0

        for line in sec.splitlines():
            total += int(line)

        m = max(m, total)

    print(m)

if __name__ == "__main__":
    main()
