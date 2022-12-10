import sys

def main() -> None:
    data = sys.stdin.read().strip()

    vals = []
    reg = 1

    for line in data.splitlines():
        if line == "noop":
            vals.append(reg)
        else:
            vals.extend([reg, reg])
            reg += int(line.split(" ")[1])

    for i, val in enumerate(vals):
        pos = i % 40

        if pos in [val - 1, val, val + 1]:
            print("#", end="")
        else:
            print(".", end="")

        if pos == 39:
            print()

if __name__ == "__main__":
    main()
