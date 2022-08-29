#!/usr/bin/env python
import pytest


def add(x, y):
    return x + y


def setup_module():
    print("\nsetup_module，只执行一次，当有多个测试类的时候使用")


def teardown_module():
    print("\nteardown_module，只执行一次，当有多个测试类的时候使用")


@pytest.mark.smoke
def test_add1():
    assert add(1, 10) == 11


def test_add2():
    assert add(1, 99) == 100


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert not hasattr(x, "check")
