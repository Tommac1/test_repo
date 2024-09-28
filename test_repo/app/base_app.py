#!/usr/bin/env python3


"""
Module docstring.
"""


class BaseApp:
    """
    Class docstring.
    """

    def __init__(self, a: int = 0, b: int = 0):
        """
        Ctor.
        :param a: A param.
        :type a: int
        :param b: B param.
        :type b: int
        """
        self.a = a
        self.b = b

    def do_action(self, operation) -> int:
        """
        Do some action.
        :param operation: Callable operation to perform on A and B parameters.
        :return: Operation performed on A and B.
        """
        if callable(operation):
            return operation(self.a, self.b)
        raise TypeError('must provide a callable')

    def set_params(self, a: int, b: int) -> None:
        """
        Setters.
        :param a: A param
        :param b: B param
        :return: None
        """
        self.a = a
        self.b = b
