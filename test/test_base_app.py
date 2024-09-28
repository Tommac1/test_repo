#!/usr/bin/env python3

import pytest

from app import base_app

def add(a: int, b: int) -> int: return a + b
def div(a: int, b: int) -> int: return a // b

class TestApp:
    def test_add(self):
        app = base_app.BaseApp(2, 3)
        assert app.do_action(add) == 5

    def test_exception(self):
        app = base_app.BaseApp()
        with pytest.raises(TypeError):
            app.do_action(3)

    def test_div0(self):
        app = base_app.BaseApp(2, 0)
        with pytest.raises(ZeroDivisionError):
            app.do_action(div)

    def test_fail(self):
        app = base_app.BaseApp()
        assert app.do_action(add) != 0  # Should fail.