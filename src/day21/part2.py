import sys
from z3 import Real, Solver

class VarDict(dict):
    def __missing__(self, key: str) -> Real:
        self[key] = Real(key)
        return self[key]

def main() -> None:
    data = sys.stdin.read().strip()

    solver = Solver()
    vars = VarDict()

    for line in data.splitlines():
        name, operation = line.split(": ")

        if name == "humn":
            continue

        monkey_var = vars[name]
        if operation.isdigit():
            solver.add(monkey_var == int(operation))
            continue

        lhs, operator, rhs = operation.split(" ")
        lhs, rhs = vars[lhs], vars[rhs]

        if name == "root":
            solver.add(lhs == rhs)
            continue

        if operator == "+":
            solver.add(lhs + rhs == monkey_var)
        elif operator == "-":
            solver.add(lhs - rhs == monkey_var)
        elif operator == "*":
            solver.add(lhs * rhs == monkey_var)
        else:
            solver.add(lhs / rhs == monkey_var)

    solver.check()
    model = solver.model()

    print(model[vars["humn"]].as_long())

if __name__ == "__main__":
    main()
