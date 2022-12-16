import sys
from dataclasses import dataclass

@dataclass
class Valve:
    id: str
    rate: int
    neighbors: list[str]

def solve(rounds_left: int, current: Valve, unopened: list[Valve], distances: dict[str, dict[str, int]], valves: dict[str, Valve], can_fork: bool) -> int:
    if rounds_left <= 0:
        return 0

    score = solve(26, valves["AA"], unopened, distances, valves, False) if can_fork else 0
    for i in range(len(unopened)):
        valve_to_open = unopened[i]
        new_unopened = unopened[:i] + unopened[i+1:]

        new_rounds_left = rounds_left - distances[current.id][valve_to_open.id] - 1
        if new_rounds_left <= 0:
            continue

        score = max(score, valve_to_open.rate * new_rounds_left + solve(new_rounds_left, valve_to_open, new_unopened, distances, valves, can_fork))

    return score

def main() -> None:
    data = sys.stdin.read().strip()

    valves: dict[str, Valve] = {}

    for line in data.splitlines():
        id = line.split(" ")[1]
        rate = int(line.split("=")[1].split(";")[0])

        if "valves" in line:
            neighbors = line.split("valves ")[1].split(", ")
        else:
            neighbors = line.split("valve ")[1].split(", ")

        valves[id] = Valve(id, rate, neighbors)

    distances = {}
    for valve1 in valves.values():
        distances[valve1.id] = {valve2.id: 1e9 for valve2 in valves.values()}

        distances[valve1.id][valve1.id] = 0

        for neighbor in valve1.neighbors:
            distances[valve1.id][neighbor] = 1

    for valve1 in valves.values():
        for valve2 in valves.values():
            for valve3 in valves.values():
                distances[valve2.id][valve3.id] = min(distances[valve2.id][valve3.id], distances[valve2.id][valve1.id] + distances[valve1.id][valve3.id])

    print(solve(26, valves["AA"], [valve for valve in valves.values() if valve.id != "AA" and valve.rate > 0], distances, valves, True))

if __name__ == "__main__":
    main()
