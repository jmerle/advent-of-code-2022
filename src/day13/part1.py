import sys

def compare(left, right) -> int:
    if not isinstance(left, list):
        left = [left]

    if not isinstance(right, list):
        right = [right]

    for i in range(min(len(left), len(right))):
        if isinstance(left[i], list) or isinstance(right[i], list):
            result = compare(left[i], right[i])
            if result != 0:
                return result
        elif left[i] < right[i]:
            return -1
        elif left[i] > right[i]:
            return 1

    if len(left) < len(right):
        return -1

    if len(left) > len(right):
        return 1

    return 0

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for i, block in enumerate(data.split("\n\n")):
        left, right = block.splitlines()
        left, right = eval(left), eval(right)

        if compare(left, right) == -1:
            t += i + 1

    print(t)

if __name__ == "__main__":
    main()
