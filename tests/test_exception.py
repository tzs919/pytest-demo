import pytest


def f():
    f()


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        f()
    print("******22*********", excinfo.value)
    print("******33**type*******", excinfo.type)
    assert "maximum recursion" in str(excinfo.value)


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    # 不运行
    print("-----11111111111-------", 2 * 5)

    pytest.skip('for a reason!')
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


# 如果测试失败则忽略，如果成功则绿勾
@pytest.mark.xfail(raises=RuntimeError)
def test_f():
    print("-----2222222222-------", 2 + 5)
    f()
