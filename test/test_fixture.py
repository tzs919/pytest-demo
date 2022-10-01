#!/usr/bin/env python
import pytest


@pytest.fixture(scope="session")
def login():
    print("这是个登录方法")
    return 'tom', '123'


@pytest.fixture()
def operate():
    print("登录后的操作")


# 参数对应的函数在测试用例运行之前即都被调用，然后在此处传入函数运行的结果值
def test_case1(login, operate):
    print(type(operate))
    x, y = login
    print("===", x, y)
    print(operate)
    print("test_case1，需要登录")


def test_case2(operate):
    print("test_case2，不需要登录 ")


def test_case3(login):
    print(login)
    print("test_case3，需要登录")
