import re
import sys

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for line in data.splitlines():
        a, b, c, d = map(int, re.findall(r"(\d+)", line))
        if (b >= c and b <= d) or (d >= a and d <= b):
            t += 1

    print(t)

if __name__ == "__main__":
    main()
