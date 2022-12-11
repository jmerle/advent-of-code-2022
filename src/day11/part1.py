import sys
from collections import deque
from dataclasses import dataclass
from typing import Callable

@dataclass
class Monkey:
    items: deque[int]
    operation: Callable[[int], int]
    test_divisible: int
    if_true: int
    if_false: int
    inspected_items: int

def main() -> None:
    data = sys.stdin.read().strip()

    monkeys: list[Monkey] = []

    for block in data.split("\n\n"):
        lines = block.splitlines()

        items = deque(map(int, lines[1].split(": ")[1].split(", ")))

        operation = lines[2].split("= ")[1]
        operation = eval(f"lambda old: {operation}")

        test_divisible = int(lines[3].split(" ")[-1])
        if_true = int(lines[4].split(" ")[-1])
        if_false = int(lines[5].split(" ")[-1])

        monkeys.append(Monkey(items, operation, test_divisible, if_true, if_false, 0))

    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.popleft()

                item = monkey.operation(item)
                item = item // 3

                next_monkey = monkey.if_true if item % monkey.test_divisible == 0 else monkey.if_false
                monkeys[next_monkey].items.append(item)

                monkey.inspected_items += 1

    inspected_items = sorted([monkey.inspected_items for monkey in monkeys], reverse=True)
    print(inspected_items[0] * inspected_items[1])

if __name__ == "__main__":
    main()
