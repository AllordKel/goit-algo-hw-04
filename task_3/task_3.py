from sys import argv, exit
from pathlib import Path
from colorama import Fore

path_to_dict = Path(argv[1])

if not path_to_dict.is_dir():
    print(f"{Fore.RED} [ERROR] {Fore.RESET} Invalid path, path should lead to derictory that exists")
    exit()

def everything_inside_dir(path_to_dict, gap):
    for path in path_to_dict.iterdir():
        if path.is_file():
            print(f"{Fore.GREEN}{"    " * gap}{path.name}{Fore.RESET}")
        else:
            print(f"{Fore.CYAN}{"    " * gap}{path.name}/{Fore.RESET}")
            everything_inside_dir(path, gap + 1)

print(f"{Fore.YELLOW}{path_to_dict.name}/{Fore.RESET}")
everything_inside_dir(path_to_dict, 1)
