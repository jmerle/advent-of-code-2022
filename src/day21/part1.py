import sys

def evaluate(operation: str, monkeys: dict[str, str]) -> int:
    if operation.isdigit():
        return int(operation)

    lhs, operator, rhs = operation.split(" ")
    lhs, rhs = evaluate(monkeys[lhs], monkeys), evaluate(monkeys[rhs], monkeys)

    if operator == "+":
        return lhs + rhs
    elif operator == "-":
        return lhs - rhs
    elif operator == "*":
        return lhs * rhs
    else:
        return lhs // rhs

def main() -> None:
    data = sys.stdin.read().strip()

    monkeys: dict[str, str] = {}
    for line in data.splitlines():
        name, operation = line.split(": ")
        monkeys[name] = operation

    print(evaluate(monkeys["root"], monkeys))

if __name__ == "__main__":
    main()
