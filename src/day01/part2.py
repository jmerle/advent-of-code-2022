import sys

def main() -> None:
    data = sys.stdin.read().strip()

    m = []

    for sec in data.split("\n\n"):
        total = 0

        for line in sec.splitlines():
            total += int(line)

        m.append(total)

    print(sum(sorted(m, reverse=True)[:3]))

if __name__ == "__main__":
    main()
