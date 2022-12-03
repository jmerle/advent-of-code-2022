import string
import sys

def main() -> None:
    data = sys.stdin.read().strip()

    s = 0
    for line in data.splitlines():
        mid = int(len(line) / 2)
        a, b = line[:mid], line[mid:]

        for ch in a:
            if ch in b:
                if ch in string.ascii_lowercase:
                    s += ord(ch) - ord("a") + 1
                else:
                    s += ord(ch) - ord("A") + 27
                break

    print(s)

if __name__ == "__main__":
    main()
