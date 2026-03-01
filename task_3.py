import sys
from pathlib import Path

from colorama import Fore, Style, init


init(autoreset=True)


def print_directory(path: Path, indent: str = "") -> None:

    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE} {item.name}")
                print_directory(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN} {item.name}")

    except PermissionError:
        print(f"{Fore.RED}Access to the file denied")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Please insert a directory")
    else:
        directory_path = Path(sys.argv[1])

        if not directory_path.exists():
            print(f"{Fore.RED}Directory path does not exist")
        elif not directory_path.is_dir():
            print(f"{Fore.RED}The path is not a directory")
        else:
            print_directory(directory_path)

            