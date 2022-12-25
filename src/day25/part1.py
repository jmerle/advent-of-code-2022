import sys

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for snafu in data.splitlines():
        num = 0
        for i, ch in enumerate(snafu):
            value = {
                "2": 2,
                "1": 1,
                "0": 0,
                "-": -1,
                "=": -2
            }[ch]
            num += 5 ** (len(snafu) - i - 1) * value

        t += num

    out = ""
    while t > 0:
        if t % 5 == 0:
            out += "0"
            t //= 5
        elif t % 5 == 1:
            out += "1"
            t //= 5
        elif t % 5 == 2:
            out += "2"
            t //= 5
        elif t % 5 == 3:
            out += "="
            t = (t + 2) // 5
        elif t % 5 == 4:
            out += "-"
            t = (t + 1) // 5

    print("".join(reversed(out)))

if __name__ == "__main__":
    main()
