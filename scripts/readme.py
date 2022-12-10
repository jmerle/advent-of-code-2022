import os
import re
import requests
from dotenv import load_dotenv
from pathlib import Path

OVERALL_LEADERBOARD_RANKS = [
    24, # Day 1
    9,  # Day 2
    26, # Day 3
    37, # Day 4
    50, # Day 5
    36, # Day 6
    41, # Day 7
    46, # Day 8
    53, # Day 9
    58, # Day 10
]

def main() -> None:
    load_dotenv()

    self_leaderboard_response = requests.get("https://adventofcode.com/2022/leaderboard/self",
                                             cookies={"session": os.environ["SESSION_COOKIE"]},
                                             headers={"User-Agent": "https://github.com/jmerle/advent-of-code-2022/blob/master/scripts/readme.py by jaspervmerle@gmail.com"})
    self_leaderboard_response.raise_for_status()

    rows = ""
    overall_score = 0

    matches = re.search(r"<span class=\"leaderboard-daydesc-both\">    Time  Rank  Score</span>(.*)</pre>", self_leaderboard_response.text, flags=re.DOTALL)
    for line in reversed(matches.group(1).splitlines()):
        line = line.strip()
        if len(line) == 0:
            continue

        parts = [part for part in line.split(" ") if len(part) > 0]
        day, part1_time, part1_rank, part1_score, part2_time, part2_rank, part2_score = parts

        day = int(parts[0])
        part1_time = parts[1]
        part1_rank = int(parts[2])
        part1_score = int(parts[3])
        part2_time = parts[4]
        part2_rank = int(parts[5])
        part2_score = int(parts[6])

        overall_score += part1_score + part2_score

        rows += f"""
        <tr>
            <td>
                <a href="https://adventofcode.com/2022/day/{day}">Day {day}</a>
                (<a href="https://github.com/jmerle/advent-of-code-2022/tree/master/src/day{day:02}">code</a>)
            </td>
            <td>{part1_time}</td>
            <td>{part1_rank}</td>
            <td>{part1_score}</td>
            <td>{part2_time}</td>
            <td>{part2_rank}</td>
            <td>{part2_score}</td>
            <td>{OVERALL_LEADERBOARD_RANKS[day - 1]}</td>
            <td>{overall_score}</td>
        </tr>"""

    table = f"""
<!-- results-start -->
<table>
    <thead>
        <tr>
            <th></th>
            <th colspan="3">Part 1</th>
            <th colspan="3">Part 2</th>
            <th colspan="2">Overall leaderboard</th>
        </tr>
        <tr>
            <th></th>
            <th>Time</th>
            <th>Rank</th>
            <th>Score</th>
            <th>Time</th>
            <th>Rank</th>
            <th>Score</th>
            <th>Rank</th>
            <th>Score</th>
        </tr>
    </thead>
    <tbody>
        {rows.lstrip()}
    </tbody>
</table>
<!-- results-end -->
    """.strip()

    readme_file = Path(__file__).parent.parent / "README.md"
    readme_content = readme_file.read_text(encoding="utf-8")

    readme_content = re.sub(r"<!-- results-start -->(.*)<!-- results-end -->", table, readme_content, flags=re.DOTALL)

    readme_file.write_text(readme_content, encoding="utf-8")

    print(f"Successfully updated the results table in the readme")

if __name__ == "__main__":
    main()
