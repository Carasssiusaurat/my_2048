#!/usr/bin/env python3

from src.my_init_game import init_game
import sys

def help() -> int:
    print("""\
        USAGE
            ./my_2048
        DESCRIPTION
            You must add the same number
            The goal is to reach the biggest number with only 16 cases
        """)
    return 0

def main() -> int:
    if len(sys.argv) < 2:
        return init_game()
    if sys.argv[1] == "-h":
        return help()
    else:
        return init_game()
    return 0

if __name__ == "__main__":
    sys.exit(main())