#!/usr/bin/python3

import marshal

def print_names_from_pyc(file_path):
    names = []
    with open(file_path, 'rb') as file:
        magic = file.read(4)
        timestamp = file.read(4)
        code = marshal.load(file)

        for instruction in code.co_consts:
            if isinstance(instruction, type(code)):
                for name in instruction.co_names:
                    if not name.startswith('__'):
                        names.append(name)

    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_names_from_pyc("hidden_4.pyc")
