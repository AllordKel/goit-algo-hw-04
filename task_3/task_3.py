from sys import argv, exit
from pathlib import Path
from colorama import Fore

path_to_dict = Path(argv[1])


if not path_to_dict.is_dir():  # Validate user input before further processing
    print(f"{Fore.RED} [ERROR] {Fore.RESET} Invalid path, path should lead to directory that exists")
    exit(1)


def everything_inside_dir(directory: Path, gap: int):
    """Recursively print directory tree with colorized output.

    Args:
        directory (Path): current directory being traversed
        gap (int): indentation level for nested entries
    """

    for path in directory.iterdir():  # going through each entity in directory

        if path.is_file():
            print(f"{Fore.GREEN}{"    " * gap}{path.name}{Fore.RESET}")
        else:
            print(f"{Fore.CYAN}{"    " * gap}{path.name}/{Fore.RESET}")
            everything_inside_dir(path, gap + 1)


print(f"{Fore.YELLOW}{path_to_dict.name}/{Fore.RESET}")  # Top-level heading for the root path

everything_inside_dir(path_to_dict, 1)  # Start recursive tree traversal from specified root directory
