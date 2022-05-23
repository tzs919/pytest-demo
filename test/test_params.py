import pytest


@pytest.fixture(params=[1, 2, 3])
def data(request):
    return request.param


def test_not_2(data):
    print(f"测试数据：{data}")
    assert data < 5
