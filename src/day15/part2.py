import re
import sys
from z3 import If, Int, Solver

def z3_abs(var: Int) -> If:
    return If(var >= 0, var, -var)

def main() -> None:
    data = sys.stdin.read().strip()

    solver = Solver()

    x = Int("x")
    y = Int("y")

    for line in data.splitlines():
        sx, sy, bx, by = map(int, re.findall(r"(-?\d+)", line))

        distance = abs(sx - bx) + abs(sy - by)

        solver.add(z3_abs(sx - x) + z3_abs(sy - y) > distance)

    solver.add(x >= 0)
    solver.add(x <= 4_000_000)
    solver.add(y >= 0)
    solver.add(y <= 4_000_000)

    solver.check()
    model = solver.model()

    print(model[x].as_long() * 4_000_000 + model[y].as_long())

if __name__ == "__main__":
    main()
