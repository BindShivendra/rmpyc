import argparse
from pathlib import Path

def remove(root):
    count = 0
    for file in root.glob("**/*.pyc"):
        print(f"\tDeleting {file=}")
        count += 1
        file.unlink(missing_ok=True)
    print(f"{count} file deleted")
def main():
    parser = argparse.ArgumentParser(
        description="Remove __pycache__/* from directory and subdirectory")
    parser.add_argument("dir_name", type=str, help="path to root of project")
    args = parser.parse_args()
    dir_name = Path(args.dir_name)
    if dir_name.exists():
        remove(dir_name)
    else:
        print("Please provide full path")
