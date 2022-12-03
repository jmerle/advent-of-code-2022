import string
import sys

def main() -> None:
    data = sys.stdin.read().strip()

    s = 0
    lines = data.splitlines()
    for i in range(0, len(lines), 3):
        a, b, c = lines[i], lines[i + 1], lines[i + 2]

        for ch in a:
            if ch in b and ch in c:
                if ch in string.ascii_lowercase:
                    s += ord(ch) - ord("a") + 1
                else:
                    s += ord(ch) - ord("A") + 27
                break

    print(s)

if __name__ == "__main__":
    main()
