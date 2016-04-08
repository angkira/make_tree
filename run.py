import json 
from sys import argv as ARGS
from apps import readFlags, make_tree


def main():
    for arg in ARGS:
        if arg[0] == '-':
            readFlags(arg[1:], ARGS)
            return 0
    make_tree(ARGS)

main()
