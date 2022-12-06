import sys

def main() -> None:
    data = sys.stdin.read().strip()

    for i in range(14, len(data)):
        if len(set(data[i-14:i])) == 14:
            print(i)
            return

if __name__ == "__main__":
    main()
