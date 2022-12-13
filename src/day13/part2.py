import sys
from functools import cmp_to_key

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

    packets = []
    for block in data.split("\n\n"):
        left, right = block.splitlines()
        left, right = eval(left), eval(right)

        packets.append(left)
        packets.append(right)

    divider1 = [[2]]
    divider2 = [[6]]
    packets.extend([divider1, divider2])

    packets = sorted(packets, key=cmp_to_key(compare))

    print((packets.index(divider1) + 1) * (packets.index(divider2) + 1))

if __name__ == "__main__":
    main()
