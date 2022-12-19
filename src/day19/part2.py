import re
import sys
from dataclasses import dataclass, field
from functools import cache

@dataclass
class Blueprint:
    id: int
    ore_robot_ore_cost: int
    clay_robot_ore_cost: int
    obsidian_robot_ore_cost: int
    obsidian_robot_clay_cost: int
    geode_robot_ore_cost: int
    geode_robot_obsidian_cost: int

    max_ore_robots: int = field(init=False)

    def __post_init__(self) -> None:
        self.max_ore_robots = max(self.ore_robot_ore_cost,
                                  self.clay_robot_ore_cost,
                                  self.obsidian_robot_ore_cost,
                                  self.geode_robot_ore_cost)

    def __hash__(self) -> int:
        return hash(self.id)

def main() -> None:
    data = sys.stdin.read().strip()

    blueprints: list[Blueprint] = []
    for line in data.splitlines():
        nums = map(int, re.findall(r"(\d+)", line))
        blueprints.append(Blueprint(*nums))

    total = 1
    for blueprint in blueprints[:3]:
        max_geodes = 0

        @cache
        def solve(blueprint: Blueprint,
                  minutes_left: int = 32,
                  ore: int = 0, clay: int = 0, obsidian: int = 0, geodes: int = 0,
                  ore_robots: int = 1, clay_robots: int = 0, obsidian_robots: int = 0, geode_robots: int = 0) -> None:
            nonlocal max_geodes

            if minutes_left == 0:
                max_geodes = max(max_geodes, geodes)
                return geodes

            if geodes + geode_robots * minutes_left + (minutes_left * (minutes_left + 1)) / 2 < max_geodes:
                return

            new_minutes_left = minutes_left - 1
            new_ore = ore + ore_robots
            new_clay = clay + clay_robots
            new_obsidian = obsidian + obsidian_robots
            new_geodes = geodes + geode_robots

            solve(blueprint,
                  new_minutes_left,
                  new_ore, new_clay, new_obsidian, new_geodes,
                  ore_robots, clay_robots, obsidian_robots, geode_robots)

            if ore_robots < blueprint.max_ore_robots and ore >= blueprint.ore_robot_ore_cost:
                solve(blueprint,
                      new_minutes_left,
                      new_ore - blueprint.ore_robot_ore_cost, new_clay, new_obsidian, new_geodes,
                      ore_robots + 1, clay_robots, obsidian_robots, geode_robots)

            if clay_robots < blueprint.obsidian_robot_clay_cost and ore >= blueprint.clay_robot_ore_cost:
                solve(blueprint,
                      new_minutes_left,
                      new_ore - blueprint.clay_robot_ore_cost, new_clay, new_obsidian, new_geodes,
                      ore_robots, clay_robots + 1, obsidian_robots, geode_robots)

            if obsidian_robots < blueprint.geode_robot_obsidian_cost and ore >= blueprint.obsidian_robot_ore_cost and clay >= blueprint.obsidian_robot_clay_cost:
                solve(blueprint,
                      new_minutes_left,
                      new_ore - blueprint.obsidian_robot_ore_cost, new_clay - blueprint.obsidian_robot_clay_cost, new_obsidian, new_geodes,
                      ore_robots, clay_robots, obsidian_robots + 1, geode_robots)

            if ore >= blueprint.geode_robot_ore_cost and obsidian >= blueprint.geode_robot_obsidian_cost:
                solve(blueprint,
                      new_minutes_left,
                      new_ore - blueprint.geode_robot_ore_cost, new_clay, new_obsidian - blueprint.geode_robot_obsidian_cost, new_geodes,
                      ore_robots, clay_robots, obsidian_robots, geode_robots + 1)

        solve(blueprint)

        print(blueprint.id, max_geodes)
        total *= max_geodes

    print(total)

if __name__ == "__main__":
    main()
