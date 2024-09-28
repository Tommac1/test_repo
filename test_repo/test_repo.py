#!/usr/bin/env python3


"""
Module docstring.
"""


import argparse

from test_repo.app import base_app


def add(a: int, b: int) -> int:
    """
    Add.
    :param a: A
    :param b: B
    :return: A + B
    """
    return a + b


def sub(a: int, b: int) -> int:
    """
    Sub.
    :param a: A
    :param b: B
    :return: A - B
    """
    return a - b


def mul(a: int, b: int) -> int:
    """
    Mul.
    :param a: A
    :param b: B
    :return: A * B
    """
    return a * b


def div(a: int, b: int) -> int:
    """
    Div.
    :param a: A
    :param b: B
    :return: A // B
    """
    return a // b


def parse_args() -> tuple[int, int, object]:
    """
    Parse arguments.
    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(prog='main', description='Perform operation.')
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int)
    parser.add_argument('op', type=str)

    args = parser.parse_args()
    op_dict = {'add': add, 'sub': sub, 'mul': mul, 'div': div}
    return args.a, args.b, op_dict.get(args.op, add)


def main():
    """
    Main.
    :return: 0
    """
    a, b, op = parse_args()
    app = base_app.BaseApp(a, b)
    result = app.do_action(op)
    print(f'Result = {result}')

    return 0


if __name__ == '__main__':
    main()
