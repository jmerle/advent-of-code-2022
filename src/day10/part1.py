import sys

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0

    nxt = 20
    reg = 1

    cycle = 0
    for line in data.splitlines():
        if line == "noop":
            cycle += 1
        else:
            cycle += 2

        if cycle >= nxt:
            t += nxt * reg
            nxt += 40

        if line != "noop":
            reg += int(line.split(" ")[1])

    print(t)

if __name__ == "__main__":
    main()
