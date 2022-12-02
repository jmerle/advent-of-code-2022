import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path
from watchfiles import Change, watch

def main() -> None:
    parser = ArgumentParser(description="Automatically run part1.py and part2.py on save.")
    parser.add_argument("data_file_name", type=str, help="the name of the data file to run on")

    args = parser.parse_args()

    print(f"Started runner for {args.data_file_name}")

    project_root = Path(__file__).parent.parent

    process = None
    process_code_file = None
    process_data_file = None

    try:
        for changes in watch(project_root):
            for change, file in changes:
                if change != Change.modified:
                    continue

                file = Path(file)
                if not file.is_file():
                    continue

                if file.name in ["part1.py", "part2.py"]:
                    file_to_run = file
                elif file.name == args.data_file_name and process_code_file is not None:
                    file_to_run = process_code_file
                else:
                    continue

                print(f"Running {file_to_run.relative_to(project_root)} on {args.data_file_name}")

                if process is not None and process.poll() is None:
                    print("Killing previous process")
                    process.kill()
                    process_data_file.close()

                module_name = str(file_to_run.relative_to(project_root)).replace("/", ".").replace(".py", "")
                data_file = (file_to_run.parent / args.data_file_name).open("r")

                print()

                process = subprocess.Popen([sys.executable, "-m", module_name], cwd=project_root, stdin=data_file)
                process_code_file = file_to_run
                process_data_file = data_file
    except KeyboardInterrupt:
        if process is not None and process.poll() is None:
            print("Killing current process")
            process.kill()
            process_data_file.close()

        sys.exit(1)

if __name__ == "__main__":
    main()
