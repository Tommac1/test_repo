#!/usr/bin/env python3

import argparse

from app import base_app

def add(a: int, b: int) -> int: return a + b
def sub(a: int, b: int) -> int: return a - b
def mul(a: int, b: int) -> int: return a * b
def div(a: int, b: int) -> int: return a // b

def parse_args() -> tuple[int, int, object]:
    parser = argparse.ArgumentParser(prog='main', description='Perform operation.')
    parser.add_argument('a')
    parser.add_argument('b')
    parser.add_argument('op')

    args = parser.parse_args()
    op_dict = {'add': add, 'sub': sub, 'mul': mul, 'div': div}
    return args.a, args.b, op_dict.get(args.op, add)

def main():
    a, b, op = parse_args()
    app = base_app.BaseApp(a, b)
    result = app.do_action(op)
    print(f'Result = {result}')

if __name__ == '__main__':
    main()
