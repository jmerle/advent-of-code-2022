import sys

def main() -> None:
    data = sys.stdin.read().strip()

    for i in range(4, len(data)):
        if len(set(data[i-4:i])) == 4:
            print(i)
            return

if __name__ == "__main__":
    main()
